"""Exact constructor audit. Archived SOURCE_* scripts are never imported/executed."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib,json

HERE=Path(__file__).parent
CELLS=[(0,1,2,3),(0,1,2,4)]
FACES=sorted(set(combinations(CELLS[0],3))|set(combinations(CELLS[1],3)))
D=[[0,0] for _ in FACES]
for j,c in enumerate(CELLS):
    for k in range(4):D[FACES.index(c[:k]+c[k+1:])][j]=(1,-1)[j]*(-1)**k
EDGES=[(u,v) for u,v in combinations(range(7),2) if any(D[u][j]*D[v][j] for j in range(2))]
CONTACTS=[(f,j) for f in range(7) for j in range(2) if D[f][j]]
def orientation(stock):
    if any(stock[u]==stock[v] for u,v in EDGES):return None
    return frozenset((u,v) if stock[u]<stock[v] else (v,u) for u,v in EDGES)
def sinks(arcs):return [v for v in range(7) if not any(u==v for u,w in arcs)]
def reverse(arcs,ss):return frozenset((v,u) if (u in ss or v in ss) else (u,v) for u,v in arcs)
def acyclic(arcs):
    left=set(range(7))
    while left:
        ss={v for v in left if not any(u==v and w in left for u,w in arcs)}
        if not ss:return False
        left-=ss
    return True
def parity(seq):return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
AUTOS=[]
for p in permutations((0,1,2)):
    for tips in ((3,4),(4,3)):
        perm=p+tips
        qf=[FACES.index(tuple(sorted(perm[v] for v in f))) for f in FACES]
        sf=[parity(tuple(perm[v] for v in f)) for f in FACES]
        qc=[CELLS.index(tuple(sorted(perm[v] for v in c))) for c in CELLS]
        sc=[(1,-1)[j]*parity(tuple(perm[v] for v in c))*(1,-1)[qc[j]] for j,c in enumerate(CELLS)]
        assert all(D[qf[f]][qc[j]]==sf[f]*D[f][j]*sc[j] for f in range(7) for j in range(2))
        AUTOS.append((perm,qf,sf,qc,sc))
def transport(z,a):
    _,qf,sf,qc,sc=a;out=[F(0)]*9
    for f in range(7):out[qf[f]]=sf[f]*z[f]
    for j in range(2):out[7+qc[j]]=sc[j]*z[7+j]
    return out
def norm(z):return sum(x*x for x in z)
def step(z,f,mask):
    c=[D[f][j]*mask.get((f,j),0) for j in range(2)];s=F(1,8);m=sum(x*x for x in c)
    fp=((1-m*s*s)*z[f]-2*s*sum(c[j]*z[7+j] for j in range(2)))/(1+m*s*s)
    out=z[:];out[f]=fp
    for j in range(2):out[7+j]+=s*c[j]*(z[f]+fp)
    mid=[(a+b)/2 for a,b in zip(z,out)];J=[F(1,2)*c[j]*mid[f]*mid[7+j] for j in range(2)]
    assert out[f]**2-z[f]**2==-sum(J)
    assert all(out[7+j]**2-z[7+j]**2==J[j] for j in range(2))
    assert norm(z)==norm(out)
    return out
def batch(z,ss,mask):
    assert all((min(u,v),max(u,v)) not in EDGES for u,v in combinations(ss,2))
    for f in ss:z=step(z,f,mask)
    return z

orders=set();covariance_checks=0
for stock in permutations(range(7)):
    arcs=orientation(stock);assert arcs is not None and acyclic(arcs);orders.add(arcs)
    for _,qf,_,_,_ in AUTOS:
        moved=[0]*7
        for f in range(7):moved[qf[f]]=stock[f]
        assert orientation(moved)==frozenset((qf[u],qf[v]) for u,v in arcs)
        covariance_checks+=1
assert len(orders)==576
proper_four=set();proper_count=0
for stock in product(range(4),repeat=7):
    arcs=orientation(stock)
    if arcs is not None:proper_count+=1;proper_four.add(arcs)
assert proper_count==len(proper_four)==144
assert all(orientation(stock) is None for stock in product(range(3),repeat=7))
# A nonzero signed state fixed by an automorphism exchanging adjacent events.
fixed=[F(0)]*9;fixed[1]=fixed[3]=1
swap=next(a for a in AUTOS if a[0]==(0,2,1,3,4))
assert transport(fixed,swap)==fixed and norm(fixed)==2
assert swap[1][1]==3 and swap[1][3]==1 and (1,3) in EDGES
# Signed batch covariance for each of 256 masks and all 12 automorphisms.
control=list(map(F,range(1,10)));initial=orientation([x*x for x in control[:7]])
mask_checks=0
for bits in product((0,1),repeat=8):
    mask=dict(zip(CONTACTS,bits));out=batch(control,sinks(initial),mask)
    for a in AUTOS:
        _,qf,_,qc,_=a;moved=transport(control,a)
        movedmask={(qf[f],qc[j]):v for (f,j),v in mask.items()}
        arcs=orientation([x*x for x in moved[:7]])
        assert batch(moved,sinks(arcs),movedmask)==transport(out,a)
        mask_checks+=1
# Freeze the state-selected orientation once; subsequently reverse only sinks.
frozen=initial;z=control[:];counts=[0]*7;first=[0]*7;attempts=0
for _ in range(40):
    ss=sinks(frozen);assert ss and acyclic(frozen)
    for f in ss:
        z=step(z,f,dict.fromkeys(CONTACTS,1));counts[f]+=1;attempts+=1
        if not first[f]:first[f]=attempts
        assert all(0<=counts[v]-counts[u]<=1 for u,v in initial)
    frozen=reverse(frozen,ss)
assert all(x<=b for x,b in zip(first,[7,10,10,10,10,10,10]))
# Reinitializing by current stock is a different algorithm: bound counterexample.
z=list(map(F,[1,100,90,80,70,60,50,0,0]));dynamic_counts=[0]*7;history=[]
for _ in range(5):
    arcs=orientation([x*x for x in z[:7]]);assert arcs is not None
    ss=sinks(arcs);history.append(ss);z=batch(z,ss,dict.fromkeys(CONTACTS,1))
    for f in ss:dynamic_counts[f]+=1
assert history==[[1,2],[1,2],[1,2],[3,4],[3,4]]
assert sum(dynamic_counts)==10 and dynamic_counts[0]==0
# Infinite starvation witness for reinitialization: all-off map is identity.
dead=list(map(F,[1,100,90,80,70,60,50,0,0]))
dead_arcs=orientation([x*x for x in dead[:7]]);dead_sinks=sinks(dead_arcs)
assert dead_sinks==[1,2] and batch(dead,dead_sinks,{})==dead

# Intake hashes compare archived data; no execution of these scripts occurs.
manifest=json.loads((HERE/'SOURCE_THM534_GLUED_FACE_CONTACT_RESET_v1.2_MANIFEST.json').read_text())
mapping=[('verify_face_reset_v1_2.py','verify_face_reset_v1_2_FULL_EXECUTED.py'),('verify_face_reset_fraction_v1_2.py','verify_face_reset_fraction_v1_2_FULL_EXECUTED.py'),('sympy_receipt.txt','sympy_receipt_v1_2.txt'),('fraction_receipt.txt','fraction_receipt_v1_2.txt')]
intake=[]
for canonical,actual in mapping:
    b=(HERE/('SOURCE_'+actual)).read_bytes();expected=manifest['files'][canonical];digest=hashlib.sha256(b).hexdigest()
    item={'canonical_name':canonical,'captured_file':'SOURCE_'+actual,'bytes':len(b),'declared_bytes':expected['bytes'],'declared_sha256':expected['sha256'],'observed_sha256':digest,'declared_digest_length':len(expected['sha256']),'sha256_matches':digest==expected['sha256'],'git_blob_sha1':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
    assert len(b)==expected['bytes'];intake.append(item)
assert all(x['sha256_matches'] for x in intake[:3])
assert not intake[3]['sha256_matches'] and intake[3]['declared_digest_length']==63
assert intake[3]['git_blob_sha1']=='ad2a3c303b01bd9ed6eea5b98dfeffe65537d130'
RESULT={'status':'PASS_EXACT_CONDITIONAL_WITH_SOURCE_MANIFEST_ERRATUM','distinct_stock_orders':5040,'acyclic_orientations_realized':len(orders),'orientation_covariance_checks':covariance_checks,'four_stock_level_assignments':4**7,'four_level_successes':proper_count,'four_level_orientations':len(proper_four),'three_level_successes':0,'nonzero_stabilizer_obstruction':True,'signed_batch_mask_covariance_checks':mask_checks,'frozen_orientation_batches':40,'frozen_first_attempt_indices':first,'dynamic_priority_history':history,'dynamic_counts_after_10_attempts':dynamic_counts,'dynamic_all_off_infinite_starvation':True,'archival_source_hash_checks':intake,'archived_scripts_executed':False,'native_priority_direction':'OPEN','native_contact_law':'OPEN','independent_review':False,'physical_promotion':0}
if __name__=='__main__':
    (HERE/'RESULTS.json').write_text(json.dumps(RESULT,indent=2)+'\n');print(json.dumps(RESULT,indent=2))
