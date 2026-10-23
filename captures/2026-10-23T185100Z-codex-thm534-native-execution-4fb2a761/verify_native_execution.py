"""Fresh exact transaction/cost/bootstrap controls; stdlib only."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

def topology(D):
    n=len(D);m=len(D[0])
    stars=[[(n+j,F(d)) for j,d in enumerate(row) if d] for row in D]
    W=[{f}|{t for t,d in star} for f,star in enumerate(stars)]
    G=[{g for g in range(n) if g!=f and W[f]&W[g]} for f in range(n)]
    R=[set().union(*(W[g] for g in {f}|G[f])) for f in range(n)]
    H=[{g for g in range(n) if g!=f and (W[f]&R[g] or W[g]&R[f])} for f in range(n)]
    square=[(G[f]|set().union(*(G[g] for g in G[f])))-{f} for f in range(n)]
    assert H==square
    assert max(map(len,R))<=15 and max(map(len,W))<=3
    return {'D':D,'n':n,'m':m,'stars':stars,'W':W,'G':G,'R':R,'H':H}

def score(T,x,f):return max(F(0),2*x[f]*sum(d*x[t] for t,d in T['stars'][f]))
def weight(T,x,f):
    s=score(T,x,f);r=max(F(0),s-max([F(0)]+[score(T,x,g) for g in T['G'][f]]))
    E=sum(x[i]**2 for i in T['R'][f]);k=len(T['stars'][f])
    return r/(k*E) if E else F(0)

def native_star(T,x,f,w,eps=F(1)):
    x=list(map(F,x));v=x[:];k=len(T['stars'][f]);c=eps*w/2
    B=sum(d*x[t] for t,d in T['stars'][f]);den=1+k*c*c
    v[f]=((1-k*c*c)*x[f]-2*c*B)/den
    for t,d in T['stars'][f]:v[t]=x[t]+2*c*d*(x[f]-c*B)/den
    mid=[(a+b)/2 for a,b in zip(x,v)]
    J={t:2*eps*w*d*mid[f]*mid[t] for t,d in T['stars'][f]}
    assert v[f]**2-x[f]**2==-sum(J.values())
    for t,d in T['stars'][f]:assert v[t]**2-x[t]**2==J[t]
    assert sum(z*z for z in v)==sum(z*z for z in x)
    for j in range(T['m']):
        before=x[T['n']+j]**2+sum(x[g]**2/len(T['stars'][g]) for g in range(T['n']) if T['D'][g][j])
        after=v[T['n']+j]**2+sum(v[g]**2/len(T['stars'][g]) for g in range(T['n']) if T['D'][g][j])
        expected=(J.get(T['n']+j,F(0)) if T['D'][f][j] else F(0))-(sum(J.values())/k if T['D'][f][j] else F(0))
        assert after-before==expected
    return v,J

def local_event(T,x,f):
    w=weight(T,x,f);v,J=native_star(T,x,f,w)
    if w:assert sum(J.values())>0
    return v

D=[[-1,1],[1,0],[0,-1],[-1,0],[0,1],[1,0],[0,-1]]
T=topology(D)
assert sum(map(len,T['G']))//2==12
assert sum(map(len,T['H']))//2==21
assert all(len(v)==6 for v in T['H'])
# Classify declared safe batches rather than just comparing writes.
safe=[]
for mask in range(128):
    selected=[f for f in range(7) if mask>>f&1]
    if all(g not in T['H'][f] for f,g in combinations(selected,2)):safe.append(mask)
assert len(safe)==8 and max(z.bit_count() for z in safe)==1

# Actual tetrahedral strip provides separated safe events.
cells=[(0,1,2,3),(1,2,3,4),(2,3,4,5),(3,4,5,6)]
faces=sorted(set(f for c in cells for f in combinations(c,3)))
Ds=[[0]*4 for _ in faces]
for j,c in enumerate(cells):
    for a in range(4):Ds[faces.index(c[:a]+c[a+1:])][j]=(-1)**a
S=topology(Ds)
a=next(f for f,row in enumerate(Ds) if row[0] and sum(bool(v) for v in row)==1)
b=next(f for f,row in enumerate(Ds) if row[3] and sum(bool(v) for v in row)==1)
assert b not in S['H'][a]
safe_commutations=0
for n in range(64):
    x=[F((1 if n>>(i%6)&1 else -1)*(i%3+1)) for i in range(S['n']+S['m'])]
    lhs=local_event(S,local_event(S,x,a),b)
    rhs=local_event(S,local_event(S,x,b),a)
    assert lhs==rhs;safe_commutations+=1
# Nontrivial positive events on both separated stars.
x=[F(0)]*(S['n']+S['m'])
for j in range(4):x[S['n']+j]=F(1)
x[a]=F(2)*Ds[a][0];x[b]=F(2)*Ds[b][3]
assert weight(S,x,a)>0 and weight(S,x,b)>0
assert local_event(S,local_event(S,x,a),b)==local_event(S,local_event(S,x,b),a)
safe_commutations+=1

# Kminus disjoint-write/read-race countercontrol.
x=[F(0)]*9;x[0]=F(-1,2);x[1]=x[2]=F(2);x[7]=F(1);x[8]=F(-1)
w1=weight(T,x,1);w2=weight(T,x,2)
assert w1==w2==F(8,25) and not T['W'][1]&T['W'][2]
first,_=native_star(T,x,1,w1);ab,_=native_star(T,first,2,w2)
first,_=native_star(T,x,2,w2);ba,_=native_star(T,first,1,w1)
assert ab==ba
ab=local_event(T,local_event(T,x,1),2);ba=local_event(T,local_event(T,x,2),1)
assert ab!=ba
race_distance=sum((u-v)**2 for u,v in zip(ab,ba));assert race_distance>0

# Empty-core bootstrap: policy stalls, permitted native event fills.
bootstrap=[]
for f in range(7):
    x=[F(0)]*9;x[f]=F(1)
    assert all(weight(T,x,g)==0 for g in range(7))
    assert all(local_event(T,x,g)==x for g in range(7))
    v,J=native_star(T,x,f,F(1))
    gain=sum(v[i]**2-x[i]**2 for i in (7,8))
    assert gain==(F(8,9) if f==0 else F(16,25))
    bootstrap.append({'face':f,'current_policy':'identity','permitted_native_event_core_gain':str(gain)})

# Declared resource cost changes the same native-current ranking.
symmetric=list(map(F,[-1,1,1,-1,-1,1,1,1,-1]))
j=[2*symmetric[f]*sum(d*symmetric[t] for t,d in T['stars'][f]) for f in range(7)]
assert j==[4,2,2,2,2,2,2]
face_density=j;channel_density=[v/len(T['stars'][f]) for f,v in enumerate(j)]
assert [f for f,v in enumerate(face_density) if v==max(face_density)]==[0]
assert channel_density==[2]*7
allocation=0
for n in range(128):
    gains=[F((n*(f+2)+f*f)%9-4) for f in range(7)]
    for costs in ([F(1)]*7,[F(len(v)) for v in T['stars']]):
        M=max([F(0)]+[a/b for a,b in zip(gains,costs)])
        raw=[F(((n>>f)&1)+1,8) for f in range(7)]
        budget=sum(c*a for c,a in zip(costs,raw));a=[v/max(F(1),budget) for v in raw]
        assert sum(c*v for c,v in zip(costs,a))<=1
        assert sum(g*v for g,v in zip(gains,a))<=M
        if M>0:
            f=next(f for f in range(7) if gains[f]/costs[f]==M)
            assert gains[f]/costs[f]==M
        allocation+=1

# Native skew flow falls outside the monotone-bootstrap theorem, as required.
for k in range(1,17):
    face=F(1);core=F(-1,2**k);core_velocity=face
    assert 2*core*core_velocity<0

# A current-read serial sequence retains each receipt and telescopes core stock.
x=[F(0)]*9;x[0]=F(-1,2);x[1]=x[2]=F(2);x[7]=F(1);x[8]=F(-1)
initial=sum(z*z for z in x);C0=x[7]**2+x[8]**2;gains=[];executed=0
for f in (1,2,0):
    old=x[7]**2+x[8]**2;w=weight(T,x,f)
    x,J=native_star(T,x,f,w)
    gain=x[7]**2+x[8]**2-old
    assert gain>=0 and (not w or gain>0)
    gains.append(gain);executed+=int(bool(w))
assert sum(z*z for z in x)==initial
assert sum(gains)==x[7]**2+x[8]**2-C0<=initial-C0
out={'status':'PASS_EXACT_NATIVE_EXECUTION_COST_AND_BOOTSTRAP_FRONTIER','Kminus_write_conflict_edges':12,'Kminus_read_write_conflict_edges':21,'Kminus_safe_declared_batch_max':1,'all_Kminus_batch_cases':128,'tetrahedral_strip':{'cells':4,'faces':len(faces),'max_read_size':max(map(len,S['R'])),'separated_recomputed_commutations':safe_commutations},'recomputed_read_race_squared_distance':str(race_distance),'bootstrap_controls':bootstrap,'resource_allocation_controls':allocation,'monotone_assumption_scope_controls':16,'serial_events_attempted':3,'serial_positive_events':executed,'serial_receipts_telescope':True,'arithmetic':'exact fractions.Fraction','native_event_cost_derived':False,'native_transaction_registers_derived':False,'new_permission_or_reset_source':False,'archived_scripts_executed':False,'independent_review':False,'physical_promotion':0}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
