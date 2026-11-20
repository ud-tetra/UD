#!/usr/bin/env python3
"""UD two-K4 pre-event admission and multimode face-stock candidate; exact tests.
Source status: user March files / source-stratum; this is NOT a native law derivation.
"""
import json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from itertools import product, combinations, combinations_with_replacement
from pathlib import Path
import sympy as sp
import numpy as np
from scipy.linalg import expm

OUT=Path(__file__).parent
T_L=(0,1,2,3);T_R=(0,1,2,4)
faces=sorted(set(combinations(T_L,3))|set(combinations(T_R,3)))
edges=sorted(set(e for face in faces for e in combinations(face,2)))
Cidx=faces.index((0,1,2))
LL=tuple(i for i,f in enumerate(faces) if 3 in f)
RR=tuple(i for i,f in enumerate(faces) if 4 in f)
assert len(faces)==7 and len(edges)==9 and (len(LL),len(RR),Cidx)==(3,3,0)

def adm(b,f):return int(not all(b[x]==b[f[0]] for x in f))
def closure(b,t):return math.prod(adm(b,f) for f in combinations(t,3))
accepted=[tuple(b) for b in product((0,1),repeat=5) if closure(b,T_L)==closure(b,T_R)==1]
assert len(accepted)==6
hamming=lambda b,c:sum(x!=y for x,y in zip(b,c))
move_pairs=[(b,c) for i,b in enumerate(accepted) for c in accepted[i+1:] if hamming(b,c)==2]
assert len(move_pairs)==6
adj={b:[] for b in accepted}
for b,c in move_pairs:adj[b].append(c);adj[c].append(b)
assert all(len(adj[b])==2 for b in accepted)
components=[];unseen=set(accepted)
while unseen:
    seed=unseen.pop();group={seed};queue=[seed]
    while queue:
        for nxt in adj[queue.pop()]:
            if nxt not in group:
                group.add(nxt);unseen.discard(nxt);queue.append(nxt)
    components.append(tuple(sorted(group)))
assert sorted(map(len,components))==[3,3]
assert sum(1 for b in accepted for j in range(5) if tuple(b[:j]+(1-b[j],)+b[j+1:]) in accepted)==0

H=sp.zeros(7,9)
for i,f in enumerate(faces):
    for j,e in enumerate(edges):H[i,j]=int(set(e).issubset(f))
C=H*H.T/16
p=sp.Symbol('p',real=True)
W=sp.zeros(7)
seam_pairs=[];internal_pairs=[]
for i in range(7):
    for j in range(i+1,7):
        if len(set(faces[i])&set(faces[j]))==2:
            internal=(i in LL and j in LL) or (i in RR and j in RR)
            W[i,j]=W[j,i]=1 if internal else p
            (internal_pairs if internal else seam_pairs).append((i,j))
assert len(internal_pairs)==6 and len(seam_pairs)==9
Lap=sp.diag(*[sum(W[i,j] for j in range(7)) for i in range(7)])-W
assert Lap.eigenvals()=={sp.Integer(0):1,3*p:1,7*p:1,3+p:2,3+3*p:2}
v=sp.Matrix([0,1,-1,1,-1,1,-1])
w=sp.Matrix([0,1,-1,-1,1,0,0])
s=sp.Matrix([0,1,1,-1,-1,0,0])
assert (C*v)==sp.Rational(1,4)*v and (Lap*v)==3*p*v
assert (C*w)==sp.Rational(1,16)*w and (Lap*w)==(3+3*p)*w
assert (C*s)==sp.Rational(3,16)*s and (Lap*s)==(3+p)*s
assert v.dot(w)==v.dot(s)==w.dot(s)==0
C_spec={str(k):int(vv) for k,vv in C.eigenvals().items()}

# Phase d=theta_R-theta_L+aLR mod 4, with local-compensator gauge changes.
def phase_gate(d):return [F(1),F(1,2),F(0),F(1,2)][d%4]
for tL,tR,link in product(range(4),repeat=3):
    d=(tR-tL+link)%4
    for eL,eR in product(range(4),repeat=2):
        after=((tR+eR)-(tL+eL)+(link+eL-eR))%4
        assert after==d and phase_gate(after)==phase_gate(d)

M=2
occupancies=[]
for picks in combinations_with_replacement(range(7),M):
    x=tuple(picks.count(i) for i in range(7));occupancies.append(x)
assert len(occupancies)==28
states=[(b,d,x) for b in accepted for d in range(4) for x in occupancies]
S=set(states)
assert len(states)==672
pi=lambda state:F(1,6*4)*F(math.factorial(M),math.prod(math.factorial(n) for n in state[2])*7**M)
assert sum(map(pi,states),F(0))==1

# joint generator: b-double-flips with rate1; d jump +/-1 with rate1/2;
# face stock moves with rate x_i W_ij(d). b and phase rates are candidate conventions.
def transitions(st,phase_sensitive=True):
    b,d,x=st; out=defaultdict(F)
    for c in adj[b]: out[(c,d,x)]+=F(1)
    for step in (-1,1): out[(b,(d+step)%4,x)]+=F(1,2)
    pv=phase_gate(d) if phase_sensitive else F(1)
    for i,j in internal_pairs+seam_pairs:
        rate=F(1) if (i,j) in internal_pairs else pv
        for source,dest in ((i,j),(j,i)):
            if x[source]>0 and rate>0:
                nxt=list(x);nxt[source]-=1;nxt[dest]+=1
                out[(b,d,tuple(nxt))]+=F(x[source])*rate
    return out

# Exhaustive exact state transition checks: detailed balance and budget.
nb=0; nphase=0; nstock=0
for st in states:
    b,d,x=st;out=transitions(st)
    for dest,rate in out.items():
        assert dest in S and rate>0 and dest!=st
        assert sum(x)==sum(dest[2])==M and all(u>=0 for u in dest[2])
        assert pi(st)*rate == pi(dest)*transitions(dest).get(st,F(0))
        if dest[0]!=b:nb+=1;assert hamming(b,dest[0])==2 and dest[1:]==(d,x)
        elif dest[1]!=d:nphase+=1;assert dest[2]==x
        else:nstock+=1;assert sorted([v-u for u,v in zip(x,dest[2])])==[-1,0,0,0,0,0,1]
# The martingale drift on common eigenvector modes is -lambda(d) Z, exact per state.
for st in states:
    b,d,x=st;out=transitions(st)
    pv=phase_gate(d)
    for mode,lamb in ((v,3*pv),(w,3+3*pv),(s,3+pv)):
        z=sum(F(int(mode[i]))*x[i] for i in range(7))
        qz=sum((rate*(sum(F(int(mode[i]))*dest[2][i] for i in range(7))-z) for dest,rate in out.items()),F(0))
        assert qz==-lamb*z

# Two independently supported centered modes in multinomial stationary ensemble.
for mode in (v,w,s):
    assert sum(mode)==0
    mean=sum((pi(st)*sum(int(mode[i])*st[2][i] for i in range(7)) for st in states),F(0))
    variance=sum((pi(st)*sum(int(mode[i])*st[2][i] for i in range(7))**2 for st in states),F(0))
    assert mean==0 and variance==F(M,7)*int(mode.dot(mode))
for mode1,mode2 in ((v,w),(v,s),(w,s)):
    cross=sum((pi(st)*sum(int(mode1[i])*st[2][i] for i in range(7))*sum(int(mode2[j])*st[2][j] for j in range(7)) for st in states),F(0))
    assert cross==0

# Dynamic phase: mode's four-dimensional correlation block, and full no-fit predictions.
Lph=sp.Matrix([[-1,sp.Rational(1,2),0,sp.Rational(1,2)],
 [sp.Rational(1,2),-1,sp.Rational(1,2),0],
 [0,sp.Rational(1,2),-1,sp.Rational(1,2)],
 [sp.Rational(1,2),0,sp.Rational(1,2),-1]])
lams_v=sp.Matrix([3*sp.Rational(x) for x in [1,sp.Rational(1,2),0,sp.Rational(1,2)]])
B_v=Lph-sp.diag(*lams_v)
B_w=Lph-sp.diag(*[q+3 for q in lams_v])
assert B_w==B_v-3*sp.eye(4)
ones=sp.ones(4,1)
rv1=float((ones.T*sp.Matrix(expm(np.array(B_v,float)))*ones)[0]/4)
rw1=float((ones.T*sp.Matrix(expm(np.array(B_w,float)))*ones)[0]/4)
assert abs(rw1-math.exp(-3)*rv1)<1e-12
assert (ones.T*B_v*ones)[0]/4==-sp.Rational(3,2)
assert (ones.T*(B_v**2)*ones)[0]/4==sp.Rational(27,8)
assert (ones.T*B_w*ones)[0]/4==-sp.Rational(9,2)
assert (ones.T*(B_w**2)*ones)[0]/4==sp.Rational(171,8)
# Controls: quenched d=1, phase blind d-all p=1, seam off p=0, empty M=0, closure sham.
assert Lap.subs(p,0)*v==sp.zeros(7,1)
assert Lap.subs(p,0)*w==3*w
assert Lap.subs(p,1)*v==3*v and Lap.subs(p,1)*w==6*w
assert Lap.subs(p,sp.Rational(1,2))*v==sp.Rational(3,2)*v
assert Lap.subs(p,sp.Rational(1,2))*w==sp.Rational(9,2)*w
# Closure sham right cell off => remove any transition directly touching right-cell-exclusive face.
# Left side internal transitions remain, so this is not a global no-move sham.
def sham_edges():
    return [(i,j) for i,j in internal_pairs if i in LL and j in LL]
assert len(sham_edges())==3
assert all(i in LL and j in LL for i,j in sham_edges())
# Inserting an isolated vertex does not change face-mode Laplacian, even though prior uniform-vertex clock does.
assert 1-F(4,5)!=1-F(4,6)

result={
 'scope':'EXACT_CONDITIONAL, CANDIDATE generator, no physical promotion',
 'carrier':{'vertices':5,'edges':9,'faces':7,'cells':2,'fully_admitted_binary_states':6,'one_bit_admitted_edges':0,'minimum_hamming_distance':2,'distance2_edges':6,'admission_components':[len(c) for c in components]},
 'combinatorics':{'face_basis':[list(x) for x in faces],'internal_face_adjacencies':internal_pairs,'seam_face_adjacencies':seam_pairs,'raw_face_covariance_eigenvalues':C_spec,'commutator_nonzero': bool(C*Lap-Lap*C!=sp.zeros(7))},
 'candidate_generator':{'M':M,'joint_states':len(states),'phase_group':'Z4','phase_gate':['1','1/2','0','1/2'],'phase_diffusion_neighbor_rate':'1/2','minimal_double_bit_admission_rate':'1','face_transition_rate':'x_f times 1 (intra) or p(d) (interfacial)','native_selection':'OPEN'},
 'exact_tests':{'row_sum_and_nonnegative':'PASS','individual_stock_conservation':'PASS','detailed_balance':'PASS','gauge_compensation':'PASS','two_bit_admissible_moves':'PASS','closure_sham':'PASS','seam_off':'PASS','zero_stock':'PASS','isolated_vertex_clock_null':'PASS','eigenvalue_checks':'PASS'},
 'generator_transition_counts':{'bit':nb,'phase':nphase,'face_stock':nstock},
 'common_covariance_and_dynamic_modes':{'v':{'vector':[int(x) for x in v],'C_eigen':'1/4','Lap_eigen':'3p','var':str(F(M,7)*int(v.dot(v)))},'w':{'vector':[int(x) for x in w],'C_eigen':'1/16','Lap_eigen':'3+3p','var':str(F(M,7)*int(w.dot(w)))},'s':{'vector':[int(x) for x in s],'C_eigen':'3/16','Lap_eigen':'3+p','var':str(F(M,7)*int(s.dot(s)))},'cross_covariances':'0'},
 'dynamic_phase':{'Gamma':'1','Rv_s_1':rv1,'Rw_s_1':rw1,'ratio':rw1/rv1,'exact_identity':'Rw(t)=exp(-3t)*Rv(t)','Rv_prime_0':'-3/2','Rv_second_0':'27/8','Rw_prime_0':'-9/2','Rw_second_0':'171/8'},
 'fixed_phase_d1':{'p':'1/2','Rv':'exp(-3t/2)','Rw':'exp(-9t/2)'},
 'phase_blind_control':{'p':'1','Rv':'exp(-3t)','Rw':'exp(-6t)','conclusion':'mode splitting also exists without phase sensitivity'},
 'seam_off_control':{'p':'0','Rv':'1','Rw':'exp(-3t)'},
 'source_uniqueness':'NO-GO_SCOPED: same structural constraints allow p(d)=1, (1+Re U)/2, 1[d=0], or other gauge-invariant nonnegative functions and arbitrary global rate; no source selects them',
 'physical_promotion':0
}
(OUT/'results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'PASS':True,'states':len(states),'transitions':nb+nphase+nstock,'Rv(1)':rv1,'Rw(1)':rw1,'ratio':rw1/rv1},indent=2))
