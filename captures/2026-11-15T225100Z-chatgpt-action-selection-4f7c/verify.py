#!/usr/bin/env python3
"""Finite exact variational/nonuniqueness gate. Standard-library Fraction only.
State: two face-sharing tetrahedra, six admissible bits, four seam phases,
28 allocations of two face-stock units to seven distinct faces.
No physical time/energy identification and no native Markov source selection.
"""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product
from collections import defaultdict
from pathlib import Path
import json, math

D=Path(__file__).resolve().parent
FACES=sorted(set(combinations((0,1,2,3),3))|set(combinations((0,1,2,4),3)))
assert FACES==[(0,1,2),(0,1,3),(0,1,4),(0,2,3),(0,2,4),(1,2,3),(1,2,4)]
ACCEPTED=tuple(b for b in product((0,1), repeat=5) if all(not all(b[i]==b[f[0]] for i in f) for f in FACES))
assert len(ACCEPTED)==6
BIT={b:tuple(c for c in ACCEPTED if sum(p!=q for p,q in zip(b,c))==2) for b in ACCEPTED}
assert all(len(BIT[b])==2 for b in BIT)
PAIRS=[]
for i,f in enumerate(FACES):
    for j,g in enumerate(FACES):
        if j<=i or len(set(f)&set(g))!=2: continue
        same= (3 in f and 3 in g) or (4 in f and 4 in g)
        PAIRS.append((i,j,'intra' if same else 'inter'))
assert len(PAIRS)==15
OCC=tuple(tuple(ls.count(i) for i in range(7)) for ls in combinations_with_replacement(range(7),2))
assert len(OCC)==28
STATES=tuple((b,d,x) for b in ACCEPTED for d in range(4) for x in OCC)
assert len(STATES)==672
V=(0,1,-1,1,-1,1,-1)
P=(F(1),F(1,2),F(0),F(1,2))
E=(0,1,2,1) # 1-cos(pi d/2), source-sine gradient potential SHAPE only
PHI_PI=(F(16,25),F(4,25),F(1,25),F(4,25)) # beta=ln 4, ADDED choice
assert sum(PHI_PI)==1

# two explicit phase generators: both reversible, reversal even, equal total
# undirected stationary phase conductance 4/5, but different allocations.
def phase_rates(kind,d):
    for delta in (-1,1):
        e=(d+delta)%4
        if kind=='sqrt_gibbs':rate=F(2)**(E[d]-E[e])
        elif kind=='flat_conductance':rate=F(1,5)/PHI_PI[d]
        elif kind=='phase_uniform':rate=F(1,2)
        else:raise ValueError(kind)
        yield e,rate

def stationary(kind,d):return F(1,4) if kind=='phase_uniform' else PHI_PI[d]

def pi(state,kind):
    b,d,x=state
    return F(1,6)*stationary(kind,d)*F(math.factorial(2),7**2*math.prod(math.factorial(t) for t in x))

def moves(state,kind,gate=P,kappa=F(0)):
    b,d,x=state
    out=defaultdict(F)
    for c in BIT[b]:out[(c,d,x)]+=F(1)
    for d2,rate in phase_rates(kind,d):out[(b,d2,x)]+=rate
    for i,j,cat in PAIRS:
        w=F(1) if cat=='intra' else gate[d]
        pair_total=x[i]+x[j]
        h=1+kappa*(pair_total-1)
        for a,z in ((i,j),(j,i)):
            if x[a] and w and h>0:
                y=list(x);y[a]-=1;y[z]+=1
                out[(b,d,tuple(y))]+=x[a]*w*h
    return dict(out)

def apply_generator(kind,values,kappa=F(0),gate=P):
    out={}
    for s in STATES:
        val=values[s]
        out[s]=sum((rate*(values[t]-val) for t,rate in moves(s,kind,gate=gate,kappa=kappa).items()),F(0))
    return out

result={}
Z={s:sum(c*n for c,n in zip(V,s[2])) for s in STATES}
for kind,kap in [('sqrt_gibbs',F(0)),('flat_conductance',F(0)),('phase_uniform',F(0)),('sqrt_gibbs',F(1))]:
    key=kind+('_kappa1' if kap else '_kappa0')
    weights={s:pi(s,kind) for s in STATES}
    assert sum(weights.values(),F(0))==1
    edges=0; nonneg=True; conservation=True; detailed=True
    for s in STATES:
        ms=moves(s,kind,kappa=kap)
        edges+=len(ms)
        for t,rate in ms.items():
            assert t in weights and rate>=0
            assert sum(s[2])==sum(t[2])==2
            assert weights[s]*rate==weights[t]*moves(t,kind,kappa=kap).get(s,F(0)),(key,s,t)
    moments=[];vals=Z
    var=sum((weights[s]*Z[s]**2 for s in STATES),F(0))
    assert var==F(12,7)
    for n in range(5):
        if n>0:vals=apply_generator(kind,vals,kappa=kap)
        moments.append(sum((weights[s]*Z[s]*vals[s] for s in STATES),F(0))/var)
    assert moments[0]==1 and moments[1]<0 and moments[2]>0 and moments[3]<0
    # exact chi-square entropy dissipation at nonstationary density mu=pi(1+eps Z)
    eps=F(1,4)
    assert all(1+eps*Z[s]>0 for s in STATES)
    chi2_0=eps**2*var/2
    chi2_derivative=eps**2*var*moments[1]
    assert chi2_derivative<0
    # finite micro-edge conductances >=0 and Dirichlet identity
    dirichlet=F(0)
    for s in STATES:
        for t,r in moves(s,kind,kappa=kap).items():
            dirichlet+=weights[s]*r*(Z[t]-Z[s])**2/2
    assert dirichlet==-var*moments[1]
    traffic=sum((weights[s]*sum((rate for t,rate in moves(s,kind,kappa=kap).items() if t[1]!=s[1]),F(0)) for s in STATES),F(0))/2
    result[key]={'states':len(STATES),'directed_edges':edges,'phase_pi':list(map(str,[(stationary(kind,d)) for d in range(4)])),
                 'moments':list(map(str,moments)), 'quadratic_entropy_initial':str(chi2_0), 'quadratic_entropy_derivative':str(chi2_derivative),
                 'dirichlet':str(dirichlet),'phase_undirected_traffic':str(traffic),
                 'positive_stock':'PASS','detailed_balance':'PASS','budget':'PASS'}

assert result['sqrt_gibbs_kappa0']['phase_undirected_traffic']==result['flat_conductance_kappa0']['phase_undirected_traffic']==str(F(4,5))
assert result['sqrt_gibbs_kappa0']['moments'][1:3]==result['flat_conductance_kappa0']['moments'][1:3]
assert result['sqrt_gibbs_kappa0']['moments'][4]!=result['flat_conductance_kappa0']['moments'][4] # kinetic differences at fourth derivative
assert result['phase_uniform_kappa0']['moments'][1:3]==['-3/2','27/8']
assert result['sqrt_gibbs_kappa0']['moments'][1:3]==['-12/5','162/25']
assert result['sqrt_gibbs_kappa1']['moments'][1] != result['sqrt_gibbs_kappa0']['moments'][1]

# Null: if the face-transfer weight is phase-blind, changes in the phase
# generator cannot affect the v correlation; hence the A/B mismatch above
# is genuinely mediated by the candidate interfacial phase gate.
for kind in ('sqrt_gibbs','flat_conductance'):
    vals=Z; moments_flat=[]
    for n in range(5):
        weights={s:pi(s,kind) for s in STATES}
        moments_flat.append(sum((weights[s]*Z[s]*vals[s] for s in STATES),F(0))/F(12,7))
        vals=apply_generator(kind,vals,gate=(F(1),)*4)
    assert moments_flat==[(-3)**n for n in range(5)]
result['phase_blind_gate_null']={'moments':[str((-3)**n) for n in range(5)],'two_phase_generators_identical_readout':'PASS'}

# Conditional sourced phase shape from March sinusoidal ansatz; no β/clock/gate selected.
result['_status']={'scope':'EXACT_CONDITIONAL/NO_GO_SCOPED','native_source_rule':'UNSELECTED',
                  'phase_shape':'E(theta_L,theta_R)=kappa[1-cos(theta_R-theta_L)]; pair gradient difference=-2*kappa sin(phi)',
                  'phase_thermal_beta':'log(4) assumed for exact-rational illustration only',
                  'positive_stock_event':'x->x-e_i+e_j conditional graph move',
                  'physical_promotion':0,
                  'gates':'q, donor mobility kappa, phase noise/traffic distribution, overall event clock open'}
(D/'results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:{'R1':v['moments'][1],'R2':v['moments'][2],'R3':v['moments'][3],'phase_traffic':v['phase_undirected_traffic'],'entropy_dot':v['quadratic_entropy_derivative']} for k,v in result.items() if k not in ('_status','phase_blind_gate_null')},indent=2))
print('ALL EXACT CHECKS PASS')
