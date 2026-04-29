from datetime import datetime
from pathlib import Path
from typing import Dict


def write_markdown_report(path: str, summary: Dict[str, float], stage: str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    content = f"""# 电商执行日报

- 生成时间: {datetime.utcnow().isoformat()}Z
- 当前阶段: {stage}

## 汇总指标

- 曝光: {summary['impressions']}
- 点击: {summary['clicks']}
- 下单: {summary['orders']}
- 成交额: {summary['revenue']}
- 花费: {summary['spend']}
- CTR: {summary['ctr']}
- CR: {summary['cr']}
- ROI: {summary['roi']}
"""
    Path(path).write_text(content, encoding="utf-8")
