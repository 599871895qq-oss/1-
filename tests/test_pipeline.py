import tempfile
import unittest
from pathlib import Path

from src.pipeline.io import ensure_sample_raw, load_csv
from src.pipeline.transform import compute_metrics, aggregate_summary


class TestPipeline(unittest.TestCase):
    def test_compute_and_summary(self):
        with tempfile.TemporaryDirectory() as d:
            raw = Path(d) / "raw.csv"
            ensure_sample_raw(str(raw))
            rows = load_csv(str(raw))
            self.assertEqual(len(rows), 3)
            metrics = compute_metrics(rows)
            self.assertIn("ctr", metrics[0])
            summary = aggregate_summary(metrics)
            self.assertGreater(summary["roi"], 0)


if __name__ == "__main__":
    unittest.main()
