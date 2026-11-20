#!/usr/bin/env python3
"""Auditable v0.3 tests: admissible source nonuniqueness and boundary/stock controls.
Exact arithmetic uses fractions.Fraction; phase Laplacian spectrum uses sympy.
This is a conditional Markov class, NOT a native UD source derivation.
"""
import json, math
from itertools import product, combinations, combinations_with_replacement
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import sympy as sp

OUT=Path(__file__).resolve().parent
TL=(0,1,2,3); TR=(0,1,2,4)
full_faces=sorted(set(combinations(TL,3))|set(combinations(TR,3)))
assert full_faces==[(0,1,2),(0,1,3),(0,1,4),(0,2,3),(0,2,4),(1,2,3),(1,2,4)]
accepted=tuple(b for b in product((0,1),repeat=5) if all(not all(b[i]==b[f[0]] for i in f) for f in full_faces))
assert len(accepted)==6
Hamming=lambda a,b:sum(x!=y for x,y in zip(a,b))
adj_b={b:tuple(c for c in accepted if Hamming(b,c)==2) for b in accepted}
assert all(len(x)==2 for x in adj_b.values())

def build_graph(kind):
    faces=full_faces if kind!='omit_shared' else [f for f in full_faces if f!=(0,1,2)]
    within=[]; inter=[]
    for i,f in enumerate(faces):
      for j,g in enumerate(faces[i+1:],i+1):
        if len(set(f)&set(g))!=2:continue
        same=(3 in f and 3 in g) or (4 in f and 4 in g)
        if kind=='reflect_shared' and (f==(0,1,2) or g==(0,1,2)):
            continue
        (within if same else inter).append((i,j))
    return faces,within,inter

def states_and_pi(faces,M):
    occup=[]
    for chosen in combinations_with_replacement(range(len(faces)),M):
        occup.append(tuple(chosen.count(i) for i in range(len(faces))))
    states=[(b,d,x) for b in accepted for d in range(4) for x in occup]
    def pi(s):return F(math.factorial(M),24*(len(faces)**M)*math.prod(math.factorial(t) for t in s[2]))
    assert sum(map(pi,states),F(0))==1
    return states,pi

# Exact admissible endpoint-normalized, gauge-invariant, reversal-even Z4 phase gate family
PHASE_GATES={'harmonic':(F(1),F(1,2),F(0),F(1,2)),
             'squared_harmonic':(F(1),F(1,4),F(0),F(1,4)),
             'strict_match':(F(1),F(0),F(0),F(0))}

def transitions(st,faces,within,inter,pvals,interaction=F(0),phase_jump_rate=F(1,2),bit_rate=F(1)):
    b,d,x=st;out=defaultdict(F)
    for c in adj_b[b]:out[(c,d,x)]+=bit_rate
    for delta in (-1,1):out[(b,(d+delta)%4,x)]+=phase_jump_rate
    for i,j in within+inter:
        wij=F(1) if (i,j) in within else pvals[d]
        # factor 1+kappa(m_ij-1) uses only the pair stock and is reversal invariant.
        c=F(1)+interaction*(x[i]+x[j]-1)
        if c<0:raise ValueError('negative candidate')
        for a,z in ((i,j),(j,i)):
            rate=x[a]*wij*c
            if rate>0:
                y=list(x);y[a]-=1;y[z]+=1
                out[(b,d,tuple(y))]+=rate
    return dict(out)

def brute_generator_case(label,kind,gate,interaction=F(0),M=2,compute_moments=True):
    faces,within,inter=build_graph(kind)
    states,pi=states_and_pi(faces,M)
    stset=set(states)
    coords={f:i for i,f in enumerate(faces)}
    # v mode restricted to exclusive faces; 3 left faces +1 and right faces -1
    v=[0 if f==(0,1,2) else (1 if 3 in f else -1) for f in faces]
    assert sum(v)==0
    Zn={st:sum(c*n for c,n in zip(v,st[2])) for st in states}
    Qz={}; trans={}; total_edges=0; stock_edges=0; bit_edges=0; phase_edges=0
    for st in states:
        edges=transitions(st,faces,within,inter,gate,interaction=interaction)
        trans[st]=edges
        assert all(dst in stset and rate>=0 and dst!=st for dst,rate in edges.items())
        assert all(sum(dst[2])==M and min(dst[2])>=0 for dst in edges)
        total_edges+=len(edges)
        for dst,rate in edges.items():
            assert pi(st)*rate==pi(dst)*transitions(dst,faces,within,inter,gate,interaction=interaction).get(st,F(0)), ('failed DB',st,dst)
            if st[0]!=dst[0]:bit_edges+=1
            elif st[1]!=dst[1]:phase_edges+=1
            else:stock_edges+=1
        Qz[st]=sum((rate*(Zn[dst]-Zn[st]) for dst,rate in edges.items()),F(0))
    mean=sum((pi(st)*Zn[st] for st in states),F(0))
    var=sum((pi(st)*(Zn[st]-mean)**2 for st in states),F(0))
    assert mean==0 and var==F(M,len(faces))*sum(t*t for t in v)
    corr_prime=sum((pi(st)*Zn[st]*Qz[st] for st in states),F(0))/var
    corr_second=None
    if compute_moments:
      corr_second=sum((pi(st)*Zn[st]*sum((rate*(Qz[dst]-Qz[st]) for dst,rate in trans[st].items()),F(0)) for st in states),F(0))/var
    return dict(label=label,geometry=kind,faces=len(faces),within_edges=len(within),interface_edges=len(inter),joint_states=len(states),directed_transitions=total_edges,stock_edges=stock_edges,bit_edges=bit_edges,phase_edges=phase_edges,rate_phase=list(map(str,gate)),donor_interaction=str(interaction),total_stock=M,variance=str(var),R_prime_0=str(corr_prime),R_second_0=str(corr_second),positivity='PASS',budget_conservation='PASS',detailed_balance='PASS')

# Gauge compensation: exhausting 4^5 and every admissible phase law.
for tl,tr,link,epsl,epsr in product(range(4),repeat=5):
    d=(tr-tl+link)%4
    d2=((tr+epsr)-(tl+epsl)+(link+epsl-epsr))%4
    assert d==d2
    assert all(p[d]==p[d2] for p in PHASE_GATES.values())

# Symbolic structure and boundary alternate spectrum
p=sp.Symbol('p',real=True)
spectra={};fixed_eigs={}
for kind in ('full','reflect_shared','omit_shared'):
    faces,within,inter=build_graph(kind)
    W=sp.zeros(len(faces))
    for i,j in within:W[i,j]=W[j,i]=1
    for i,j in inter:W[i,j]=W[j,i]=p
    L=sp.diag(*[sum(W[i,j] for j in range(len(faces))) for i in range(len(faces))])-W
    spectra[kind]=dict((str(k),int(v)) for k,v in L.eigenvals().items())
    assert all(sum(L[i,j] for j in range(len(faces)))==0 for i in range(len(faces)))
    if kind=='full':assert spectra[kind]=={'0':1,'3*p':1,'7*p':1,'p + 3':2,'3*p + 3':2}
    if kind=='omit_shared':assert spectra[kind]=={'0':1,'2*p':1,'3':2,'2*p + 3':2}
    if kind=='reflect_shared':assert spectra[kind]=={'0':2,'2*p':1,'3':2,'2*p + 3':2}

# Phase-family classification under endpoint and reversal constraints.
# Every even p:Z4->[0,1], p(0)=1, p(2)=0 has form (1,q,0,q).
for q in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
    seq=(F(1),q,F(0),q)
    assert seq[0]==1 and seq[2]==0 and seq[1]==seq[3] and all(0<=u<=1 for u in seq)
assert PHASE_GATES['harmonic'] != PHASE_GATES['squared_harmonic']

cases=[]
for law,gate in PHASE_GATES.items():
    cases.append(brute_generator_case(law,'full',gate,interaction=F(0),M=2,compute_moments=True))
cases.append(brute_generator_case('harmonic-interacting-stock','full',PHASE_GATES['harmonic'],interaction=F(1),M=2,compute_moments=True))
for kind in ('reflect_shared','omit_shared'):
    cases.append(brute_generator_case('harmonic-'+kind,kind,PHASE_GATES['harmonic'],interaction=F(0),M=2,compute_moments=True))
assert len(cases)==6
slope=dict((d['label'],F(d['R_prime_0'])) for d in cases)
assert slope['harmonic']==-F(3,2),slope
assert slope['squared_harmonic']==-F(9,8),slope
assert slope['strict_match']==-F(3,4),slope
assert slope['harmonic-interacting-stock']==-F(27,14),slope
assert slope['harmonic-reflect_shared']==-F(1),slope
assert slope['harmonic-omit_shared']==-F(1),slope

# For same M=2 multinomial stationary measure, pair-invariant donor multiplier rescales initial
# Dirichlet slope by exactly 1 + 2 κ(M−1)/F, but not necessarily whole-time correlation.
assert slope['harmonic-interacting-stock']/slope['harmonic']==F(9,7)
second=dict((d['label'],F(d['R_second_0'])) for d in cases)
# Exclude pure time-reparametrization: second derivatives not quadratic in slope ratio
assert second['harmonic-interacting-stock'] != second['harmonic']*F(9,7)**2

result={
 'version':'v0.3','timestamp':'2026-11-15','status':'EXACT_CONDITIONAL / NO-GO_SCOPED / OPEN','physical_promotion':0,
 'source_derived':'March trion gate, defined relative seam phase, positive stock necessary pre-event conditions; no constitutive rate selected',
 'phase_nonuniqueness_theorem':{'premises':'gauge invariant, phase reversal even, 0<=p<=1, p(0)=1, p(2)=0 on Z4','all_solutions':'(1,q,0,q), 0<=q<=1','selection':'undetermined continuum of q','conditional_first_harmonic':'if affine in cos(phi), q=1/2 uniquely (added constitutive axiom)'},
 'reversible_donor_family':{'rate':'x_i*w_ij(d)*[1+kappa*(x_i+x_j-1)]','kappa':'arbitrary nonnegative; kappa=0 and kappa=1 tested','equilibrium':'same multinomial stock law for both kappa values','initial_slope_ratio_formula':'1+2*kappa*(M-1)/F','M2_F7_kappa1':'9/7'},
 'geometry_spectra':spectra,'cases':cases,
 'admitted_bits':len(accepted),'admitted_one_bit_edges':0,'admitted_minimal_undirected_edges':sum(len(v) for v in adj_b.values())//2,
 'comparison':{'q_half_minus_q_quarter_initial_slope':str(slope['harmonic']-slope['squared_harmonic']),
               'second_derivative_harmonic':str(second['harmonic']),
               'second_derivative_stock_kappa1':str(second['harmonic-interacting-stock']),
               'stock_kappa1_not_global_clock_relabeling':True},
 'bridge':'No physical k, temporal calibration, source constitutive law, or data; preserved G05/G06 and other NO-GOs'}
(OUT/'results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'PASS':True,'cases':[{'label':x['label'],'states':x['joint_states'],'Rprime':x['R_prime_0'],'Rsecond':x['R_second_0']} for x in cases],
                  'source_nonunique':True,'second_not_clock_rescale':True},indent=2))
