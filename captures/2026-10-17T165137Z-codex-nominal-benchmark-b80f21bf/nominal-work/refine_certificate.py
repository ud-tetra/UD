#!/usr/bin/env python3
"""Recompute frame bounds from actual dyadic factors and the 105-mode time Gram."""
import json,time
from pathlib import Path
import numpy as np
from flint import arb,acb,acb_mat,ctx,fmpq
ctx.prec=512
P=Path(__file__).resolve().parent;O=P/'output';t=time.monotonic()
def ab(x):return arb(fmpq(*x))
def upper(x):return str(x.upper())
def lower(x):return str(x.lower())
def iv(r):
 a,b=ab(r['a']),ab(r['b']);return (a+b)/2+arb(0,((b-a)/2).upper())
f=np.load(O/'MODAL_FACTORS.npz');roots=json.loads((P/'sources/REFINED_ROOT_INTERVALS.json').read_text());freq=[arb(0)];minl=arb(1);minr=arb(1);maxl=arb(0);maxr=arb(0);bounds=[]
for j,r in enumerate(roots):
 ls=[]
 for part,rows in [(0,62),(2,37)]:
  re=f[f'{j}_{part}'];im=f[f'{j}_{part+1}'];rank=re.shape[1]
  z=acb_mat([[acb(arb(int(re[i,k]))/(1<<60),arb(int(im[i,k]))/(1<<60)) for k in range(rank)] for i in range(rows)])
  g=z.conjugate().transpose()*z;lo=[];hi=[]
  for k in range(rank):
   radius=sum((abs(g[k,l]) for l in range(rank) if k!=l),arb(0))
   lo.append((g[k,k].real-radius).lower());hi.append((g[k,k].real+radius).upper())
  ls.append((min(lo),max(hi)))
 minl=min(minl,arb(ls[0][0]));minr=min(minr,arb(ls[1][0]));maxl=max(maxl,arb(ls[0][1]));maxr=max(maxr,arb(ls[1][1]));bounds.append({'mode':j,'left_min_lower':str(ls[0][0]),'right_min_lower':str(ls[1][0])})
 if j:freq.extend([iv(r).sqrt(),-iv(r).sqrt()])
row=[arb(0) for _ in freq]
for i,a in enumerate(freq):
 for j in range(i+1,len(freq)):
  d=(freq[j]-a)/2;z=(acb(0,4096*d).exp()-1)/(acb(0,d).exp()-1)/4096
  e=arb(abs(z).upper());row[i]+=e;row[j]+=e
rho=max(x.upper() for x in row);a=1-arb(rho);b=1+arb(rho);assert a>0
p=json.loads((O/'PROGRESS.json').read_text());g=json.loads((O/'GRAM_ERRORS.json').read_text());s=json.loads((O/'SPECTRAL_CERTIFICATE.json').read_text());v=np.load(O/'SPECTRAL_PROPOSAL.npz');sig=v['sigma']
rl=arb(p['left_cholesky_verified']['residual']);rr=arb(p['right_cholesky_verified']['residual'])
uniform=json.loads((O/'UNIFORM_BOUNDS.json').read_text())
g={'left':uniform['left_gram_error_upper'],'right':uniform['right_gram_error_upper']}
el=(arb(g['left'])+rl)/(a*minl-arb(g['left'])-rl)
er=(arb(g['right'])+rr)/(a*minr/2-arb(g['right'])-rr)
assert el<1 and er<1
svderr=arb(s['svd_error_upper']);mod=json.loads((O/'MODAL_VERIFICATION.json').read_text());de=b*arb(mod['modal_error_frobenius_upper'])+arb(uniform['trajectory_hankel_error_upper'])
lo=((1-el)*(1-er)).sqrt()*(arb(int(sig[-1]))/(1<<52)-svderr)-de
hi=((1+el)*(1+er)).sqrt()*(arb(int(sig[0]))/(1<<52)+svderr)+de
contract=json.loads((P/'sources/FROZEN_CONTRACT.json').read_text());threshold=ab(contract['spectral_rule']['selection_threshold'])
# Store dyadic outward bounds to avoid interpreting formatted Arb text as exact decimals.
def updy(x,bits=100):return [int((x*(1<<bits)).ceil().upper().unique_fmpz()),1<<bits]
def lody(x,bits=100):return [int((x*(1<<bits)).floor().lower().unique_fmpz()),1<<bits]
# ceil/floor can be interval balls; their unique integer must be certified.
result={'status':'CERTIFIED_INTERVAL_CONSTRUCTOR','physical_promotion':0,'independent_review':'pending','rank_above_exact_frozen_threshold':1893,'selection_threshold':contract['spectral_rule']['selection_threshold'],'sigma_1893_lower_dyadic':lody(lo),'sigma_1_upper_dyadic':updy(hi),'sigma_1894_upper_dyadic':updy(de),'condition_upper_dyadic':updy(hi/lo),'sigma_1893_lower':lower(lo),'sigma_1_upper':upper(hi),'tail_upper':upper(de),'condition_upper':upper(hi/lo),'temporal_gram_min_lower':lower(a),'temporal_gram_max_upper':upper(b),'actual_left_modal_min_lower':lower(minl),'actual_right_modal_min_lower':lower(minr),'eta_left_upper':upper(el),'eta_right_upper':upper(er),'rank_count_pass':bool(lo>threshold and de<threshold),'conditioning_pass':bool(hi/lo<2029),'seconds':time.monotonic()-t,'per_mode_factor_bounds':bounds}
assert result['rank_count_pass'] and result['conditioning_pass']
(O/'REFINED_CERTIFICATE.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='per_mode_factor_bounds'},indent=2),flush=True)
