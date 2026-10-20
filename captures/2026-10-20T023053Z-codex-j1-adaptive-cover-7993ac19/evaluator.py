"""Adaptive integer-word selector; delegates unchanged inputs to frozen kernel."""
import sys
sys.dont_write_bytecode=True
import math,json
from fractions import Fraction as F
from pathlib import Path
import kernel
from rounding import bits
HERE=Path(__file__).resolve().parent
COVER=json.loads((HERE/'COVER.json').read_text());NODES=COVER['nodes']
LOWER,UPPER=map(F,COVER['domain']['omega']);GAMMA_LOWER,GAMMA_UPPER=map(F,COVER['domain']['gamma'])

def select(omega,gamma):
 if type(omega) is not float or type(gamma) is not float or not math.isfinite(omega) or not math.isfinite(gamma):raise ValueError('parameters must be finite native binary64 floats')
 w,g=F.from_float(omega),F.from_float(gamma)
 if not LOWER<=w<=UPPER or not GAMMA_LOWER<=g<=GAMMA_UPPER:raise ValueError('input outside adaptive certified rectangle')
 ww,gg=bits(omega),bits(gamma);idx=0
 while NODES[idx]['kind']=='split':
  node=NODES[idx];word=ww if node['axis']=='omega' else gg;idx=node['left'] if word<=node['cut_word'] else node['right']
 return idx

def evaluate(omega,gamma):
 idx=select(omega,gamma);nodes=kernel.trace(NODES[idx]['certificate']['state'],omega,gamma)
 return complex(nodes[11],nodes[15])
