"""Průběh položek v čase podle METODIKA.md: y(t) = D(t) · (s0 + součet amp · S(t))."""
import csv
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares
from scipy.stats import norm

YEARS = np.arange(2025, 2051)
MILESTONES = [2030, 2040, 2050]
Z90 = norm.ppf(0.9)
JUMP_K = 4.0
PEAK_K = 0.5
TM_SPREAD = 3.0
RHO = 0.6
FACTORS = ("elektrifikace", "povolovani", "cena")
LOSS_ITEM = "ztráty v sítích"
# Tyto položky jdou proti společnému faktoru: rychlejší elektrifikace je snižuje.
REVERSED = {"hutní plyny (vysokopecní a koksárenský)", "zemní plyn: stávající kogenerace", "přímotopy", "úspory a účinnost"}


def num(row, key):
    value = (row.get(key) or "").strip().replace(" ", "").replace(",", ".")
    return float(value) if value else None


def read_rows(path):
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def read_drivers(path):
    """Roční index každého vlivu, mezi milníky lineárně."""
    if not Path(path).exists():
        return {}
    points = {}
    for row in read_rows(path):
        points.setdefault(row["vliv"].strip(), []).append((int(row["rok"]), num(row, "hodnota")))
    drivers = {}
    for name, pts in points.items():
        pts.sort()
        drivers[name] = np.interp(YEARS, [p[0] for p in pts], [p[1] for p in pts])
    return drivers


def logistic(t, tm, k):
    return 1.0 / (1.0 + np.exp(np.clip(-k * (t - tm), -500, 500)))


def s_curve(t, tm, k):
    """Normovaná S-křivka: S(2025) = 0 a S(2050) = 1."""
    # Střed daleko mimo období by dělil téměř nulou, proto ho držíme v dosahu pěti převrácených k.
    tm = np.clip(tm, 2025.0 - 5.0 / k, 2050.0 + 5.0 / k)
    low, high = logistic(2025.0, tm, k), logistic(2050.0, tm, k)
    return (logistic(t, tm, k) - low) / (high - low)


def fit_parts(base, target, mid30, mid40):
    """Části křivky z výchozí hodnoty, cíle a hodnot pro roky 2030 a 2040."""
    t = np.array([2030.0, 2040.0])
    points = np.array([mid30, mid40])
    span = max(abs(target - base), abs(mid30 - base), abs(mid40 - base))
    if span < 1e-9:
        return []
    monotone = (min(base, target) - 1e-9 <= min(points)) and (max(points) <= max(base, target) + 1e-9) \
        and (target - base) * (mid40 - mid30) >= -1e-9 and abs(target - base) > 1e-9
    if monotone:
        def error(p):
            return (base + (target - base) * s_curve(t, p[0], p[1]) - points) / span
        fit = least_squares(error, [2038.0, 0.25], bounds=([2015.0, 0.08], [2060.0, 3.0]))
        return [{"amp": target - base, "tm": float(fit.x[0]), "k": float(fit.x[1])}]
    # Položka, která vzroste a zase klesne, nebo naopak: rozdíl dvou S-křivek.
    peak = max([mid30, mid40], key=lambda v: abs(v - base))
    amp1 = (peak - base) * 1.15
    amp2 = target - base - amp1

    def error2(p):
        value = base + amp1 * s_curve(t, p[0], PEAK_K) + amp2 * s_curve(t, p[1], PEAK_K)
        return (value - points) / span
    fit = least_squares(error2, [2030.0, 2045.0], bounds=([2020.0, 2030.0], [2045.0, 2050.0]))
    return [{"amp": amp1, "tm": float(fit.x[0]), "k": PEAK_K}, {"amp": amp2, "tm": float(fit.x[1]), "k": PEAK_K}]


def item_model(row, drivers):
    """Parametry výchozí křivky položky."""
    base = num(row, "zaklad_2025_GWh")
    name = (row.get("ridic") or "").strip()
    driver = drivers.get(name, np.ones(len(YEARS)))
    at = {year: driver[list(YEARS).index(year)] for year in MILESTONES}
    target = num(row, "p50_2050")
    if row["prubeh"].strip() == "skok":
        amp = target / at[2050] - base
        parts = [{"amp": amp, "tm": num(row, "skok_rok_p50"), "k": JUMP_K}] if abs(amp) > 1e-9 else []
    else:
        parts = fit_parts(base, target / at[2050], num(row, "p50_2030") / at[2030], num(row, "p50_2040") / at[2040])
    return {"base": base, "target": target, "driver": driver, "parts": parts,
            "jump": row["prubeh"].strip() == "skok", "saving": num(row, "p10_2050") < 0}


def curve(model, target=None, tm_shift=0.0):
    """Výchozí křivka, případně s jiným cílem nebo posunutým načasováním. Vrací pole po letech."""
    t = YEARS.astype(float)
    level = np.full(len(t), model["base"], dtype=float)
    for part in model["parts"]:
        level = level + part["amp"] * s_curve(t, part["tm"] + tm_shift, part["k"])
    value = model["driver"] * level
    if target is not None:
        value = value + (target - model["target"]) * deviation(t)
    return value if model["saving"] else np.maximum(value, 0)


def deviation(t):
    """Odchylka od výchozího cíle se přičítá až od roku 2030: σ(x) = 3x² − 2x³."""
    x = np.clip((t - 2030.0) / 20.0, 0.0, 1.0)
    return 3 * x ** 2 - 2 * x ** 3


def quantile(z, p10, p50, p90, saving=False):
    upper = p50 + z / Z90 * (p90 - p50)
    lower = p50 + z / Z90 * (p50 - p10)
    value = np.where(z >= 0, upper, lower)
    return np.minimum(value, 0) if saving else np.maximum(value, 0)


def simulate_item(row, model, z, z_time, runs):
    """Běhy jedné položky: cíl z P10 až P90 v roce 2050, načasování kolem výchozího roku."""
    targets = quantile(z, num(row, "p10_2050"), num(row, "p50_2050"), num(row, "p90_2050"), model["saving"])
    t = YEARS.astype(float)
    driver_end = model["driver"][-1]
    if model["jump"]:
        tm = quantile(z_time, num(row, "skok_rok_p10"), num(row, "skok_rok_p50"), num(row, "skok_rok_p90"))
        grid = s_curve(t[:, None], tm[None, :], JUMP_K)
        # Událost po roce 2050 se do roku 2050 neprojeví.
        grid = np.where(tm[None, :] > 2050.0, 0.0, grid)
        level = model["base"] + (targets / driver_end - model["base"]) * grid
    else:
        # Cíl a rok se v běhu mění. Vzestup u dvou částí zůstává, cíl dorovná poslední část.
        shift = z_time * TM_SPREAD / Z90
        parts = model["parts"]
        level = np.full((len(t), runs), model["base"], dtype=float)
        remaining = targets / driver_end - model["base"]
        for index, part in enumerate(parts):
            grid = s_curve(t[:, None], (part["tm"] + shift)[None, :], part["k"])
            amp = remaining if index == len(parts) - 1 else part["amp"]
            level = level + amp * grid
            remaining = remaining - amp
        if not parts:
            level = level + (targets - model["target"]) / driver_end * deviation(t)[:, None]
    value = model["driver"][:, None] * level
    return value if model["saving"] else np.maximum(value, 0)


def simulate(rows, models, rng, runs):
    """P10, P50 a P90 součtů po letech pro jednu stranu a cestu. Ztráty v sítích jdou s ostatní spotřebou."""
    factors = {name: rng.standard_normal(runs) for name in FACTORS}
    total = np.zeros((len(YEARS), runs))
    default_total = np.zeros(len(YEARS))
    loss = None
    for row, model in zip(rows, models):
        own = rng.standard_normal(runs)
        shared = factors.get(row["faktor"].strip())
        sign = -1.0 if row["polozka"].strip() in REVERSED else 1.0
        z = own if shared is None else sign * np.sqrt(RHO) * shared + np.sqrt(1 - RHO) * own
        z_time = rng.standard_normal(runs)
        runs_value = simulate_item(row, model, z, z_time, runs)
        if row["polozka"].strip() == LOSS_ITEM:
            loss = (model, runs_value)
            continue
        total += runs_value
        default_total += curve(model)
    if loss is not None:
        total += loss[1] * total / default_total[:, None]
    return [np.percentile(total, q, axis=1).round(1).tolist() for q in (10, 50, 90)]


def item_band(row, model, rng, runs=4000):
    z, z_time = rng.standard_normal(runs), rng.standard_normal(runs)
    return np.percentile(simulate_item(row, model, z, z_time, runs), [10, 50, 90], axis=1)
