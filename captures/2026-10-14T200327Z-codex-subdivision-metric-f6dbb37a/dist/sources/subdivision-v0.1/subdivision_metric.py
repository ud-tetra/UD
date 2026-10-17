"""Fresh exact subdivision/retraction construction; archived programmes are data only."""
from fractions import Fraction as F
from itertools import combinations,permutations
from math import factorial
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parent
def zero(r,c):return [[F(0) for _ in range(c)] for _ in range(r)]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def transpose(a):return list(map(list,zip(*a)))
def add(a,b,sign=1):return [[x+sign*y for x,y in zip(r,s)] for r,s in zip(a,b)]
def multiply(a,b):
    assert len(a[0])==len(b)
    out=zero(len(a),len(b[0]));sparse=[[(j,v) for j,v in enumerate(row) if v] for row in b]
    for i,row in enumerate(a):
        for k,x in enumerate(row):
            if x:
                for j,y in sparse[k]:out[i][j]+=x*y
    return out
def det(a):
    if len(a)==1:return a[0][0]
    return sum((-1)**j*a[0][j]*det([r[:j]+r[j+1:] for r in a[1:]]) for j in range(len(a)) if a[0][j])
def rank(a):
    a=[row[:] for row in a];pivot=0
    for col in range(len(a[0])):
        found=next((i for i in range(pivot,len(a)) if a[i][col]),None)
        if found is None:continue
        a[pivot],a[found]=a[found],a[pivot];v=a[pivot][col];a[pivot]=[x/v for x in a[pivot]]
        for i in range(pivot+1,len(a)):
            if a[i][col]:
                v=a[i][col];a[i]=[x-v*y for x,y in zip(a[i],a[pivot])]
        pivot+=1
        if pivot==len(a):break
    return pivot
def parity(xs):return (-1)**sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)))
def boundary(basis):
    ix={s:i for i,s in enumerate(basis)};out=zero(len(basis),len(basis))
    for s,j in ix.items():
        if len(s)>1:
            for k in range(len(s)):out[ix[s[:k]+s[k+1:]]][j]=F((-1)**k)
    return out
def build():
    old=[s for k in range(1,5) for s in combinations(range(4),k)]
    new=[s for k in range(1,5) for s in combinations(range(1,16),k) if all((a&b)==a for a,b in zip(s,s[1:]))]
    oi={s:i for i,s in enumerate(old)};ni={s:i for i,s in enumerate(new)}
    s=zero(149,15);r=zero(15,149)
    for simplex,j in oi.items():
        for perm in permutations(simplex):
            prefix=0;flag=[]
            for v in perm:prefix|=1<<v;flag.append(prefix)
            s[ni[tuple(flag)]][j]=F(parity(perm))
    for flag,j in ni.items():
        degree=len(flag)
        for simplex,i in oi.items():
            if len(simplex)==degree:r[i][j]=det([[F(bool(mask&(1<<v)),mask.bit_count()) for mask in flag] for v in simplex])
    return old,new,boundary(old),boundary(new),s,r
def metric(s,r,weights):
    q=add(eye(149),multiply(s,r),-1)
    wq=[[weights[len(flag)-1]*v for v in row] for flag,row in zip(NEW,q)]
    return add(multiply(transpose(r),r),multiply(transpose(q),wq)),q
OLD,NEW,B,BP,S,R=build()
def verify():
    assert [sum(len(x)==k for x in NEW) for k in range(1,5)]==[15,50,60,24]
    assert multiply(B,B)==zero(15,15) and multiply(BP,BP)==zero(149,149)
    assert multiply(BP,S)==multiply(S,B)
    assert multiply(R,BP)==multiply(B,R)
    assert multiply(R,S)==eye(15)
    old_ranks=[];fine_ranks=[]
    for k in range(1,4):
        rows=[i for i,x in enumerate(OLD) if len(x)==k];cols=[i for i,x in enumerate(OLD) if len(x)==k+1]
        old_ranks.append(rank([[B[i][j] for j in cols] for i in rows]))
        rows=[i for i,x in enumerate(NEW) if len(x)==k];cols=[i for i,x in enumerate(NEW) if len(x)==k+1]
        fine_ranks.append(rank([[BP[i][j] for j in cols] for i in rows]))
    complement_ranks=[y-x for x,y in zip(old_ranks,fine_ranks)]
    assert old_ranks==[3,3,1] and fine_ranks==[14,36,24] and complement_ranks==[11,33,23]
    gram=multiply(transpose(S),S)
    assert gram==[[F(factorial(len(OLD[i]))) if i==j else F(0) for j in range(15)] for i in range(15)]
    a=add(transpose(B),B,-1);ap=add(transpose(BP),BP,-1)
    defect=add(multiply(ap,S),multiply(S,a),-1)
    vertex_defects=[sum(defect[j][i]**2 for j in range(149)) for i in range(4)]
    assert vertex_defects==[F(7)]*4
    # Naive degree-diagonal metric: exact isometry and chain map, but wrong adjoint.
    gd=[F(1,factorial(len(flag))) for flag in NEW]
    naive=[[BP[j][i]*gd[j]/gd[i]-BP[i][j] for j in range(149)] for i in range(149)]
    nd=add(multiply(naive,S),multiply(S,a),-1)
    naive_vertex=[sum(gd[j]*nd[j][i]**2 for j in range(149)) for i in range(4)]
    assert naive_vertex==[F(11)]*4
    assert multiply(transpose(S),[[gd[i]*v for v in row] for i,row in enumerate(S)])==eye(15)
    cases=[]
    for weights in [(F(1),)*4,(F(2),)*4,(F(1,2),F(2),F(3),F(4))]:
        h,q=metric(S,R,weights)
        assert h==transpose(h)
        assert multiply(q,q)==q and multiply(R,q)==zero(15,149)
        assert multiply(BP,q)==multiply(q,BP)
        hs=multiply(h,S);assert hs==transpose(R)
        assert multiply(transpose(S),hs)==eye(15)
        # SPD follows from ||Rx||² + sum wk||Qkx||² and x=S Rx+Qx.
        assert all(w>0 for w in weights)
        # This is equivalent to BP^{dagger_H}S=S B^T because H is SPD.
        assert multiply(transpose(BP),hs)==multiply(hs,transpose(B))
        scalar_support={}
        for degree in range(4):
            i=next(i for i,x in enumerate(NEW) if len(x)==degree+1)
            scalar_support[str(degree)]={'coordinate':list(NEW[i]),'metric_diagonal':str(h[i][i])}
        off=sum(h[i][j]!=0 for i in range(149) for j in range(149) if i!=j)
        cases.append({'complement_degree_weights':list(map(str,weights)),'all_three_conditions':'PASS',
            'positive_definite':'Exact split-norm proof; no numerical eigenvalue inference',
            'nonzero_off_diagonal_entries':off,'sample_coordinate_norms':scalar_support})
    # The basic partition and generator counterexamples use exact rational arithmetic.
    for aspect in [F(1),F(3,2),F(7,4),F(2)]:assert 2/(2/aspect)==aspect
    receipt={'status':'PASS','version':'0.1','reading_edition':'0.11','physical_promotion':0,
      'old_f':[4,6,4,1],'new_f':[15,50,60,24],'dimensions':{'old':15,'subdivided':149,'complement':134},
      'source_subdivision_gram_factors':[1,2,6,24],'boundary_chain_identity':True,
      'old_boundary_ranks':old_ranks,'fine_boundary_ranks':fine_ranks,'complement_boundary_ranks':complement_ranks,
      'affine_retraction_chain_identity':True,'retraction_left_inverse':True,
      'unit_euclidean_generator_vertex_defect_squared':list(map(str,vertex_defects)),
      'bounded_S_over_sqrt24_vertex_defect_squared':['7/24']*4,
      'naive_factorial_metric_vertex_generator_defect_squared':list(map(str,naive_vertex)),
      'metric_cases':cases,'weighted_adjoint_check':'BP^T H S=H S B^T; SPD makes this equivalent to weighted-adjoint intertwining',
      'sqrt2_role':'Only the edge degree factor among factorial normalizations; not universal subdivision or feedback law',
      'source_selected_metric':'OPEN','source_selected_retraction':'OPEN','independent_human_review':'PENDING',
      'scope':'Exact conditional metric extension, constructor-team checks. Original Euclidean no-go unchanged; no physical norm/time or funded event law.',
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    return receipt
if __name__=='__main__':
    receipt=verify();p=ROOT/'dist/sources/subdivision-v0.1/SUBDIVISION_METRIC_ROOT_VERIFICATION_v0.1.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'status':receipt['status'],'dimensions':receipt['dimensions'],'metric_cases':len(receipt['metric_cases']),'naive_vertex_defect_squared':receipt['naive_factorial_metric_vertex_generator_defect_squared'],'physical_promotion':0}))
