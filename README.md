# 电商全链路研究与执行项目

本项目用于从 0 到 1 搭建电商运营研究与执行体系，覆盖商品卡、短视频、直播及数据复盘。

## 当前初始化内容

- `docs/`：方法文档与复盘模板
- `src/metrics/`：核心指标计算示例
- `tests/`：指标口径测试示例
- `data/`：原始与处理后数据目录占位

## 快速开始

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

## 首批核心指标

- CTR（点击率）= clicks / impressions
- CR（转化率）= orders / clicks
- ROI（投产比）= revenue / spend


## 执行阶段硬性要求（可随时切换）

项目执行采用 A/B/C 三阶段机制，并要求满足阶段硬性产物。

- 阶段定义与硬性要求：`docs/20-阶段切换规则.md`
- 当前阶段状态：`docs/STAGE_STATUS.md`

切换原则：只要满足目标阶段最小输入，可立即切换；缺失产物需在 24 小时内补齐。
