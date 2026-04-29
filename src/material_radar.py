from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Optional


@dataclass(frozen=True)
class VideoMaterial:
    video_id: str
    title: str
    product: str
    category: str
    likes: int
    comments: int
    shares: int
    views: int
    completion_rate: float
    growth_7d: float


@dataclass(frozen=True)
class ScoreWeights:
    like_rate: float = 0.35
    comment_rate: float = 0.25
    share_rate: float = 0.20
    completion_rate: float = 0.10
    growth_7d: float = 0.10


MOCK_MATERIALS: List[VideoMaterial] = [
    VideoMaterial("v001", "3秒见效收纳神器", "收纳盒", "家居", 12000, 860, 430, 210000, 0.41, 0.23),
    VideoMaterial("v002", "油皮亲妈粉底液测评", "粉底液", "美妆", 34000, 4100, 2100, 550000, 0.52, 0.37),
    VideoMaterial("v003", "学生党百元耳机横评", "蓝牙耳机", "3C", 28000, 2500, 1100, 470000, 0.49, 0.31),
    VideoMaterial("v004", "一周掉秤食谱公开", "代餐奶昔", "食品", 19500, 3200, 1900, 398000, 0.58, 0.35),
]


def safe_rate(numerator: int, denominator: int) -> float:
    return 0.0 if denominator <= 0 else numerator / denominator


def compute_hot_score(item: VideoMaterial, weights: ScoreWeights | None = None) -> float:
    use_weights = weights or ScoreWeights()
    like_rate = safe_rate(item.likes, item.views)
    comment_rate = safe_rate(item.comments, item.views)
    share_rate = safe_rate(item.shares, item.views)
    return (
        like_rate * use_weights.like_rate
        + comment_rate * use_weights.comment_rate
        + share_rate * use_weights.share_rate
        + item.completion_rate * use_weights.completion_rate
        + item.growth_7d * use_weights.growth_7d
    )


def rank_materials(
    materials: Iterable[VideoMaterial],
    product: Optional[str] = None,
    category: Optional[str] = None,
    limit: int = 10,
    weights: ScoreWeights | None = None,
) -> List[dict]:
    if limit < 1:
        raise ValueError("limit must be >= 1")

    filtered = list(materials)
    if product:
        needle = product.lower()
        filtered = [m for m in filtered if needle in m.product.lower() or needle in m.title.lower()]

    if category:
        filtered = [m for m in filtered if m.category == category]

    ranked = sorted(filtered, key=lambda m: compute_hot_score(m, weights), reverse=True)
    return [
        {
            "video_id": m.video_id,
            "title": m.title,
            "product": m.product,
            "category": m.category,
            "hot_score": round(compute_hot_score(m, weights), 6),
            "like_rate": round(safe_rate(m.likes, m.views), 6),
            "comment_rate": round(safe_rate(m.comments, m.views), 6),
            "share_rate": round(safe_rate(m.shares, m.views), 6),
        }
        for m in ranked[:limit]
    ]
