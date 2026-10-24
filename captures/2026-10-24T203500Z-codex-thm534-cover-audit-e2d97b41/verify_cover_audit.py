#!/usr/bin/env python3
"""Fresh exact presentation-dependence controls; constructor only."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json

def norm(x):return sum(v*v for v in x)
def solve(A,b):
    a=[list(row)+[v] for row,v in zip(A,b)]
    for k in range(len(b)):
        p=next(i for i in range(k,len(b)) if a[i][k]);a[k],a[p]=a[p],a[k]
        d=a[k][k];a[k]=[v/d for v in a[k]]
        for i in range(len(b)):
            if i!=k and a[i][k]:
                d=a[i][k];a[i]=[v-d*w for v,w in zip(a[i],a[k])]
    return [row[-1] for row in a]

CELLS=list(combinations(range(5),4));FACES=list(combinations(range(5),3))
D=[[Q(0)]*5 for _ in range(10)]
for j,c in enumerate(CELLS):
    for i in range(4):D[FACES.index(c[:i]+c[i+1:])][j]=Q((-1)**(i+j))
FS=[{f for f in range(10) if D[f][j]} for j in range(5)]
W=[fs|set(range(10,15)) for fs in FS]
def H(j,h):
    M=[[Q(0)]*15 for _ in range(15)]
    for f in FS[j]:
        for l,d in enumerate(D[f]):
            M[10+l][f]=h[f]*d/2;M[f][10+l]=-h[f]*d/2
    return M
def event(x,j,h,t=Q(1)):
    M=H(j,h);ids=sorted(W[j])
    A=[[Q(a==b)-t*M[a][b]/2 for b in ids] for a in ids]
    rhs=[x[a]+t*sum(M[a][b]*x[b] for b in ids)/2 for a in ids]
    y=list(x)
    for a,v in zip(ids,solve(A,rhs)):y[a]=v
    return y
def scores(x,h,m=1):
    return [norm([a-b for a,b in zip(event(x,j,h,Q(1,m)),x)]) for j in range(5)]
def update(x,h,c=Q(4)):
    s=scores(x,h);E=norm(x)
    w=[max(Q(0),s[j]-max([Q(0)]+[s[l] for l in range(5) if l!=j]))/(c*E) if E else Q(0) for j in range(5)]
    assert all(0<=v<=1 for v in w) and sum(bool(v) for v in w)<=1
    y=list(x)
    for j,v in enumerate(w):
        if v:y=event(y,j,h,v)
    return y,w
def check_receipt(x,y,j,h,t):
    mid=[(a+b)/2 for a,b in zip(x,y)]
    J=[[t*h[f]*D[f][l]*mid[f]*mid[10+l] if f in FS[j] else Q(0) for l in range(5)] for f in range(10)]
    for f in range(10):assert y[f]**2-x[f]**2==-sum(J[f])
    for l in range(5):assert y[10+l]**2-x[10+l]**2==sum(row[l] for row in J)
    for e in range(5):
        owned=lambda v:v[10+e]**2+sum(v[f]**2/2 for f in FS[e])
        assert owned(y)-owned(x)==sum((Q(l==e)-Q(f in FS[e],2))*J[f][l] for f in range(10) for l in range(5))

def main():
    h=[1]*10;x=list(map(Q,[1,0,1,0,0,1,1,0,0,1,1,0,0,0,0]))
    coarse,w=update(x,h);assert w==[Q(8,357)]+[Q(0)]*4 and coarse!=x
    normalizations=[]
    for c in (Q(4),Q(8),Q(16),Q(32)):
        y,v=update(x,h,c);assert v[0]==Q(32,357)/c
        assert norm(y)==6;check_receipt(x,y,0,h,v[0])
        normalizations.append({'c':str(c),'weight':str(v[0]),'output':list(map(str,y))})
    assert len({tuple(item['output']) for item in normalizations})==4
    clone_controls=0;partition_controls=0
    for n in range(32):
        z=[Q(((i+2)*(n+5))%19-9,(i+n)%3+1) for i in range(15)]
        for mask in ([1]*10,[0]*10,[int(i%2==0) for i in range(10)],[int(i%3!=0) for i in range(10)]):
            Ms=[H(j,mask) for j in range(5)]
            for m in (2,3,4):
                for a in range(15):
                    for b in range(15):
                        assert sum(m*(M[a][b]/m) for M in Ms)==sum(M[a][b] for M in Ms)
                partition_controls+=1
                s=scores(z,mask,m)
                # Each indexed clone conflicts with its equal-score twin.
                clone_weights=[]
                for j in range(5):
                    for r in range(m):
                        competitors=[s[l] for l in range(5) for q in range(m) if (l,q)!=(j,r)]
                        clone_weights.append(max(Q(0),s[j]-max([Q(0)]+competitors)))
                assert all(v==0 for v in clone_weights);clone_controls+=1
    # Single native private pair: finite activity and sequential Cayley refinement.
    pair=lambda t:[(1-t*t/4)/(1+t*t/4),t/(1+t*t/4)]
    full=pair(Q(1));half=pair(Q(1,2))
    assert full==[Q(3,5),Q(4,5)] and half==[Q(15,17),Q(8,17)]
    assert norm([full[0]-1,full[1]])==Q(4,5)
    assert 2*norm([half[0]-1,half[1]])==Q(8,17)
    twice=[half[0]**2-half[1]**2,2*half[0]*half[1]]
    assert twice==[Q(161,289),Q(240,289)] and twice!=full
    assert norm(full)==norm(twice)==1
    # Analytic open-sector gap inherited from v2.14, not finite sampling.
    assert Q(64,119)-Q(501,1250)==Q(20381,148750)>0
    report={'status':'PASS','arithmetic':'exact fractions.Fraction','physical_promotion':0,
      'review':'CONSTRUCTOR_ONLY; INDEPENDENT_REVIEW_PENDING',
      'clone_margin_controls':clone_controls,'generator_partition_controls':partition_controls,
      'clone_multiplicities':[2,3,4],'coarse_weight':'8/357',
      'refined_update':'IDENTITY_FOR_ALL_STATES_IN_THE_INDEXED_CLONE_EXTENSION',
      'normalization_family':normalizations,'private_pair_reference_activity':'4/5',
      'two_half_activity_sum':'8/17','two_half_cayley_output':list(map(str,twice)),
      'open_sector_margin_lower_bound':'20381/148750',
      'disposition':'NO_RETRACTION_OF_FIXED_COVER_THEOREMS; NATIVE_COVER_AND_COST_SELECTION_OPEN'}
    Path(__file__).with_name('RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='normalization_family'},indent=2))

if __name__=='__main__':main()
