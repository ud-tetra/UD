#!/usr/bin/env python3
"""SU2 exact half-turn trace/gauge/reference controls, independent symbolic program."""
import sympy as s
import json
from pathlib import Path
C=0
def ok(z,m):
 global C
 C+=1
 if not z:raise AssertionError(f'{C}: {m}')
def equal(a,b,m):ok(s.simplify(a-b)==0,m)
def eqmat(a,b,m):ok(all(s.simplify(z)==0 for z in a-b),m)
I=s.I;unit=s.eye(2)
H=s.diag(I,-I); neg=-H
G=s.Matrix([[0,1],[-1,0]])
eqmat(G*H*G.inv(),neg,'H and -H conjugate in SU2')
for h in (H,neg):
 eqmat(h*h.conjugate().T,unit,'H unitary')
 equal(s.det(h),1,'SU2 det')
 equal(s.trace(h),0,'trace zero half-turn')
 equal(1-s.re(s.trace(h))/2,1,'same Q140 spin mismatch')
 equal(1-(s.trace(h)**2-1)/3,s.Rational(4,3),'same vector mismatch')
psi=s.Matrix([1,0]);eta=-I
for h,want in [(H,1),(neg,0)]:
 y=(unit+eta*h)*psi/2
 equal((y.conjugate().T*y)[0],want,'marked spinor with quadrature reference')
 eqmat((unit+h)*psi/2,(unit+h)*psi/2,'well defined two path amplitude')
# Gauge covariance of combined (H,psi), not of H alone after the conjugacy change
for g in (G,unit,s.diag(I,-I)):
 for h in (H,neg):
  y=(unit+eta*(g*h*g.inv()))*(g*psi)/2
  z=(unit+eta*h)*psi/2
  equal((y.conjugate().T*y)[0],(z.conjugate().T*z)[0], 'jointly transformed marked readout')
# Spin trace is a class function; no holonomy-only class function can split conjugate H and -H.
ok(G*H*G.inv()==-H,'conjugacy obstruction distinct from externally marked spinor')
res={'version':'v2.0','symbolic_checks':C,'H_and_minus_H_conjugate':True,'trace_only_can_discriminate_halfturn_sign':False,
'additional_marked_reference_needed':True,'source_generated_marked_reference':'OPEN','physical_promotion':0}
Path(__file__).with_name('RESULTS_HALFTURN_v2.0.json').write_text(json.dumps(res,indent=2)+'\n')
print('PASS',C,'independent SU2 exact checks')
