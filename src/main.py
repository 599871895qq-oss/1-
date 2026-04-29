from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from fastapi import FastAPI, Query
from pydantic import BaseModel


@dataclass
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


MOCK_MATERIALS: List[VideoMaterial] = [
    VideoMaterial("v001", "3秒见效收纳神器", "收纳盒", "家居", 12000, 860, 430, 210000, 0.41, 0.23),
    VideoMaterial("v002", "油皮亲妈粉底液测评", "粉底液", "美妆", 34000, 4100, 2100, 550000, 0.52, 0.37),
    VideoMaterial("v003", "学生党百元耳机横评", "蓝牙耳机", "3C", 28000, 2500, 1100, 470000, 0.49, 0.31),
    VideoMaterial("v004", "一周掉秤食谱公开", "代餐奶昔", "食品", 19500, 3200, 1900, 398000, 0.58, 0.35),
]


class ScoreWeights(BaseModel):
    like_rate: float = 0.35
    comment_rate: float = 0.25
    share_rate: float = 0.2
    completion_rate: float = 0.1
    growth_7d: float = 0.1


class MaterialOut(BaseModel):
    video_id: str
    title: str
    product: str
    category: str
    hot_score: float
    like_rate: float
    comment_rate: float
    share_rate: float


app = FastAPI(title="Douyin Viral Material Radar", version="0.1.0")


def _safe_rate(numerator: int, denominator: int) -> float:
    return 0.0 if denominator <= 0 else numerator / denominator


def compute_hot_score(item: VideoMaterial, weights: ScoreWeights) -> float:
    like_rate = _safe_rate(item.likes, item.views)
    comment_rate = _safe_rate(item.comments, item.views)
    share_rate = _safe_rate(item.shares, item.views)

    return (
        like_rate * weights.like_rate
        + comment_rate * weights.comment_rate
        + share_rate * weights.share_rate
        + item.completion_rate * weights.completion_rate
        + item.growth_7d * weights.growth_7d
    )


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/materials", response_model=List[MaterialOut])
def list_materials(
    product: Optional[str] = Query(default=None, description="按产品关键词过滤"),
    category: Optional[str] = Query(default=None, description="按类目过滤"),
    limit: int = Query(default=10, ge=1, le=100),
) -> List[MaterialOut]:
    weights = ScoreWeights()
    candidates = MOCK_MATERIALS

    if product:
        candidates = [m for m in candidates if product.lower() in m.product.lower() or product.lower() in m.title.lower()]

    if category:
        candidates = [m for m in candidates if m.category == category]

    ranked = sorted(candidates, key=lambda m: compute_hot_score(m, weights), reverse=True)

    result: List[MaterialOut] = []
    for m in ranked[:limit]:
        result.append(
            MaterialOut(
                video_id=m.video_id,
                title=m.title,
                product=m.product,
                category=m.category,
                hot_score=round(compute_hot_score(m, weights), 6),
                like_rate=round(_safe_rate(m.likes, m.views), 6),
                comment_rate=round(_safe_rate(m.comments, m.views), 6),
                share_rate=round(_safe_rate(m.shares, m.views), 6),
            )
        )
    return result
