"""Sestaví index.html: toky elektřiny pro každý rok, cestu a okamžik.

Spuštění: python3 -B build.py
Čte tabulky ve složce web/ a logikou funkce moment() ze šablony hlavní stránky počítá MW.
Do web/ mimo tuto složku nezapisuje. Stránka sama už nic nepočítá, jen kreslí.
"""
import csv
import importlib.util
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
WEB = HERE.parent.parent
sys.path.insert(0, str(WEB))

import numpy as np  # noqa: E402

from model import YEARS, item_model, num, read_drivers, read_rows, s_curve  # noqa: E402

spec = importlib.util.spec_from_file_location("hlavni_build", WEB / "build.py")
hlavni = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hlavni)

PATHS = ["progresivni", "konzervativni"]
MOMENTS = ["rocni", "zima", "leto"]
SMR = "SMR"
TOLERANCE_MW = 1.0

SOURCES = [
    ("smr", "Malé reaktory SMR", "SMR", "atom", "#2fe6d8", [SMR]),
    ("slunce", "Fotovoltaika", "Slunce", "sun", "#ffb81c", ["fotovoltaika střešní", "fotovoltaika pozemní"]),
    ("vitr", "Vítr", "Vítr", "wind", "#3ddc97", ["vítr"]),
    ("voda", "Malé vodní zdroje", "Voda", "drop", "#4aa3ff", ["malé vodní elektrárny", "geotermální energie"]),
    ("biomasa", "Biomasa a bioplyn", "Biomasa", "leaf", "#a3e635", ["biomasa", "bioplyn"]),
    ("odpad", "Využití odpadu", "Odpad", "bin", "#e0a36b", ["energetické využití odpadu"]),
    ("plyn", "Plyny", "Plyny", "flame", "#b7a6e8",
     ["zemní plyn: stávající kogenerace", "nové plynové bloky", "syntetický plyn z odpadu",
      "hutní plyny (vysokopecní a koksárenský)", "důlní plyn"]),
    ("uhli", "Uhlí a paliva", "Uhlí", "coal", "#94a3b8",
     ["černé uhlí: Dětmarovice", "černé uhlí: teplárny a průmysl", "hnědé uhlí",
      "ostatní paliva a odpadní teplo (přidaná položka)", "baterie", "jiné skladování", "vodík zpět na elektřinu"]),
]
CONSUMERS = [
    ("prumysl", "Průmysl", "Průmysl", "factory", ["Třinecké železárny", "Nová huť", "ostatní průmysl a chemie", "doly"]),
    ("domacnosti", "Domácnosti", "Domácnosti", "house", ["domácnosti bez vytápění"]),
    ("sluzby", "Služby a ostatní", "Služby", "office",
     ["služby a veřejný sektor", "zemědělství a stavebnictví", "datacentra", "úspory a účinnost"]),
    ("teplo", "Teplo a chlazení", "Teplo", "heat",
     ["vytápění tepelnými čerpadly", "přímotopy", "elektrokotle v teplárnách", "chlazení"]),
    ("doprava", "Doprava", "Doprava", "train", ["osobní auta", "nákladní doprava", "vlaky", "MHD"]),
    ("energetika", "Energetika", "Energetika", "bolt",
     ["vlastní spotřeba zdrojů", "ostatní energetika (přidaná položka)", "ztráty v sítích"]),
]
FULL_NAMES = {
    "smr": "Malé jaderné reaktory SMR", "voda": "Malé vodní elektrárny a geotermální energie",
    "odpad": "Energetické využití odpadu", "uhli": "Uhlí a ostatní paliva", "teplo": "Vytápění a chlazení",
    "doprava": "Doprava na elektřinu", "energetika": "Energetika a ztráty", "flotila": "Flotila a další odběr vodíku",
}
BOILER = "elektrokotle v teplárnách"
BATTERY_LOSS = "ztráty baterií"
HYDROGEN = ["výroba vodíku: MHD", "výroba vodíku: nákladní doprava", "výroba vodíku: osobní auta",
            "výroba vodíku", "výroba syntetického plynu"]
FLEET_PREFIX = "výroba vodíku: "

ITEM_LABELS = {
    "výroba vodíku": "Vodík mimo flotilu",
    "výroba vodíku: MHD": "Vodík pro MHD",
    "výroba vodíku: nákladní doprava": "Vodík pro nákladní dopravu",
    "výroba vodíku: osobní auta": "Vodík pro osobní auta",
    "výroba syntetického plynu": "Syntetický plyn",
    "úspory a účinnost": "Úspory a účinnost, snižují spotřebu",
}


def text(row, key):
    return (row.get(key) or "").strip()


def label(name):
    if name in ITEM_LABELS:
        return ITEM_LABELS[name]
    plain = name.replace(" (přidaná položka)", "")
    return plain[0].upper() + plain[1:]


def page_items():
    """Položky přesně tak, jak je dostane hlavní stránka, včetně zaokrouhlení a sdílených roků událostí."""
    rows = read_rows(WEB / "polozky.csv")
    drivers = read_drivers(WEB / "ridici_vlivy.csv")
    season = {(text(r, "polozka"), text(r, "cesta")): r for r in read_rows(WEB / "sezonni_profily.csv")}
    items = []
    for row in rows:
        model = item_model(row, drivers)
        profile = season.get((text(row, "polozka"), text(row, "cesta")), {})
        items.append({
            "name": text(row, "polozka"), "side": text(row, "strana"), "path": text(row, "cesta"),
            "base": model["base"], "p10": num(row, "p10_2050"), "p50": num(row, "p50_2050"),
            "parts": [{"amp": round(p["amp"], 3), "tm": round(p["tm"], 2), "k": round(p["k"], 3)} for p in model["parts"]],
            "driver": [round(float(v), 4) for v in model["driver"]] if text(row, "ridic") else None,
            "jump": num(row, "skok_rok_p50") if model["jump"] else None,
            "event": text(row, "udalost").split(",")[0],
            "kw": num(profile, "zima_koef_p50") or 0, "ks": num(profile, "leto_koef_p50") or 0,
            "flex": text(profile, "flexibilni") == "ano",
        })
    smr_main = next(it for it in items if it["name"] == SMR and it["path"] == "progresivni")
    jumps = {}
    for it in items:
        if it["name"] == SMR and it["path"] != "progresivni":
            it["kw"], it["ks"] = smr_main["kw"], smr_main["ks"]
        share = f'{it["path"]}|{it["event"]}' if it["event"] else f'{it["path"]}|{it["side"]}|{it["name"]}'
        it["jump_key"] = share
        if it["jump"] is not None:
            jumps[share] = it["jump"]
        elif it["name"] == SMR:
            jumps[share] = smr_main["jump"]
    return items, jumps


def item_gwh(it, jumps, index):
    year = float(YEARS[index])
    if it["name"] == SMR:
        return it["p50"] * float(s_curve(year, jumps[it["jump_key"]], 4))
    driver = it["driver"][index] if it["driver"] else 1.0
    level = it["base"]
    for part in it["parts"]:
        tm = jumps[it["jump_key"]] if it["jump"] is not None else part["tm"]
        level += part["amp"] * float(s_curve(year, tm, part["k"]))
    value = driver * level
    return value if it["p10"] < 0 else max(0.0, value)


def electrolyser_hours():
    source = (WEB / "sablona.html").read_text(encoding="utf-8")
    found = re.search(r"ELECTROLYSER_HOURS\s*=\s*([\d.]+)", source)
    if not found:
        raise SystemExit("V šabloně chybí plné hodiny elektrolyzéru.")
    return float(found.group(1))


def battery_tables():
    rows = read_rows(WEB / "sezonni_kontrola.csv")
    table = {}
    for path in PATHS:
        chosen = [r for r in rows if text(r, "cesta") == path]
        table[path] = {
            "years": [int(r["rok"]) for r in chosen],
            "mw": [num(r, "zima_baterie_MW") for r in chosen],
            "hours": {int(r["rok"]): num(r, "zima_baterie_vydrz_h") for r in chosen},
            "daily": hlavni.BATTERY_DAILY[path],
        }
    return table


def hourly_store():
    """Velikost zásoby z hodinového výpočtu pro progresivní cestu v roce 2050, pokud soubor existuje."""
    path = WEB.parent / "graf_scenare" / "hodinovy_model" / "vysledky" / "doporuceni_mixy.csv"
    if not path.exists():
        return None
    with open(path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            if row.get("mix") == "SMR1":
                return {"t": float(row["sklad_t"]), "batteryGWh": float(row["baterie_E_GWh"])}
    return None


def assign_rows(items):
    owners = {}
    for node_id, _, _, _, _, names in SOURCES:
        owners.update({("vyroba", n): node_id for n in names})
    for node_id, _, _, _, names in CONSUMERS:
        owners.update({("spotreba", n): node_id for n in names})
    owners[("spotreba", BATTERY_LOSS)] = "baterie"
    owners.update({("spotreba", n): "elektrolyzer" for n in HYDROGEN})
    missing = sorted({it["name"] for it in items if (it["side"], it["name"]) not in owners})
    if missing:
        raise SystemExit("Položky bez uzlu: " + ", ".join(missing))
    return owners


def graph():
    nodes = [{"id": i, "label": a, "short": b, "icon": c, "color": d, "kind": "source"} for i, a, b, c, d, _ in SOURCES]
    nodes += [{"id": i, "label": a, "short": b, "icon": c, "color": "#ffcf5c", "kind": "consumer"} for i, a, b, c, _ in CONSUMERS]
    nodes += [
        {"id": "sit", "label": "Síť mimo kraj", "short": "Síť", "icon": "pylon", "color": "#ff6b6b", "kind": "grid"},
        {"id": "baterie", "label": "Baterie", "short": "Baterie", "icon": "battery", "color": "#a08cff", "kind": "store"},
        {"id": "elektrolyzer", "label": "Elektrolyzér", "short": "Elektrolyzér", "icon": "cell", "color": "#f08cb4", "kind": "store"},
        {"id": "nadrz", "label": "Nádrž na vodík", "short": "Nádrž", "icon": "tank", "color": "#2fe0b0", "kind": "store"},
        {"id": "flotila", "label": "Flotila na vodík", "short": "Flotila", "icon": "truck", "color": "#2fe0b0", "kind": "fleet"},
    ]
    for node in nodes:
        node["full"] = FULL_NAMES.get(node["id"], node["label"])
    edges = [{"id": n["id"], "from": n["id"], "to": "kraj", "color": n["color"], "kind": "in"} for n in nodes if n["kind"] == "source"]
    edges += [{"id": n["id"], "from": "kraj", "to": n["id"], "color": "#ffcf5c", "kind": "out"} for n in nodes if n["kind"] == "consumer"]
    edges += [
        {"id": "dovoz", "from": "sit", "to": "kraj", "color": "#ff6b6b", "kind": "import"},
        {"id": "vyvoz", "from": "kraj", "to": "sit", "color": "#7dd3fc", "kind": "export"},
        {"id": "kBaterie", "from": "kraj", "to": "baterie", "color": "#a08cff", "kind": "down"},
        {"id": "kElektrolyzer", "from": "kraj", "to": "elektrolyzer", "color": "#f08cb4", "kind": "down"},
        {"id": "h2Nadrz", "from": "elektrolyzer", "to": "nadrz", "color": "#2fe0b0", "kind": "chain"},
        {"id": "h2Flotila", "from": "nadrz", "to": "flotila", "color": "#2fe0b0", "kind": "chain"},
    ]
    return nodes, edges


def state_for(path, moment, index, items, jumps, owners, table, hours, node_items):
    """Toky v MW pro jeden rok, cestu a okamžik. Zima a léto odpovídají moment() ze šablony."""
    rows = [(it, item_gwh(it, jumps, index)) for it in items if it["path"] == path]
    avg = lambda g: g * 1000 / 8760
    coef = (lambda it: it["kw"]) if moment == "zima" else (lambda it: it["ks"])
    values = {key: {} for key in node_items}
    avail = load = electro = boiler = 0.0
    year = int(YEARS[index])

    for it, gwh in rows:
        owner = owners[(it["side"], it["name"])]
        if it["side"] == "vyroba":
            mw = avg(gwh) if moment == "rocni" else avg(gwh) * coef(it)
            avail += mw
        else:
            if moment == "rocni":
                mw = avg(gwh)
            elif moment == "zima" or not it["flex"]:
                mw = avg(gwh) * coef(it)
            else:
                mw = 0.0
            load += mw
            if it["name"].startswith(FLEET_PREFIX):
                electro += gwh * 1000 / hours
            if it["name"] == BOILER and moment != "rocni":
                boiler = avg(gwh) * it["ks"]
        values[owner][it["name"]] = values[owner].get(it["name"], 0.0) + mw

    bat = table[path]
    battery_mw = float(np.interp(year, bat["years"], bat["mw"]))
    daily = float(np.interp(year, bat["years"], bat["daily"]))
    balance = avail - load
    surplus = max(balance, 0.0)
    if moment == "rocni":
        charge = heat = for_h2 = 0.0
        spare = surplus
    else:
        charge = min(daily, surplus)
        heat = min(boiler, surplus - charge)
        for_h2 = min(max(surplus - charge - heat, 0.0), electro)
        spare = max(surplus - charge - heat - for_h2, 0.0)
    values["teplo"][BOILER] = values["teplo"].get(BOILER, 0.0) + heat

    # Elektřina pro vodík v tomto okamžiku: pevná část řádků plus podíl z přebytku.
    h2_rows = sum(values["elektrolyzer"].values())
    h2_in = h2_rows + for_h2
    # Flotila bere vodík rovnoměrně po celý rok, proto je odběr z nádrže roční průměr řádků.
    draw_items = {it["name"]: avg(gwh) for it, gwh in rows if it["name"] in HYDROGEN}
    draw = sum(draw_items.values())
    tank_delta = h2_in - draw
    battery_loss = sum(values["baterie"].values())
    battery_in = battery_loss + charge

    flows = {}
    for node_id, *_ in SOURCES:
        flows[node_id] = sum(values[node_id].values())
    for node_id, *_ in CONSUMERS:
        flows[node_id] = sum(values[node_id].values())
    flows["dovoz"] = max(-balance, 0.0)
    flows["vyvoz"] = spare
    flows["kBaterie"] = battery_in
    flows["kElektrolyzer"] = h2_in
    flows["h2Nadrz"] = h2_in
    flows["h2Flotila"] = draw

    meta = {
        "avail": avail, "load": load, "balance": balance, "surplus": surplus,
        "batteryMw": battery_mw, "batteryH": bat["hours"].get(year), "daily": daily,
        "electro": electro, "charge": charge, "heat": heat, "forH2": for_h2, "spare": spare,
        "draw": draw, "tankDelta": tank_delta, "batteryLoss": battery_loss, "import": flows["dovoz"],
    }
    return flows, values, draw_items, meta


def residuals(flows, values, draw_items, meta):
    """Reziduál každého uzlu v MW: vše, co přitéká, minus vše, co odtéká nebo se ukládá."""
    out = {}
    source_sum = sum(flows[s[0]] for s in SOURCES)
    consumer_sum = sum(flows[c[0]] for c in CONSUMERS)
    out["kraj"] = source_sum + flows["dovoz"] - consumer_sum - flows["kBaterie"] - flows["kElektrolyzer"] - flows["vyvoz"]
    out["baterie"] = flows["kBaterie"] - meta["charge"] - meta["batteryLoss"]
    out["elektrolyzer"] = flows["kElektrolyzer"] - flows["h2Nadrz"]
    out["nadrz"] = flows["h2Nadrz"] - flows["h2Flotila"] - meta["tankDelta"]
    out["flotila"] = flows["h2Flotila"] - sum(draw_items.values())
    for node_id, *_ in SOURCES + CONSUMERS:
        out[node_id] = flows[node_id] - sum(values[node_id].values())
    return out


def clean(value):
    return round(float(value), 3)


def build_data():
    items, jumps = page_items()
    owners = assign_rows(items)
    table = battery_tables()
    hours = electrolyser_hours()
    nodes, edges = graph()
    names = {n["id"]: [] for n in nodes}
    for it in items:
        owner = owners[(it["side"], it["name"])]
        if it["name"] not in names[owner]:
            names[owner].append(it["name"])
    node_items = {key: names[key] for key in names}
    for node in nodes:
        node["items"] = [label(n) for n in names[node["id"]]]
    fleet_names = [n for n in HYDROGEN if any(it["name"] == n for it in items)]
    fleet_node = next(n for n in nodes if n["id"] == "flotila")
    fleet_node["items"] = [label(n) for n in fleet_names]

    states, worst = {}, (0.0, None)
    first_surplus = {}
    for path in PATHS:
        states[path] = {}
        first_surplus[path] = None
        for moment in MOMENTS:
            series = []
            for index, year in enumerate(YEARS):
                flows, values, draw_items, meta = state_for(path, moment, index, items, jumps, owners, table, hours, node_items)
                for node_id, gap in residuals(flows, values, draw_items, meta).items():
                    if abs(gap) > worst[0]:
                        worst = (abs(gap), (path, moment, int(year), node_id))
                if min(flows.values()) < -1e-9:
                    raise SystemExit(f"Záporný tok: {path} {moment} {year}")
                if moment == "leto" and meta["surplus"] > 0.5 and first_surplus[path] is None:
                    first_surplus[path] = int(year)
                item_values = {key: [clean(values[key].get(n, 0.0)) for n in node_items[key]]
                               for key in node_items if node_items[key]}
                item_values["flotila"] = [clean(draw_items.get(n, 0.0)) for n in fleet_names]
                series.append({
                    "e": [clean(flows[e["id"]]) for e in edges],
                    "i": item_values,
                    "m": {k: (None if v is None else clean(v)) for k, v in meta.items()},
                })
            states[path][moment] = series
    if worst[0] > TOLERANCE_MW:
        raise SystemExit(f"Bilance uzlu nesedí o {worst[0]:.3f} MW: {worst[1]}")
    print(f"Největší reziduál uzlu před zaokrouhlením: {worst[0]:.6f} MW")
    return {
        "years": [int(y) for y in YEARS], "nodes": nodes, "edges": edges, "states": states,
        "firstSurplus": first_surplus, "electrolyserHours": hours, "store": hourly_store(),
    }


def main():
    template = (HERE / "sablona_toky.html").read_text(encoding="utf-8")
    fonts = (WEB / "fonts.css").read_text(encoding="utf-8")
    payload = json.dumps(build_data(), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = template.replace("/*FONTS*/", fonts).replace("/*DATA*/null", payload)
    (HERE / "index.html").write_text(page, encoding="utf-8")
    print(f"index.html: {len(page.encode('utf-8')) // 1024} kB")


if __name__ == "__main__":
    main()
