import os.path
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

STATIC_ROOT = os.path.join(BASE_DIR, 'root')
print(STATIC_ROOT)
