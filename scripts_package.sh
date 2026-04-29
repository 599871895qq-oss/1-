#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

mkdir -p dist
python - <<'PY'
from pathlib import Path
import zipfile

root = Path('.')
out = root / 'dist' / 'douyin_material_radar_mvp.zip'
if out.exists():
    out.unlink()

with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as zf:
    for p in root.rglob('*'):
        if p.is_dir():
            continue
        rel = p.relative_to(root)
        s = str(rel)
        if s.startswith('.git/') or s.startswith('dist/'):
            continue
        if '/__pycache__/' in s or s.endswith('.pyc') or s.startswith('.pytest_cache/'):
            continue
        zf.write(p, rel)
print(out)
PY
