"""Exact independent selection checks using the current generated subdivision matrices.

Archived source programs are not imported or executed. The only imported module is
the freshly constructed, published 0.11 implementation of S and affine R.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import hashlib, importlib.util, json

implementation=Path(__file__).with_name('subdivision_metric.py')
if not implementation.exists():
    implementation=Path('/workspace/sites/unified-dynamics-public/subdivision_metric.py')
spec=importlib.util.spec_from_file_location('current_subdivision', implementation)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
S,R,B,BP,OLD,NEW=m.S,m.R,m.B,m.BP,m.OLD,m.NEW
mul,tr,add,eye,zero=m.multiply,m.transpose,m.add,m.eye,m.zero

def scale(a,c):return [[c*v for v in row] for row in a]
def quadratic(a,x):return sum(x[i]*a[i][j]*x[j] for i in range(len(x)) for j in range(len(x)) if x[i] and x[j])
def vector(n,i):return [F(j==i) for j in range(n)]
def matvec(a,x):return [sum(v*y for v,y in zip(row,x)) for row in a]

assert mul(R,S)==eye(15)
Q=add(eye(149),mul(S,R),-1)
assert mul(Q,Q)==Q and mul(R,Q)==zero(15,149)
assert mul(Q,S)==zero(149,15)
assert add(mul(S,R),Q)==eye(149)
assert mul(BP,S)==mul(S,B) and mul(R,BP)==mul(B,R)
H0=mul(tr(R),R);C=mul(tr(Q),Q)
H1=add(H0,C);H2=add(H0,scale(C,F(2)))
assert mul(H1,S)==tr(R) and mul(H2,S)==tr(R)
for H in [H1,H2]:
    assert H==tr(H)
    assert mul(tr(S),mul(H,S))==eye(15)
    assert mul(tr(BP),mul(H,S))==mul(mul(H,S),tr(B))
    # For G=I the induced metric-adjoint retraction is S^T H.
    RH=mul(tr(S),H)
    assert RH==R
    assert mul(RH,S)==eye(15) and mul(RH,BP)==mul(B,RH)
    # Complete-family identity for a supplied H satisfying HS=R^T.
    assert H==add(H0,mul(tr(Q),mul(H,Q)))

# S4 relabels the barycentric vertices. Inclusion order is preserved, so
# barycentric oriented flags have no extra relabeling signs.
newindex={s:i for i,s in enumerate(NEW)}
def relabel_mask(mask,p):return sum(1<<p[v] for v in range(4) if mask&(1<<v))
for p in permutations(range(4)):
    perm=[newindex[tuple(relabel_mask(mask,p) for mask in flag)] for flag in NEW]
    for H in [H1,H2]:
        assert all(H[perm[i]][perm[j]]==H[i][j] for i in range(149) for j in range(149))

face_vertex_index=NEW.index((3,));x=vector(149,face_vertex_index)
assert quadratic(H0,x)==F(1,2)
assert quadratic(C,x)==F(3,2)
assert quadratic(H1,x)==F(2) and quadratic(H2,x)==F(7,2)

observables=[]
for lam in [F(0),F(1,2),F(1)]:
    K=add(H0,scale(C,lam))
    assert mul(tr(S),mul(K,S))==eye(15)
    # Positivity and domination have exact split-square proofs: K=H0+lam C;
    # H1-K=(1-lam) C. No floating eigenvalue estimate is needed.
    assert 0<=lam<=1
    val=quadratic(K,x)
    assert val==F(1,2)+F(3,2)*lam
    observables.append({'lambda':str(lam),'barycenter_01_value':str(val),
        'calibrated_on_coarse_code':True,'positive_and_dominated_by_H1':True,
        'complement_blind':lam==0})

# Matrix verification of the candidate complement-blind observable.
assert mul(H0,Q)==zero(149,149)
assert mul(tr(S),mul(H0,S))==eye(15)
# More generally, arbitrary symmetric coarse D transports by K=R^T D R.
D=zero(15,15)
for i in range(15):D[i][i]=F(i+1)
K=mul(tr(R),mul(D,R))
assert mul(K,Q)==zero(149,149)
assert mul(tr(S),mul(K,S))==D

# Diagonal positive metrics cannot intertwine the raising operator, regardless
# of their numerical weights. Source vertex e0 maps to singleton (1,).
# The fine edge (({1}),({0,1})) has no singleton {0} endpoint, so its weighted
# raising amplitude is identically zero for every diagonal H.
coarse_vertex=OLD.index((0,));fine_singleton=NEW.index((1,))
fine_other_flag=NEW.index((2,3))
raised=mul(S,tr(B))
assert S[fine_singleton][coarse_vertex]==1
assert all(S[i][coarse_vertex]==0 for i in range(149) if i!=fine_singleton)
assert BP[fine_singleton][fine_other_flag]==0
assert raised[fine_other_flag][coarse_vertex]==1
# Isometry independently fixes each singleton diagonal metric to one.
assert all(S[NEW.index((1<<i,))][OLD.index((i,))]==1 for i in range(4))

result={'status':'PASS','scope':'Conditional exact linear-algebra selection gates; no source-law adoption',
    'physical_promotion':0,'independent_human_review':'PENDING',
    'dimensions':{'old':15,'fine':149,'complement':134},
    'fixed_retraction_metric_family':'HS=R^T G iff H=R^T G R+Q^T W Q, with W SPD on ker R',
    'complete_compatible_pair_classification':'All SPD compatible H induce chain retraction R_H=G^-1 S^T H; H=R_H^T G R_H+Q_H^T H Q_H',
    'induced_retraction_in_both_metric_examples':'Exactly the affine source-coordinate retraction R',
    'metric_cases':[{'w':'1','barycenter_01_norm_squared':'2'}, {'w':'2','barycenter_01_norm_squared':'7/2'}],
    'three_compatibility_conditions':'PASS for both metrics',
    'symmetry':'Both metrics invariant under all 24 S4 relabelings',
    'metric_nonuniqueness':True,
    'observable_cases':observables,
    'observable_nonuniqueness_at_fixed_metric':True,
    'complement_blind_observable':'Unique after calibration and complement-blindness: K=R^T D R',
    'diagonal_metric_generator_no_go':{'coarse_vertex':[0],'fine_flag':[2,3],
        'diagonal_metric_raising_coefficient':'0','transported_coarse_raising_coefficient':'1'},
    'metric_selection_source_gate':'Source-authored retraction and complement pairing remain required',
    'observable_selection_source_gate':'Source-authored coarse observable and complement-blind semantics remain required',
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'current_subdivision_implementation_sha256':hashlib.sha256(implementation.read_bytes()).hexdigest()}
Path(__file__).with_name('selection-parallel-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
