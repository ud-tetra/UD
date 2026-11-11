"""Exact rational constructor controls for a conditional local soft-strength law."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import json

EPS=F(1,4)
def mobility(f,t):
    n=f*f+t*t
    return (f**4+t**4)/(n*n) if n else F(1)
def gradient(f,t):
    n=f*f+t*t
    if not n:return (F(0),F(0))
    p=f*f/n
    return ((4*p-2)*2*f*t*t/(n*n),-(4*p-2)*2*f*f*t/(n*n))
def step(f,t,d,permission=1,law=mobility):
    h=permission*law(f,t);b=EPS*h/2;c=(1-b*b)/(1+b*b);s=2*b/(1+b*b)
    fn=c*f-d*s*t;tn=d*s*f+c*t
    current=2*EPS*d*h*((f+fn)/2)*((t+tn)/2)
    assert fn*fn-f*f==-current and tn*tn-t*t==current
    assert fn*fn+tn*tn==f*f+t*t
    return fn,tn,current
grid=[(F(i,3),F(j,3)) for i,j in product(range(-4,5),repeat=2)]
primitive_checks=gradient_checks=pair_robustness=0
for f,t in grid:
    h=mobility(f,t)
    if f or t:
        assert F(1,2)<=h<=1
        gf,gt=gradient(f,t);n=f*f+t*t;a=(f*f-t*t)/n
        assert 1-n*(gf*gf+gt*gt)==(2*a*a-1)**2
        gradient_checks+=1
        b=EPS*h/2
        # Rank-one derivative perturbation away from its orthogonal rotation.
        perturbation_squared=EPS*EPS*n*(gf*gf+gt*gt)/(1+b*b)**2
        assert perturbation_squared<=EPS*EPS
    for d,permission in product((-1,1),(0,1)):
        step(f,t,d,permission);primitive_checks+=1
    assert mobility(f,t)==mobility(t,f)==mobility(-f,t)==mobility(f,-t)
    for scale in (F(-3),F(1,7),F(5)):
        assert mobility(scale*f,scale*t)==h
        a=step(f,t,1);b=step(scale*f,scale*t,1)
        assert b[:2]==(scale*a[0],scale*a[1])
for d,permission in product((-1,1),(0,1)):
    images={x:step(*x,d,permission)[:2] for x in grid}
    for x,y in product(grid,repeat=2):
        dx=sum((a-b)**2 for a,b in zip(x,y));dy=sum((a-b)**2 for a,b in zip(images[x],images[y]))
        assert (1-EPS)**2*dx<=dy<=(1+EPS)**2*dx;pair_robustness+=1
# The coefficient itself has no continuous scale-invariant vacuum extension.
for k in (1,2,4,16,1024):
    delta=F(1,k)
    assert mobility(delta,0)==1 and mobility(delta,delta)==F(1,2)
    out=step(delta,delta,1);assert out[0]**2+out[1]**2==2*delta*delta
# Seeds and replenishment are possible when the contact is independently permitted.
assert step(F(1),F(0),1)[:2]==(F(63,65),F(16,65))
assert step(F(0),F(1),1)[:2]==(F(-16,65),F(63,65))
def face_only(f,t):return f*f/(f*f+t*t) if f or t else F(0)
assert step(F(0),F(1),1,law=face_only)[:2]==(0,1)
# The source constraints do not force the squared-share law: all-open also works.
assert step(F(1),F(1),1)[:2]==(F(223,257),F(287,257))
assert step(F(1),F(1),1,law=lambda f,t:F(1))[:2]==(F(47,65),F(79,65))
assert step(F(1),F(1),1)[:2]!=step(F(1),F(1),1,law=lambda f,t:F(1))[:2]
# Quadratic class without separability: beta is not fixed by symmetry/endpoints.
for p in [F(i,16) for i in range(17)]:
    q=1-p
    for beta in (F(0),F(1),F(2)):
        h=p*p+q*q+beta*p*q
        assert F(1,2)<=h<=1

CELLS=[(0,1,2,3),(0,1,2,4)]
FACES=sorted(set(combinations(CELLS[0],3))|set(combinations(CELLS[1],3)))
D=[[0,0] for _ in FACES]
for j,c in enumerate(CELLS):
    for k in range(4):D[FACES.index(c[:k]+c[k+1:])][j]=(1,-1)[j]*(-1)**k
CONTACTS=[(f,j) for f in range(7) for j in range(2) if D[f][j]]
def local(z,contact,permission=1):
    f,j=contact;out=z[:];out[f],out[7+j],current=step(z[f],z[7+j],D[f][j],permission)
    for core in range(2):
        delta=out[7+core]**2-z[7+core]**2
        receipt=current*int(core==j)
        for face in range(7):
            weight=F(int(D[face][core]!=0),sum(int(v!=0) for v in D[face]))
            delta+=weight*(out[face]**2-z[face]**2)
            if face==f:receipt-=weight*current
        assert delta==receipt
    assert sum(x*x for x in out)==sum(x*x for x in z)
    return out
def parity(s):return (-1)**sum(s[i]>s[j] for i in range(len(s)) for j in range(i+1,len(s)))
AUTOS=[]
for p in permutations((0,1,2)):
    for tips in ((3,4),(4,3)):
        perm=p+tips;qf=[FACES.index(tuple(sorted(perm[v] for v in f))) for f in FACES]
        sf=[parity(tuple(perm[v] for v in f)) for f in FACES]
        qc=[CELLS.index(tuple(sorted(perm[v] for v in c))) for c in CELLS]
        sc=[(1,-1)[j]*parity(tuple(perm[v] for v in c))*(1,-1)[qc[j]] for j,c in enumerate(CELLS)]
        assert all(D[qf[f]][qc[j]]==sf[f]*D[f][j]*sc[j] for f in range(7) for j in range(2))
        AUTOS.append((qf,sf,qc,sc))
def transport(z,a):
    qf,sf,qc,sc=a;out=[F(0)]*9
    for f in range(7):out[qf[f]]=sf[f]*z[f]
    for j in range(2):out[7+qc[j]]=sc[j]*z[7+j]
    return out
control=[F(i-3,7) for i in range(9)];signed_checks=0
for f,t in grid:
    for contact in CONTACTS:
        z=control[:];z[contact[0]]=f;z[7+contact[1]]=t;out=local(z,contact)
        for a in AUTOS:
            qf,_,qc,_=a
            assert local(transport(z,a),(qf[contact[0]],qc[contact[1]]))==transport(out,a)
            signed_checks+=1
mask_paths=0
for mask in product((0,1),repeat=8):
    z=control[:]
    for contact,permission in zip(CONTACTS,mask):z=local(z,contact,permission)
    assert sum(x*x for x in z)==sum(x*x for x in control);mask_paths+=1
assert all(local(control,c,0)==control for c in CONTACTS)
pairs=[(a,b) for a,b in combinations(CONTACTS,2) if not {a[0],7+a[1]}&{b[0],7+b[1]}]
assert len(pairs)==15
for a,b in pairs:assert local(local(control,a),b)==local(local(control,b),a)
overlap=((1,0),(3,0))
assert local(local(control,overlap[0]),overlap[1])!=local(local(control,overlap[1]),overlap[0])
dark=[F(0)]*9;dark[1]=dark[3]=1
field=[F(0)]*9
for f,j in CONTACTS:
    h=mobility(dark[f],dark[7+j]);field[f]-=D[f][j]*h*dark[7+j];field[7+j]+=D[f][j]*h*dark[f]
assert field==[0]*9
RESULT={'status':'PASS_EXACT_CONDITIONAL_LOCAL_SOFT_STRENGTH_NOT_NATIVE_SELECTION','primitive_permission_sign_controls':primitive_checks,'nonzero_gradient_certificates':gradient_checks,'exact_pairwise_robustness_controls':pair_robustness,'signed_carrier_covariance_checks':signed_checks,'supplied_permission_mask_paths':mask_paths,'disjoint_contact_commutation_checks':len(pairs),'squared_share_range':['1/2','1'],'pair_state_update_lower_lipschitz':'3/4','pair_state_update_upper_lipschitz':'5/4','continuous_pair_field_lipschitz_bound':2,'continuous_Kminus_field_lipschitz_bound':8,'seed_and_replenishment_controls':True,'face_only_empty_face_failure':True,'raw_coefficient_discontinuous_at_vacuum':True,'source_nonuniqueness_counterexample':True,'overlapping_updates_order_dependent':True,'nonzero_open_contact_stationary_field':True,'new_constitutive_axiom':'quadratic separable normalized-stock response; not recovered in source','hard_admission':'OPEN','native_scheduler':'OPEN','action_unit':'OPEN','independent_review':False,'physical_promotion':0}
if __name__=='__main__':
    (Path(__file__).parent/'RESULTS.json').write_text(json.dumps(RESULT,indent=2)+'\n');print(json.dumps(RESULT,indent=2))
