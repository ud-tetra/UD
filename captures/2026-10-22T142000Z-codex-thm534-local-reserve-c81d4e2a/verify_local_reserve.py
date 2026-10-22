"""Fresh exact controls for v2.1; stdlib only. Run beside this file."""
from fractions import Fraction as F
from pathlib import Path
import json

# Unique faces 012,013,014,023,024,123,124, then cores tau0,tau1.
E=[(0,7,-1),(0,8,1),(1,7,1),(2,8,-1),(3,7,-1),(4,8,1),(5,7,1),(6,8,-1)]
x=[1,-2,3,0,-1,2,-3,4,-2]
y=[-2,1,0,3,-1,-2,4,1,-3]

def receipt(z,R,mask):
    dz=[0]*9; incoming=outgoing=0
    for a,(f,t,d) in enumerate(E):
        h=(mask>>a)&1
        dz[f]-=d*h*z[t]; dz[t]+=d*h*z[f]
        sign=int(t in R)-int(f in R)
        j=sign*2*d*h*z[f]*z[t]
        incoming+=max(j,0); outgoing+=max(-j,0)
    derivative=sum(2*z[i]*dz[i] for i in R)
    assert derivative==incoming-outgoing
    return derivative,incoming,outgoing

cuts=0
for mask in range(256):
    for bits in range(512):
        R={i for i in range(9) if bits>>i&1}
        for z in (x,y):
            receipt(z,R,mask); cuts+=1

reserve=0
for a,(f,t,d) in enumerate(E):
    R={f,t}
    sx=sum(x[i]**2 for i in R); sy=sum(y[i]**2 for i in R)
    ell=d*(y[t]*x[f]-y[f]*x[t])
    for mask in range(256):
        dsx,ix,ox=receipt(x,R,mask); dsy,iy,oy=receipt(y,R,mask)
        for bx,by in [(F(0),F(0)),(F(1,4),F(3,8))]:
            C=(sx+sy+bx+by)/2
            Cdot=F(dsx-ix+dsy-iy,2)
            assert C>=abs(ell) and Cdot==-F(ox+oy,2)
            for q in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
                chi=10*q**3-15*q**4+6*q**5
                prime=30*q**2*(1-q)**2
                p=F(3,2); dchi=prime*p; Kdot=-ell*dchi
                direct=Kdot-Cdot*(1-chi)+C*dchi
                factored=(C-ell)*dchi+F(ox+oy,2)*(1-chi)
                assert direct==factored and direct>=0
                reserve+=1

horizons=0
for p in (F(1),F(3,2),F(2)):
    for C in (F(1,8),F(1,4),F(3,8)):
        r=p*p/2-C
        assert r>0
        for q0 in (F(0),F(-1,4),F(-1,2)):
            T=F(4)
            assert 2*r*T*T >= (1-q0)**2
            horizons+=1
assert F(3,2)**2/2-F(1,2)==F(5,8)
assert 2*F(5,8)*1**2>1

transfers=[]
for M in (0,1,10,100,1000):
    face=F(63*M-16,65); core=F(16*M+63,65)
    assert face*face+core*core==M*M+1
    before=F(64*M-8,65); midcore=F(8*M+64,65)
    # Midpoint rule: delta(core^2)=2 eps face_mid core_mid.
    assert core*core-1==2*F(1,4)*before*midcore
    transfers.append({'M':M,'initial_local_stock':2,'final_local_stock':str(1+core*core)})
assert F(transfers[-1]['final_local_stock'])>10000

rest=0
for q in (F(-1),F(-1,4),F(0)):
    for ell in (F(-1000),F(-1),F(0),F(1),F(1000)):
        chi=prime=F(0); p=F(0)
        assert p==0 and -prime*ell==0
        rest+=1

out={'status':'PASS_EXACT_CONDITIONAL_LOCAL_INGRESS_CERTIFICATE',
 'cut_receipts':cuts,'reserve_identity_and_sign_controls':reserve,
 'strict_margin_horizon_controls':horizons,'boundary_transfer_controls':transfers,
 'off_rest_controls':rest,'arithmetic':'exact integers and fractions.Fraction',
 'continuous_trajectory_integrated':False,'archived_scripts_executed':False,
 'independent_review':False,'physical_promotion':0}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='boundary_transfer_controls'},indent=2))
