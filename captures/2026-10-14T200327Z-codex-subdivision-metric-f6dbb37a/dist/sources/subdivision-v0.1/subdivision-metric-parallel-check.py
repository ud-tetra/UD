#!/usr/bin/env python3
"""Fresh exact constructor-team check; no imported scientific code.

Original vertices are 0,1,2,3. A barycentric vertex is a nonempty subset.
A barycentric simplex is an inclusion-ordered strict flag. All arithmetic
uses fractions. The completed metric is a conditional construction, not a
claim that source governance independently selects that metric.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
import json
from pathlib import Path

def zeros(n,m): return [[F(0) for _ in range(m)] for _ in range(n)]
def eye(n):
    a=zeros(n,n)
    for i in range(n): a[i][i]=F(1)
    return a
def transpose(a): return [list(r) for r in zip(*a)]
def mul(a,b):
    out=zeros(len(a),len(b[0]))
    br=[[(j,x) for j,x in enumerate(row) if x] for row in b]
    for i,row in enumerate(a):
        for k,x in enumerate(row):
            if x:
                for j,y in br[k]: out[i][j]+=x*y
    return out
def add(a,b): return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def sub(a,b): return [[x-y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(a,s): return [[s*x for x in row] for row in a]
def zero(a): return all(not x for row in a for x in row)
def sign(p): return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def determinant(a):
    n=len(a)
    return sum((F(sign(p))*prod(a[i][p[i]] for i in range(n)) for p in permutations(range(n))), F(0))
def prod(xs):
    x=F(1)
    for y in xs: x*=y
    return x
def rank(a):
    a=[r[:] for r in a]; n=len(a); m=len(a[0]); i=0
    for j in range(m):
        piv=next((h for h in range(i,n) if a[h][j]),None)
        if piv is None: continue
        a[i],a[piv]=a[piv],a[i]; d=a[i][j]; a[i]=[x/d for x in a[i]]
        for h in range(n):
            if h!=i and a[h][j]:
                d=a[h][j]; a[h]=[x-d*y for x,y in zip(a[h],a[i])]
        i+=1
        if i==n: break
    return i

original=[[tuple(t) for t in combinations(range(4),k+1)] for k in range(4)]
faces=[frozenset(t) for k in original for t in k]
refined=[]
for k in range(4):
    flags=[]
    for chain in combinations(faces,k+1):
        ordered=tuple(sorted(chain,key=lambda t:(len(t),tuple(t))))
        if all(ordered[i]<ordered[i+1] for i in range(k)): flags.append(ordered)
    refined.append(sorted(flags,key=lambda flag:tuple((len(f),tuple(sorted(f))) for f in flag)))
index0=[{x:i for i,x in enumerate(xs)} for xs in original]
index1=[{x:i for i,x in enumerate(xs)} for xs in refined]
def boundaries(xs,ids):
    ans=[None]
    for k in range(1,4):
        b=zeros(len(xs[k-1]),len(xs[k]))
        for j,sigma in enumerate(xs[k]):
            for h in range(k+1): b[ids[k-1][sigma[:h]+sigma[h+1:]]][j]=F((-1)**h)
        ans.append(b)
    return ans
B=boundaries(original,index0); C=boundaries(refined,index1)
S=[]; R=[]
for k in range(4):
    s=zeros(len(refined[k]),len(original[k])); r=zeros(len(original[k]),len(refined[k]))
    for j,sigma in enumerate(original[k]):
        for p in permutations(sigma):
            flag=tuple(frozenset(p[:h+1]) for h in range(k+1))
            s[index1[k][flag]][j]+=F(sign(p))
    for j,flag in enumerate(refined[k]):
        for i,sigma in enumerate(original[k]):
            r[i][j]=determinant([[F(1,len(face)) if v in face else F(0) for face in flag] for v in sigma])
    S.append(s); R.append(r)
Q=[]; H=[]
for k in range(4):
    q=sub(eye(len(refined[k])),mul(S[k],R[k])); Q.append(q)
    H.append(add(mul(transpose(R[k]),R[k]),mul(transpose(q),q)))

checks={}
def check(name,predicate):
    checks[name]=bool(predicate)
    assert predicate,name
for k in range(4):
    fact=prod(range(1,k+2))
    check(f'retraction_degree_{k}',mul(R[k],S[k])==eye(len(original[k])))
    check(f'subdivision_euclidean_gram_degree_{k}',mul(transpose(S[k]),S[k])==scale(eye(len(original[k])),fact))
    check(f'projector_degree_{k}',mul(Q[k],Q[k])==Q[k])
    check(f'kernel_projector_degree_{k}',zero(mul(R[k],Q[k])))
    check(f'metric_times_subdivision_degree_{k}',mul(H[k],S[k])==transpose(R[k]))
    check(f'metric_isometry_degree_{k}',mul(transpose(S[k]),mul(H[k],S[k]))==eye(len(original[k])))
    # Since u=S R u+Q u, ||R u||²+||Q u||²=0 iff u=0.
    check(f'spd_reconstruction_certificate_degree_{k}',add(mul(S[k],R[k]),Q[k])==eye(len(refined[k])))
for k in range(1,4):
    check(f'subdivision_chain_degree_{k}',mul(C[k],S[k])==mul(S[k-1],B[k]))
    check(f'retraction_chain_degree_{k}',mul(R[k-1],C[k])==mul(B[k],R[k]))
    # H_k S_k B_kᵀ = C_kᵀ H_(k-1) S_(k-1): multiplying
    # by H_k^{-1} yields the required weighted-adjoint equality.
    check(f'weighted_adjoint_intertwining_degree_{k}',mul(H[k],mul(S[k],transpose(B[k])))==mul(transpose(C[k]),mul(H[k-1],S[k-1])))
for k in (2,3):
    check(f'original_boundary_squared_degree_{k}',zero(mul(B[k-1],B[k])))
    check(f'refined_boundary_squared_degree_{k}',zero(mul(C[k-1],C[k])))

# The action on refined flags has no orientation sign: inclusion order stays
# inclusion order. Original sorted simplices have the induced permutation sign.
for p in permutations(range(4)):
    for k in range(4):
        orig=[]
        for sigma in original[k]:
            image=tuple(p[v] for v in sigma)
            orig.append((index0[k][tuple(sorted(image))],sign(image)))
        ref=[index1[k][tuple(frozenset(p[v] for v in face) for face in flag)] for flag in refined[k]]
        check(f'S_equivariance_{p}_degree_{k}',all(S[k][ref[i]][orig[j][0]]==orig[j][1]*S[k][i][j] for i in range(len(ref)) for j in range(len(orig))))
        check(f'R_equivariance_{p}_degree_{k}',all(R[k][orig[i][0]][ref[j]]==orig[i][1]*R[k][i][j] for i in range(len(orig)) for j in range(len(ref))))
        check(f'H_invariance_{p}_degree_{k}',all(H[k][ref[i]][ref[j]]==H[k][i][j] for i in range(len(ref)) for j in range(len(ref))))

naive=[]
for k in range(1,4):
    delta=sub(scale(mul(transpose(C[k]),S[k-1]),F(k+1)),mul(S[k],transpose(B[k])))
    nonzero=[x for row in delta for x in row if x]
    naive.append({'degree':k,'rank':rank(delta),'nonzero_entries':len(nonzero),'max_abs':str(max(abs(x) for x in nonzero)), 'fails':bool(nonzero)})
    check(f'naive_factorial_metric_generator_failure_degree_{k}',bool(nonzero))

out={'scope':'constructor-team exact check; conditional metric; source selection OPEN; physical promotion 0',
     'original_f_vector':[len(x) for x in original], 'refined_f_vector':[len(x) for x in refined],
     'original_dimension':sum(map(len,original)), 'refined_dimension':sum(map(len,refined)),
     'checks':checks,'check_count':len(checks),'all_passed':all(checks.values()),
     'metric_formula':'H_k = R_k^T R_k + (I-S_k R_k)^T (I-S_k R_k)',
     'naive_factorial_metric_adjoint_defects':naive,
     'metric_nonzero_entries':[sum(bool(x) for row in a for x in row) for a in H],
     'metric_max_denominators':[max(x.denominator for row in a for x in row) for a in H]}
Path(__file__).with_name('subdivision-metric-parallel-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({key:out[key] for key in ('original_f_vector','refined_f_vector','check_count','all_passed','naive_factorial_metric_adjoint_defects','metric_max_denominators')},indent=2))
