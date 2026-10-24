"""Fresh exact native finite-event controls; no archived-code imports."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json
D=[[-1,1],[1,0],[0,-1],[-1,0],[0,1],[1,0],[0,-1]]
STAR=[[(7+j,F(d)) for j,d in enumerate(row) if d] for row in D]
W=[{f}|{t for t,d in star} for f,star in enumerate(STAR)]
G=[{g for g in range(7) if g!=f and W[f]&W[g]} for f in range(7)]
READ=[set().union(*(W[g] for g in {f}|G[f])) for f in range(7)]

def star(x,f,t):
    x=list(map(F,x));v=x[:];k=len(STAR[f]);c=t/2
    B=sum(d*x[i] for i,d in STAR[f]);den=1+k*c*c
    v[f]=((1-k*c*c)*x[f]-2*c*B)/den
    for i,d in STAR[f]:v[i]=x[i]+2*c*d*(x[f]-c*B)/den
    return v

def activity(x,f,t):
    k=len(STAR[f]);B=sum(d*x[i] for i,d in STAR[f])
    return t*t*(B*B+k*x[f]*x[f])/(1+k*t*t/4)

def coregain(x,f,t):
    k=len(STAR[f]);B=sum(d*x[i] for i,d in STAR[f]);a=x[f];c=t/2
    return 4*c*((1-k*c*c)*a*B+c*(k*a*a-B*B))/(1+k*c*c)**2

def weights(x,eps=F(1)):
    score=[activity(x,f,eps) for f in range(7)];out=[]
    for f in range(7):
        gap=max(F(0),score[f]-max([F(0)]+[score[g] for g in G[f]]))
        stock=sum(x[i]**2 for i in READ[f]);k=len(STAR[f])
        out.append(gap/(k*stock) if stock else F(0))
    assert all(0<=z<=1 for z in out)
    active=[f for f in range(7) if out[f]]
    assert all(not W[f]&W[g] for i,f in enumerate(active) for g in active[i+1:])
    return out

def owned(x):return [x[7+j]**2+sum(x[f]**2/len(STAR[f]) for f in range(7) if D[f][j]) for j in range(2)]
def event(x,eps=F(1),permission=None):
    x=list(map(F,x));w=weights(x,eps)
    if permission is not None:w=[a*b for a,b in zip(w,permission)]
    v=x[:]
    for f in range(7):
        if w[f]:
            step=star(x,f,eps*w[f])
            assert sum((step[i]-x[i])**2 for i in W[f])==activity(x,f,eps*w[f])>0
            for i in W[f]:v[i]=step[i]
    mid=[(a+b)/2 for a,b in zip(x,v)];J=[[F(0)]*2 for _ in range(7)]
    for f in range(7):
        for i,d in STAR[f]:J[f][i-7]=2*eps*w[f]*d*mid[f]*mid[i]
    assert sum(z*z for z in v)==sum(z*z for z in x)
    for f in range(7):assert v[f]**2-x[f]**2==-sum(J[f])
    for j in range(2):assert v[7+j]**2-x[7+j]**2==sum(row[j] for row in J)
    before=owned(x);after=owned(v)
    for j in range(2):
        assert after[j]-before[j]==sum(J[f][j]-(F(1,len(STAR[f])) if D[f][j] else F(0))*sum(J[f]) for f in range(7))
    return v,w,J

simp=[(0,1,2),(0,1,3),(0,1,4),(0,2,3),(0,2,4),(1,2,3),(1,2,4),(0,1,2,3),(0,1,2,4)]
orient=[1]*8+[-1];actions=[]
for pp in permutations((0,1,2)):
    for qq in ((3,4),(4,3)):
        vm=pp+qq;perm=[];sign=[]
        for i,ss in enumerate(simp):
            image=[vm[k] for k in ss];j=simp.index(tuple(sorted(image)))
            parity=(-1)**sum(image[a]>image[b] for a in range(len(image)) for b in range(a+1,len(image)))
            perm.append(j);sign.append(orient[i]*orient[j]*parity)
        actions.append((perm,sign))
def action(x,P):
    out=[F(0)]*9
    for i,j in enumerate(P[0]):out[j]=P[1][i]*x[i]
    return out

diag=events=covariance=locality=odd=0
for n in range(256):
    x=[F((1 if n>>(i%8)&1 else -1)*(((n+1)*(i+2)+i*i)%7+1),(n//(i+1))%3+1) for i in range(9)]
    for eps in (F(1,4),F(1)):
        for f in range(7):
            v=star(x,f,eps)
            assert sum((a-b)**2 for a,b in zip(v,x))==activity(x,f,eps)
            assert sum(v[i]**2-x[i]**2 for i in (7,8))==coregain(x,f,eps)
            diag+=1
        v,w,J=event(x,eps);vn,_,_=event([-a for a in x],eps)
        assert vn==[-a for a in v];events+=1;odd+=1
    for P in actions:
        vp,wp,_=event(action(x,P))
        assert vp==action(v,P) and all(wp[P[0][f]]==w[f] for f in range(7))
        covariance+=1
    for f in range(7):
        y=x[:]
        for i in set(range(9))-READ[f]:y[i]+=100+i
        assert weights(y)[f]==w[f];locality+=1

bootstrap=[]
for f in range(7):
    for sign in (-1,1):
        x=[F(0)]*9;x[f]=F(sign);v,w,J=event(x)
        assert w[f]==(F(2,3) if f==0 else F(4,5))
        assert v[f]==sign*(F(7,11) if f==0 else F(21,29))
        for i,d in STAR[f]:assert v[i]==sign*d*(F(6,11) if f==0 else F(20,29))
        gain=sum(v[i]**2 for i in (7,8))
        assert gain==(F(72,121) if f==0 else F(400,841))
        bootstrap.append({'face':f,'sign':sign,'core_gain':str(gain)})
symmetric=list(map(F,[-1,1,1,-1,-1,1,1,1,-1]));v,w,J=event(symmetric)
assert w==[F(2,15)]+[F(0)]*6
assert (v[0],v[7],v[8])==(F(-163,227),F(253,227),F(-253,227))
assert J[0]==[F(12480,51529)]*2 and owned(v)==[F(9,2)]*2
back=[F(0)]*9;back[1]=F(-1);back[7]=F(1)
vb,wb,Jb=event(back)
assert wb[1]==F(2,5) and (vb[1],vb[7])==(F(-17,13),F(7,13))
assert Jb[1][0]==F(-120,169)
# Positive reference gain becomes negative if the event is merely weakened.
x=[F(0)]*9;x[1]=F(1);x[7]=F(-1,3)
assert coregain(x,1,F(1))==F(56,225)
assert coregain(x,1,F(1,4))==F(-160,1521)

permission_cases=0
single=[F(0)]*9;single[1]=F(1)
for x in (single,symmetric,back):
    for mask in range(128):
        permission=[(mask>>f)&1 for f in range(7)]
        vp,wp,_=event(x,permission=permission)
        assert all(not wp[f] for f in range(7) if not permission[f])
        if mask==0:assert vp==x
        permission_cases+=1

tie=[F(0)]*9;tie[1]=F(1);tie[3]=F(-1)
assert event(tie)[0]==tie
perturb=0
for delta in (F(1,4),F(-1,4),F(1,16),F(-1,16),F(1,64),F(-1,64),F(1,256),F(-1,256)):
    y=tie[:];y[1]+=delta;v,_,_=event(y)
    assert sum((a-b)**2 for a,b in zip(v,tie))<=113**2*delta**2
    scaled=[delta*z for z in single]
    assert event(scaled)[0]==[delta*z for z in event(single)[0]]
    perturb+=1
assert event([F(0)]*9)[0]==[F(0)]*9
out={'status':'PASS_EXACT_CONDITIONAL_FINITE_ACTIVITY_BIDIRECTIONAL_BOOTSTRAP','native_displacement_and_gain_diagnostics':diag,'norm_midpoint_owned_event_controls':events,'odd_map_controls':odd,'all_12_signed_covariance_controls':covariance,'locality_controls':locality,'hard_permission_controls':permission_cases,'bootstrap_controls':bootstrap,'symmetric_shared_weight':'2/15','symmetric_shared_receipt_each':'12480/51529','backflow_receipt':'-120/169','trial_positive_gain':'56/225','weakened_same_event_gain':'-160/1521','tie_vacuum_scaling_controls':perturb,'read_sizes':[len(r) for r in READ],'write_sizes':[len(s) for s in W],'arithmetic':'exact fractions.Fraction','globally_one_way_core_gain':False,'new_field_registers':0,'native_objective_cost_and_priority':'OPEN','archived_scripts_executed':False,'independent_review':False,'physical_promotion':0}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
