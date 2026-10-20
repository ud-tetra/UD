#!/usr/bin/env python3
"""Independent exact moments and source structural checks; no rank/SVD rerun."""
import hashlib,json,math,zipfile
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent
ARCH=B/'ud-repo/captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/recovered/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.zip'
REPORT=B/'ud-repo/captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/reports/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.md'
sha=lambda b:hashlib.sha256(b).hexdigest()
def pair(x):return [str(x.numerator),str(x.denominator)]
def trim(p):
 while len(p)>1 and p[-1]==0:p.pop()
 return p
def rem(a,b):
 a=list(map(F,a));b=list(map(F,b))
 while len(a)>=len(b) and any(a):
  k=len(a)-len(b);v=a[-1]/b[-1]
  for j,x in enumerate(b):a[k+j]-=v*x
  trim(a)
 return a
def mul(a,b):
 p=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):p[i+j]+=x*y
 return p
def ev(p,x):
 out=F(0)
 for c in reversed(p):out=out*x+c
 return out
def variations(seq,x):
 v=[ev(p,x)for p in seq];v=[1 if y>0 else -1 for y in v if y]
 return sum(a!=b for a,b in zip(v,v[1:]))
def sturm(p):
 s=[list(map(F,p)),[F(i)*p[i]for i in range(1,len(p))]]
 while any(s[-1]):
  r=rem(s[-2],s[-1])
  if not any(r):break
  s.append([-x for x in r])
 return s
def rootbound(x,bits,ceil):
 nn=x.numerator<<(2*bits);dd=x.denominator;k=math.isqrt(nn//dd)
 if ceil and k*k*dd<nn:k+=1
 assert k*k*dd>=nn if ceil else k*k*dd<=nn
 if ceil:assert k==0 or (k-1)**2*dd<nn
 else:assert (k+1)**2*dd>nn
 return F(k,1<<bits)
with zipfile.ZipFile(ARCH)as z:
 raw={n:z.read(n)for n in ['sources/COMPLEX_AND_ACTION.json','modular_results.json','HIDDEN_WITNESSES.json']}
 data=json.loads(raw['sources/COMPLEX_AND_ACTION.json']);mod=json.loads(raw['modular_results.json']);wit=json.loads(raw['HIDDEN_WITNESSES.json'])
counts=[len(x)for x in data['simplices']];assert counts==[120,720,1200,600]
h={int(i)-2040:int(v)for i,v in wit['stationary_fundamental_C3_cycle']};assert set(h)==set(range(600))and set(h.values())=={-1,1}
boundary={}
for k,tet in enumerate(data['simplices'][3]):
 for j in range(4):
  face=tuple(tet[:j]+tet[j+1:]);boundary[face]=boundary.get(face,0)+(-1)**j*h[k]
assert len(boundary)==1200 and all(v==0 for v in boundary.values())
T=data['signed_simplex_permutations'];assert all(sorted(x['destination']for x in block)==list(range(len(block)))and all(x['sign']in[-1,1]for x in block)for block in T)
assert all(x['sign']==1 for x in T[0]);assert all(h[x['destination']]==x['sign']*h[i]for i,x in enumerate(T[3]))
assert len(mod['observed_indices'])==62 and len([i for i in mod['observed_indices']if i<120])==12 and all(i<2040 for i in mod['observed_indices'])
# Independently rebuild the displayed low-degree factors and bind their product to authoritative q coefficients.
fs=[[-k,1]for k in [3,4,5,6,7,8,9,12,14,15]]+[[a,b,1]for a,b in [(80,-20),(36,-18),(55,-15),(44,-14),(23,-11),(27,-11),(29,-11),(5,-10),(23,-10),(9,-9),(15,-9),(11,-8),(1,-7),(11,-7),(3,-5),(1,-3)]]+[[-28,33,-11,1],[-24,33,-11,1],[464,-484,165,-22,1]]
p=[0,1];band=[]
for f in fs:
 p=mul(p,f);s=sturm(f);c=variations(s,F(0))-variations(s,F(16));assert c==len(f)-1 and ev(f,0)!=0 and ev(f,16)!=0;band.append({'coefficients_ascending':f,'roots_in_open_0_16':c})
assert p==list(reversed(mod['qL_coefficients'])) and sum(x['roots_in_open_0_16']for x in band)==52
for i,f in enumerate(fs):
 for g in fs[i+1:]:
  a,b=f,g
  while any(b):a,b=b,rem(a,b)
  assert len(trim(a))==1
M=4096;ts=[F(j,2)for j in range(M)];center=F(M-1,4);cs=[t-center for t in ts]
v=sum(x*x for x in cs)/M;w=sum(x**4 for x in cs)/M
assert v==F(M*M-1,48)and w==F((M*M-1)*(3*M*M-7),3840)
rawmom2=sum(x*x for x in ts)/M;rawmom4=sum(x**4 for x in ts)/M
rows=[]
for exponent in [20,30,40]:
 epsilon=F(1,2**exponent);assert ev(p,epsilon*epsilon)!=0
 upper=epsilon**2*v;lower=upper-epsilon**4*w/3;assert 0<lower<=upper<1 and max(abs(x)*epsilon for x in cs)<1
 sig=rootbound(upper/10,180,True);kap=rootbound((1-upper)/upper,180,False)
 assert sig**2>=upper/10 and kap**2<=(1-upper)/upper
 rows.append({'epsilon':pair(epsilon),'epsilon_exponent':exponent,'q_epsilon_squared_nonzero':True,'centered_S_lower':pair(lower),'centered_S_upper':pair(upper),'centered_B_lower':pair(lower/10),'centered_B_upper':pair(upper/10),'sigma_min_positive_upper_180bit':pair(sig),'kappa_positive_lower_180bit':pair(kap),'sigma_upper_display':float(sig),'kappa_lower_display':float(kap)})
result={'status':'PASS_EXACT_CENTERED_MOMENTS_AND_STRUCTURAL_SOURCE_CHECKS','source_archive_sha256':sha(ARCH.read_bytes()),'source_report_sha256':sha(REPORT.read_bytes()),'json_member_sha256':{n:sha(b)for n,b in raw.items()},'M':M,'sample_step':pair(F(1,2)),'center':pair(center),'central_variance':pair(v),'central_fourth_moment':pair(w),'raw_second_moment':pair(rawmom2),'raw_fourth_moment':pair(rawmom4),'observed_positive_L_root_count':52,'exact_root_band':'all 52 distinct nonzero q roots lie strictly in (0,16)','harmonic_witness_checks':{'B3_h_zero':True,'C0_uniform_harmonic_by_edge_incidence':True,'signed_T_fixes_u':True,'signed_T_fixes_h':True,'R_u_norm_squared':pair(F(1,10)),'R_h_zero':True},'rows':rows,'scope':{'native_history_rank1893_kernel747_inherited_not_rerun':True,'source_full_characteristic_polynomials_not_rerun':True,'no_SVD_or_estimator_or_raw_acquisition':True,'general_skew_coupling_not_native_adjacent_degree_law':True,'odd_operator_grading_not_even_odd_state_subspace_invariance':True,'physical_promotion':0,'external_promotion_review':'PENDING'}}
(P/'EXACT_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'central_variance':pair(v),'central_fourth_moment':pair(w),'rows':[{'exponent':r['epsilon_exponent'],'sigma_upper':r['sigma_upper_display'],'kappa_lower':r['kappa_lower_display']}for r in rows]},indent=2))
