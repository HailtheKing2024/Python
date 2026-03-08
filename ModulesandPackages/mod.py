import sys
from pathlib import Path

folder = Path(__file__).parent / "src"
sys.path.insert(0, str(folder))
from Package.mod1 import load_data

load_data()
