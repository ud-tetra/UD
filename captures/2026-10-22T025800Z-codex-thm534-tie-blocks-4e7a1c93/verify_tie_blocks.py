"""Fresh exact constructor checks; no archived verifier is imported or executed."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from collections import Counter
from pathlib import Path
import json

CELLS=[(0,1,2,3),(0,1,2,4)]
FACES=sorted(set(combinations(CELLS[0],3))|set(combinations(CELLS[1],3)))
D=[[0,0] for _ in FACES]
for j,c in enumerate(CELLS):
    for k in range(4):D[FACES.index(c[:k]+c[k+1:])][j]=(1,-1)[j]*(-1)**k
FOOT=[{f}|{7+j for j in range(2) if D[f][j]} for f in range(7)]
EDGES=[(u,v) for u,v in combinations(range(7),2) if FOOT[u]&FOOT[v]]
CONTACTS=[(f,j) for f in range(7) for j in range(2) if D[f][j]]
def partition(w):
    parent=list(range(7))
    def find(i):
        while parent[i]!=i:i=parent[i]
        return i
    for u,v in EDGES:
        if w[u]==w[v]:parent[find(u)]=find(v)
    groups={}
    for i in range(7):groups.setdefault(find(i),[]).append(i)
    return tuple(sorted(tuple(v) for v in groups.values()))
def quotient(p):
    index={f:i for i,b in enumerate(p) for f in b}
    return sorted({tuple(sorted((index[u],index[v]))) for u,v in EDGES if index[u]!=index[v]})
def orient(p,w):
    assert all(len({w[f] for f in b})==1 for b in p)
    value=[w[b[0]] for b in p]
    assert all(value[u]!=value[v] for u,v in quotient(p))
    return frozenset((u,v) if value[u]<value[v] else (v,u) for u,v in quotient(p))
def sinks(n,arcs):return [v for v in range(n) if not any(u==v for u,w in arcs)]
def acyclic(n,arcs):
    left=set(range(n))
    while left:
        ss={v for v in left if not any(u==v and w in left for u,w in arcs)}
        if not ss:return False
        left-=ss
    return True
def parity(s):return (-1)**sum(s[i]>s[j] for i in range(len(s)) for j in range(i+1,len(s)))
AUTOS=[]
for p in permutations((0,1,2)):
    for tips in ((3,4),(4,3)):
        perm=p+tips;qf=[FACES.index(tuple(sorted(perm[v] for v in f))) for f in FACES]
        sf=[parity(tuple(perm[v] for v in f)) for f in FACES]
        qc=[CELLS.index(tuple(sorted(perm[v] for v in c))) for c in CELLS]
        sc=[(1,-1)[j]*parity(tuple(perm[v] for v in c))*(1,-1)[qc[j]] for j,c in enumerate(CELLS)]
        assert all(D[qf[f]][qc[j]]==sf[f]*D[f][j]*sc[j] for f in range(7) for j in range(2))
        AUTOS.append((qf,sf,qc,sc))
P=set();partition_covariance=0
for w in product(range(4),repeat=7):
    p=partition(w);P.add(p);arcs=orient(p,w);assert acyclic(len(p),arcs)
    for qf,_,_,_ in AUTOS:
        wp=[0]*7
        for f in range(7):wp[qf[f]]=w[f]
        pp=partition(wp);assert pp==tuple(sorted(tuple(sorted(qf[f] for f in b)) for b in p))
        qb=[pp.index(tuple(sorted(qf[f] for f in b))) for b in p]
        assert orient(pp,wp)==frozenset((qb[u],qb[v]) for u,v in arcs)
        partition_covariance+=1
assert len(P)==225
distribution=dict(sorted(Counter(map(len,P)).items()))
assert distribution=={1:1,2:14,3:61,4:86,5:50,6:12,7:1}
BLOCKS=sorted({b for p in P for b in p});assert len(BLOCKS)==78
orientation_count=0;prefix_checks=0;max_bound=0
for p in sorted(P):
    n=len(p);edges=quotient(p);foot=[set().union(*(FOOT[f] for f in b)) for b in p]
    adj=[{v if i==u else u for u,v in edges if i in (u,v)} for i in range(n)]
    bounds=[]
    for i in range(n):
        dist={i:0};todo=[i]
        for u in todo:
            for v in adj[u]:
                if v not in dist:dist[v]=dist[u]+1;todo.append(v)
        assert len(dist)==n;bounds.append(1+sum(dist.values()))
    max_bound=max(max_bound,*bounds)
    orientations=set()
    for order in permutations(range(n)):
        rank={v:i for i,v in enumerate(order)}
        orientations.add(frozenset((u,v) if rank[u]<rank[v] else (v,u) for u,v in edges))
    orientation_count+=len(orientations)
    for initial in orientations:
        arcs=initial;counts=[0]*n;first=[0]*n;attempts=0
        for _ in range(20):
            assert acyclic(n,arcs);ss=sinks(n,arcs);assert ss
            assert all(not foot[u]&foot[v] for u,v in combinations(ss,2))
            for v in ss:
                counts[v]+=1;attempts+=1
                if not first[v]:first[v]=attempts
                assert all(0<=counts[b]-counts[a]<=1 for a,b in initial);prefix_checks+=1
            arcs=frozenset((v,u) if u in ss or v in ss else (u,v) for u,v in arcs)
        assert all(0<x<=b for x,b in zip(first,bounds))
assert orientation_count==5625 and max_bound==10

EPS=F(1,4);S=EPS/2
def norm(z):return sum(x*x for x in z)
def matrix(block,mask):return [[D[f][j]*mask.get((f,j),0) if f in block else 0 for j in range(2)] for f in range(7)]
def joint(z,block,mask):
    m=matrix(block,mask)
    a=sum(row[0]**2 for row in m);b=sum(row[0]*row[1] for row in m);c=sum(row[1]**2 for row in m)
    k00=1+S*S*a;k01=S*S*b;k11=1+S*S*c;det=k00*k11-k01*k01;assert det>0
    r0=(1-S*S*a)*z[7]-S*S*b*z[8]+2*S*sum(m[f][0]*z[f] for f in range(7))
    r1=(1-S*S*c)*z[8]-S*S*b*z[7]+2*S*sum(m[f][1]*z[f] for f in range(7))
    out=z[:];out[7]=(k11*r0-k01*r1)/det;out[8]=(k00*r1-k01*r0)/det
    for f in range(7):out[f]=z[f]-S*sum(m[f][j]*(z[7+j]+out[7+j]) for j in range(2))
    mid=[(x+y)/2 for x,y in zip(z,out)]
    J=[[2*EPS*m[f][j]*mid[f]*mid[7+j] for j in range(2)] for f in range(7)]
    for f in range(7):
        assert out[f]-z[f]==-EPS*sum(m[f][j]*mid[7+j] for j in range(2))
        assert out[f]**2-z[f]**2==-sum(J[f])
    for j in range(2):
        assert out[7+j]-z[7+j]==EPS*sum(m[f][j]*mid[f] for f in range(7))
        assert out[7+j]**2-z[7+j]**2==sum(J[f][j] for f in range(7))
        weight=[F(int(D[f][j]!=0),sum(int(v!=0) for v in D[f])) for f in range(7)]
        owned_delta=out[7+j]**2-z[7+j]**2+sum(weight[f]*(out[f]**2-z[f]**2) for f in range(7))
        assert owned_delta==sum(J[f][j]-weight[f]*sum(J[f]) for f in range(7))
    assert norm(out)==norm(z)
    return out
def solve(a,b):
    a=[list(map(F,row))+[F(v)] for row,v in zip(a,b)];n=len(b)
    for j in range(n):
        k=next(k for k in range(j,n) if a[k][j]);a[k],a[j]=a[j],a[k];scale=a[j][j];a[j]=[x/scale for x in a[j]]
        for k in range(n):
            if k!=j:
                scale=a[k][j]
                if scale:a[k]=[x-scale*y for x,y in zip(a[k],a[j])]
    return [row[-1] for row in a]
def full_solve(z,block,mask):
    m=matrix(block,mask);a=[[F(0) for _ in range(9)] for _ in range(9)]
    for f in range(7):
        for j in range(2):a[f][7+j]=-m[f][j];a[7+j][f]=m[f][j]
    return solve([[F(i==j)-S*a[i][j] for j in range(9)] for i in range(9)],[z[i]+S*sum(a[i][j]*z[j] for j in range(9)) for i in range(9)])
control=[F(i-3,7) for i in range(9)];live=dict.fromkeys(CONTACTS,1);mask_controls=0
for bits in product((0,1),repeat=8):
    mask=dict(zip(CONTACTS,bits))
    for block in BLOCKS:joint(control,block,mask);mask_controls+=1
for block in BLOCKS:assert joint(control,block,live)==full_solve(control,block,live)
def transport(z,a):
    qf,sf,qc,sc=a;out=[F(0)]*9
    for f in range(7):out[qf[f]]=sf[f]*z[f]
    for j in range(2):out[7+qc[j]]=sc[j]*z[7+j]
    return out
signed_controls=0
for block in ((1,3),tuple(range(7))):
    for bits in product((0,1),repeat=8):
        mask=dict(zip(CONTACTS,bits));out=joint(control,block,mask)
        for a in AUTOS:
            qf,_,qc,_=a;mp={(qf[f],qc[j]):v for (f,j),v in mask.items()}
            assert joint(transport(control,a),tuple(qf[f] for f in block),mp)==transport(out,a)
            signed_controls+=1
pairs=[]
for a,b in combinations(BLOCKS,2):
    if not set().union(*(FOOT[f] for f in a))&set().union(*(FOOT[f] for f in b)):pairs.append((a,b))
assert len(pairs)==49
for a,b in pairs:
    for bits in ((0,)*8,(1,)*8,(0,1)*4,(1,0)*4):
        mask=dict(zip(CONTACTS,bits));assert joint(joint(control,a,mask),b,mask)==joint(joint(control,b,mask),a,mask)
# Symmetric nonzero state: quotient service is possible but no support transfer occurs.
dark=[F(0)]*9;dark[1]=dark[3]=1;p=partition([x*x for x in dark[:7]])
assert p==((0,2,4,5,6),(1,3))
assert all(joint(dark,block,live)==dark for block in p)
# One-sided discontinuity of the first-block update at that exact stock tie.
for denominator in (1,2,4,16,1024):
    delta=F(1,denominator);z=dark[:];z[3]+=delta;p=partition([x*x for x in z[:7]]);ss=sinks(len(p),orient(p,[x*x for x in z[:7]]))
    assert len(ss)==1 and p[ss[0]]==(3,)
    out=joint(z,p[ss[0]],live);assert out[7]==-F(16,65)*(1+delta)
# Equal stocks can demand a full seven-face, two-core event with nonzero response.
all_tied=[F(1)]*7+[F(0),F(0)];all_tied[0]=-1
assert partition([x*x for x in all_tied[:7]])==(tuple(range(7)),)
assert joint(all_tied,tuple(range(7)),live)!=all_tied
RESULT={'status':'PASS_EXACT_CONDITIONAL_CHANGED_EVENT_FAMILY','four_level_assignments':4**7,'connected_tie_partitions':len(P),'partition_size_distribution':distribution,'partition_orientation_covariance_checks':partition_covariance,'connected_joint_blocks':len(BLOCKS),'quotient_partition_orientation_pairs':orientation_count,'batches_per_pair':20,'quotient_attempt_prefix_checks':prefix_checks,'maximum_quotient_attempt_bound':max_bound,'joint_block_mask_receipt_checks':mask_controls,'independent_full_solve_controls':len(BLOCKS),'signed_joint_mask_covariance_checks':signed_controls,'disjoint_joint_pair_mask_controls':len(pairs)*4,'nonzero_open_contact_stationary_control':True,'first_block_update_discontinuous_at_tie':True,'equal_stock_full_block_coordinates':9,'partition_and_orientation_frozen':True,'native_event_family':'OPEN','native_contact_law':'OPEN','physical_promotion':0,'independent_review':False}
if __name__=='__main__':
    (Path(__file__).parent/'RESULTS.json').write_text(json.dumps(RESULT,indent=2)+'\n');print(json.dumps(RESULT,indent=2))
