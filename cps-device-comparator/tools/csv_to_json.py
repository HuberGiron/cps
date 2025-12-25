#!/usr/bin/env python3
"""
Convierte data/devices.csv a data/devices.json (con IDs y rutas de imagen/datasheet).
Uso:
  python tools/csv_to_json.py
"""
from __future__ import annotations
import csv, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "devices.csv"
JSON_PATH = ROOT / "data" / "devices.json"

def slugify(s: str) -> str:
    s = s.lower()
    s = s.replace("–","-").replace("—","-").replace("‑","-").replace("−","-").replace("×","x")
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"[\s_]+", "-", s.strip())
    s = re.sub(r"-{2,}", "-", s)
    return s.strip("-")

def main() -> None:
    if not CSV_PATH.exists():
        raise SystemExit(f"No existe {CSV_PATH}")

    devices = []
    seen = {}
    with CSV_PATH.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required = {"model","category","frequency","ram","storage","protocols","io"}
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise SystemExit(f"Faltan columnas en CSV: {sorted(missing)}")

        for row in reader:
            model = (row.get("model") or "").strip()
            if not model:
                continue
            category = (row.get("category") or "").strip()

            base = slugify(model)
            if base in seen:
                # desambiguar con categoría o sufijo incremental
                cat = slugify(category) or "extra"
                cand = f"{base}-{cat}"
                if cand in seen:
                    i = 2
                    while f"{base}-{i}" in seen:
                        i += 1
                    dev_id = f"{base}-{i}"
                else:
                    dev_id = cand
            else:
                dev_id = base
            seen[dev_id] = True

            img = (row.get("image") or "").strip() or f"assets/img/{dev_id}.svg"
            pdf = (row.get("datasheet") or "").strip() or f"datasheets/{dev_id}.pdf"

            devices.append({
                "id": dev_id,
                "model": model,
                "category": category,
                "frequency": (row.get("frequency") or "").strip(),
                "ram": (row.get("ram") or "").strip(),
                "storage": (row.get("storage") or "").strip(),
                "protocols": (row.get("protocols") or "").strip(),
                "io": (row.get("io") or "").strip(),
                "image": img,
                "datasheet": pdf
            })

    JSON_PATH.write_text(json.dumps({"version": 1, "devices": devices}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK: {JSON_PATH} ({len(devices)} dispositivos)")

if __name__ == "__main__":
    main()
