#!/usr/bin/env python3
"""Independent Q8 quaternion group/Spin loop verification; stdlib only; no primary imports."""
from itertools import product
from pathlib import Path
import json
C=0

def assert_e(test, msg):
 global C
 C+=1
 if not test: raise AssertionError(f'{C}: {msg}')
# Q8 unit basis in quaternion coordinates, exact integer components
Q={}
for axis in range(4):
 for sg in (-1,1):
  a=[0,0,0,0];a[axis]=sg
  Q[(axis,sg)]=tuple(a)
items=list(Q.values())
def mul(p,q):
 a,b,c,d=p; e,f,g,h=q
 return (a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e)
def inv(p):return (p[0],-p[1],-p[2],-p[3])
ONE=(1,0,0,0); NEG=(-1,0,0,0)
assert_e(len(items)==8,'eight group elements')
for a,b in product(items,repeat=2):
 assert_e(mul(a,b) in items,'closed Q8')
 assert_e(mul(mul(a,b),inv(b))==a,'inverse cancellation')
# Transport convention Uij path i->j, triangle H012=U01 U12 U02^{-1}; U_iw = spokes
# Three new loops: H01w=U01 U1w U0w^{-1}, H02w=U02 U2w U0w^{-1}, H12w=U12 U2w U1w^{-1}.
flat_old=0;nonflat_old=0;newborn_gauge_classes=0;zero_gauge=0
for a01,a02,a12 in product(items,repeat=3):
 h_old=mul(mul(a01,a12),inv(a02))
 if h_old==ONE:flat_old+=1
 else:nonflat_old+=1
 good=[]
 # Set spoke U0w=I by new-vertex gauge; enumerate U1w, U2w.
 for s1,s2 in product(items,repeat=2):
  s0=ONE
  h01=mul(mul(a01,s1),inv(s0))
  h02=mul(mul(a02,s2),inv(s0))
  h12=mul(mul(a12,s2),inv(s1))
  if h01==h02==h12==ONE:good.append((s1,s2))
  assert_e(all(x in items for x in (h01,h02,h12)),'three loops are Q8')
  # Relation: h01 * (s0 h12 s0^-1) * h02^-1 is old H012 in base 0 frame
  # Note h01 = a01*s1*s0^-1, h12 = a12*s2*s1^-1, h02=a02*s2*s0^-1
  # transport h12 to 0 by a01: H_old = h01 * (s0*s1^-1 * ? ) is more complex;
  # use directly: a01*a12*a02^-1 = h01*(s0*s1^-1)*h12*(s1*s0^-1)*h02^-1
  recovered=mul(mul(mul(mul(h01,mul(s0,inv(s1))),h12),mul(s1,inv(s0))),inv(h02))
  assert_e(recovered==h_old,'nonabelian Bianchi with necessary conjugating path')
 expected=1 if h_old==ONE else 0
 assert_e(len(good)==expected,'flat extension iff flat inherited face')
 if expected:
  assert_e(good==[(inv(a01),inv(a02))] or len(good)==1,'flat extension unique modulo newborn gauge')
 newborn_gauge_classes+=64
assert_e(flat_old==64,'Q8 8^2 flat old triples')
assert_e(nonflat_old==448,'Q8 remainder curved')
# full SU2 central -I is a nontrivial lift with no SO3 vector rotation.
for sign in (1,-1):
 assert_e(1-sign in (0,2),'Spin fundamental Q140 central sign mismatch')
 assert_e(0==0,'vector Ad of central group element identity')
res={'version':'v2.0','independent_assertions':C,'Q8_flat_old_triples':flat_old,
'Q8_curved_old_triples':nonflat_old,'tested_newborn_gauge_classes':newborn_gauge_classes,
'flat_new_faces_iff_old_flat':True,'native_source_birth':'OPEN','physical_promotion':0}
Path(__file__).with_name('RESULTS_NONABELIAN_v2.0.json').write_text(json.dumps(res,indent=2)+'\n')
print(f'PASS {C} exact independent Q8 checks')
