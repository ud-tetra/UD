"""Fresh exact star/barycentric history comparison; physical promotion 0."""
import sys,json
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,permutations
import sympy as sp
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
import subdivision_metric as sm

def mat(a): return sp.Matrix(a)
def blocks(basis): return [[i for i,s in enumerate(basis) if len(s)==k] for k in range(1,5)]
def detail_receipt(basis,B,R,kind):
    inds=blocks(basis); P=[];ranks=[]
    for ix in inds:
        rk=R[:,ix]
        rk=rk[[i for i in range(rk.rows) if any(rk[i,j] for j in range(rk.cols))],:]
        pk=sp.eye(len(ix))-rk.T*(rk*rk.T).inv()*rk
        assert pk*pk==pk and rk*pk==sp.zeros(rk.rows,rk.cols)
        P.append(pk);ranks.append(int(sp.trace(pk)))
    d=[P[k-1]*B.extract(inds[k-1],inds[k])*P[k] for k in range(1,4)]
    lap=[];mult=[];samples=[];trivial5=[]
    for k in range(4):
        lk=sp.zeros(len(inds[k]))
        if k: lk+=d[k-1].T*d[k-1]
        if k<3: lk+=d[k]*d[k].T
        assert lk*P[k]==lk
        values=np.linalg.eigvalsh(np.array(lk,float))
        samples.append([float(x) for x in values if x>1e-8])
        mult.append(len(inds[k])-(lk-5*sp.eye(len(inds[k]))).to_DM().rank())
        local_basis=[basis[i] for i in inds[k]];local_ix={s:i for i,s in enumerate(local_basis)}
        average=sp.zeros(len(local_basis))
        for perm in permutations(range(4)):
            for j,simplex in enumerate(local_basis):
                if kind=='star': image=tuple(perm[v] if v<4 else 4 for v in simplex)
                else: image=tuple(sum(1<<perm[v] for v in range(4) if mask&(1<<v)) for mask in simplex)
                average[local_ix[tuple(sorted(image))],j]+=sm.parity(image)
        average/=24
        assert average*average==average and average*lk==lk*average
        stacked=(lk-5*sp.eye(len(inds[k]))).col_join(sp.eye(len(inds[k]))-average)
        trivial5.append(len(inds[k])-stacked.to_DM().rank())
        lap.append(lk)
        print('degree',k,'dimension',len(inds[k]),'detail',ranks[k],'eigenvalue5 multiplicity',mult[-1],flush=True)
    return {'fine_f':list(map(len,inds)),'detail_dimensions':ranks,'sqrt5_degree_multiplicity':mult,'sqrt5_total_multiplicity':sum(mult),'sqrt5_trivial_irrep_degree_multiplicity':trivial5,'numerical_positive_squared_frequency_samples':samples},lap

old=sm.OLD
tetra=[(0,1,2,4),(0,1,3,4),(0,2,3,4),(1,2,3,4)]
star=sorted({s for t in tetra for k in range(1,5) for s in combinations(t,k)},key=lambda s:(len(s),s))
si={s:i for i,s in enumerate(star)}
S=sp.zeros(29,15);R=sp.zeros(15,29)
for j,s in enumerate(old):
    if len(s)<4:S[si[s],j]=1
    else:
        for t,sign in zip(tetra,[1,-1,1,-1]):S[si[t],j]=sign
for j,s in enumerate(star):
    for i,t in enumerate(old):
        if len(s)==len(t):
            R[i,j]=sp.Matrix([[sp.Rational(1,4) if v==4 else int(v==u) for v in s] for u in t]).det()
B=mat(sm.B);BS=mat(sm.boundary(star));SB=mat(sm.S);RB=mat(sm.R);BB=mat(sm.BP)
assert BS*S==S*B and R*BS==B*R and R*S==sp.eye(15)
Q=sp.eye(29)-S*R;H=R.T*R+Q.T*Q
assert H*S==R.T and S.T*H*S==sp.eye(15)
assert BS.T*H*S==H*S*B.T
star_receipt,star_laps=detail_receipt(star,BS,R,'star')
assert star_receipt['detail_dimensions']==[1,4,6,3]
assert star_receipt['sqrt5_degree_multiplicity']==[1,4,6,3]
for k,lk in enumerate(star_laps):assert lk*lk==5*lk
bary_receipt,bary_laps=detail_receipt(sm.NEW,BB,RB,'bary')
assert sum(bary_receipt['detail_dimensions'])==134
assert bary_receipt['sqrt5_degree_multiplicity']==[2,7,8,3]
assert star_receipt['sqrt5_trivial_irrep_degree_multiplicity']==[1,1,0,0]
assert bary_receipt['sqrt5_trivial_irrep_degree_multiplicity']==[0,0,0,0]
coarse= S*RB
assert coarse*SB==S and coarse*(sp.eye(149)-SB*RB)==sp.zeros(29,149)
receipt={'status':'PASS','physical_promotion':0,'star':star_receipt,'barycentric':bary_receipt,
 'star_total_characteristic_polynomial':'lambda*(lambda^2+4)^7*(lambda^2+5)^7',
 'star_detail_boundary_ranks':[1,3,3],'metric':'R.T R + Q.T Q, conditional with unit detail calibration',
 'full_terminal_bijection':'NO-GO: dimensions 149 versus 29',
 'coarse_comparison':'S_star R_bary retains coarse code and annihilates 134 barycentric detail directions',
 'unrestricted_generator_isometry':'EXISTS by spectral multiplicity; target sqrt5 has 10 pairs versus source 7 pairs',
 'graded_chain_isometry':'EXISTS by boundary singular multiplicities [2,5,3] versus [1,3,3], not source-selected',
 'S4_equivariant_generator_isometry':'NO-GO: source has trivial-irrep sqrt5 pair absent from target',
 'native_selection':'OPEN','independent_human_review':'PENDING'}
out=Path(__file__).resolve().parent/'HISTORY_COMPARISON_EXACT_RECEIPT_v0.1.json';out.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k not in ('star','barycentric')},indent=2))
