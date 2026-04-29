import unittest

from src.material_radar import MOCK_MATERIALS, VideoMaterial, rank_materials, safe_rate


class MaterialRadarTests(unittest.TestCase):
    def test_safe_rate_zero_guard(self):
        self.assertEqual(safe_rate(1, 0), 0.0)

    def test_rank_returns_descending_hot_score(self):
        data = rank_materials(MOCK_MATERIALS)
        self.assertGreaterEqual(data[0]["hot_score"], data[-1]["hot_score"])

    def test_filter_by_category(self):
        data = rank_materials(MOCK_MATERIALS, category="美妆")
        self.assertTrue(data)
        self.assertTrue(all(item["category"] == "美妆" for item in data))

    def test_limit_validation(self):
        with self.assertRaises(ValueError):
            rank_materials(MOCK_MATERIALS, limit=0)

    def test_product_keyword_filter(self):
        sample = [VideoMaterial("a", "高效清洁", "清洁剂", "家居", 10, 2, 1, 100, 0.5, 0.2)]
        data = rank_materials(sample, product="清洁")
        self.assertEqual(len(data), 1)


if __name__ == "__main__":
    unittest.main()
