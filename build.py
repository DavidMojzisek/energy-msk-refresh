"""Sestaví index.html ze šablony a dat. Spuštění: python3 build.py"""
import json
import re
from pathlib import Path

import numpy as np

from model import YEARS, curve, item_model, num, read_drivers, read_rows, simulate

HERE = Path(__file__).resolve().parent
PATHS = ["progresivni", "konzervativni"]
RUNS = 10000

# Skutečnost v GWh. Výroba je brutto, spotřeba je součet sektorů plus ztráty v sítích.
# 2023: výroba ERÚ Roční zpráva, sektory Dopadová studie Tab. 6, ztráty 6 018,9 - 5 805,4 z Tab. 1.
# 2024 a 2025: čtvrtletní zprávy ERÚ, ztráty jsou netto z tab. 6.2 × 3,547 % / (1 - 3,547 %).
LOSS = 0.03547 / (1 - 0.03547)
HISTORY = [
    {"y": 2023, "gen": 3703.2208, "use": 7090.2833 + 213.5},
    {"y": 2024, "gen": 3052.3406, "use": 6810.1894 + 5931.2084 * LOSS},
    {"y": 2025, "gen": 2805.1634, "use": 7069.9644},
]


def text(row, key):
    return (row.get(key) or "").strip()


def build_data():
    path = HERE / "polozky.csv"
    rows = read_rows(path) if path.exists() else []
    drivers = read_drivers(HERE / "ridici_vlivy.csv")
    models = [item_model(r, drivers) for r in rows]
    popis_path = HERE / "polozky_popis.csv"
    popis = {(text(r, "polozka"), text(r, "cesta")): r for r in read_rows(popis_path)} if popis_path.exists() else {}
    rng = np.random.default_rng(20261104)
    items, bands, fit_report = [], {}, []
    for route in PATHS:
        bands[route] = {}
        for side in ("vyroba", "spotreba"):
            chosen = [(r, m) for r, m in zip(rows, models) if text(r, "cesta") == route and text(r, "strana") == side]
            if chosen:
                bands[route][side] = simulate([c[0] for c in chosen], [c[1] for c in chosen], rng, RUNS)
    for r, m in zip(rows, models):
        jump = m["jump"]
        plain = popis.get((text(r, "polozka"), text(r, "cesta")), {})
        driver = None if not text(r, "ridic") else [round(float(v), 4) for v in m["driver"]]
        items.append({
            "name": text(r, "polozka"), "side": text(r, "strana"), "path": text(r, "cesta"),
            "base": m["base"], "p10": num(r, "p10_2050"), "p50": num(r, "p50_2050"), "p90": num(r, "p90_2050"),
            "parts": [{"amp": round(p["amp"], 3), "tm": round(p["tm"], 2), "k": round(p["k"], 3)} for p in m["parts"]],
            "driver": driver, "driverName": text(r, "ridic"), "maxRate": num(r, "tempo_max_GWh_rok"),
            "grade": text(r, "stupen"), "how": text(r, "odvozeni"), "src": text(r, "zdroj"), "note": text(r, "poznamka"),
            "page": text(r, "strana_studie"), "quote": text(r, "citace"),
            "jump": num(r, "skok_rok_p50") if jump else None,
            "jumpLow": num(r, "skok_rok_p10") if jump else None,
            "jumpHigh": num(r, "skok_rok_p90") if jump else None,
            "event": text(r, "udalost").split(",")[0],
            "plain": text(plain, "jak_se_doslo"), "plainSrc": text(plain, "ze_zdroju"), "plainEst": text(plain, "odhad"),
        })
        value = curve(m)
        for year, key in ((2030, "p50_2030"), (2040, "p50_2040")):
            wanted = num(r, key)
            got = float(value[year - 2025])
            if not jump and abs(got - wanted) > max(25.0, 0.1 * abs(wanted)):
                fit_report.append((text(r, "polozka"), text(r, "cesta")[:4], year, round(wanted, 1), round(got, 1)))
    (HERE / "kontrola_krivek.txt").write_text(
        "Položky, kde S-křivka v milníku nesedí na tabulku o více než 10 % a 25 GWh:\n"
        + "\n".join(f"{a} | {b} | {c} | tabulka {d} | křivka {e}" for a, b, c, d, e in fit_report) + "\n",
        encoding="utf-8")
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
