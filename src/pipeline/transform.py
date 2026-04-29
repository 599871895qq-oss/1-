from typing import Dict, List
from src.metrics.core import ctr, cr, roi


def compute_metrics(rows: List[Dict[str, str]]) -> List[Dict[str, object]]:
    out = []
    for r in rows:
        impressions = float(r["impressions"])
        clicks = float(r["clicks"])
        orders = float(r["orders"])
        revenue = float(r["revenue"])
        spend = float(r["spend"])
        out.append(
            {
                **r,
                "ctr": round(ctr(clicks, impressions), 4),
                "cr": round(cr(orders, clicks), 4),
                "roi": round(roi(revenue, spend), 4),
            }
        )
    return out


def aggregate_summary(rows: List[Dict[str, object]]) -> Dict[str, float]:
    impressions = sum(float(r["impressions"]) for r in rows)
    clicks = sum(float(r["clicks"]) for r in rows)
    orders = sum(float(r["orders"]) for r in rows)
    revenue = sum(float(r["revenue"]) for r in rows)
    spend = sum(float(r["spend"]) for r in rows)
    return {
        "impressions": impressions,
        "clicks": clicks,
        "orders": orders,
        "revenue": revenue,
        "spend": spend,
        "ctr": round(ctr(clicks, impressions), 4),
        "cr": round(cr(orders, clicks), 4),
        "roi": round(roi(revenue, spend), 4),
    }
