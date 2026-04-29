import argparse
from pathlib import Path

from src.pipeline.io import ensure_sample_raw, load_csv, save_csv
from src.pipeline.transform import compute_metrics, aggregate_summary
from src.pipeline.report import write_markdown_report


def current_stage() -> str:
    p = Path("docs/STAGE_STATUS.md")
    if not p.exists():
        return "A"
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.startswith("- 当前阶段："):
            return line.split("：", 1)[1].strip()
    return "A"


def main() -> None:
    parser = argparse.ArgumentParser(description="Run ecommerce analysis pipeline")
    parser.add_argument("--input", default="data/raw/sample_traffic.csv")
    parser.add_argument("--output", default="data/processed/metrics.csv")
    parser.add_argument("--report", default="reports/daily_report.md")
    args = parser.parse_args()

    ensure_sample_raw(args.input)
    rows = load_csv(args.input)
    metrics_rows = compute_metrics(rows)
    fieldnames = list(metrics_rows[0].keys())
    save_csv(args.output, metrics_rows, fieldnames)
    summary = aggregate_summary(metrics_rows)
    write_markdown_report(args.report, summary, current_stage())
    print(f"pipeline done: {args.output}, {args.report}")


if __name__ == "__main__":
    main()
