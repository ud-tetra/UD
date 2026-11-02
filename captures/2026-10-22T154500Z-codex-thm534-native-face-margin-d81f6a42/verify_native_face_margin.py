"""Fresh exact native-carrier controls; original real faces/cores only."""
from fractions import Fraction as F
from pathlib import Path
from itertools import permutations
import json
D=[[-1,1],[1,0],[0,-1],[-1,0],[0,1],[1,0],[0,-1]]
STARS=[[(7+j,F(d)) for j,d in enumerate(row) if d] for row in D]
SUP=[{f}|{t for t,d in star} for f,star in enumerate(STARS)]
CONFLICT=[{g for g in range(7) if g!=f and SUP[f]&SUP[g]} for f in range(7)]
READ=[set().union(*(SUP[g] for g in {f}|CONFLICT[f])) for f in range(7)]
assert [len(r) for r in READ]==[9,6,6,6,6,6,6]

def weights(x,mean=False):
    score=[max(F(0),2*x[f]*sum(d*x[t] for t,d in STARS[f])) for f in range(7)]
    if mean:score=[v/len(STARS[f]) for f,v in enumerate(score)]
    stock=[sum(x[i]**2 for i in READ[f]) for f in range(7)]
    w=[]
    for f in range(7):
        gap=max(F(0),score[f]-max([F(0)]+[score[g] for g in CONFLICT[f]]))
        w.append(gap/(len(STARS[f])*stock[f]) if stock[f] else F(0))
        assert w[f]>=0 and w[f]**2*len(STARS[f])<=1
    active=[f for f in range(7) if w[f]]
    assert all(not SUP[f]&SUP[g] for i,f in enumerate(active) for g in active[i+1:])
    return w,score,stock

def star_event(x,f,w,eps=F(1)):
    v=x[:];c=eps*w/2;k=len(STARS[f]);B=sum(d*x[t] for t,d in STARS[f]);den=1+k*c*c
    v[f]=((1-k*c*c)*x[f]-2*c*B)/den
    for t,d in STARS[f]:v[t]=x[t]+2*c*d*(x[f]-c*B)/den
    return v

def owned(x):return [x[7+j]**2+sum((F(1,2) if f==0 else F(1))*x[f]**2 for f in range(7) if D[f][j]) for j in range(2)]
def event(x,eps=F(1),mean=False,permission=None):
    w,score,stock=weights(x,mean)
    if permission is not None:w=[a*b for a,b in zip(w,permission)]
    v=x[:]
    for f in range(7):
        if w[f]:
            vv=star_event(x,f,w[f],eps)
            for i in SUP[f]:v[i]=vv[i]
    mid=[(F(a)+F(b))/2 for a,b in zip(x,v)];J=[[F(0)]*2 for _ in range(7)]
    for f in range(7):
        for t,d in STARS[f]:J[f][t-7]=2*eps*w[f]*d*mid[f]*mid[t]
    assert sum(z*z for z in v)==sum(z*z for z in x)
    for f in range(7):assert v[f]**2-x[f]**2==-sum(J[f])
    for j in range(2):assert v[7+j]**2-x[7+j]**2==sum(row[j] for row in J)
    before=owned(x);after=owned(v)
    for j in range(2):
        assert after[j]-before[j]==sum(J[f][j]-(F(1,2) if f==0 else F(1) if D[f][j] else F(0))*sum(J[f]) for f in range(7))
    for f in range(7):
        if w[f]:assert sum(J[f])>0
    assert sum(before)==sum(after)
    return v,w,J

simp=[(0,1,2),(0,1,3),(0,1,4),(0,2,3),(0,2,4),(1,2,3),(1,2,4),(0,1,2,3),(0,1,2,4)]
orient=[1]*8+[-1]
actions=[]
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

cases=covariance=locality=0;patterns=set()
for n in range(256):
    x=[F((1 if n>>(i%8)&1 else -1)*(((n+1)*(i+2)+i*i)%7+1),(n//(i+1))%3+1) for i in range(9)]
    for eps in (F(1,4),F(1)):
        v,w,J=event(x,eps);patterns.add(tuple(f for f in range(7) if w[f]));cases+=1
    # Local vector field has zero original norm derivative.
    velocity=[F(0)]*9
    for f in range(7):
        for t,d in STARS[f]:
            velocity[f]-=w[f]*d*x[t];velocity[t]+=w[f]*d*x[f]
    assert sum(a*b for a,b in zip(x,velocity))==0
    for P in actions:
        xp=action(x,P);vp,wp,_=event(xp)
        assert vp==action(v,P)
        assert all(wp[P[0][f]]==w[f] for f in range(7))
        covariance+=1
    for f in range(7):
        outside=set(range(9))-READ[f]
        y=x[:]
        for i in outside:y[i]+=100+i
        wy=weights(y)[0]
        assert wy[f]==w[f]
        a=star_event(x,f,w[f]);b=star_event(y,f,wy[f])
        assert all(a[i]-x[i]==b[i]-y[i] for i in SUP[f])
        locality+=1

x=list(map(F,[-1,1,1,-1,-1,1,1,1,-1]));v,w,J=event(x)
assert w==[F(1,9)]+[F(0)]*6
assert (v[0],v[7],v[8])==(F(-125,163),F(179,163),F(-179,163))
assert J[0]==[F(5472,26569)]*2 and owned(v)==owned(x)==[F(9,2)]*2
assert event(x,mean=True)[0]==x

# Aggregate gain does not imply gain of each incident core.
y=[F(0)]*9;y[0]=1;y[7]=-2;y[8]=-1
vy,_,Jy=event(y)
assert Jy[0][1]==F(-1485,5329) and sum(Jy[0])>0
# Equal-stock tie controls approach identity from both winner sides.
tie=[F(0)]*9;tie[1]=1;tie[3]=-1;tie[7]=1
assert event(tie)[0]==tie
perturbations=0
for delta in (F(1,4),F(-1,4),F(1,16),F(-1,16),F(1,64),F(-1,64),F(1,256),F(-1,256)):
    y=tie[:];y[1]+=delta;vy,_,_=event(y)
    assert sum((a-b)**2 for a,b in zip(vy,tie))<=92**2*delta**2
    scaled=[delta*z for z in x]
    assert event(scaled)[0]==[delta*z for z in v]
    perturbations+=1
assert event([F(0)]*9)[0]==[F(0)]*9
# Snapshot vs recomputed local event order, despite disjoint writes.
y=[F(0)]*9;y[0]=F(-1,2);y[1]=y[2]=2;y[7]=1;y[8]=-1
wy=weights(y)[0];assert wy[1]==wy[2]==F(8,25)
frozen_ab=star_event(star_event(y,1,wy[1]),2,wy[2])
frozen_ba=star_event(star_event(y,2,wy[2]),1,wy[1]);assert frozen_ab==frozen_ba
first=star_event(y,1,wy[1]);recompute_ab=star_event(first,2,weights(first)[0][2])
first=star_event(y,2,wy[2]);recompute_ba=star_event(first,1,weights(first)[0][1])
assert recompute_ab!=recompute_ba
permission_cases=0
for prep in (x,tie,y):
    for mask in range(128):
        permission=[(mask>>f)&1 for f in range(7)]
        vv,ww,_=event(prep,permission=permission)
        assert all(not ww[f] for f in range(7) if not permission[f])
        if mask==0:assert vv==prep
        permission_cases+=1
out={'status':'PASS_EXACT_CONDITIONAL_NATIVE_CARRIER_FACE_MARGIN','event_norm_midpoint_ownership_controls':cases,'all_12_signed_covariance_controls':covariance,'local_read_set_controls':locality,'hard_face_permission_controls':permission_cases,'active_patterns_observed':[list(z) for z in sorted(patterns)],'read_set_sizes':[len(z) for z in READ],'write_set_sizes':[len(z) for z in SUP],'symmetric_shared_weight':'1/9','symmetric_shared_current_each':'5472/26569','symmetric_owned_stocks':['9/2','9/2'],'mean_score_control':'identity at same symmetric state','negative_individual_current_control':'-1485/5329 while aggregate is positive','tie_vacuum_scaling_controls':perturbations,'frozen_disjoint_events_commute':True,'recomputed_events_need_not_commute':True,'arithmetic':'exact fractions.Fraction','new_carrier_registers':0,'physical_energy_or_canonical_claim':False,'native_constitutive_uniqueness':False,'archived_scripts_executed':False,'independent_review':False,'physical_promotion':0}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
