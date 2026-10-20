"""Exact union-domain guard and integer-word adaptive selectors."""
import sys
sys.dont_write_bytecode=True
import math,json
from fractions import Fraction as F
from pathlib import Path
import kernel
from rounding import bits
HERE=Path(__file__).resolve().parent
COVERS=[json.loads((HERE/name).read_text()) for name in ['COVER.json','EXTENSION_COVER.json']]
LOWER,UPPER=map(F,COVERS[0]['domain']['omega']);GAMMA_LOWER,GAMMA_SWITCH=map(F,COVERS[0]['domain']['gamma']);GAMMA_UPPER=F(COVERS[1]['domain']['gamma'][1]);LEFT_UPPER=F(143989,32000)

def validated(omega,gamma):
 if type(omega) is not float or type(gamma) is not float or not math.isfinite(omega) or not math.isfinite(gamma):raise ValueError('parameters must be finite native binary64 floats')
 return F.from_float(omega),F.from_float(gamma)

def select_component(component,omega,gamma):
 w,g=validated(omega,gamma);cover=COVERS[component];wl,wu=map(F,cover['domain']['omega']);gl,gu=map(F,cover['domain']['gamma'])
 if not wl<=w<=wu or not gl<=g<=gu:raise ValueError('input outside component rectangle')
 nodes=cover['nodes'];ww,gg=bits(omega),bits(gamma);idx=0
 while nodes[idx]['kind']=='split':
  node=nodes[idx];word=ww if node['axis']=='omega' else gg;idx=node['left'] if word<=node['cut_word'] else node['right']
 return idx

def select(omega,gamma):
 w,g=validated(omega,gamma)
 if not LOWER<=w<=UPPER or not GAMMA_LOWER<=g<=GAMMA_UPPER or (g>GAMMA_SWITCH and w>LEFT_UPPER):raise ValueError('input outside certified union')
 component=0 if g<=GAMMA_SWITCH else 1
 return component,select_component(component,omega,gamma)

def evaluate_component(component,omega,gamma):
 idx=select_component(component,omega,gamma);nodes=kernel.trace(COVERS[component]['nodes'][idx]['certificate']['state'],omega,gamma)
 return complex(nodes[11],nodes[15])

def evaluate(omega,gamma):
 component,idx=select(omega,gamma);nodes=kernel.trace(COVERS[component]['nodes'][idx]['certificate']['state'],omega,gamma)
 return complex(nodes[11],nodes[15])
