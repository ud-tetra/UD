"""Exact constructor replay; never fit an operator or input to the requested value."""
import itertools,json,math
from fractions import Fraction as F
V=list(range(4))
M=[frozenset((frozenset((0,1)),frozenset((2,3)))),frozenset((frozenset((0,2)),frozenset((1,3)))),frozenset((frozenset((0,3)),frozenset((1,2))))]
perms=list(itertools.permutations(V));actions=[]
for p in perms:
 images=[]
 for m in M:
  mm=frozenset(frozenset(p[i] for i in edge) for edge in m);images.append(M.index(mm))
 actions.append(list(p)+[4+i for i in images])
assert len(actions)==24 and len({tuple(a) for a in actions})==24
pairs=set(itertools.product(range(7),repeat=2));orbits=[]
while pairs:
 seed=min(pairs);orbit={(a[seed[0]],a[seed[1]]) for a in actions};assert orbit<=pairs;orbits.append(orbit);pairs-=orbit
assert len(orbits)==6 and sorted(map(len,orbits))==[3,4,6,12,12,12]
transpose_classes=[]
for orbit in orbits:
 merged=orbit|{(j,i) for i,j in orbit}
 if merged not in transpose_classes:transpose_classes.append(merged)
assert len(transpose_classes)==5
characters=[sum(i==a[i] for i in range(7)) for a in actions]
assert F(sum(c*c for c in characters),24)==6
# Orbit indicators form a linearly independent complete commutant basis:
# commuting permutation matrices is precisely constancy on ordered-pair orbits.
for orbit in orbits:
 for a in actions:assert {(a[i],a[j]) for i,j in orbit}==orbit
# Equal total burdens do not equate the two preserved channel families.
assert F(1,5)+F(3,5)==F(4,5)==F(2,5)+F(2,5)
assert (F(1,5)-F(3,5))**2==F(4,25) and (F(2,5)-F(2,5))**2==0
uniform=[F(1,3)]*7;split=[F(2,3)]*4+[F(1,6)]*3
for a in actions:
 assert [uniform[a[i]] for i in range(7)]==uniform
 assert [split[a[i]] for i in range(7)]==split
assert all(0<x<=1 for x in split)
du=math.prod(uniform);ds=math.prod(split)
assert ds==2*du and du==F(1,3**7)
# Candidate formula R=S^-2 (x f^Delta)^4 with x=nu0/M.
def response(x,s,f,d=7):return (x*f**d)**4/s**2
r1=response(F(1),F(1),F(1,3));r2=response(F(2),F(1),F(1,3));assert r2==16*r1
assert response(F(1),F(2),F(1,3))==r1/4
assert response(F(1),F(1),F(2,3))==2**28*r1
assert F(23814,100)==F(11907,50)==F(3**5*7**2,2*5**2)
result={'status':'PASS','verification':'exact integer/Fraction arithmetic; constructor replay only','claim_lane':'development — no registry entry','physical_promotion':0,'independent_review':'pending','declared_model':'unsigned S4 permutation action on four VF labels plus three opposite-edge matchings; not the 15D chain register','group_elements':24,'commutant_dimension':6,'self_adjoint_commutant_dimension':5,'ordered_pair_orbit_sizes':sorted(map(len,orbits)),'uniform_determinant':str(du),'split_determinant':str(ds),'determinant_ratio':str(ds/du),'normalization_countermodel_ratio':str(r2/r1),'conditional_log_sensitivities':{'nu0':4,'M':-4,'S':-2,'f':28},'requested_decimal_arithmetic_only':{'fraction':'11907/50','prime_factorization':'3^5 * 7^2 / (2 * 5^2)','source_derivation':False},'result':'COUNT_AND_SYMMETRY_DO_NOT_SELECT_UNIFORM_SCREEN_OR_238_14','scope_limitations':['Actual WBS channel action is not supplied; this is an explicitly declared unsigned representation','Positive equivariant contractions used as logical countermodels, not selected native dynamics','Physical units, thermodynamics and cascade depth remain undeclared','No theorem that UD can never derive a value under additional source laws']}
print(json.dumps(result,indent=2))
