"""Sestaví index.html z předpočítané mřížky hodinového modelu. Spuštění: python3 -B build.py
Stránka nic nepočítá, jen vybírá nejbližší spočítaný stav. Čísla se čtou z mrizka.json, které píše graf_scenare/hodinovy_model/podscenare/predpocet.py."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
WEB = HERE.parent.parent
ROOT = WEB.parent
GRID = ROOT / "graf_scenare/hodinovy_model/podscenare/mrizka.json"


def main():
    data = json.load(open(GRID, encoding="utf-8"))
    current = hashlib.sha256(open(ROOT / "graf_scenare/polozky.csv", "rb").read()).hexdigest()
    if data.pop("tabulkaSha") != current:
        raise SystemExit("Tabulka položek se změnila, nejdřív spusťte predpocet.py.")
    template = (HERE / "sablona_toky.html").read_text(encoding="utf-8")
    fonts = (WEB / "fonts.css").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = template.replace("/*FONTS*/", fonts).replace("/*DATA*/null", payload)
    (HERE / "index.html").write_text(page, encoding="utf-8")
    print(f"index.html {len(page.encode('utf-8')) // 1024} kB, data {len(payload.encode('utf-8')) // 1024} kB")


if __name__ == "__main__":
    main()
