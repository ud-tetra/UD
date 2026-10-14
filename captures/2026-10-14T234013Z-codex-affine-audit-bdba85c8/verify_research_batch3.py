#!/usr/bin/env python3
"""Independent exact replay. Imported source code is never executed."""
import collections, hashlib, itertools as it, json, pathlib, sys
import sympy as s
ROOT=pathlib.Path(__file__).resolve().parent
checks={}
def check(name, condition, **data):
    assert condition, (name,data)
    checks[name]={'passed':True,**data}
bits=list(it.product(range(2),repeat=3)); perms=list(it.permutations(range(3)))
identity=tuple(range(8))
def action(v,g):
    return tuple(bits.index(tuple(bits[i][g[j]]^v[j] for j in range(3))) for i in range(8))
def compose(a,b): return tuple(a[b[i]] for i in range(len(a)))
primitive={action(v,g) for v in bits if sum(v)<=1 for g in perms}
closure={identity}; todo=[identity]
while todo:
    a=todo.pop()
    for b in primitive:
        c=compose(a,b)
        if c not in closure: closure.add(c); todo.append(c)
check('primitive_action_closure',len(primitive)==24 and len(closure)==48,primitive=24,closure=48)
def parity(p): return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2
diagonals=sorted({min(x,tuple(1-a for a in x)) for x in bits})
def label(v,g):
    # Centered Boolean points: translations are sign changes.
    sigma=tuple(diagonals.index(min(y,tuple(1-a for a in y))) for x in diagonals
                for y in [tuple(x[g[j]]^v[j] for j in range(3))])
    return ((sum(v)+parity(g))%2,sigma)
labels={action(v,g):label(v,g) for v in bits for g in perms}
check('C2_times_S4_bijection',len(set(labels.values()))==48)
check('C2_times_S4_homomorphism',all(labels[compose(a,b)]==
      (labels[a][0]^labels[b][0],compose(labels[a][1],labels[b][1])) for a in closure for b in closure))
def alpha(a,b): return (-1)**(parity(labels[a][1])*labels[b][0])
check('projective_cocycle',all(alpha(a,b)*alpha(compose(a,b),c)==alpha(b,c)*alpha(a,compose(b,c))
      for a in closure for b in closure for c in closure),triples=48**3)
A=next(a for a,l in labels.items() if l==(1,tuple(range(4))))
B=next(a for a,l in labels.items() if l[0]==0 and parity(l[1])==1)
X=s.Matrix([[0,1],[1,0]]); Z=s.diag(1,-1)
check('nontrivial_projective_commutator',compose(A,B)==compose(B,A) and X*Z==-Z*X
      and alpha(A,B)==-alpha(B,A),commuting_group_elements=True,anticommuting_lifts=True)
# G = (F2^2 x C13) semidirect C2, reflection swaps coordinates and inverts C13.
V=list(it.product(range(2),repeat=2)); G=list(it.product(V,range(13),range(2)))
def mul(a,b):
    v,k,e=a; u,l,f=b; u=u[::-1] if e else u
    return (tuple(x^y for x,y in zip(v,u)),(k+(-1)**e*l)%13,e^f)
one=((0,0),0,0)
inv={a:next(b for b in G if mul(a,b)==one) for a in G}
remaining=set(G); classes=[]
while remaining:
    a=next(iter(remaining)); c={mul(mul(b,a),inv[b]) for b in G};classes.append(c);remaining-=c
check('semidirect_104_classes',len(classes)==29,order=len(G),class_sizes=dict(collections.Counter(map(len,classes))))
# Dual of abelian normal subgroup. Nonfixed reflection orbits induce dimension-two irreps.
dual=list(it.product(range(13),V))
def reflect(x): return ((-x[0])%13,x[1][::-1])
induced={frozenset((x,reflect(x))) for x in dual if reflect(x)!=x}
check('complex_irrep_dimensions',len(induced)==25 and 4+25*4==104,linear=4,dimension_two=25)
def frob(orb): return frozenset(((7*k)%13,v) for k,v in orb)
remaining=set(induced); froborbits=[]
while remaining:
    x=next(iter(remaining)); o={x}; y=frob(x)
    while y!=x: o.add(y); y=frob(y)
    froborbits.append(o);remaining-=o
degrees=sorted(map(len,froborbits))
check('F7_Wedderburn_correction',degrees==[1,6,6,12] and 4+sum(4*d for d in degrees)==104,
      matrix_two_extension_degrees=degrees,correct_dimension=104,imported_dimension=56)
check('affine_group_algebra_dimension',4+2*4+4*9==48 and 48*(1+12)==624,
      affine=48,with_optional_C13=624)
# Conditional scattering checks, exact over rational functions.
z=s.symbols('z',real=True); u,t=s.symbols('u t',real=True)
S=s.zeros(8); entries=[(0,1,u),(0,4,s.I*t),(1,2,u),(1,5,s.I*t),
    (2,3,u),(2,6,s.I*t),(3,0,u),(3,7,s.I*t),(4,0,s.I*t),(4,7,u),
    (5,1,s.I*t),(5,4,u),(6,2,s.I*t),(6,5,u),(7,3,s.I*t),(7,6,u)]
for i,j,x in entries: S[i,j]=x
check('eight_terminal_unitarity',s.simplify(S*S.conjugate().T-(u*u+t*t)*s.eye(8))==s.zeros(8))
T=s.zeros(8)
for i,j,x in entries: T[i,j]=1-z if x==u else z
L=s.eye(8)-T; current=s.Matrix([1,0,-1,0,0,0,0,0])
unknown=s.symbols('v0:8'); potential=s.Matrix(unknown)
solution=s.solve(list(L*potential-current)+[unknown[2]],unknown)
Vsol=s.Matrix([s.factor(solution[x]) for x in unknown])
expected=s.Matrix([1/(1-z),z/(2*(1-z)),0,(2-z)/(2*(1-z)),
                   (1+z)/(2*(1-z)),1/(2*(1-z)),s.Rational(1,2),1/(2*(1-z))])
check('eight_terminal_dc_solution',all(s.cancel(x)==0 for x in Vsol-expected),
      potentials_in_I_h_over_e2=[str(x) for x in Vsol],domain='0<z<1')
check('conditional_Hall_and_conductance',s.cancel(Vsol[1]-Vsol[3])==-1 and s.cancel(1/Vsol[0])==1-z,
      Rxy_in_h_over_e2=-1,G_in_e2_over_h='1-z',R14='z/(2*(1-z))')
check('endpoint_qualifications',L.subs(z,0).rank()==6 and
      L.subs(z,1).rank()<L.subs(z,1).row_join(current).rank(),
      z0_rank=int(L.subs(z,0).rank()),z1_incompatible_nonzero_injected_current=True)
# A declared two-terminal binomial benchmark, not the full floating-probe noise.
I0,I,e=s.symbols('I0 I e',positive=True)
Sincident=2*e*I0*z*(1-z); Smeasured=s.cancel(Sincident.subs(I0,I/(1-z)))
check('shot_noise_normalization',Smeasured==2*e*I*z and s.diff(Sincident,z).subs(z,s.Rational(1,2))==0,
      fixed_incident_current=str(Sincident),fixed_measured_current=str(Smeasured),
      full_eight_terminal_voltage_probe_noise='OPEN')
# Receipt counting remains distinct from native eligibility or winding.
F=[(w,p) for w in range(4) for p in range(2)]
O=[(w,a,p) for w in range(3) for a in range(3) for p in range(2)]
E=[(w,a,p) for w in range(1,4) for a in range(3) for p in range(2)]
for name,Q,step in [('O',O,1),('E',E,-1)]:
    cells=collections.Counter((a[1]==b[1],a[2]==b[2]) for a,b in it.combinations(Q,2))
    check(name+'_pair_partition',cells=={(True,True):18,(True,False):27,(False,True):54,(False,False):54},
          same_address_same_parity=18,same_address_cross_parity=27,
          cross_address_same_parity=54,cross_address_cross_parity=54)
    check('F'+name+'_count_and_weight_compatibility',len(F)*len(Q)==144 and
          sum(f[0]==q[0] for f in F for q in Q)==36 and
          sum(f[0] in (q[0],q[0]+step) for f in F for q in Q)==72,
          cartesian=144,ordered_F_then_Q_weight_compatible=36,either_order_weight_compatible=72)
n,k=s.symbols('n k')
check('quadratic_burden_is_not_event_label',s.simplify(k*((n+1)**2-n**2)-k*(2*n+1))==0
      and s.simplify(k*((n-1)**2-n**2)-k*(1-2*n))==0,
      activation='k*(2*n+1)',deactivation='k*(1-2*n)',work_identification='NOT_DERIVED')
result={'scope':'Independent finite-model checks; no physical or independent-review promotion',
        'passed':True,'checks':checks,'count':len(checks),
        'environment':{'python':sys.version,'sympy':s.__version__}}
(ROOT/'RESEARCH_BATCH3_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':True,'check_families':len(checks),'output':'RESEARCH_BATCH3_CHECKS.json'}))
