"""Sestaví index.html stránky grafů z grafy.json. Spuštění: python3 -B build.py. Stránka čísla jen čte a kreslí, výsledky v šabloně nejsou."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
DATA = ROOT / "graf_scenare/hodinovy_model/podscenare/grafy.json"


def main():
    data = json.load(open(DATA, encoding="utf-8"))
    current = hashlib.sha256(open(ROOT / "graf_scenare/polozky.csv", "rb").read()).hexdigest()
    if data.pop("tabulkaSha") != current:
        raise SystemExit("Tabulka položek se změnila, nejdřív spusťte predpocet.py.")
    template = (HERE / "sablona_grafy.html").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = template.replace("/*DATA*/null", payload)
    (HERE / "index.html").write_text(page, encoding="utf-8")
    print(f"index.html {len(page.encode('utf-8')) // 1024} kB")


if __name__ == "__main__":
    main()
