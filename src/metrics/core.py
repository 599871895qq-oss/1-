"""Core ecommerce metric calculations."""


def safe_divide(numerator: float, denominator: float) -> float:
    """Return numerator / denominator; returns 0.0 when denominator is 0."""
    if denominator == 0:
        return 0.0
    return numerator / denominator


def ctr(clicks: float, impressions: float) -> float:
    """Click-through rate: clicks / impressions."""
    return safe_divide(clicks, impressions)


def cr(orders: float, clicks: float) -> float:
    """Conversion rate: orders / clicks."""
    return safe_divide(orders, clicks)


def roi(revenue: float, spend: float) -> float:
    """Return on investment: revenue / spend."""
    return safe_divide(revenue, spend)
