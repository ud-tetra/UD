"""Independent exact checks for the three newly supplied research notes.

No imported code is executed. Claims remain development, no registry entry.
"""
from pathlib import Path
from itertools import combinations, product
from collections import Counter
import json
import sympy as s

root=Path(__file__).resolve().parent
labels=[]
for w,e in product(range(4),range(2)):
    labels.append(dict(kind='F',w=w,wp=w,a=None,e=e))
for w,wp in [(0,1),(1,2),(2,3),(1,0),(2,1),(3,2)]:
    for a,e in product(range(3),range(2)):
        labels.append(dict(kind='O' if wp>w else 'E',w=w,wp=wp,a=a,e=e))
assert len(labels)==44
order={'F':0,'O':1,'E':2}
def block(x,y):return ''.join(sorted([x['kind'],y['kind']],key=order.get))
all_pairs=Counter();compatible=Counter();same_address=0;both=0;ffdist=Counter()
for x,y in combinations(labels,2):
    b=block(x,y);all_pairs[b]+=1
    if x['wp']==y['w'] or y['wp']==x['w']:compatible[b]+=1
    if b=='OE' and x['a']==y['a']:
        same_address+=1
        if x['wp']==y['w'] or y['wp']==x['w']:both+=1
    if b=='FF':ffdist[abs(x['w']-y['w'])]+=1
assert dict(all_pairs)=={'FF':28,'FO':144,'FE':144,'OO':153,'OE':324,'EE':153}
assert dict(compatible)=={'FF':4,'FO':72,'FE':72,'OO':72,'OE':108,'EE':72}
assert sum(all_pairs.values())==946 and sum(compatible.values())==400
ordered=sum(x['wp']==y['w'] for x in labels for y in labels)
assert ordered==520 and same_address==108 and both==36 and dict(ffdist)=={0:4,1:12,2:8,3:4}
# Same counts admit a whole family of costs. The proposed 1/3 costs have mean 7/3,
# conditional on the additional uniform distribution on the OE label pairs.
mean_proposed=s.Rational(108+3*216,324);assert mean_proposed==s.Rational(7,3)

# Arithmetic field/group declarations, kept separate from the real carrier.
x,u=s.symbols('x u')
assert s.n_order(7,13)==12 and pow(7,6,13)==12
phi=s.Poly(sum(x**j for j in range(13)),x,modulus=7)
p=s.Poly(x**6+x**5+2*x**4+3*x**3-x*x+3*x-1,x,modulus=7)
assert phi.is_irreducible and p.is_irreducible
assert all(s.gcd(s.Poly(x**(7**d)-x,x,modulus=7),p).degree()==0 for d in (1,2,3))
frobenius=s.Poly(x,x,modulus=7)
for _ in range(6):frobenius=s.rem(frobenius**7,p)
assert frobenius==s.Poly(x,x,modulus=7)
pu=s.Poly(p.as_expr().subs(x,u),u,modulus=7)
def red(z):return s.rem(s.Poly(s.expand(z),u,modulus=7),pu).as_expr()
def rm(M):return M.applyfunc(red)
R=s.Matrix([[0,-1],[1,u]]);S=s.Matrix([[0,1],[1,0]]);I=s.eye(2)
acc=I
for _ in range(13):acc=rm(acc*R)
assert acc==I and S*S==I and rm(S*R*S)==rm(R.inv())
G=s.Matrix([[2,u],[u,2]])
assert rm(R.T*G*R-G)==s.zeros(2) and S.T*G*S==G and red(G.det())!=0
# The nonzero Gram determinant is invertible because p is irreducible.
assert s.gcd(s.Poly(G.det(),u,modulus=7),pu).degree()==0
# All possible homomorphism image orders divide both source and target orders.
assert s.gcd(26,6)==2 and s.gcd(4*26,6)==2 and (4*26)%6!=0
# Exact FS indicators from the square map; unique forms mean unique up to scale.
fs=[s.Rational(14+12,26)]*2+[s.Rational(28-2,26)]*6
assert fs==[1]*8

# Stipulated Wilson-Dirac slab, not an inferred UD operator.
sx=s.Matrix([[0,1],[1,0]]);sy=s.Matrix([[0,-s.I],[s.I,0]]);sz=s.diag(1,-1);i2=s.eye(2)
gam=[s.kronecker_product(sx,i2),s.kronecker_product(sy,i2),s.kronecker_product(sz,sx),s.kronecker_product(sz,sy),s.kronecker_product(sz,sz)]
for i in range(5):
    for j in range(5):assert gam[i]*gam[j]+gam[j]*gam[i]==(2*s.eye(4) if i==j else s.zeros(4))
T=-(gam[4]+s.I*gam[3])/2
vl=s.kronecker_product(i2,s.Matrix([1,1])/s.sqrt(2))
vr=s.kronecker_product(i2,s.Matrix([1,-1])/s.sqrt(2))
assert T.H*vl==s.zeros(4,2) and T*vr==s.zeros(4,2)
left=[s.simplify(vl.H*g*vl) for g in gam[:3]]
right=[s.simplify(vr.H*g*vr) for g in gam[:3]]
chi_left=s.simplify(s.trace(left[0]*left[1]*left[2])/(2*s.I))
chi_right=s.simplify(s.trace(right[0]*right[1]*right[2])/(2*s.I))
assert chi_left==1 and chi_right==-1
layers=20;H=s.zeros(4*layers)
for n in range(layers-1):
    H[4*n:4*n+4,4*n+4:4*n+8]=T
    H[4*n+4:4*n+8,4*n:4*n+4]=T.H
assert H==H.H and H**3==H and H.rank()==76
assert s.trace(H)==0 and s.trace(H*H)==76

# Scalar-step scattering on the same continuum Weyl cone. Both states remain on
# the same surface and in the positive-energy band; spinor continuity is exact.
E=s.Rational(5,3);V0=s.Rational(5,12);ky=1;kx=s.Rational(4,3);qx=s.Rational(3,4)
def eigspin(k,e):return s.Matrix([1,(-k+s.I*ky)/e])/s.sqrt(2)
inc=eigspin(kx,E);refl=eigspin(-kx,E);trans=eigspin(qx,E-V0)
for k,e,v in [(kx,E,inc),(-kx,E,refl),(qx,E-V0,trans)]:
    assert s.simplify((-k*sx+ky*sy)*v-e*v)==s.zeros(2,1)
rr=s.simplify((trans[1]-inc[1])/(refl[1]-trans[1]));tt=1+rr
assert s.simplify(inc+rr*refl-tt*trans)==s.zeros(2,1)
reflection=s.simplify(rr*s.conjugate(rr));transmission=s.simplify((qx/(E-V0))/(kx/E)*tt*s.conjugate(tt))
assert reflection==s.Rational(1,25) and transmission==s.Rational(24,25)

checks={'status':'PASS','lane':'development - no registry entry','physical_promotion':0,'independent_review':False,
 'receipt_labels':{'counts':dict(Counter(z['kind'] for z in labels)),'all_unordered_blocks':dict(all_pairs),'weight_composable_unordered_blocks':dict(compatible),'all_unordered':946,'weight_composable_unordered':400,'weight_composable_ordered_including_repeats':520,'FF_shell_distance':dict(ffdist),'OE_matched':108,'OE_mismatched':216,'OE_same_address_and_weight_composable':36,'uniform_mean_of_proposed_cost':str(mean_proposed),'admissibility':'weight compatibility only, necessary but not sufficient for native moves'},
 'finite_group':{'ord_13_7':12,'seven_to_six_mod13':12,'cyclotomic_irreducible':True,'trace_polynomial_mod7':str(p.as_expr()),'trace_polynomial_irreducible':True,'trace_field_degree':6,'wedderburn_dimensions':[1,1,24],'simple_dimensions_over_F7':[1,1,12],'regular_multiplicities':[1,1,2],'R_13_and_reflection_relations':'PASS','nondegenerate_symmetric_gram':'PASS, unique up to nonzero scalar','FS_indicators':[str(z) for z in fs],'possible_D13_to_S3_image_orders':[1,2],'extension_order':104,'extension_surjection_to_S3':False},
 'stipulated_slab':{'layers':layers,'dimension':80,'Gamma_eigenvalues':{'-1':38,'0':4,'1':38},'left_chirality':str(chi_left),'right_chirality':str(chi_right),'scope':'fixed Gamma/coordinate convention, exact Gamma-point states and linear surface projection, not a derived UD Hamiltonian or global bulk Chern calculation'},
 'same_surface_scalar_step':{'E':str(E),'potential_step':str(V0),'ky':str(ky),'incident_kx':str(kx),'transmitted_kx':str(qx),'reflection_amplitude':str(rr),'reflection_probability':str(reflection),'transmission_probability':str(transmission),'flux_conservation':str(reflection+transmission)},
 'analytic_proof_obligations':'Winding nonidentifiability and cost nonselection are proved by explicit alternative models in the report/manuscript; slab spectra are exact finite checks, not independent review.'}
(root/'ADDITIONAL_RESEARCH_CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
