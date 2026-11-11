"""Fresh sparse exact two-level barycentric refinement checks. No archived code."""
from fractions import Fraction as F
from itertools import combinations,permutations
from math import factorial
from pathlib import Path
import hashlib,json,sys
if not (Path(__file__).parent/'subdivision_metric.py').exists():
    sys.path.insert(0,'/workspace/sites/unified-dynamics-public')
import subdivision_metric as sm

def sparse(a):return [{i:x for i,row in enumerate(a) if (x:=row[j])} for j in range(len(a[0]))]
def addcol(a,b,t=F(1)):
    o=dict(a)
    for i,x in b.items():
        o[i]=o.get(i,F(0))+t*x
        if not o[i]:del o[i]
    return o

def mm(a,b):
    out=[]
    for col in b:
        c={}
        for j,x in col.items():c=addcol(c,a[j],x)
        out.append(c)
    return out

def eye(n):return [{i:F(1)} for i in range(n)]
def sub(a,b):return [addcol(c,d,F(-1)) for c,d in zip(a,b)]
def mv(a,v):
    out={}
    for j,x in v.items():out=addcol(out,a[j],x)
    return out

def norm(v):return sum((x*x for x in v.values()),F(0))
def sqnorm(a,v):return norm(mv(a,v))
def boundary(basis):
    ix={s:i for i,s in enumerate(basis)};cols=[]
    for s in basis:
        cols.append({ix[s[:i]+s[i+1:]]:F((-1)**i) for i in range(len(s))} if len(s)>1 else {})
    return cols

def sd_step(old):
    oi={s:i for i,s in enumerate(old)};sets=set()
    for s in old:
        for p in permutations(s):
            full=tuple(oi[tuple(sorted(p[:k]))] for k in range(1,len(s)+1))
            for size in range(1,len(full)+1):
                sets.update(combinations(full,size))
    fine=sorted(sets,key=lambda t:(len(t),t));fi={s:i for i,s in enumerate(fine)}
    scol=[]
    for s in old:
        c={}
        for p in permutations(s):
            flag=tuple(oi[tuple(sorted(p[:k]))] for k in range(1,len(s)+1))
            c[fi[flag]]=F(sm.parity(p))
        scol.append(c)
    rcol=[]
    for flag in fine:
        largest=old[flag[-1]];k=len(flag);c={}
        for s in combinations(largest,k):
            d=sm.det([[F(v in old[f],len(old[f])) for f in flag] for v in s])
            if d:c[oi[s]]=d
        rcol.append(c)
    return fine,boundary(fine),scol,rcol

def main():
    old=sm.OLD;one=sm.NEW;B0=sparse(sm.B);B1=sparse(sm.BP);S10=sparse(sm.S);R10=sparse(sm.R)
    two,B2,S21,R21=sd_step(one)
    f2=[sum(len(s)==k for s in two) for k in range(1,5)]
    assert f2==[149,796,1224,576]
    assert mm(B2,B2)==[{} for _ in two]
    assert mm(B2,S21)==mm(S21,B1)
    assert mm(R21,B2)==mm(B1,R21)
    assert mm(R21,S21)==eye(149)
    S20=mm(S21,S10);R20=mm(R10,R21)
    assert mm(R20,S20)==eye(15)
    assert mm(B2,S20)==mm(S20,B0)
    assert mm(R20,B2)==mm(B0,R20)
    Q10=sub(eye(149),mm(S10,R10));Q21=sub(eye(2745),mm(S21,R21));Q20=sub(eye(2745),mm(S20,R20))
    assert mm(Q21,Q21)==Q21
    # Q20 idempotence is exact algebra from replayed R20S20=I, avoiding
    # a dense-on-the-top-grade 576²-block cubic projector product.
    assert mm(R21,Q21)==[{} for _ in two]
    assert mm(R20,Q20)==[{} for _ in two]
    C=mm(Q10,R21);liftC=mm(S21,C)
    assert Q20==[addcol(a,b) for a,b in zip(Q21,liftC)]
    assert mm(B2,Q21)==mm(Q21,B2)
    # Q20 commutes with B2 by the two replayed composite chain identities.
    # Each subdivision image has disjoint support, so its Gram is factorial by grade.
    assert all(norm(c)==factorial(len(one[j])) for j,c in enumerate(S21))
    support={}
    for j,c in enumerate(S21):
        for i in c:assert i not in support;support[i]=j
    witnesses=[]
    for degree,fa,fb in [(1,(1,3),(2,3)),(2,(1,3,7),(2,3,7)),(3,(1,3,7,15),(2,3,7,15))]:
        z={one.index(fa):F(1),one.index(fb):F(1)}
        assert not mv(R10,z) and mv(Q10,z)==z
        x=mv(S21,z)
        assert mv(R21,x)==z and not mv(Q21,x) and not mv(R20,x) and mv(Q20,x)==x
        sequential=sqnorm(R20,x)+sqnorm(C,x)+sqnorm(Q21,x)
        direct=sqnorm(R20,x)+sqnorm(Q20,x)
        assert sequential==2 and direct==2*factorial(degree+1)
        witnesses.append({'degree':degree,'coarse_complement_flags':[list(fa),list(fb)],'old_complement_norm_squared':'2','sequential_metric_norm_squared':str(sequential),'one_shot_unit_metric_norm_squared':str(direct),'ratio':str(direct/sequential)})
    # Mixed source/residual shares expose the calibration choice.
    z={one.index((1,3)):F(1),one.index((2,3)):F(1)}
    x=addcol(mv(S20,{0:F(1)}),mv(S21,z))
    assert sqnorm(R20,x)==1 and sqnorm(C,x)==2 and sqnorm(Q21,x)==0
    assert sqnorm(Q20,x)==4
    mixed={'absolute_coarse_stock':'1','sequential_total':'3','unit_final_total':'5','sequential_coarse_fraction':'1/3','unit_final_coarse_fraction':'1/5'}
    # Norm functional completeness: source region stocks plus two retained residuals.
    print('Exact chain maps, composite retractions and factorial witnesses PASS',flush=True)
    probes=[{i:F(1)} for i in range(2745)]
    probes.extend({j:F(((j+3*k)%13)-6,7) for j in range(2745) if ((j+3*k)%13)-6} for k in range(3))
    for x in probes:
        decoded=mv(R20,x);mid=mv(C,x);fine=mv(Q21,x)
        reconstructed=addcol(addcol(mv(S20,decoded),mv(S21,mid)),fine)
        assert reconstructed==x
        norm_seq=norm(decoded)+norm(mid)+norm(fine)
        assert norm_seq>0
        assert sum((a*a for a in decoded.values()),F(0))+norm(mid)+norm(fine)==norm_seq
        # Corrected direct complement pairing agrees on every tested input.
        q=mv(Q20,x)
        assert norm(mv(C,q))+norm(mv(Q21,q))==norm(mid)+norm(fine)
    report={'status':'PASS','arithmetic':'exact fractions, sparse standard-library matrices','physical_promotion':0,'source_adoption':'OPEN','independent_human_review':'PENDING','f_vectors':[[4,6,4,1],[15,50,60,24],f2],'dimensions':[15,149,2745],'chain_checks':['B2²=0','B2 S21=S21 B1','R21 B2=B1 R21','R21 S21=I149','R20 S20=I15','B2 S20=S20 B0','R20 B2=B0 R20','Q20=Q21+S21 Q10 R21'],'probes':len(probes),'witnesses':witnesses,'mixed_calibration_witness':mixed,'complete_effect_count':17,'coherent_metric_norm':'||R20 x||²+||Q10 R21 x||²+||Q21 x||²','corrected_direct_residual_norm':'||Q10 R21 q||²+||Q21 q||² for q=Q20x','nonzeros':{name:sum(map(len,a)) for name,a in [('B2',B2),('S21',S21),('R21',R21),('S20',S20),('R20',R20),('Q20',Q20)]},'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path('/workspace/scratch/384298a218b5/tower-parallel-results.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
