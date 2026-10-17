#!/usr/bin/env python3
"""Full record exact action, adjoint and energy checks; no nominal factor substitution."""
import os,time,sys,json,hashlib,resource
from pathlib import Path
import numpy as np
from flint import arb,ctx
ctx.prec=512
P=Path(__file__).resolve().parent;O=P/'output';sys.path.insert(0,str(P.parent/'spectral-work'))
from hankel_exact import HankelRecord
Y=np.load(O/'FROZEN_RECORD.npy',mmap_mode='r');H=HankelRecord(Y,2**48);t=time.monotonic();out={}
def log(k,v):out[k]=v;(O/'ACTIONS_PROGRESS.json').write_text(json.dumps(out,indent=2));print(k,v,flush=True)
E=H.energy();log('energy',{'exact_numerator':E.numerator,'exact_denominator':E.denominator,'seconds':time.monotonic()-t})
x=((np.arange(H.cols,dtype=np.int64)*13+7)%5)-2;z=((np.arange(H.rows,dtype=np.int64)*11+3)%7)-3
t0=time.monotonic();hx,d=H.action(x);log('H_action',{'seconds':time.monotonic()-t0,'output_length':len(hx),'sha256':hashlib.sha256(','.join(map(str,hx)).encode()).hexdigest()})
t0=time.monotonic();htz,dd=H.action(z,transpose=True);log('HT_action',{'seconds':time.monotonic()-t0,'output_length':len(htz),'sha256':hashlib.sha256(','.join(map(str,htz)).encode()).hexdigest()})
lhs=sum(int(a)*int(b) for a,b in zip(z,hx));rhs=sum(int(a)*int(b) for a,b in zip(x,htz));assert lhs==rhs and d==dd
# Direct 32-entry comparisons verify the polynomial index convention in both directions.
for ii in np.linspace(0,H.rows-1,32,dtype=int):
 i,c=divmod(int(ii),62);assert hx[ii]==sum(int(Y[a,i+j,c])*int(x[j*37+a]) for j in range(4096) for a in range(37))
for jj in np.linspace(0,H.cols-1,32,dtype=int):
 j,a=divmod(int(jj),37);assert htz[jj]==sum(int(Y[a,i+j,c])*int(z[i*62+c]) for i in range(4096) for c in range(62))
log('exact_checks',{'adjoint_identity':True,'direct_H_entries':32,'direct_HT_entries':32,'common_denominator':d,'bilinear_numerator':str(lhs)})
g=np.load(O/'FACTOR_GRAMS.npz');gl=g['left'];gr=g['right'];product=sum(int(a)*int(b) for a,b in zip(gl.flat,gr.T.flat));energy_core=arb(product)/(1<<106)
er=json.loads((O/'GRAM_ERRORS.json').read_text());el,er=arb(er['left']),arb(er['right'])
nl=arb(sum(int(v)**2 for v in gl.flat)).sqrt()/(1<<52);nr=arb(sum(int(v)**2 for v in gr.flat)).sqrt()/(1<<54)
trace_error=el*nr+er*nl+el*er
sp=json.loads((O/'SPECTRAL_CERTIFICATE.json').read_text());delta=arb(sp['modal_hankel_error_upper'])+arb(sp['trajectory_hankel_error_upper'])
actual_energy=arb(E.numerator)/arb(E.denominator);lo=actual_energy.sqrt()-delta;hi=actual_energy.sqrt()+delta
assert energy_core+trace_error>lo**2 and energy_core-trace_error<hi**2
log('energy_consistency',{'data_energy':str(actual_energy),'factor_gram_energy':str(energy_core),'trace_error_upper':str(trace_error.upper()),'model_data_norm_error_upper':str(delta.upper()),'compatible':True})
log('resource',{'seconds':time.monotonic()-t,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
(O/'ACTIONS_CERTIFICATE.json').write_text(json.dumps(out,indent=2))
