from pathlib import Path

PACKAGE_PATH = Path(__file__).parent

PROJECT_PATH = PACKAGE_PATH.parent

CLEAN_DATA = Path(PACKAGE_PATH, "data/clean_data")

RAW_DATA = Path(PACKAGE_PATH, "data/raw_data")
