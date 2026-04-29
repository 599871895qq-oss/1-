# 项目运行说明（Project Runbook）

## 1. 环境要求

- Python 3.10+
- Bash / Zsh

## 2. 初始化

在仓库根目录执行：

```bash
python --version
```

## 3. 目录说明

- `src/metrics/core.py`：核心指标计算（CTR/CR/ROI）
- `tests/test_metrics_core.py`：指标测试用例
- `docs/10-复盘模板.md`：复盘模板
- `docs/20-阶段切换规则.md`：阶段切换硬规则
- `docs/STAGE_STATUS.md`：当前执行阶段状态

## 4. 运行测试

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

预期输出：

- `Ran 5 tests`
- `OK`

## 5. 日常执行流程（建议）

1. 查看阶段状态：`docs/STAGE_STATUS.md`
2. 按当前阶段执行任务（A/B/C）
3. 记录实验/复盘到 `docs/10-复盘模板.md`
4. 修改代码后运行测试
5. 提交代码并更新阶段状态

## 6. 阶段切换操作

切换阶段前后必须遵循：

1. 满足目标阶段最小输入（见 `docs/20-阶段切换规则.md`）
2. 在 `docs/STAGE_STATUS.md` 记录切换时间、原因和下一检查点
3. 若有缺失产物，在 24 小时内补齐

## 7. 常见问题

### Q1: 测试运行失败怎么办？

- 确认当前目录在仓库根目录
- 确认 Python 版本满足要求
- 重新执行测试命令并定位报错行

### Q2: 可以跳过 A 阶段直接去 B/C 吗？

可以，但必须满足目标阶段最小输入，并在状态文件中记录切换原因。

## 8. 下一步建议

- 增加 `requirements.txt` 或 `pyproject.toml`
- 新增指标：CPC、CPA、LTV
- 增加数据读取与报表导出脚本
