#!/usr/bin/env python3
"""Exact control tests of UD coface receipt sufficiency and Spin(3) visibility.
No native event law or physical energy/clock asserted. Standard-library only.
"""
from itertools import product, permutations, combinations
from fractions import Fraction
from collections import Counter, defaultdict
from pathlib import Path
import json, hashlib

N=0
def ck(value, message):
    global N
    N+=1
    if not value: raise AssertionError(f'#{N}: {message}')

# Quaternion group Q8 = +/- 1,i,j,k; exact signed basis representation.
# (sign, basis): 0=1, 1=i, 2=j, 3=k
G=tuple((sign,a) for sign in (1,-1) for a in range(4))
ONE=(1,0); MINUS=(-1,0)
mt={
(0,0):(1,0),(0,1):(1,1),(0,2):(1,2),(0,3):(1,3),
(1,0):(1,1),(1,1):(-1,0),(1,2):(1,3),(1,3):(-1,2),
(2,0):(1,2),(2,1):(-1,3),(2,2):(-1,0),(2,3):(1,1),
(3,0):(1,3),(3,1):(1,2),(3,2):(-1,1),(3,3):(-1,0)}
def mul(a,b):
    s,t=mt[(a[1],b[1])]
    return (a[0]*b[0]*s,t)
def inv(a): return a if a[1]==0 else (-a[0],a[1])
def prod(*xs):
    z=ONE
    for x in xs:z=mul(z,x)
    return z
for a,b,c in product(G,repeat=3):
    ck(mul(mul(a,b),c)==mul(a,mul(b,c)),'Q8 associativity')
for a in G:
    ck(mul(a,inv(a))==ONE and mul(inv(a),a)==ONE,'Q8 inverses')

# Apex gauge acts on THREE new links by one common right factor.
TRIPLES=list(product(G,repeat=3))
def apex_orbit(spokes):
    return frozenset(tuple(mul(z,h) for z in spokes) for h in G)
sp_orbits=set(apex_orbit(t) for t in TRIPLES)
ck(len(sp_orbits)==64,'exact Q8 64 apex gauge orbits')
ck(all(len(orb)==8 for orb in sp_orbits),'free apex gauge action')

# Vector projection of Q8 is V4=Q8/{+/-1}; multiplication is XOR on 2bits.
# Use the basis index 0/1/2/3; i*j=k mod central sign.
def vproj(g):return g[1]
def vorbit(triple):
    return frozenset(tuple(x^h for x in triple) for h in range(4))
ve_orbits=set(vorbit(tuple(vproj(s) for s in triple)) for triple in TRIPLES)
ck(len(ve_orbits)==16,'Q8 SO3-vector projected gauge classes')
fibers=defaultdict(set)
for orb in sp_orbits:
    exemplar=next(iter(orb))
    fibers[vorbit(tuple(vproj(s) for s in exemplar))].add(orb)
ck(len(fibers)==16 and all(len(v)==4 for v in fibers.values()),'four Q8 Spin lifts per vector orbit')
for k,v in fibers.items():
    ck(len(v)==4,'each vector orbit has exactly four Spin classes')

# Fix inherited face (012) old links to +1 and new central links s_i +/-1.
CENTRAL=(ONE,MINUS)
def sign_plaquettes(t):
    # U01=U02=U12=+1; H_01w=U1w U0w^-1, etc
    u0,u1,u2=t
    return (prod(u1,inv(u0)),prod(u2,inv(u0)),prod(u2,inv(u1)))
spin_lifts=set(apex_orbit(t) for t in product(CENTRAL,repeat=3))
ck(len(spin_lifts)==4,'central lifts mod apex spin sign, 4 classes')
patterns=set()
for t in product(CENTRAL,repeat=3):
    p=sign_plaquettes(t)
    ck(all(x in CENTRAL for x in p),'central holonomies')
    ck(prod(*p)==ONE,'even central face parity')
    patterns.add(tuple(x[0] for x in p))
ck(patterns=={(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)},'four central face patterns')

# Full Spin gauge conjugacy at old reference vertex cannot alter central holonomy.
# For each old/new gauge (g0,g1,gw), direct link transformation.
def hol01w(U01,U0w,U1w):return prod(U01,U1w,inv(U0w))
for g0,g1,gw in product(G,repeat=3):
    old=prod(g0,inv(g1))
    nu0=prod(g0,ONE,inv(gw))
    nu1=prod(g1,MINUS,inv(gw))
    H=hol01w(old,nu0,nu1)
    ck(H==MINUS,'central -1 loop survives arbitrary vertex gauge')

# Spinorial versus vector readout: center {+/-I} acts trivially on SO3 vectors,
# but a coherent reference arm enables an invariant two-path interference contrast.
# e1 spinor and H=+/-I give detector probability ||(I+H)psi/2||^2=1/0.
for H,P in ((ONE,Fraction(1)),(MINUS,Fraction(0))):
    amplitude=(Fraction(1)+Fraction(H[0]))/2
    ck(amplitude**2==P,'relative two-path spinor signal')
    ck(vproj(H)==0,'both central elements map to SO3 identity')
    ck(H==ONE or H==MINUS,'center witness')
# The single isolated spinor ray cannot distinguish a global phase.
for H in CENTRAL:
    isolated_density=Fraction(H[0]**2)
    ck(isolated_density==1,'single-path density blind to central +/- sign')

# Proof that noncentral Q8 SO3 identity is only center; exact group quotient.
for a in G:
    ck((vproj(a)==0)==(a in CENTRAL),'kernel of vector map is center')

# Coface topology receipts: each old face generates (1,3,3,1) counts.
base_tet=(0,1,2,3)
faces=tuple(combinations(base_tet,3))
old_f=(4,6,4,1)
def simplex_faces(tet, k):return {frozenset(v) for v in combinations(tet,k+1)}
for f in faces:
    added=frozenset(f+(4,))
    old={k:simplex_faces(base_tet,k) for k in range(4)}
    new={k:old[k] | simplex_faces(tuple(sorted(added)),k) for k in range(4)}
    d=tuple(len(new[k])-len(old[k]) for k in range(4))
    ck(d==(1,3,3,1),'fresh boundary coface exact incidence increment')
    ck(sum((-1)**k*d[k] for k in range(4))==0,'Euler preserved')
    ck(tuple(len(new[k]) for k in range(4))==(5,9,7,2),'new 2 tetra fvector')
    face_owners=Counter(frozenset(fa) for t in (base_tet,tuple(sorted(added))) for fa in combinations(t,3))
    ck(face_owners[frozenset(f)]==2,'shared facet gets two owners')
    ck(sum(o==1 for o in face_owners.values())==6,'6 boundary triangles')

# Binary labels (0,0,1,1), label-preserving automorphisms S2xS2.
labels=(0,0,1,1)
G_label=[]
for perm in permutations(base_tet):
    if all(labels[perm[i]]==labels[i] for i in base_tet):G_label.append(perm)
ck(len(G_label)==4,'label preserving group order 4')
for f in faces:
    ck(any(tuple(sorted(g[i] for i in f))!=f for g in G_label),'no globally fixed face')
# Any arbitrary lexicographic face selector violates covariance on this symmetric source state.
lex_face=min(faces)
ck(any(tuple(sorted(g[i] for i in lex_face))!=lex_face for g in G_label),'vertex ID selector is not covariant')

# One resource bank, four individually admissible requests. Serial arbitration
# preserves stock but changes winner with ordering, no source event selection.
resource_winners={}
for order in permutations(faces):
    free=Fraction(1); bound=Fraction(0); chosen=[]
    for f in order:
        if free>=1:
            free-=1;bound+=1;chosen.append(f)
        ck(free+bound==1,'atomic resource conservative')
        ck(free>=0,'atomic no double-spend')
    ck(len(chosen)==1,'exactly one funded birth under provided total-order scheduler')
    resource_winners[''.join(map(str,order[0]))]=resource_winners.get(''.join(map(str,order[0])),0)+1
ck(len(resource_winners)==4 and set(resource_winners.values())=={6},'all 4 faces can win; schedule external')

# Conservation alone does not select debit or donor.
for d in [Fraction(1,10),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)]:
    ck((1-d)+d==1 and d>0,'arbitrary positive debit conserves')
for donor in range(4):
    r=[Fraction(1)]*4
    r[donor]-=Fraction(1,2)
    newborn=Fraction(1,2)
    ck(sum(r)+newborn==4,'four donor allocations same total')

out={
 'version':'v1.8','status':'EXACT_SCOPED_NO_GO_NATIVE_SOURCE_OPEN','physical_promotion':0,
 'checks':N,'Q8_spin_apex_gauge_orbits':len(sp_orbits),
 'Q8_SO3_vector_apex_gauge_orbits':len(ve_orbits),
 'Q8_spin_lifts_per_vector_orbit':sorted(set(map(len,fibers.values()))),
 'central_lifts_per_fixed_vector_spokes':len(spin_lifts),
 'central_new_face_sign_patterns':sorted(patterns),
 'single_path_spinor_density':{'plus':1,'minus':1},
 'relative_path_spinor_prob':{'plus':1,'minus':0},
 'label_preserving_symmetry_order':len(G_label),
 'symmetric_face_selection':'IMPOSSIBLE_WITHOUT_ADDITIONAL_SOURCE_DATA',
 'atomic_order_control_all_four_faces_as_winners':resource_winners,
 'coface_delta':[1,3,3,1],
 'common_birth_event_rule':'OPEN',
 'native_positive_debit':'OPEN',
 'native_spinor_detector':'OPEN',
 'independent_peer_review':'NOT_PERFORMED'
}
loc=Path(__file__).resolve().parent
(loc/'RESULTS_v1.8.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',N,'exact checks; Spin/Vector gauge classes 64/16, central 4, event winners 4')
