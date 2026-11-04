"""Sestaví index.html ze šablony a dat. Spuštění: python3 build.py"""
import csv
import json
import re
from pathlib import Path

import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.stats import norm

HERE = Path(__file__).resolve().parent
PATHS = ["progresivni", "konzervativni"]
YEARS = np.arange(2025, 2051)
MILESTONES = [2030, 2040, 2050]
RUNS = 10000
RHO = 0.6
Z90 = norm.ppf(0.9)

# Skutečnost v GWh. Výroba je brutto, spotřeba je součet sektorů plus ztráty v sítích.
# 2023: výroba ERÚ Roční zpráva, sektory Dopadová studie Tab. 6, ztráty 6 018,9 - 5 805,4 z Tab. 1.
# 2024 a 2025: čtvrtletní zprávy ERÚ, ztráty jsou netto z tab. 6.2 × 3,547 % / (1 - 3,547 %).
LOSS = 0.03547 / (1 - 0.03547)
HISTORY = [
    {"y": 2023, "gen": 3703.2208, "use": 7090.2833 + 213.5},
    {"y": 2024, "gen": 3052.3406, "use": 6810.1894 + 5931.2084 * LOSS},
    {"y": 2025, "gen": 2805.1634, "use": 7069.9644},
]


def read_items():
    path = HERE / "polozky.csv"
    if not path.exists():
        return []
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def num(row, key):
    value = (row.get(key) or "").strip().replace(" ", "").replace(",", ".")
    return float(value) if value else None


def quantile(z, p10, p50, p90):
    """Hodnota z normálního skóre přes P10, P50 a P90, po částech lineárně."""
    upper = p50 + z / Z90 * (p90 - p50)
    lower = p50 + z / Z90 * (p50 - p10)
    value = np.where(z >= 0, upper, lower)
    # Úspory jsou záporná položka, ostatní položky nemohou klesnout pod nulu.
    return np.minimum(value, 0) if p10 < 0 else np.maximum(value, 0)


def item_curve(base, levels, jump_years):
    """Roční křivky položky. levels má tvar (3, n), jump_years je None nebo pole n roků."""
    n = levels.shape[1]
    start = np.full(n, base) if jump_years is None else levels[0]
    knots = np.vstack([start, levels])
    curve = PchipInterpolator([2025] + MILESTONES, knots, axis=0)(YEARS)
    if jump_years is not None:
        curve = np.where(YEARS[:, None] < jump_years[None, :], base, curve)
    return curve


def simulate(rows, rng):
    """Vrátí P10, P50 a P90 součtů po letech pro jednu stranu a cestu."""
    total = np.zeros((len(YEARS), RUNS))
    factors = {name: rng.standard_normal(RUNS) for name in ("elektrifikace", "povolovani", "cena")}
    for row in rows:
        own = rng.standard_normal(RUNS)
        shared = factors.get(row["faktor"].strip())
        z = own if shared is None else np.sqrt(RHO) * shared + np.sqrt(1 - RHO) * own
        levels = np.vstack([
            quantile(z, num(row, f"p10_{m}"), num(row, f"p50_{m}"), num(row, f"p90_{m}"))
            for m in MILESTONES
        ])
        jumps = None
        if row["prubeh"].strip() == "skok":
            jumps = np.round(quantile(rng.standard_normal(RUNS), num(row, "skok_rok_p10"),
                                      num(row, "skok_rok_p50"), num(row, "skok_rok_p90")))
        total += item_curve(num(row, "zaklad_2025_GWh"), levels, jumps)
    return [np.percentile(total, q, axis=1).round(1).tolist() for q in (10, 50, 90)]


def median_curve(row):
    """Výchozí křivka položky. U skoku je to hladina po události, rok skoku určuje stránka."""
    levels = np.array([[num(row, f"p50_{m}")] for m in MILESTONES])
    jumps = None
    if row["prubeh"].strip() == "skok":
        jumps = np.array([2025.0])
    return item_curve(num(row, "zaklad_2025_GWh"), levels, jumps)[:, 0].round(2).tolist()


def build_data():
    rows = read_items()
    rng = np.random.default_rng(20261104)
    items, bands = [], {}
    for path in PATHS:
        bands[path] = {}
        for side in ("vyroba", "spotreba"):
            subset = [r for r in rows if r["cesta"].strip() == path and r["strana"].strip() == side]
            if subset:
                bands[path][side] = simulate(subset, rng)
    for r in rows:
        p = {k: num(r, k) for k in ("p10_2050", "p50_2050", "p90_2050", "zaklad_2025_GWh")}
        items.append({
            "name": r["polozka"].strip(), "side": r["strana"].strip(), "path": r["cesta"].strip(),
            "base": p["zaklad_2025_GWh"], "p10": p["p10_2050"], "p50": p["p50_2050"], "p90": p["p90_2050"],
            "curve": median_curve(r), "grade": r["stupen"].strip(), "how": r["odvozeni"].strip(),
            "src": r["zdroj"].strip(), "note": r["poznamka"].strip(),
            "page": (r.get("strana_studie") or "").strip(), "quote": (r.get("citace") or "").strip(),
            "jump": num(r, "skok_rok_p50") if r["prubeh"].strip() == "skok" else None,
            "jumpLow": num(r, "skok_rok_p10") if r["prubeh"].strip() == "skok" else None,
            "jumpHigh": num(r, "skok_rok_p90") if r["prubeh"].strip() == "skok" else None,
            "event": r["udalost"].strip().split(",")[0],
        })
    return {"years": YEARS.tolist(), "history": HISTORY, "items": items, "bands": bands}


def fonts_css():
    cached = HERE / "fonts.css"
    if cached.exists():
        return cached.read_text(encoding="utf-8")
    html = (HERE.parent / "sources" / "CEET-FlowSim-v310-offline.html").read_text(encoding="utf-8", errors="replace")
    faces = re.findall(r"@font-face\s*\{[^}]*\}", html)
    css = "/* Saira, DM Sans, JetBrains Mono: SIL Open Font License */\n" + "\n".join(faces)
    cached.write_text(css, encoding="utf-8")
    return css


def main():
    template = (HERE / "sablona.html").read_text(encoding="utf-8")
    payload = json.dumps(build_data(), ensure_ascii=False).replace("</", "<\\/")
    page = template.replace("/*FONTS*/", fonts_css()).replace("/*DATA*/null", payload)
    (HERE / "index.html").write_text(page, encoding="utf-8")


if __name__ == "__main__":
    main()
