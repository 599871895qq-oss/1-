from __future__ import annotations

if __package__ in (None, ""):
    from material_radar import MOCK_MATERIALS, rank_materials
else:
    from .material_radar import MOCK_MATERIALS, rank_materials


if __name__ == "__main__":
    for row in rank_materials(MOCK_MATERIALS, limit=3):
        print(row)
