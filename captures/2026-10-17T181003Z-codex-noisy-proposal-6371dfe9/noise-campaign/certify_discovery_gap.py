#!/usr/bin/env python3
"""Exact sketch Gram and residual-verified temporal separation, uniform under vector noise."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import json,time,resource
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from flint import ctx,arb,fmpz_mat,fmpq
from proof_math import fm,arr,norm_exact,up,down,quantize64
ctx.prec=512
P=Path(__file__).resolve().parent;t=time.monotonic();Y=np.memmap(P/'records/clean.i64le',dtype='<i8',mode='r',shape=(37,8191,62));X=np.array(Y.transpose(1,2,0).reshape(8191,2294),dtype=np.int64)
assert int(X.max())<=2**49 and int(X.min())>=-2**49 and 2294*2**49<2**63
sign=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64)
Z=X@sign # exact integer operations; all partial sums fit int64 by the bound above
print('exact sketch complete',time.monotonic()-t,flush=True);del X
z=fm(Z);G=z.transpose()*z;gg=arr(G);Gfloat=np.array(gg,dtype=float)/2.**108;d,Q=eigh(Gfloat,check_finite=False);idx=np.argsort(d)[::-1];d=d[idx];Q=Q[:,idx];qn=quantize64(Q,60);dn=quantize64(d,40);q=fm(qn)
eta=norm_exact(arr(q.transpose()*q)-np.eye(160,dtype=object)*(1<<120),120)
R=arr(G*q)-qn.astype(object)*dn.astype(object)[None,:]*(1<<68);res=norm_exact(R,168);gnorm=norm_exact(gg,108)
assert eta<1;s=(1+eta).sqrt();dist=eta/(1+(1-eta).sqrt());radius=gnorm*eta+res*s+arb(max(abs(int(v)) for v in dn))/(1<<40)*dist*(s+1)
lower=(arb(int(dn[104]))/(1<<40)-radius).sqrt();upper=(arb(int(dn[105]))/(1<<40)+radius).sqrt()
delta=F(1,2**20);eta_squared=F(37*8191*2294*160,64**2)*delta**2;noise=arb(fmpq(eta_squared.numerator,eta_squared.denominator)).sqrt()
assert lower>3*noise and upper<noise
result={'status':'CERTIFIED_UNIFORM_TEMPORAL_ORDER_SEPARATION','physical_promotion':0,'independent_review':'pending','lane':'development — no registry entry','temporal_order':105,'sketch_columns':160,'sketch_denominator':64,'sketch_noise_squared_ceiling':[eta_squared.numerator,eta_squared.denominator],'sigma105_baseline_lower':down(lower),'sigma106_baseline_upper':up(upper),'cutoff':up(2*noise),'eigenvalue_radius_upper':up(radius),'uniform_implication':'For every perturbation with each62-vector l2<=2^-20, exact sketch has105 singular values above2*noise_envelope. Numerical proposal estimates and phase fitting are separate.','baseline_finite_rank_105_claimed':False,'seconds':time.monotonic()-t,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'readable':{'sigma105_lower':float(lower.lower()),'sigma106_upper':float(upper.upper()),'noise_envelope':float(noise),'cutoff':float(2*noise)}}
(P/'DISCOVERY_GAP_CERTIFICATE.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2),flush=True)
