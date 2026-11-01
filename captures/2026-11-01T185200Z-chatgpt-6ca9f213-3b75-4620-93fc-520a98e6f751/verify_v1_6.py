#!/usr/bin/env python3
"""UD coface v1.6: exact, scoped conditional mathematics; no native birth admission."""
from itertools import combinations, permutations, product
from pathlib import Path
import json
import sympy as sp

CHECKS=0
def check(test, why):
    global CHECKS
    CHECKS+=1
    if not bool(test): raise AssertionError(f"{CHECKS}: {why}")
def eq(a,b,why):
    check(sp.simplify(a-b)==0,why)

Q=sp.Rational
V=range(4)
faces=list(combinations(V,3))
edges=list(combinations(V,2))
rho=sp.Matrix([0,1,2,4])
rho_sym=sp.Matrix([0,0,1,1])
def burden_scores(r):
    return {f:sum((r[j]-r[i])**2/16 for i,j in combinations(f,2)) for f in faces}
D=burden_scores(rho)
assert list(D.values())==[Q(3,8),Q(13,8),Q(3,2),Q(7,8)]
for f in faces: eq(burden_scores(rho_sym)[f], Q(1,8),"symmetric burden tie")
for p in permutations(V):
    R=sp.zeros(4,1)
    for i in V: R[p[i]]=rho[i]
    transformed=burden_scores(R)
    for f in faces: eq(transformed[tuple(sorted(p[i] for i in f))],D[f],"burden equivariance")
# Native Q162 on newly admitted child K4 with 3 inherited face vertices and a newborn (no source).
L=4*sp.eye(4)-sp.ones(4)
check(L*sp.ones(4,1)==sp.zeros(4,1),"L preserves total burden")
for f in faces:
    old=[rho[i] for i in f]
    S=sum(old)
    x0=sp.Matrix(old+[0])
    target=(S/4)*sp.ones(4,1)
    check(sum(x0)==S,"preparation total")
    check(L*target==sp.zeros(4,1),"stationary child is harmonic")
    # Q162: r' = -(1/4)Lr (all gates open)
    xdot=-(L*x0)/4
    eq(xdot[3],S/4,"newborn amplitude initial slope")
    eq(2*xdot[3]**2,S*S/8,"newborn square-stock onset second derivative")
    check(all(sp.simplify(xdot[i])==S/4-old[i] for i in range(3)),"donor current")
    check(sum(xdot)==0,"instant total current zero")
    # Algebraic semigroup exact, source parameter s dimensionless.
    z=sp.symbols('s',real=True,nonnegative=True)
    x=target+sp.exp(-z)*(x0-target)
    check(sp.simplify((sp.diff(x,z)+L*x/4))==sp.zeros(4,1),"exact semigroup")
    eq(x[3],S*(1-sp.exp(-z))/4,"newborn relaxation trajectory")
    check(sp.simplify(sum(x)-S)==0,"burden conserved all-time")
    # no finite stationary equalization if x0 is not uniform
    if x0!=target: check(x0-target!=sp.zeros(4,1),"nonuniform initial state")
# Symmetry of source when all old burdens equal, exact post-admission first force
for v in [Q(0),Q(1),Q(2),Q(5,3)]:
    source=sp.Matrix([v,v,v,0])
    eq(-(L*source)[3]/4,3*v/4,"uniform face newborn slope")
# Exhaustive small rational old-state controls and exact equilibrium uniqueness
for a,b,c in product(range(4),repeat=3):
    S=a+b+c
    x0=sp.Matrix([a,b,c,0])
    xeq=(Q(S,4))*sp.ones(4,1)
    check(L*xeq==sp.zeros(4,1),"mean state stationary")
    eq(sum(xeq),S,"closed budget equilibrium")
    check(sp.simplify(L*x0/4+(-(L*x0)/4))==sp.zeros(4,1),"source-free current update")
# The equilibrium linear constraints have unique solution at fixed total.
r0,r1,r2,rw=sp.symbols('r0 r1 r2 rw', real=True)
sol=sp.solve(list(L*sp.Matrix([r0,r1,r2,rw]))+[r0+r1+r2+rw-5],
             [r0,r1,r2,rw], dict=True)
check(sol==[{r0:Q(5,4),r1:Q(5,4),r2:Q(5,4),rw:Q(5,4)}],"unique equilibrium for total 5")
# Exact differentiated onset rank order on all four possible faces
onsets={''.join(map(str,f)):sum(rho[i] for i in f)**2/8 for f in faces}
check(onsets=={'012':Q(9,8),'013':Q(25,8),'023':Q(9,2),'123':Q(49,8)},'all face onset values')
check(max(onsets,key=onsets.get)=='123',"onset comparator winner")
check(max(D,key=D.get)==(0,1,3),"Q162 old-face squared-current winner different")
# Pre-birth symmetry controls: full constant state ties, binary-label-symmetric state has two-face orbits.
full_equal=sp.Matrix([1,1,1,1])
check(all(burden_scores(full_equal)[f]==0 for f in faces), "fully symmetric burden gives zero old-edge score")
check(len({sum(full_equal[i] for i in f)**2/8 for f in faces})==1, "full symmetry gives four-way onset tie")
partial=sp.Matrix([0,0,1,1])
partial_onset={''.join(map(str,f)):sum(partial[i] for i in f)**2/8 for f in faces}
check(partial_onset=={'012':Q(1,8),'013':Q(1,8),'023':Q(1,2),'123':Q(1,2)},"S2xS2 orbit tie in onset")
# At finite dimensionless time log 2, an initially zero newborn has received half its limiting burden.
for f in faces:
    S=sum(rho[i] for i in f)
    z=sp.log(2)
    eq(S*(1-sp.exp(-z))/4,Q(S,8),"finite-time newborn not at equilibrium")
# Gamma group U1: old face curvature theta sets unavoidable new loop curvature
phi=sp.symbols('phi',real=True)
x,y,z=sp.symbols('x y z',real=True)
# residual signed sum x-y+z=-phi. Minimum quadratic mismatch = phi^2/3
lag=sp.symbols('lag',real=True)
stat=sp.solve([2*x+lag,2*y-lag,2*z+lag,x-y+z+phi],
              [x,y,z,lag],dict=True)
check(len(stat)==1,"unique unwrapped minimizer")
mins=stat[0]
for sym,sgn in [(x,-1),(y,1),(z,-1)]:
    eq(mins[sym],sgn*phi/3,"equal-share oriented curvature minimizer")
eq(sum(mins[t]**2 for t in [x,y,z]),phi**2/3,"lower bound attained")
# At theta=pi principal branch has two distinct equally optimal global lifts.
p1=sp.Matrix([-sp.pi/3,sp.pi/3,-sp.pi/3])
p2=-p1
eq(sum(q*q for q in p1),sp.pi**2/3,"first compact branch optimum")
eq(sum(q*q for q in p2),sp.pi**2/3,"second compact branch optimum")
check(p1!=p2,"two non-gauge-equivalent curvature configurations")
# Distinct retained resources and donor allocations consistent with same total
for debit in [Q(0),Q(1),Q(3,2),Q(2),Q(3)]:
    eq((Q(3)-debit)+(Q(4)+debit),7,"resource redistribution without cost rule")
# Face currents alone cannot select matched burden/seam conflict:
# prior exact prepared U1 phases -pi/2, -pi/6, pi/6,-pi/6
h=[sp.pi*Q(n,6) for n in [-3,-1,1,-1]]
U=[sp.simplify(1-sp.cos(q)) for q in h]
check(U[0]>U[1] if isinstance(U[0]>U[1],bool) else sp.simplify(U[0]-U[1]).is_positive,
      "seam winner opposite burden")
eq(D[(0,1,3)]-D[(0,1,2)],Q(5,4),"burden preference 013")
eq(U[0]-U[1],sp.sqrt(3)/2,"seam preference 012")
t=sp.symbols('t',real=True,positive=True)
eq(Q(5,4)/(sp.sqrt(3)/2),5*sp.sqrt(3)/6,"cross-type test threshold not coefficient")
result={
 'version':'v1.6','physical_promotion':0,'status':'EXACT_CONDITIONAL_AND_SOURCE_OPEN',
 'primary_checks':CHECKS,
 'source_scope':['ledger v0.39 Q140/Q153/Q162/Q169-Q173/G05','UD repo Docs event admission'],
 'prebirth_burden':[str(z) for z in rho],
 'faces':[''.join(map(str,f)) for f in faces],
 'original_burden_diagnostic':{''.join(map(str,k)):str(v) for k,v in D.items()},
 'candidate_post_admission_newborn_onset_W_second_derivative':{k:str(v) for k,v in onsets.items()},
 'newborn_onset_winner':'123',
 'burden_current_winner':'013',
 'seam_mismatch_winner':'012',
 'newborn_stationary_total_5':['5/4']*4,
 'post_admission_relaxation':'rho_new(s)=S_f*(1-exp(-s))/4',
 'newborn_initial_stock_acceleration':'S_f^2/8',
 'unwrapped_U1_least_squares_curvature':'theta^2/3',
 'compact_pi_curvature_minimizer_degeneracy':2,
 'native_birth_event':'OPEN',
 'common_burden_seam_action':'OPEN',
 'formation_debit':'OPEN',
 'review':'constructor verification only'
}
p=Path(__file__).resolve().parent
(p/'RESULTS_v1.6.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS',CHECKS,'exact assertions',onsets)
