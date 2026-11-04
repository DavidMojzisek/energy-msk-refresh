"""Sestaví index.html ze šablony a dat. Spuštění: python3 build.py"""
import json
import re
from pathlib import Path

import numpy as np

from model import YEARS, curve, item_model, num, read_drivers, read_rows, simulate, widen_band

HERE = Path(__file__).resolve().parent
PATHS = ["progresivni", "konzervativni"]
RUNS = 10000
# Pozorované rozpětí pětileté změny čisté spotřeby MSK 2014 až 2025: -8,3 % až +12,3 %, tedy 20,6 procentního bodu (Dopadová studie Tab.14 s.54, ERÚ tab. 6.2).
HINDCAST_WIDTH_2030 = 0.206

# Skutečnost v GWh. Výroba je brutto, spotřeba je součet sektorů plus ztráty v sítích.
# 2023: výroba ERÚ Roční zpráva, sektory Dopadová studie Tab. 6, ztráty 6 018,9 - 5 805,4 z Tab. 1.
# 2024 a 2025: čtvrtletní zprávy ERÚ, ztráty jsou netto z tab. 6.2 × 3,547 % / (1 - 3,547 %).
LOSS = 0.03547 / (1 - 0.03547)
HISTORY = [
    {"y": 2023, "gen": 3703.2208, "use": 7090.2833 + 213.5},
    {"y": 2024, "gen": 3052.3406, "use": 6810.1894 + 5931.2084 * LOSS},
    {"y": 2025, "gen": 2805.1634, "use": 7069.9644},
]


TRENDS = ("pop_msk", "velikost_dom", "auta_na_os", "eff_auta", "eff_nakladni", "teplo_budovy")

# Denní nabíjení baterií v MW v letech 2025, 2030, 2040 a 2050, viz sezonni_metodika.md.
BATTERY_DAILY = {"progresivni": [2.0, 10.0, 425.0, 750.0], "konzervativni": [2.0, 2.0, 2.0, 2.0]}
NUMBERS = HERE  # kopie z hodinového výpočtu, přidává je nastroje/rebuild.sh


def html_must(rows):
    head = "<tr><th>Cesta a období</th><th>Bilance dnes, GWh</th><th>Jen vítr navíc</th><th>Jen fotovoltaika navíc</th><th>Jen SMR navíc</th><th>Vítr na mezi 2 014 MW a</th></tr>"
    name = {"progresivni": "Progresivní", "konzervativni": "Konzervativní"}
    body = ""
    for r in rows:
        wind = f"+{r['vitr']} MW" + (", nad mezí" if r["vitr_nad"] else "")
        body += (f'<tr data-must="{r["cesta"]}"><td>{name[r["cesta"]]}, {r["uroven"]}</td><td class="n">{r["bilance"]}</td><td class="n">{wind}</td>'
                 f'<td class="n">+{r["fve"]} GWp</td><td class="n">+{r["smr"]}</td><td>{r["mez"]}</td></tr>')
    return f'<table class="grades">{head}{body}</table>'


def html_tempo(rows):
    head = "<tr><th>Případ</th><th>Vítr 2050</th><th>Vítr za rok</th><th>Proti maximu</th><th>Fotovoltaika 2050</th><th>Fotovoltaika za rok</th><th>Proti maximu</th></tr>"
    body = "".join(f'<tr><td>{r["jmeno"]}</td><td class="n">{r["vitr"]}</td><td class="n">{r["vitr_rok"]}</td><td class="n">{r["vitr_krat"]}</td><td class="n">{r["fve"]}</td><td class="n">{r["fve_rok"]}</td><td class="n">{r["fve_krat"]}</td></tr>' for r in rows)
    return f'<table class="grades">{head}{body}</table>'


def html_rezerva(table):
    hours = list(next(iter(table.values())))
    head = "<tr><th>Podíl zatížení</th>" + "".join(f"<th>{h}</th>" for h in hours) + "</tr>"
    body = "".join(f"<tr><td>{k}</td>" + "".join(f'<td class="n">{v[h]}</td>' for h in hours) + "</tr>" for k, v in table.items())
    return f'<table class="grades">{head}{body}</table>'


def fill_numbers(template):
    """Čísla z hodinového výpočtu jdou do textu stránky z jednoho souboru, který píše 60_prepocet_zprava.py."""
    data = json.loads((NUMBERS / "stranka_cisla.json").read_text(encoding="utf-8"))
    values = dict(data["T"], html_must=html_must(data["must"]), html_tempo=html_tempo(data["tempo"]), html_rezerva=html_rezerva(data["rezerva"]))
    out = re.sub(r"\{\{([a-z0-9_]+)\}\}", lambda m: values[m.group(1)], template)
    assert "{{" not in out, out[out.index("{{"):][:60]
    flh = json.loads((NUMBERS / "elektrolyzer_plne_hodiny.json").read_text(encoding="utf-8"))
    found = re.search(r"ELECTROLYSER_HOURS\s*=\s*([\d.]+), ELECTROLYSER_LOSS\s*=\s*([\d.]+)", template)
    assert abs(float(found.group(1)) - flh["plne_hodiny"]) < 0.5, ("ELECTROLYSER_HOURS", flh["plne_hodiny"])
    assert abs(float(found.group(2)) - flh["mira_ztrat"]) < 1e-5, ("ELECTROLYSER_LOSS", flh["mira_ztrat"])
    return out


def text(row, key):
    return (row.get(key) or "").strip()


def build_data():
    path = HERE / "polozky.csv"
    rows = read_rows(path) if path.exists() else []
    drivers = read_drivers(HERE / "ridici_vlivy.csv")
    models = [item_model(r, drivers) for r in rows]
    popis_path = HERE / "polozky_popis.csv"
    popis = {(text(r, "polozka"), text(r, "cesta")): r for r in read_rows(popis_path)} if popis_path.exists() else {}
    profile_path = HERE / "sezonni_profily.csv"
    profiles = {(text(r, "polozka"), text(r, "cesta")): r for r in read_rows(profile_path)} if profile_path.exists() else {}
    check_path = HERE / "sezonni_kontrola.csv"
    battery = {}
    if check_path.exists():
        for route in PATHS:
            chosen = [r for r in read_rows(check_path) if text(r, "cesta") == route]
            battery[route] = {"years": [int(r["rok"]) for r in chosen], "mw": [num(r, "zima_baterie_MW") for r in chosen],
                              "daily": BATTERY_DAILY[route]}
    rng = np.random.default_rng(20261104)
    items, bands, fit_report, fit_report_band = [], {}, [], []
    for route in PATHS:
        bands[route] = {}
        for side in ("vyroba", "spotreba"):
            chosen = [(r, m) for r, m in zip(rows, models) if text(r, "cesta") == route and text(r, "strana") == side]
            if chosen:
                bands[route][side] = simulate([c[0] for c in chosen], [c[1] for c in chosen], rng, RUNS)
                if side == "spotreba":
                    bands[route][side], ratio = widen_band(bands[route][side], HINDCAST_WIDTH_2030)
                    fit_report_band.append(f"{route}: násobek pásma spotřeby 2030 {ratio:.3f}")
    for r, m in zip(rows, models):
        jump = m["jump"]
        plain = popis.get((text(r, "polozka"), text(r, "cesta")), {})
        season = profiles.get((text(r, "polozka"), text(r, "cesta")), {})
        driver = None if not text(r, "ridic") else [round(float(v), 9) for v in m["driver"]]
        items.append({
            "name": text(r, "polozka"), "side": text(r, "strana"), "path": text(r, "cesta"),
            "base": m["base"], "p10": num(r, "p10_2050"), "p50": num(r, "p50_2050"), "p90": num(r, "p90_2050"),
            "parts": [dict({"amp": round(p["amp"], 9), "tm": round(p["tm"], 9), "k": round(p["k"], 9)}, **{x: p[x] for x in ("hard", "cap") if x in p}) for p in m["parts"]],
            "nodes": m["nodes"],
            "driver": driver, "driverName": text(r, "ridic"), "maxRate": num(r, "tempo_max_GWh_rok"),
            "grade": text(r, "stupen"), "how": text(r, "odvozeni"), "src": text(r, "zdroj"), "note": text(r, "poznamka"),
            "page": text(r, "strana_studie"), "quote": text(r, "citace"),
            "jump": num(r, "skok_rok_p50") if jump else None,
            "jumpLow": num(r, "skok_rok_p10") if jump else None,
            "jumpHigh": num(r, "skok_rok_p90") if jump else None,
            "event": text(r, "udalost").split(",")[0],
            "plain": text(plain, "jak_se_doslo"), "plainSrc": text(plain, "ze_zdroju"), "plainEst": text(plain, "odhad"),
            "kw": num(season, "zima_koef_p50") or 0, "ks": num(season, "leto_koef_p50") or 0, "flex": text(season, "flexibilni") == "ano",
        })
        value = curve(m)
        for year, key in ((2030, "p50_2030"), (2040, "p50_2040")):
            wanted = num(r, key)
            got = float(value[year - 2025])
            if not jump and abs(got - wanted) > max(25.0, 0.1 * abs(wanted)):
                fit_report.append((text(r, "polozka"), text(r, "cesta")[:4], year, round(wanted, 1), round(got, 1)))
    (HERE / "kontrola_krivek.txt").write_text(
        "Položky, kde S-křivka v milníku nesedí na tabulku o více než 10 % a 25 GWh:\n"
        + "\n".join(f"{a} | {b} | {c} | tabulka {d} | křivka {e}" for a, b, c, d, e in fit_report) + "\n" + "\n".join(fit_report_band) + "\n",
        encoding="utf-8")
    trends = {}
    trend_path = HERE / "ridici_vlivy.csv"
    if trend_path.exists():
        for r in read_rows(trend_path):
            if text(r, "vliv") in TRENDS and text(r, "rok") == "2050":
                trends[text(r, "vliv")] = {"values": [round(float(v), 5) for v in drivers[text(r, "vliv")]], "p10": num(r, "p10"), "p90": num(r, "p90"),
                                           "grade": text(r, "stupen"), "src": text(r, "zdroj")}
    return {"years": YEARS.tolist(), "history": HISTORY, "items": items, "bands": bands, "battery": battery, "trends": trends}


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
    page = fill_numbers(template).replace("/*FONTS*/", fonts_css()).replace("/*DATA*/null", payload)
    (HERE / "index.html").write_text(page, encoding="utf-8")


if __name__ == "__main__":
    main()
