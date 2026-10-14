"""Exact sparse two-level barycentric refinement and calibrated detail accounting."""
from fractions import Fraction as F
from itertools import combinations,permutations
from functools import lru_cache
from math import factorial
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parent
def clean(v):return {i:x for i,x in v.items() if x}
def add(a,b,sign=1):
    c=a.copy()
    for i,x in b.items():c[i]=c.get(i,F(0))+sign*x
    return clean(c)
def apply(a,v):
    out={}
    for j,x in v.items():
        for i,y in a[j].items():out[i]=out.get(i,F(0))+x*y
    return clean(out)
def compose(a,b):return [apply(a,c) for c in b]
def norm(v):return sum(x*x for x in v.values())
def det(a):
    if len(a)==1:return a[0][0]
    return sum((-1)**j*a[0][j]*det([r[:j]+r[j+1:] for r in a[1:]]) for j in range(len(a)) if a[0][j])
def parity(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def boundary(basis):
    ix={s:i for i,s in enumerate(basis)}
    return [{ix[s[:j]+s[j+1:]]:F((-1)**j) for j in range(len(s))} if len(s)>1 else {} for s in basis]
def subdivide(old):
    ix={s:i for i,s in enumerate(old)}
    @lru_cache(None)
    def flags(index):
        face=old[index];out=[(index,)]
        for size in range(1,len(face)):
            for proper in combinations(face,size):out.extend(p+(index,) for p in flags(ix[proper]))
        return tuple(out)
    new=sorted((flag for i in range(len(old)) for flag in flags(i)),key=lambda s:(len(s),s))
    ni={s:i for i,s in enumerate(new)};assert len(ni)==len(new)
    s=[]
    for simplex in old:
        col={}
        for p in permutations(simplex):
            flag=tuple(ix[tuple(sorted(p[:j]))] for j in range(1,len(p)+1));col[ni[flag]]=F(parity(p))
        s.append(col)
    r=[]
    for flag in new:
        source_faces=[old[j] for j in flag];maximum=source_faces[-1];col={}
        for source in combinations(maximum,len(flag)):
            coefficient=det([[F(v in face,len(face)) for face in source_faces] for v in source])
            if coefficient:col[ix[source]]=coefficient
        r.append(col)
    return new,s,r
def detail(s,r,x):return add(x,apply(s,apply(r,x)),-1)
def count_next(f):
    v,e,t,c=f;return [v+e+t+c,2*e+6*t+14*c,6*t+36*c,24*c]
def counts(levels):
    out=[];f=[4,6,4,1]
    for level in range(levels+1):
        n=sum(f);out.append({'level':level,'f_vector':f.copy(),'dimension':n,'new_directions':0 if level==0 else n-out[-1]['dimension'],'total_details':n-15});f=count_next(f)
    return out
def verify():
    k0=[s for n in range(1,5) for s in combinations(range(4),n)]
    k1,s10,r10=subdivide(k0);k2,s21,r21=subdivide(k1)
    b0,b1,b2=map(boundary,[k0,k1,k2])
    assert len(k0)==15 and len(k1)==149 and len(k2)==2745
    for basis,s,r,b,bp in [(k0,s10,r10,b0,b1),(k1,s21,r21,b1,b2)]:
        assert compose(r,s)==[{i:F(1)} for i in range(len(basis))]
        assert compose(bp,s)==compose(s,b)
        assert compose(r,bp)==compose(b,r)
        owned=set()
        for simplex,col in zip(basis,s):
            assert len(col)==factorial(len(simplex)) and all(abs(v)==1 for v in col.values())
            assert not owned.intersection(col);owned.update(col)
    for b in [b0,b1,b2]:assert all(not c for c in compose(b,b))
    s20=compose(s21,s10);r20=compose(r10,r21)
    assert compose(r20,s20)==[{i:F(1)} for i in range(15)]
    assert compose(b2,s20)==compose(s20,b0) and compose(r20,b2)==compose(b0,r20)
    records=[]
    for degree in [1,2,3]:
        source=tuple(range(degree+1));col=s10[k0.index(source)];j,k=list(col)[:2];m=factorial(degree+1)
        # Two oriented descendants whose affine coarse contributions cancel.
        z={j:col[j],k:-col[k]}
        assert not apply(r10,z)
        x=apply(s21,z);assert not apply(r20,x)
        sequential=norm(z);fresh=norm(x)
        assert sequential==2 and fresh==m*sequential
        records.append({'degree':degree,'factor':m,'sequential_norm_squared':str(sequential),'fresh_composite_norm_squared':str(fresh)})
    # Simpler unscaled edge witness, then add a calibrated coarse vertex.
    index1={s:i for i,s in enumerate(k1)};index0={s:i for i,s in enumerate(k0)}
    edgeid=index0[(0,1)];z={index1[(index0[(0,)],edgeid)]:F(1),index1[(index0[(1,)],edgeid)]:F(1)}
    assert not apply(r10,z) and norm(z)==2
    lifted=apply(s21,z);assert norm(lifted)==4
    probes=[{j:F(1)} for j in [0,148,149,400,945,946,2000,2168,2169,2744]]+[lifted]
    mixed=add(apply(s20,{index0[(0,)]:F(1)}),lifted);probes.append(mixed)
    ledger=[]
    for x in probes:
        c0=apply(r20,x);z1=detail(s10,r10,apply(r21,x));z2=detail(s21,r21,x)
        assert x==add(add(apply(s20,c0),apply(s21,z1)),z2)
        q20=detail(s20,r20,x)
        assert q20==add(z2,apply(s21,z1))
        sequential=norm(c0)+norm(z1)+norm(z2)
        recursive=norm(apply(r10,apply(r21,x)))+norm(detail(s10,r10,apply(r21,x)))+norm(z2)
        assert sequential==recursive
        # Transported composite complement form W20 matches both retained levels.
        induced=norm(detail(s10,r10,apply(r21,q20)))+norm(detail(s21,r21,q20))
        assert sequential==norm(c0)+induced
        fresh=norm(c0)+norm(q20)
        fractions=[v*v/sequential for v in c0.values()]+[norm(z1)/sequential,norm(z2)/sequential]
        assert sum(fractions)==1
        ledger.append({'sequential_norm_squared':str(sequential),'fresh_composite_norm_squared':str(fresh),'coarse_stock':str(norm(c0)),'first_detail_stock':str(norm(z1)),'new_detail_stock':str(norm(z2))})
    assert ledger[-1]=={'sequential_norm_squared':'3','fresh_composite_norm_squared':'5','coarse_stock':'1','first_detail_stock':'2','new_detail_stock':'0'}
    fcounts=counts(4);assert fcounts[2]['f_vector']==[149,796,1224,576]
    assert fcounts[2]['new_directions']==2596 and fcounts[2]['total_details']==2730
    return {'status':'PASS','version':'0.1','reading_edition':'0.13','physical_promotion':0,
      'scope':'Exact conditional consistency for the same retained refinement sequence; no native metric/history/event adoption.',
      'counts':fcounts,'all_sparse_chain_identities':True,'all_step_and_composite_retractions':True,
      'sparse_nonzeros':{'B2':sum(map(len,b2)),'S21':sum(map(len,s21)),'R21':sum(map(len,r21)),'S20':sum(map(len,s20)),'R20':sum(map(len,r20))},
      'factorial_detail_witnesses':records,'edge_detail_witness':{'sequential':'2','fresh_composite':'4'},
      'probe_count':len(probes),'probe_ledgers':ledger,'mixed_witness':{'coarse_stock':'1','sequential_total':'3','fresh_composite_total':'5','sequential_coarse_fraction':'1/3','fresh_coarse_fraction':'1/5'},
      'complete_effect_count':17,'metric_regrouping':'PASS after transporting calibrated detail pairings; fresh unit composite fails on retained details',
      'coarse_observable_composition':'R20=R10R21;K2=R21^T(R10^T D R10)R21=R20^T D R20',
      'composite_detail_form':'PSD on ambient; positive definite on ker R20; kills the original coarse image',
      'dense_2745_metric_materialized':False,'source_adoption':'OPEN','independent_human_review':'PENDING',
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
    r=verify();p=ROOT/'dist/sources/refinement-tower-v0.1/REFINEMENT_TOWER_ROOT_VERIFICATION_v0.1.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'dimensions':[x['dimension'] for x in r['counts'][:3]],'edge_detail':r['edge_detail_witness'],'probes':r['probe_count'],'physical_promotion':0}))
