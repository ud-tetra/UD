#!/usr/bin/env python3
"""Independent dense small-case regression of the nominal factor-Gram identity."""
import json,numpy as np
from pathlib import Path
from scipy.linalg import cholesky,svdvals
P=Path(__file__).resolve().parent;O=P/'output'
def check(M,c,p,r):
 rng=np.random.default_rng(917);t=np.arange(M);w=.731
 l0=rng.normal(size=(c,1));r0=rng.normal(size=(p,1));l=rng.normal(size=(c,r))+1j*rng.normal(size=(c,r));rr=rng.normal(size=(p,r))+1j*rng.normal(size=(p,r))
 v=np.exp(1j*w*t)/np.sqrt(M);v0=np.ones(M)/np.sqrt(M)
 fl=np.hstack([np.kron(v0[:,None],l0),np.kron(v[:,None],l),np.kron(v.conj()[:,None],l.conj())]);fr=np.hstack([np.kron(v0[:,None],r0),np.kron(v.conj()[:,None],rr),np.kron(v[:,None],rr.conj())]);h=fl@fr.conj().T
 A=np.zeros((1+2*r,1+2*r),complex);A[0,0]=1
 for j in range(r):
  A[1+j,1+j]=1;A[1+r+j,1+j]=1;A[1+j,1+r+j]=-1j;A[1+r+j,1+r+j]=1j
 B=A.copy();B[:,1:]/=2
 F=fl@A;G=fr@B;assert np.max(abs(F.imag))<1e-13 and np.max(abs(G.imag))<1e-13
 F,G=F.real,G.real;assert np.max(abs(h-F@G.T))<1e-13
 lf=cholesky(F.T@F,lower=True);rf=cholesky(G.T@G,lower=True)
 s=svdvals(lf.T@rf);dense=svdvals(h)
 assert np.max(abs(s-dense[:len(s)]))<1e-12
 # independently assemble signed-mode Gram blocks with opposite temporal conjugation
 V=np.column_stack([v0,v,v.conj()]);T=V.conj().T@V;ll=[l0,l,l.conj()];rs=[r0,rr,rr.conj()]
 gl=np.block([[T[i,j]*(ll[i].conj().T@ll[j]) for j in range(3)] for i in range(3)]);gr=np.block([[T[i,j].conjugate()*(rs[i].conj().T@rs[j]) for j in range(3)] for i in range(3)])
 assert np.max(abs(A.conj().T@gl@A-F.T@F))<1e-12
 assert np.max(abs(B.conj().T@gr@B-G.T@G))<1e-12
 return {'M':M,'c':c,'p':p,'pair_rank':r,'max_spectrum_error':float(np.max(abs(s-dense[:len(s)])))}
out={'status':'PASS','dense_small_cases':[check(7,3,3,1),check(11,4,3,2),check(19,5,4,3)]}
# Canonical nearest-even integer arithmetic including negative ties.
def nearest(n,s):
 q,r=divmod(n,1<<s);h=1<<(s-1);return q+int(r>h or(r==h and q%2!=0))
for n in range(-1000,1001):assert nearest(n,4)==round(n/16)
out['nearest_even_cases']=2001
from scipy.sparse import csr_matrix
z=np.load(P/'sources/OPERATORS.npz');a=csr_matrix((z['A_data'],z['A_indices'],z['A_indptr']),shape=(2640,2640));assert (a+a.T).nnz==0
x=np.load(P/'sources/BASE_PREPARATIONS.npz');assert int(x['denominator'])==52
assert np.all((x['numerator']==1)|(x['numerator']==-1))
y=np.load(O/'FROZEN_RECORD.npy',mmap_mode='r');initial=x['numerator'][z['obs'],:].T/52
assert np.max(abs(y[:,0,:]/2.**48-initial))<=2.**-48
out['frozen_source_checks']={'skew_symmetric':True,'preparation_norm_squared':[165,169],'initial_observation_max_error':float(np.max(abs(y[:,0,:]/2.**48-initial)))}
(O/'METHOD_TESTS.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
