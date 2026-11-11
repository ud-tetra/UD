"""Fresh exact Gaussian-rational controls; no archived-script execution."""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter
import json

class C:
    def __init__(self,r=0,i=0):self.r=F(r);self.i=F(i)
    def __add__(self,b):
        b=b if isinstance(b,C) else C(b)
        return C(self.r+b.r,self.i+b.i)
    __radd__=__add__
    def __neg__(self):return C(-self.r,-self.i)
    def __sub__(self,b):return self+(-b if isinstance(b,C) else C(-b))
    def __mul__(self,b):
        b=b if isinstance(b,C) else C(b)
        return C(self.r*b.r-self.i*b.i,self.r*b.i+self.i*b.r)
    __rmul__=__mul__
    def conj(self):return C(self.r,-self.i)
    def norm(self):return self.r*self.r+self.i*self.i
    def __eq__(self,b):
        b=b if isinstance(b,C) else C(b)
        return self.r==b.r and self.i==b.i
I=C(0,1)
E=[(0,7,-1),(0,8,1),(1,7,1),(2,8,-1),(3,7,-1),(4,8,1),(5,7,1),(6,8,-1)]
s=[-1,1,1,-1,-1,1,1,1,-1]
T=[C(v) if i<7 else C(0,-v) for i,v in enumerate(s)]
for f,t,d in E:
    assert s[f]==d*s[t]
    assert T[f].conj()*C(0,-d)*T[t]==-1

def rank(a):
    a=[[F(v) for v in row] for row in a];r=0
    for c in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][c]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r];v=a[r][c];a[r]=[z/v for z in a[r]]
        for i in range(len(a)):
            if i!=r:
                v=a[i][c];a[i]=[z-v*w for z,w in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

ranks=Counter()
for mask in range(256):
    L=[[0]*9 for _ in range(9)];adj=[[] for _ in range(9)]
    for a,(f,t,d) in enumerate(E):
        if mask>>a&1:
            L[f][f]+=1;L[t][t]+=1;L[f][t]-=1;L[t][f]-=1
            adj[f].append(t);adj[t].append(f)
    seen=set();components=[]
    for v in range(9):
        if v in seen:continue
        stack=[v];component=set()
        while stack:
            w=stack.pop()
            if w in component:continue
            component.add(w);seen.add(w);stack.extend(adj[w])
        components.append(component)
    rr=rank(L);assert rr==mask.bit_count()==9-len(components)
    for component in components:
        assert all(sum(L[i][j] for j in component)==0 for i in range(9))
    ranks[rr]+=1

simplices=[(0,1,2),(0,1,3),(0,1,4),(0,2,3),(0,2,4),(1,2,3),(1,2,4),(0,1,2,3),(0,1,2,4)]
orient=[1]*8+[-1]
def carrier_action(vertex_map):
    perm=[];sign=[]
    for i,ss in enumerate(simplices):
        image=[vertex_map[v] for v in ss]
        inversions=sum(image[a]>image[b] for a in range(len(image)) for b in range(a+1,len(image)))
        j=simplices.index(tuple(sorted(image)))
        perm.append(j);sign.append(orient[i]*orient[j]*(-1)**inversions)
    ep=[next(b for b,(ff,tt,dd) in enumerate(E) if (ff,tt)==(perm[f],perm[t])) for f,t,d in E]
    for a,(f,t,d) in enumerate(E):
        ff,tt,dd=E[ep[a]]
        assert dd==d*sign[f]*sign[t]
    return perm,sign,ep
reflection=carrier_action([0,1,2,4,3])
rotation=carrier_action([1,2,0,3,4])
actions=[reflection,rotation]
def field_action(z,action):
    perm,sign,_=action;out=[0]*9
    for i,j in enumerate(perm):out[j]=sign[i]*z[i]
    return out
def gate_action(v,action):
    out=[0]*8
    for i,j in enumerate(action[2]):out[j]=v[i]
    return out
assert reflection[2]==[1,0,3,2,5,4,7,6]
assert all(field_action(T,a)==T for a in actions)
assert sum(z.norm() for z in T)==9
assert all((T[f]-C(0,d)*T[t]).norm()==0 for f,t,d in E)

invariant=[];safe=[]
for mask in range(256):
    if all(sum(1<<a[2][i] for i in range(8) if mask>>i&1)==mask for a in actions):
        invariant.append(mask);used=set();independent=True
        for i,(f,t,d) in enumerate(E):
            if mask>>i&1:
                if used&{f,t}:independent=False
                used|={f,t}
        if independent:safe.append(mask)
assert invariant==[0,3,252,255] and safe==[0]

def chi(q):
    if q<=0:return F(0)
    if q>=1:return F(1)
    return 10*q**3-15*q**4+6*q**5

def cp(q):return 30*q*q*(1-q)**2 if 0<q<1 else F(0)
def flow(z,q,p,beta):
    dz=[C() for _ in range(9)];om=[F(0)]*9;dp=[];cost=[];curr=[]
    for a,(f,t,d) in enumerate(E):
        h=chi(q[a]);U=2*beta[a]/(1+(q[a]+1)**2)
        up=-4*beta[a]*(q[a]+1)/(1+(q[a]+1)**2)**2
        dz[f]+=(-d*h)*z[t];dz[t]+=(d*h)*z[f]
        om[f]+=h+U;om[t]+=h+U
        qq=(z[f]-C(0,d)*z[t]).norm()/2;stock=z[f].norm()+z[t].norm()
        dp.append(-up*stock/2-cp(q[a])*qq);cost.append(qq)
        curr.append(2*d*h*(z[f].conj()*z[t]).r)
    dz=[v-I*(o*w) for v,o,w in zip(dz,om,z)]
    return dz,p,dp,cost,curr

complex_cases=currents=covariance=0
for n in range(64):
    z=[C((n+3*i)%7-3,(2*n+5*i)%7-3) for i in range(9)]
    q=[(F(-1),F(0),F(1,4),F(1,2),F(1),F(2))[(n+i)%6] for i in range(8)]
    p=[F((n+i)%5-2,2) for i in range(8)]
    beta=[(F(1),F(4),F(5))[(n+i)%3] for i in range(8)]
    dz,dq,dp,cost,curr=flow(z,q,p,beta)
    u=[t.conj()*v for t,v in zip(T,z)];Lu=[C() for _ in range(9)]
    for a,(f,t,d) in enumerate(E):
        h=chi(q[a]);U=2*beta[a]/(1+(q[a]+1)**2)
        Lu[f]+=h*(u[f]-u[t])+U*u[f]
        Lu[t]+=h*(u[t]-u[f])+U*u[t]
        assert cost[a]==(u[f]-u[t]).norm()/2
        assert curr[a]==2*h*(u[f].conj()*u[t]).i
        currents+=1
    assert [t.conj()*v for t,v in zip(T,dz)]==[-I*v for v in Lu]
    for action in actions:
        transformed=flow(field_action(z,action),gate_action(q,action),gate_action(p,action),gate_action(beta,action))
        assert transformed[0]==field_action(dz,action)
        assert transformed[1]==gate_action(dq,action)
        assert transformed[2]==gate_action(dp,action)
        assert transformed[3]==gate_action(cost,action)
        covariance+=1
    complex_cases+=1

degree=[sum(i in (f,t) for f,t,d in E) for i in range(9)]
leak=[(degree[f]-degree[t])**2 for f,t,d in E]
assert leak==[4,4,9,9,9,9,9,9]
_,_,wake,cost,_=flow(T,[F(0)]*8,[F(0)]*8,[F(1)]*8)
assert wake==[1]*8 and cost==[0]*8
out={'status':'PASS_EXACT_COMPLEX_GRAPH_AND_SELECTION_OBSTRUCTIONS','contact_gauge_checks':8,'all_binary_forest_rank_checks':256,'rank_histogram':dict(sorted(ranks.items())),'complex_field_equivalence_cases':complex_cases,'gauge_current_and_cost_checks':currents,'signed_symmetry_covariance_cases':covariance,'invariant_contact_batches':invariant,'independent_invariant_batches':safe,'positive_fixed_state_combined_stock':9,'onset_cost_second_derivatives_beta_abs_a_one':leak,'initial_gate_accelerations_beta_abs_a_one':[str(v) for v in wake],'arithmetic':'Gaussian rational pairs and fractions.Fraction; exact elimination','continuous_trajectory_integrated':False,'independent_review':False,'archived_scripts_executed':False,'native_identification':False,'physical_promotion':0}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
