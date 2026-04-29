from __future__ import annotations

from src.material_radar import MOCK_MATERIALS, rank_materials


if __name__ == "__main__":
    for row in rank_materials(MOCK_MATERIALS, limit=3):
        print(row)
