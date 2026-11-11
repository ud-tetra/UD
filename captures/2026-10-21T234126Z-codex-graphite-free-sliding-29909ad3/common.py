from pathlib import Path
import sys,numpy as np
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'graphite-branch-aware'))
from geometry import setup,clearance
# Reuse immutable input construction helpers without importing a conflicting common module.
import importlib.util
spec=importlib.util.spec_from_file_location('qualified_helpers',ROOT/'graphite-safe-full/common.py');helpers=importlib.util.module_from_spec(spec);spec.loader.exec_module(helpers)
positions=helpers.positions;directions=helpers.directions;input_guard=helpers.input_guard

def load(case):
 a=np.load(ROOT/'graphite-free-sliding'/case/'RELAXED.npz');B=a['B_extended'];nei,b=setup(ROOT,case,a);return a,B,nei,b
