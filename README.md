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
