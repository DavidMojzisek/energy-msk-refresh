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
SHIFT_MAX = 6.0
RHO = 0.6
FACTORS = ("elektrifikace", "povolovani", "cena")
LOSS_ITEM = "ztráty v sítích"
OWN_ITEM = "vlastní spotřeba zdrojů"
SMR_ITEM = "SMR"
# Ztráty v sítích, stejný vzorec v obou cestách: r / (1 - r) × (spotřeba bez ztrát - část, která neteče sítí). r = 3,547 %, Dopadová studie Tab.1 s.27.
LOSS_R = 0.03547
LOSS_K = LOSS_R / (1.0 - LOSS_R)
# Lokální část mimo vlastní spotřebu zdrojů: rozdíl tab. 6.3 a 6.2 ERÚ za rok 2025 (886,8302 GWh) minus vlastní spotřeba 391,862 GWh.
LOCAL_OTHER = 886.8302 - 391.862
# Vlastní spotřeba zdrojů: celostátní míry ERÚ 2025 Q4 kap. 3.1 krát kalibrace na kraj 1,4367, stejný výpočet v tabulce popisů.
OWN_CAL = 1.4367
_PE, _PSE, _PPE, _JE, _VE, _VTE, _FVE = 0.123451, 0.066352, 0.019803, 0.054755, 0.009025, 0.012331, 0.008158
OWN_RATES = {"černé uhlí: Dětmarovice": _PE, "černé uhlí: teplárny a průmysl": _PE, "hnědé uhlí": _PE, "hutní plyny (vysokopecní a koksárenský)": _PE,
             "ostatní paliva a odpadní teplo (přidaná položka)": _PE, "biomasa": _PE, "energetické využití odpadu": _PE,
             "zemní plyn: stávající kogenerace": _PSE, "důlní plyn": _PSE, "bioplyn": _PSE,
             "nové plynové bloky": _PPE, "syntetický plyn z odpadu": _PPE, SMR_ITEM: _JE,
             "malé vodní elektrárny": _VE, "vítr": _VTE, "fotovoltaika střešní": _FVE, "fotovoltaika pozemní": _FVE}
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


def pchip_slopes(xs, ys):
    """Směrnice monotónní kubické interpolace podle Fritsche a Carlsona (1980), krok po kroku stejně jako v sablona.html."""
    n = len(xs)
    d = [(ys[i + 1] - ys[i]) / (xs[i + 1] - xs[i]) for i in range(n - 1)]
    m = [0.0] * n
    m[0], m[-1] = d[0], d[-1]
    for i in range(1, n - 1):
        m[i] = 0.0 if d[i - 1] * d[i] <= 0 else (d[i - 1] + d[i]) / 2.0
    for i in range(n - 1):
        if d[i] == 0:
            m[i] = m[i + 1] = 0.0
        else:
            a, b = m[i] / d[i], m[i + 1] / d[i]
            s = a * a + b * b
            if s > 9.0:
                tau = 3.0 / s ** 0.5
                m[i], m[i + 1] = tau * a * d[i], tau * b * d[i]
    return m


def pchip_eval(t, nodes):
    """Hodnota v čase t (pole libovolného tvaru) z uzlů {"x", "y", "m"}. Mimo rozsah platí krajní hodnota."""
    xs, ys, ms = (np.asarray(nodes[k], dtype=float) for k in ("x", "y", "m"))
    tt = np.clip(t, xs[0], xs[-1])
    i = np.clip(np.searchsorted(xs, tt, side="right") - 1, 0, len(xs) - 2)
    h = xs[i + 1] - xs[i]
    u = (tt - xs[i]) / h
    return (ys[i] * (2 * u ** 3 - 3 * u ** 2 + 1) + h * ms[i] * (u ** 3 - 2 * u ** 2 + u)
            + ys[i + 1] * (-2 * u ** 3 + 3 * u ** 2) + h * ms[i + 1] * (u ** 3 - u ** 2))


def warp(t, shift):
    """Posun průběhu v čase pro křivku přes uzly. Konce 2025 a 2050 zůstávají, posun je omezený, aby čas nešel pozpátku."""
    x = np.clip((t - 2025.0) / 25.0, 0.0, 1.0)
    return t - np.clip(shift, -SHIFT_MAX, SHIFT_MAX) * 4.0 * x * (1.0 - x)


def half_year(nodes, base):
    """Rok, kdy křivka poprvé urazí polovinu své největší odchylky od roku 2025. Jen výchozí hodnota posuvníku."""
    grid = np.linspace(2025.0, 2050.0, 2501)
    value = pchip_eval(grid, nodes) - base
    top = np.abs(value).max()
    return float(grid[np.argmax(np.abs(value) >= top / 2.0)]) if top > 0 else 2038.0


def part_s(t, part, tm_shift=0.0):
    tm = part["tm"] + tm_shift
    if part.get("hard"):
        return (t >= tm) * 1.0
    if "cap" in part:
        tm = min(tm, part["cap"])
    return s_curve(t, tm, part["k"])


def fit_parts(base, target, mid30, mid40):
    """Části křivky z výchozí hodnoty, cíle a hodnot pro roky 2030 a 2040."""
    t = np.array([2030.0, 2040.0])
    points = np.array([mid30, mid40])
    span = max(abs(target - base), abs(mid30 - base), abs(mid40 - base))
    # Plochý řádek: zaokrouhlení P50 proti základu nesmí dělat S-křivku.
    if span < 0.06:
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
    kind = (row.get("krivka") or "").strip()
    param = (row.get("krivka_parametry") or "").strip()
    nodes = None
    if kind == "odvozena":
        # Řádek počítá derived() z ostatních řádků, tady drží jen základ.
        return {"base": base, "target": target, "driver": np.ones(len(YEARS)), "parts": [], "nodes": None, "jump": False, "saving": False, "derived": True}
    if row["prubeh"].strip() == "skok":
        amp = target / at[2050] - base
        parts = [{"amp": amp, "tm": num(row, "skok_rok_p50"), "k": float(param) if kind == "skok_k" else JUMP_K}] if abs(amp) > 1e-9 else []
        if kind == "tvrdy_skok":
            # Uzavření s daným datem: výchozí hodnota do posledního roku provozu, cíl od dalšího roku.
            for part in parts:
                part["hard"] = True
        elif kind == "dva_skoky":
            # První stupeň sedí na hodnotu tabulky pro rok 2040, druhý stupeň dorovná cíl 2050.
            first = num(row, "p50_2040") / at[2040] - base
            parts = [{"amp": first, "tm": num(row, "skok_rok_p50"), "k": JUMP_K},
                     {"amp": amp - first, "tm": float(param), "k": JUMP_K, "cap": 2050.0}]
    elif kind in ("pchip", "uzly"):
        points = {2025.0: base, 2030.0: num(row, "p50_2030") / at[2030], 2040.0: num(row, "p50_2040") / at[2040], 2050.0: target / at[2050]}
        if kind == "uzly":
            for pair in param.split(";"):
                year, value = pair.split(":")
                points[float(year)] = float(value)
        xs = sorted(points)
        ys = [points[x] for x in xs]
        nodes = {"x": xs, "y": ys, "m": pchip_slopes(xs, ys)}
        # Část s nulovou amplitudou drží jen výchozí rok posuvníku času, hodnotu dávají uzly.
        parts = [{"amp": 0.0, "tm": half_year(nodes, base), "k": 1.0}]
    elif kind == "logistika":
        tm, k = param.split(";")
        parts = [{"amp": target / at[2050] - base, "tm": float(tm), "k": float(k)}]
    else:
        parts = fit_parts(base, target / at[2050], num(row, "p50_2030") / at[2030], num(row, "p50_2040") / at[2040])
    return {"base": base, "target": target, "driver": driver, "parts": parts, "nodes": nodes,
            "jump": row["prubeh"].strip() == "skok", "saving": num(row, "p10_2050") < 0}


def own_use(gen):
    """Vlastní spotřeba z hodnot řádků výroby, gen je slovník název -> hodnota nebo pole."""
    return OWN_CAL * sum(rate * gen[name] for name, rate in OWN_RATES.items() if name in gen)


def grid_loss(others, own):
    """others je součet spotřeby bez ztrát v sítích, včetně vlastní spotřeby own, ta sítí neteče."""
    return LOSS_K * np.maximum(others - own - LOCAL_OTHER, 0.0)


def path_curves(rows, models):
    """Výchozí křivky všech řádků jedné cesty včetně odvozených. Vrací slovník název -> pole po letech."""
    out = {}
    side = {}
    for row, model in zip(rows, models):
        name = row["polozka"].strip()
        side[name] = row["strana"].strip()
        if not model.get("derived"):
            out[name] = curve(model)
    own = own_use({n: v for n, v in out.items() if side[n] == "vyroba"})
    if OWN_ITEM in side:
        out[OWN_ITEM] = own
    others = sum(v for n, v in out.items() if side[n] == "spotreba")
    if LOSS_ITEM in side:
        out[LOSS_ITEM] = grid_loss(others, own)
    return out


def curve(model, target=None, tm_shift=0.0):
    """Výchozí křivka, případně s jiným cílem nebo posunutým načasováním. Vrací pole po letech."""
    t = YEARS.astype(float)
    if model.get("nodes"):
        level = pchip_eval(warp(t, tm_shift), model["nodes"])
    else:
        level = np.full(len(t), model["base"], dtype=float)
        for part in model["parts"]:
            level = level + part["amp"] * part_s(t, part, tm_shift)
    value = model["driver"] * level
    if target is not None:
        value = value + (target - model["target"]) * deviation(t)
    return value if model["saving"] else np.maximum(value, 0)


def deviation(t):
    """Odchylka od výchozího cíle se přičítá až od roku 2030: σ(x) = 3x² − 2x³."""
    x = np.clip((t - 2030.0) / 20.0, 0.0, 1.0)
    return 3 * x ** 2 - 2 * x ** 3


CLIP_Z = False


def quantile(z, p10, p50, p90, saving=False):
    if CLIP_Z:
        z = np.clip(z, -Z90, Z90)
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
        parts = model["parts"]
        step_k = parts[0]["k"] if parts else JUMP_K
        # SMR je binární volba cesty: v progresivní cestě do roku 2050 stojí, los mění jen rok. Případ bez SMR se počítá zvlášť.
        if row["polozka"].strip() == SMR_ITEM:
            tm = np.minimum(tm, 2050.0)
        grid = (t[:, None] >= tm[None, :]) * 1.0 if parts and parts[0].get("hard") else s_curve(t[:, None], tm[None, :], step_k)
        # Událost po roce 2050 se do roku 2050 neprojeví.
        grid = np.where(tm[None, :] > 2050.0, 0.0, grid)
        if len(parts) == 2:
            # Dva stupně: druhý drží odstup od prvního a do roku 2050 proběhne, cíl dorovná on.
            second = s_curve(t[:, None], np.minimum(tm + parts[1]["tm"] - parts[0]["tm"], parts[1]["cap"])[None, :], JUMP_K)
            second = np.where(tm[None, :] > 2050.0, 0.0, second)
            level = model["base"] + parts[0]["amp"] * grid + (targets / driver_end - model["base"] - parts[0]["amp"]) * second
        else:
            level = model["base"] + (targets / driver_end - model["base"]) * grid
    elif model.get("nodes"):
        # Křivka přes uzly: odchylka běhu v milníku je z P10 až P90 tabulky pro ten rok, mezi milníky lineárně, 2025 bez odchylky.
        shift = z_time * TM_SPREAD / Z90
        level = pchip_eval(warp(t[:, None], shift[None, :]), model["nodes"])
        points = [np.zeros(runs)]
        for year in MILESTONES:
            p50 = num(row, f"p50_{year}")
            points.append(quantile(z, num(row, f"p10_{year}"), p50, num(row, f"p90_{year}"), model["saving"]) - p50)
        marks = [2025.0, 2030.0, 2040.0, 2050.0]
        weights = np.array([np.interp(t, marks, np.eye(4)[i]) for i in range(4)])
        extra = (weights[:, :, None] * np.array(points)[:, None, :]).sum(axis=0)
        value = model["driver"][:, None] * level + extra
        return value if model["saving"] else np.maximum(value, 0)
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


def draw_rows(rows, models, rng, runs):
    """Losování jedné cesty: jedna sada společných faktorů, jeden rok pro položky stejné události, rok událostí závislých na povolování jde s faktorem povolování.
    Vrací dvojice (řádek, model, z, z_time). Odvozené řádky nese z pro svou nejistotu míry."""
    factors = {name: rng.standard_normal(runs) for name in FACTORS}
    events = {}
    for row, model in zip(rows, models):
        own = rng.standard_normal(runs)
        shared = factors.get(row["faktor"].strip())
        sign = -1.0 if row["polozka"].strip() in REVERSED else 1.0
        z = own if shared is None else sign * np.sqrt(RHO) * shared + np.sqrt(1 - RHO) * own
        event = (row.get("udalost") or "").split(",")[0].strip()
        if event and event in events:
            z_time = events[event]
        else:
            z_time = rng.standard_normal(runs)
            if row["faktor"].strip() == "povolovani":
                # Přísnější povolování znamená pozdější rok.
                z_time = -np.sqrt(RHO) * factors["povolovani"] + np.sqrt(1 - RHO) * z_time
            if event:
                events[event] = z_time
        yield row, model, z, z_time


def bound_ratio(row, z):
    """Nejistota odvozeného řádku: poměr kvantilu k P50 z mezí tabulky."""
    p10, p50, p90 = num(row, "p10_2050"), num(row, "p50_2050"), num(row, "p90_2050")
    return quantile(z, p10, p50, p90) / max(p50, 1e-9)


def simulate_path(rows, models, rng, runs):
    """P10, P50 a P90 součtů po letech pro jednu cestu, výroba i spotřeba z jednoho losování. Vlastní spotřeba a ztráty se počítají z losovaných řádků."""
    n = len(YEARS)
    gen, use, own_sum = np.zeros((n, runs)), np.zeros((n, runs)), np.zeros((n, runs))
    derived = {}
    for row, model, z, z_time in draw_rows(rows, models, rng, runs):
        name = row["polozka"].strip()
        if model.get("derived"):
            derived[name] = (row, z)
            continue
        value = simulate_item(row, model, z, z_time, runs)
        if row["strana"].strip() == "vyroba":
            gen += value
            own_sum += OWN_RATES.get(name, 0.0) * value
        else:
            use += value
    own = OWN_CAL * own_sum
    if OWN_ITEM in derived:
        own = own * bound_ratio(*derived[OWN_ITEM])
        use = use + own
    if LOSS_ITEM in derived:
        use = use + grid_loss(use, own) * bound_ratio(*derived[LOSS_ITEM])
    band = lambda a: [x for x in np.percentile(a, [10, 50, 90], axis=1).round(1).tolist()]
    return {"vyroba": band(gen), "spotreba": band(use)}


def widen_band(band, width_share):
    """Pravidlo z hindcastu: je-li pásmo P10 až P90 v roce 2030 užší než width_share mediánu, odchylky od mediánu se vynásobí poměrem.
    Do roku 2030 platí celý násobek, od 2030 do 2040 klesá lineárně na 1. Vrací pásmo a násobek."""
    low, mid, high = (np.array(b, dtype=float) for b in band)
    i = 2030 - int(YEARS[0])
    ratio = width_share * mid[i] / (high[i] - low[i])
    if ratio <= 1.0:
        return band, 1.0
    factor = np.interp(YEARS.astype(float), [2025.0, 2030.0, 2040.0, 2050.0], [ratio, ratio, 1.0, 1.0])
    return [(mid + (low - mid) * factor).round(1).tolist(), mid.round(1).tolist(), (mid + (high - mid) * factor).round(1).tolist()], float(ratio)


def item_band(row, model, rng, runs=4000):
    z, z_time = rng.standard_normal(runs), rng.standard_normal(runs)
    return np.percentile(simulate_item(row, model, z, z_time, runs), [10, 50, 90], axis=1)
