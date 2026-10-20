"""Four frozen trial states joined by exact damping and frequency selectors."""
import sys
sys.dont_write_bytecode=True
import math,importlib.util
from pathlib import Path
from fractions import Fraction as F
import shifted_evaluator as SHIFTED
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
BASE_PATH=REPO/'captures/2026-10-20T004900Z-codex-j1-damping-region-57f89a2c/evaluator.py'
_spec=importlib.util.spec_from_file_location('previous_J1_two_input_evaluator',BASE_PATH)
BASELINE=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(BASELINE)
LOWER=BASELINE.LOWER
UPPER=BASELINE.UPPER
GAMMA_LOWER=BASELINE.GAMMA_LOWER
GAMMA_UPPER=SHIFTED.GAMMA_UPPER
GAMMA_SWITCH=F(411,4096)

def band(omega,gamma):
 if type(omega) is not float or type(gamma) is not float or not math.isfinite(omega) or not math.isfinite(gamma):raise ValueError('parameters must be finite native binary64 floats')
 w,g=F.from_float(omega),F.from_float(gamma)
 if not LOWER<=w<=UPPER or not GAMMA_LOWER<=g<=GAMMA_UPPER:raise ValueError('input outside joined parameter rectangle')
 return 'baseline' if g<=GAMMA_SWITCH else 'shifted'

def evaluate(omega,gamma):
 return BASELINE.evaluate(omega,gamma) if band(omega,gamma)=='baseline' else SHIFTED.evaluate(omega,gamma)
