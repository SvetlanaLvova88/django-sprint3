
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
DJANGO_PROJECT_DIR = PROJECT_DIR / "blogicum"

if DJANGO_PROJECT_DIR.is_dir():
    sys.path.insert(0, str(DJANGO_PROJECT_DIR))
