"""Two frozen P2 estimators joined by an exact frequency selector."""
import sys
sys.dont_write_bytecode=True
import math,importlib.util
from pathlib import Path
from fractions import Fraction as F
import neighbor_evaluator as NEIGHBOR
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
OLD_PATH=REPO/'captures/2026-10-19T231026Z-codex-j1-floating-band-2bbebc9d/evaluator.py'
_spec=importlib.util.spec_from_file_location('original_frozen_J1_band',OLD_PATH)
ORIGINAL=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ORIGINAL)
LOWER=ORIGINAL.LOWER
UPPER=NEIGHBOR.UPPER
SWITCH=F(577,128)

def branch(omega):
 if type(omega) is not float or not math.isfinite(omega):raise ValueError('frequency must be a finite native binary64 float')
 q=F.from_float(omega)
 if not LOWER<=q<=UPPER:raise ValueError('frequency outside joined certified interval')
 return 'original' if q<=SWITCH else 'neighbor'

def evaluate(omega):
 return ORIGINAL.evaluate(omega) if branch(omega)=='original' else NEIGHBOR.evaluate(omega)
