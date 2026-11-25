"""Download raw Parquet datasets from the GitHub release into data/raw/.

    Run from the repository root:
    uv run python scripts/download_data.py

"""

import urllib.request
from pathlib import Path

REPO = "heltonwo/dbt-duckdb-pipeline"
TAG = "raw-data-v1"
BASE = f"https://github.com/{REPO}/releases/download/{TAG}"

MONTHS = [
    "2025-07", "2025-08", "2025-09", "2025-10", "2025-11", "2025-12",
    "2026-01", "2026-02", "2026-03", "2026-04", "2026-05", "2026-06",
]
FILES = [f"raw_job_postings_{m}.parquet" for m in MONTHS] + ["raw_job_skills.parquet"]

DATA_DIR = Path.cwd() / "data" / "raw"   # relative to where you RUN it

if __name__ == "__main__":
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        dest = DATA_DIR / name
        if dest.exists():
            print(f"  already have {name}")
            continue
        print(f"  downloading {name} ...")
        urllib.request.urlretrieve(f"{BASE}/{name}", dest)
    print(f"Done. {len(FILES)} files in {DATA_DIR}")
