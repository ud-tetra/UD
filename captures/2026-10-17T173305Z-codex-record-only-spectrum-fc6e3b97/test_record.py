#!/usr/bin/env python3
"""Fail-closed input tests and independent mathematical regression cases."""
import json,tempfile,sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.linalg import cholesky,svdvals
from proof_math import nearest,verify,arb,quantize64
from certify_record import run
P=Path(__file__).resolve().parent
import argparse
parser=argparse.ArgumentParser();parser.add_argument('--record',default=str(P/'inputs/normalized_history.i64le'));parser.add_argument('--contract',default=str(P/'inputs/FROZEN_CONTRACT.json'));parser.add_argument('--proposal',default=str(P/'output/PROPOSAL.npz'));parser.add_argument('--certificate',default=str(P/'certified-v02/CERTIFICATE.json'));parser.add_argument('--result',default=str(P/'TEST_RESULTS.json'));args=parser.parse_args();cases=[]
for n in range(-1000,1001):assert nearest(n,4)==round(n/16)
cases.append('2001 signed ties-even checks')
for x in [8.,float('inf'),float('nan')]:
 try:quantize64(np.array([x]),60)
 except ArithmeticError:pass
 else:raise AssertionError('Out of range or nonfinite dyadic cast accepted')
cases.append('overflow/NaN/infinity dyadic casts fail closed')
rng=np.random.default_rng(172026);M=11;c=4;p=3;r=2;t=np.arange(M);v=np.exp(1j*.731*t)/np.sqrt(M);v0=np.ones(M)/np.sqrt(M);l=rng.normal(size=(c,r))+1j*rng.normal(size=(c,r));rr=rng.normal(size=(p,r))+1j*rng.normal(size=(p,r));l0=rng.normal(size=(c,1));r0=rng.normal(size=(p,1))
f=np.hstack([np.kron(v0[:,None],l0),np.kron(v[:,None],l),np.kron(v.conj()[:,None],l.conj())]);g=np.hstack([np.kron(v0[:,None],r0),np.kron(v.conj()[:,None],rr),np.kron(v[:,None],rr.conj())]);H=f@g.conj().T
Freal=np.column_stack([f[:,0].real,2*f[:,1:3].real,2*f[:,1:3].imag]);Greal=np.column_stack([g[:,0].real,g[:,1:3].real,g[:,1:3].imag]);assert np.max(abs(H-Freal@Greal.T))<1e-13
s=svdvals(cholesky(Freal.T@Freal,lower=True).T@cholesky(Greal.T@Greal,lower=True));assert np.max(abs(s-svdvals(H)[:5]))<1e-12;cases.append('independent dense factor/core spectrum')
# Test a dimensionless exact rank-one Hankel impulse and the rank-r perturbation inequality.
N=9;r=3;delta=np.eye(N)[:,::-1]*.25;model=rng.normal(size=(N,r))@rng.normal(size=(r,N));assert svdvals(model+delta)[r]>=.25-1e-12;cases.append('flat impulse spectrum and rank-r lower bound')
coef=np.full((1,2294),1<<55,np.int64);contract=json.loads((Path(args.contract)).read_text())
with tempfile.TemporaryDirectory() as tmp:
 d=Path(tmp);h=verify(np.empty(0,np.int64),coef,arb(0),contract,d,lambda *a,**k:None);assert h['status']=='HOLD';cases.append('wrong proposed rank returns HOLD')
 with np.load(Path(args.proposal)) as z:theta=z['theta'].copy();coeff=z['coeff'].copy()
 bad=coeff.copy();bad[0,0]=np.iinfo(np.int64).min;np.savez(d/'minint.npz',theta=theta,coeff=bad)
 try:run(Path(args.record),Path(args.contract),d/'minint.npz',d/'minint-output')
 except ValueError:pass
 else:raise AssertionError('int64 minimum overflowed the range guard')
 assert not(d/'minint-output/CERTIFICATE.json').exists();cases.append('signed int64 minimum rejected without abs overflow')
 theta[1]=theta[0];np.savez(d/'duplicate.npz',theta=theta,coeff=coeff)
 try:run(Path(args.record),Path(args.contract),d/'duplicate.npz',d/'duplicate-output')
 except ValueError:pass
 else:raise AssertionError('Duplicate frequency was accepted')
 assert not(d/'duplicate-output/CERTIFICATE.json').exists();cases.append('duplicate frequencies produce no acceptance certificate')
 (d/'bad-contract.json').write_text('{}')
 try:run(Path(args.record),d/'bad-contract.json',Path(args.proposal),d/'bad-contract-output')
 except ValueError:pass
 else:raise AssertionError('Changed gate was accepted')
 assert not(d/'bad-contract-output/CERTIFICATE.json').exists();cases.append('altered contract produces no acceptance certificate')
 (d/'short.i64le').write_bytes(b'\0'*64)
 try:run(d/'short.i64le',Path(args.contract),Path(args.proposal),d/'short-output')
 except ValueError:pass
 else:raise AssertionError('Incomplete record was accepted')
 assert not(d/'short-output/CERTIFICATE.json').exists();cases.append('incomplete record produces no acceptance certificate')
certificate=json.loads((Path(args.certificate)).read_text());assert certificate['status']=='CERTIFIED_NUMERIC_RECORD_SIGNATURE'
lo,hi,tail=[F(*certificate[k]) for k in ['sigma_r_lower','sigma_1_upper','projection_tail_frobenius_upper']];T=F(*certificate['selection_threshold']);assert lo>T>tail and hi/lo<F('706.570')<2029;cases.append('exact rational frozen acceptance rule')
result={'status':'PASS','checks':cases,'physical_promotion':0,'independent_review':'pending'};Path(args.result).write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
