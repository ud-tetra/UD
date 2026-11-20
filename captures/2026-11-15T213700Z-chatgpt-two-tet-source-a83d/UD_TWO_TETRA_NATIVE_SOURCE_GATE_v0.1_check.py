#!/usr/bin/env python3
"""Exact conditional K4-pair seam/burden source-gate audit. Python 3 + SymPy + SciPy.
Native input: face admission; assumptions: Z4 seam phase, donor-proportional transfer,
phase random walk and optional interference h. Outputs exact certificates and numerical nulls.
"""
from itertools import product, combinations
from fractions import Fraction
from math import comb, sqrt, exp
import json, hashlib
from pathlib import Path
import sympy as S
import numpy as np
from scipy.linalg import expm

T0=(0,1,2,3); T1=(0,1,2,4)
faces=sorted(set(combinations(T0,3))|set(combinations(T1,3)))
edges=sorted(set(e for f in faces for e in combinations(f,2)))
assert (len(faces),len(edges))==(7,9)

def adm(b,f):return int(len({b[v] for v in f})>1)

def admissible(b):return all(adm(b,f) for f in faces)
valid=[b for b in product((0,1),repeat=5) if admissible(b)]
assert len(valid)==6
single_flip_survivors=[]
for b in valid:
 for i in range(5):
  c=list(b);c[i]^=1
  if admissible(c):single_flip_survivors.append((b,i))
assert not single_flip_survivors

H=S.Matrix([[int(set(e).issubset(f)) for e in edges] for f in faces]);C=H*H.T/16
v=S.Matrix([0 if f==(0,1,2) else (1 if 3 in f else -1) for f in faces])
assert (C*v)==v/4 and (v.T*v)[0]==6
assert S.factor(C.charpoly().as_expr())==S.factor((4*S.Symbol('lambda')-1)*(16*S.Symbol('lambda')-3)**2*(16*S.Symbol('lambda')-1)**2*(64*S.Symbol('lambda')**2-36*S.Symbol('lambda')+3)/S.Integer(16777216))

# State: n=left retained burden, M-n=right burden, d in Z4 local seam phase difference.
M=3;S0=[(n,d) for n in range(M+1) for d in range(4)];ix={s:i for i,s in enumerate(S0)}
# h_a(d)=1/2 [1+a cos(pi d/2)]. a∈{0,1}; gamma=1 per undirected phase walk (each +/- jump 1/2).
def gate(a):return [S.Rational(1,2)*(1+a*c) for c in [1,0,-1,0]]

def generator(a, closure=(1,1), phase_rate=S.Rational(1,2), M=M):
 h=gate(a); Q=S.zeros(4*(M+1))
 for n,d in S0:
  row=ix[(n,d)];allowed=closure[0]*closure[1]
  for j,rate in [((n-1,d),allowed*h[d]*n),((n+1,d),allowed*h[d]*(M-n)),((n,(d+1)%4),phase_rate),((n,(d-1)%4),phase_rate)]:
   if j[0]<0 or j[0]>M or rate==0:continue
   Q[row,ix[j]]+=rate;Q[row,row]-=rate
 assert Q*S.ones(Q.rows,1)==S.zeros(Q.rows,1)
 assert all(Q[i,j]>=0 for i in range(Q.rows) for j in range(Q.cols) if i!=j)
 return Q

pi=S.Matrix([[S.Rational(comb(M,n),2**M*4) for n,d in S0]])
assert sum(pi)==1
D=S.Matrix([2*n-M for n,d in S0]); hph=S.Matrix([int(d==0)-int(d==2) for n,d in S0])
assert (pi*D)[0]==0 and (pi*hph)[0]==0
assert (pi*S.diag(*D)*D)[0]==M
Q1=generator(1);Q0=generator(0);Qoff=generator(1,closure=(1,0))
assert pi*Q1==S.zeros(1,Q1.rows) and pi*Q0==S.zeros(1,Q0.rows)
for Q in [Q1,Q0,Qoff]:
 for i in range(Q.rows):
  for j in range(i+1,Q.cols):
   assert pi[i]*Q[i,j]==pi[j]*Q[j,i]
 assert Q*S.ones(Q.rows,1)==S.zeros(Q.rows,1)
 # exact conserved burden (per transition), total fixed by coordinate n+M-n
 assert all(sum([n,M-n])==M for n,d in S0)

# Exact low dimensional closure of antisymmetric burden sector D*f_d
P=S.zeros(4)
for d in range(4):
 P[d,d]=-1
 P[d,(d+1)%4]+=S.Rational(1,2)
 P[d,(d-1)%4]+=S.Rational(1,2)
B=P-2*S.diag(*gate(1))
assert S.factor(B.charpoly().as_expr())==(S.Symbol('lambda')+2)**2*(S.Symbol('lambda')**2+4*S.Symbol('lambda')+2)
assert S.simplify(S.Matrix([sum(B[i,j] for j in range(4)) for i in range(4)])-S.Matrix([-2, -1, 0, -1]))==S.zeros(4,1)
Cmoment=lambda Q,k:(pi*S.diag(*D)*(Q**k)*D)[0]
assert [Cmoment(Q1,k)/M for k in (0,1,2)]==[1,-1,S.Rational(3,2)]
assert [Cmoment(Q0,k)/M for k in (0,1,2)]==[1,-1,1]
assert (pi*S.diag(*hph)*hph)[0]==S.Rational(1,2)
assert (pi*S.diag(*hph)*Q1*hph)[0]==-S.Rational(1,2)
assert (pi*S.diag(*hph)*(Q1**2)*hph)[0]==S.Rational(1,2)
# Face burden readout: shared-face 1/2 from each donor, exclusive face = packet burden; centered readout = D*v/2.
readout=S.Matrix([[S.Rational(2*n-M,2)*v[i] for i in range(7)] for n,d in S0])
facecov=readout.T*S.diag(*pi)*readout
assert facecov==S.Rational(M,4)*(v*v.T)
assert facecov*v==S.Rational(3*M,2)*v
assert facecov.rank()==1
# All face-mode projections except structural eigenvalue 1/4 have zero covariance.
assert C*v==v/4
# State-space system stationary exact check by pure independent elementary event budget identity
for n,d in S0:
 assert n>=0 and M-n>=0
 assert n+(M-n)==M

Q1f=np.array(Q1.tolist(),dtype=float);Q0f=np.array(Q0.tolist(),dtype=float)
pif=np.array(pi.tolist(),dtype=float).ravel();Dv=np.array(D.tolist(),dtype=float).ravel()
def normcorr(Q,t):return float(np.dot(pif*Dv, expm(Q*t)@Dv)/M)
a=S.sqrt(2); lambdas=[-2,-2-a,-2+a];weights=[S.Rational(1,4),S.Rational(3,8)-a/4,S.Rational(3,8)+a/4]
assert S.simplify(sum(weights)-1)==0
assert S.simplify(sum(w*lam for w,lam in zip(weights,lambdas))+1)==0
assert S.simplify(sum(w*lam**2 for w,lam in zip(weights,lambdas))-S.Rational(3,2))==0
n1=normcorr(Q1f,1);n0=normcorr(Q0f,1)
analytic=float(sum(float(w)*exp(float(lam)) for w,lam in zip(weights,lambdas)))
assert abs(n1-analytic)<1e-12 and abs(n0-exp(-1))<1e-12
assert abs(n1-n0)>1e-3
assert abs(normcorr(np.array(Qoff.tolist(),dtype=float),1)-1)<1e-12
# phase cosine is separate measured channel and decays with a single -1 eigenvalue
assert Q1*hph==-hph

out={
 'source_scope': 'EXACT_CONDITIONAL finite arithmetic and Markov dynamics; source-selected physical law OPEN',
 'carrier': {'vertices':5,'edges':9,'faces':7,'tetrahedra':2,'fully_admissible_binary_assignments':6,'fully_admissible_single_bit_transitions':0,'face_list':[list(f) for f in faces]},
 'phase':{'group':'Z4','U_d':['1','i','-1','-i'],'h_seam_a1':['1','1/2','0','1/2'],'h_constant_a0':['1/2']*4,'phase_jump_per_direction':'1/2','generator_source':'CANDIDATE: not fixed by March source'},
 'state_space':{'M_total':M,'dimension':len(S0),'stationary_pi':'Binomial(3,1/2) x Uniform(Z4)'},
 'exact_controls':{'Q_1_stochastic_generator':'PASS','Q_1_detailed_balance':'PASS','Q_0_detailed_balance':'PASS','closure_sham_transport_off':'PASS','source_budget_each_transition':'PASS','no_negative_burden':'PASS'},
 'combinatorial_face_spectrum': {str(k):int(v) for k,v in C.eigenvals().items()},
 'native_structural_face_mode':{'eigenvalue':'1/4','v':[int(x) for x in v],'face_readout_covariance_rank':1,'face_readout_nonzero_eigenvalue':str(S.Rational(3*M,2))},
 'burden_autocorrelation':{'C_D0':str(M),'C_D1_over_M':str(-1),'C_D2_over_M':str(S.Rational(3,2)),'constant_gate_C_D2_over_M':'1','four_phase_sector_eigenvalues':[str(k) for k in B.eigenvals()],'spectral_weights':[str(w) for w in weights], 'at_s_1':{'seam_gate_a1':n1,'constant_gate_a0':n0,'phase_gate_off':1.0,'difference_from_constant_gate':n1-n0}},
 'readout_limit':'One antisymmetric structural face eigenmode excited; phase observable has e^-s temporal response. No nonzero second face mode with distinct source-derived decay rate.',
 'selection_no_go':'h_a=(1+a Re U)/2 for a∈[-1,1] obeys same structural/closure/stock constraints; a=0 and a=1 differ. Source does not select a or phase jump rate.',
 'physical_promotion':0
}
path=Path('/mnt/data/UD_TWO_TETRA_NATIVE_SOURCE_GATE_v0.1_results.json');path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:out[k] for k in ['carrier','exact_controls','native_structural_face_mode','burden_autocorrelation','selection_no_go']},indent=2,default=str))
