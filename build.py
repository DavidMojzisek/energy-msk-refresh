"""Sestaví index.html ze šablony a dat. Spuštění: python3 build.py"""
import json
import re
from pathlib import Path

import numpy as np

from model import LOCAL_OTHER, LOSS_K, OWN_CAL, OWN_RATES, YEARS, curve, item_model, num, path_curves, read_drivers, read_rows, simulate_path, widen_band

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

NUMBERS = HERE  # kopie z hodinového výpočtu, přidává je nastroje/rebuild.sh


def must_rest(text):
    """Co musí přibýt k větru na mezi. Hodnota se nemění, jen se neopakuje vítr ze záhlaví sloupce."""
    rest = text.split(" a ", 1)[1]
    if rest in ("0,0 GWp FVE", "0 SMR"):
        return "nic dalšího"
    return "+" + rest.replace("GWp FVE", "GWp fotovoltaiky")


def html_must(rows):
    head = ("<tr><th>Období, které má vyjít bez schodku</th><th>Bilance 2050, GWh</th><th>Jen vítr navíc</th><th>Jen fotovoltaika navíc</th>"
            "<th>Jen SMR navíc, reaktory po 500 MW, bez podkladu</th><th>Vítr doplněný na mez 2 014 MW a k tomu, v ročním součtu</th></tr>")
    body = ""
    for r in rows:
        wind = f"+{r['vitr']} MW" + (", nad mezí" if r["vitr_nad"] else "")
        body += (f'<tr data-must="{r["cesta"]}"><td>{r["uroven"].capitalize()}</td><td class="n">{r["bilance"]}</td><td class="n">{wind}</td>'
                 f'<td class="n">+{r["fve"]} GWp</td><td class="n">+{r["smr"]}</td><td>{must_rest(r["mez"])}</td></tr>')
    return f'<table class="grades">{head}{body}</table>'


TEMPO_NAMES = {"Tabulka, progresivní": "Výchozí progresivní cesta", "Půl na půl pro úroveň 1": "Vítr a fotovoltaika půl na půl, vyrovnaný rok",
               "Vítr na mezi a zbytek FVE": "Vítr na mezi, zbytek fotovoltaika, rok vyrovnaný v hodinovém výpočtu", "Jen FVE": "Jen fotovoltaika, vyrovnaný rok"}


def html_tempo(rows, t):
    head = "<tr><th>Případ</th><th>Vítr 2050</th><th>Vítr za rok</th><th>Proti rekordu</th><th>Fotovoltaika 2050</th><th>Fotovoltaika za rok</th><th>Proti rekordu</th></tr>"
    body = "".join(f'<tr data-must="progresivni"><td>{TEMPO_NAMES[r["jmeno"]]}</td><td class="n">{r["vitr"]}</td><td class="n">{r["vitr_rok"]}</td><td class="n">{r["vitr_krat"]}</td><td class="n">{r["fve"]}</td><td class="n">{r["fve_rok"]}</td><td class="n">{r["fve_krat"]}</td></tr>' for r in rows)
    body += (f'<tr data-must="konzervativni"><td>Jen vítr, vyrovnaný rok</td><td class="n">{t["kv_vitr"]} MW</td><td class="n">{t["kv_tempo"]} MW</td><td class="n">{t["kv_krat"]} ×</td>'
             '<td class="n">žádná navíc</td><td class="n">žádná navíc</td><td class="n"></td></tr>')
    return f'<table class="grades">{head}{body}</table>'


def html_otevrene(rows):
    head = "<tr><th>Změna</th><th>Progresivní, GWh</th><th>Konzervativní, GWh</th></tr>"
    body = "".join(f'<tr><td>{r["jmeno"]}</td><td class="n">{r["prog"]}</td><td class="n">{r["kons"]}</td></tr>' for r in rows)
    return f'<table class="grades">{head}{body}</table>'


# Názvy řádků z přepočtu srozumitelně pro čtenáře stránky. Text a čísla za nimi zůstávají.
RADKY8_TEXT = {"Přiměřenost, LOLE.": "Přiměřenost soustavy.", "Regulace FVE.": "Regulace fotovoltaiky."}


def html_radky8(rows):
    def body(name, text):
        text = text.replace("Bez sazby výpadků ze zdroje se nepočítá.", "Očekávaná doba nedodávky (LOLE) se bez sazby výpadků ze zdroje nepočítá.").replace("roky FVE a tepla", "roky fotovoltaiky a tepla")
        return f"<li><b>{RADKY8_TEXT.get(name, name)}</b> {text}</li>"
    return "".join(body(*r) for r in rows)


NBSP_NUM = re.compile(r"(?<=\d)(?<!\d{4}) (?=\d{3}(?!\d))")
NBSP_UNIT = re.compile(r"(?<=\d) (?=(?:%|GWh|TWh|MWh|MWp|MW|GWp|kWh|t\b|h\b|×))")


def keep_together(html):
    """Číslo a jednotka se nesmí rozdělit na dva řádky. Jen v textu stránky, ne ve skriptu, stylech ani atributech značek."""
    head, sep, tail = html.partition("<script>")
    parts = re.split(r"(<style\b.*?</style>|<[^>]+>)", head, flags=re.S)
    parts[::2] = [NBSP_NUM.sub(" ", NBSP_UNIT.sub(" ", p)) for p in parts[::2]]
    return "".join(parts) + sep + tail


def html_urovne(m):
    body = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in m["urovne"])
    return f'<table class="grades"><tr><th>Úroveň</th><th>Co případ žádá</th></tr>{body}</table>'


def html_blackout(m):
    body = "".join(f"<tr><td>{a}</td><td>{b} <span class=\"zdroj\">Zdroj: {c}.</span></td><td>{d}</td></tr>" for a, b, c, d in m["blackout"])
    return f'<table class="grades"><tr><th>Skupina</th><th>Co se stane</th><th>Rozdíl mezi cestami</th></tr>{body}</table>'


ROZ_HEAD = ("Co nesedělo", "Velikost", "Jak se to vyřešilo", "Dopad na výsledek")


def html_rozpory():
    """Jediný zdroj je web/ROZPORY.md. Otevřené řádky jdou první a jsou označené, na telefonu se řádek skládá pod sebe."""
    rows = []
    for line in (HERE / "ROZPORY.md").read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.startswith("|") else []
        assert not cells or len(cells) == 4, line[:80]
        if len(cells) == 4 and cells[0] != ROZ_HEAD[0] and not set(cells[0]) <= {"-"}:
            rows.append(cells)
    assert rows
    opened = [r for r in rows if r[2].startswith("Nevyřešeno")]
    closed = [r for r in rows if r[2].startswith("Vyřešeno")]
    assert len(opened) + len(closed) == len(rows), "Řádek ROZPORY.md nezačíná slovem Nevyřešeno nebo Vyřešeno."

    def row(r, cls):
        return f'<tr class="{cls}">' + "".join(f'<td data-k="{h}">{c}</td>' for h, c in zip(ROZ_HEAD, r)) + "</tr>"
    head = "<tr>" + "".join(f"<th>{h}</th>" for h in ROZ_HEAD) + "</tr>"
    body = f'<tr class="skupina"><td colspan="4">Otevřené, {len(opened)}</td></tr>' + "".join(row(r, "otevreny") for r in opened)
    body += f'<tr class="skupina"><td colspan="4">Vyřešené, {len(closed)}</td></tr>' + "".join(row(r, "vyreseny") for r in closed)
    return f'<table class="grades rozpory"><thead>{head}</thead><tbody>{body}</tbody></table>'


def html_rezerva(table):
    hours = list(next(iter(table.values())))
    head = "<tr><th>Podíl zatížení</th>" + "".join(f"<th>{h}</th>" for h in hours) + "</tr>"
    body = "".join(f"<tr><td>{k}</td>" + "".join(f'<td class="n">{v[h]}</td>' for h in hours) + "</tr>" for k, v in table.items())
    return f'<table class="grades">{head}{body}</table>'


def fill_numbers(template):
    """Čísla z hodinového výpočtu jdou do textu stránky z jednoho souboru, který píše 60_prepocet_zprava.py."""
    data = json.loads((NUMBERS / "stranka_cisla.json").read_text(encoding="utf-8"))
    texty = json.loads((NUMBERS / "stranka_texty.json").read_text(encoding="utf-8"))
    t = dict(data["T"], **texty["T"])
    mez = next(r for r in data["tempo"] if r["jmeno"] == "Vítr na mezi a zbytek FVE")
    t = dict(t, mez_rok=mez["vitr_rok"].replace(" MW", ""), mez_krat=mez["vitr_krat"])
    values = dict(t, html_must=html_must(data["must"]), html_tempo=html_tempo(data["tempo"], t), html_rezerva=html_rezerva(data["rezerva"]),
                  html_otevrene=html_otevrene(texty["otevrene"]), html_radky8=html_radky8(texty["radky8"]), html_rozpory=html_rozpory(),
                  html_urovne=html_urovne(texty["metoda"]), html_blackout=html_blackout(texty["metoda"]), blackout_meritko=texty["metoda"]["meritko"], blackout_chybi=texty["metoda"]["chybi"])
    out = keep_together(re.sub(r"\{\{([a-z0-9_]+)\}\}", lambda m: values[m.group(1)], template))
    assert "{{" not in out, out[out.index("{{"):][:60]
    flh = json.loads((NUMBERS / "elektrolyzer_plne_hodiny.json").read_text(encoding="utf-8"))
    out, n = re.subn(r"ELECTROLYSER_HOURS\s*=\s*[\d.]+, ELECTROLYSER_LOSS\s*=\s*[\d.]+", f"ELECTROLYSER_HOURS = {flh['plne_hodiny']:.2f}, ELECTROLYSER_LOSS = {flh['mira_ztrat']:.6f}", out)
    assert n == 1
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
            last = chosen[-1]
            battery[route] = {"years": [int(r["rok"]) for r in chosen], "daily": [num(r, "leto_baterie_vykon_MW") for r in chosen], "boiler": [num(r, "leto_kotle_vykon_MW") for r in chosen],
                              "gasYears": [2025, 2027, 2030, 2031, 2035, 2050], "gasMw": [0, 0, 283, 433, 433, 433] if route == "progresivni" else [0, 0, 283, 433, 683, 683],
                              "cut": {"p50": num(last, "zima_snizeni_baterii_P50_MW"), "worst": num(last, "zima_snizeni_baterii_nejhorsi_MW")} if route == "progresivni" else None}
    rng = np.random.default_rng(20261104)
    items, bands, fit_report, fit_report_band = [], {}, [], []
    curves_by_path, gap_runs = {}, {}
    for route in PATHS:
        chosen = [(r, m) for r, m in zip(rows, models) if text(r, "cesta") == route]
        curves_by_path[route] = path_curves([c[0] for c in chosen], [c[1] for c in chosen])
        bands[route] = simulate_path([c[0] for c in chosen], [c[1] for c in chosen], rng, RUNS, sample=30)
        gap_runs[route] = bands[route].pop("mezera")
        bands[route]["spotreba"], ratio = widen_band(bands[route]["spotreba"], HINDCAST_WIDTH_2030)
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
        value = curves_by_path[text(r, "cesta")][text(r, "polozka")]
        for year, key in ((2030, "p50_2030"), (2040, "p50_2040")):
            wanted = num(r, key)
            got = float(value[year - 2025])
            if abs(got - wanted) > max(25.0, 0.1 * abs(wanted)):
                fit_report.append((text(r, "polozka"), text(r, "cesta")[:4], year, round(wanted, 1), round(got, 1)))
    (HERE / "kontrola_krivek.txt").write_text(
        "Položky, kde křivka v milníku nesedí na tabulku o více než 10 % a 25 GWh:\n"
        + "\n".join(f"{a} | {b} | {c} | tabulka {d} | křivka {e}" for a, b, c, d, e in fit_report) + "\n" + "\n".join(fit_report_band) + "\n",
        encoding="utf-8")
    trends = {}
    trend_path = HERE / "ridici_vlivy.csv"
    if trend_path.exists():
        for r in read_rows(trend_path):
            if text(r, "vliv") in TRENDS and text(r, "rok") == "2050":
                trends[text(r, "vliv")] = {"values": [round(float(v), 5) for v in drivers[text(r, "vliv")]], "p10": num(r, "p10"), "p90": num(r, "p90"),
                                           "grade": text(r, "stupen"), "src": text(r, "zdroj")}
    derived = {"ownCal": OWN_CAL, "ownRates": OWN_RATES, "lossK": LOSS_K, "localOther": LOCAL_OTHER}
    return {"years": YEARS.tolist(), "history": HISTORY, "items": items, "bands": bands, "battery": battery, "trends": trends, "derived": derived, "gapRuns": gap_runs,
            "den": json.loads((HERE / "stranka_texty.json").read_text(encoding="utf-8"))["den"], "real": json.loads((HERE / "realisticky.json").read_text(encoding="utf-8")),
            "ekon": json.loads((HERE / "ekonomika.json").read_text(encoding="utf-8"))}


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
