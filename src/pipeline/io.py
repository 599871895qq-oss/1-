import csv
from pathlib import Path
from typing import List, Dict


FIELDS = ["date", "channel", "impressions", "clicks", "orders", "revenue", "spend"]


def load_csv(path: str) -> List[Dict[str, str]]:
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def save_csv(path: str, rows: List[Dict[str, object]], fieldnames: List[str]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def ensure_sample_raw(path: str) -> None:
    p = Path(path)
    if p.exists():
        return
    p.parent.mkdir(parents=True, exist_ok=True)
    rows = [
        {"date": "2026-04-01", "channel": "商品卡", "impressions": 10000, "clicks": 500, "orders": 40, "revenue": 8000, "spend": 2000},
        {"date": "2026-04-01", "channel": "短视频", "impressions": 20000, "clicks": 900, "orders": 55, "revenue": 10000, "spend": 2800},
        {"date": "2026-04-01", "channel": "直播", "impressions": 15000, "clicks": 700, "orders": 70, "revenue": 14000, "spend": 3500},
    ]
    save_csv(str(p), rows, FIELDS)
