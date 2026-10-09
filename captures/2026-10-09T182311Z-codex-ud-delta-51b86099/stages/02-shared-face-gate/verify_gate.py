"""Exact shared-interface gate audit; run alongside baseline_verify.py."""
import contextlib, io, json, runpy
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    m=runpy.run_path(str(Path(__file__).with_name('baseline_verify.py')))
Q=m['Q']; mul=m['mul']; add=m['add']; scale=m['scale']; tr=m['transpose']
zeros=m['zeros']; eye=m['eye']; rref=m['rref']; A=m['A']; ix=m['ix']; I=m['I']; n=m['n']
L=add(m['L1'],m['L2']); checks={}
def ck(name,ok):
    checks[name]=bool(ok)
    assert ok,name
q=m['Rq']; f=m['Rf']; v=m['Rv']; w=m['Rw']
p=add(v,f*2); r=add(w,scale(add([q[0]],[q[1]]),-1))
R=q+p+f+r
# z=(q1,q2,p1,p2,f,r); H(g)=H0+gD.
H0=[[0,0,1,0,0,0],[0,0,0,1,0,0],[-3,0,0,0,0,1],
    [0,-3,0,0,0,1],[0,0,0,0,0,1],[0,0,-1,-1,-3,0]]
D=[[0,0,0,0,-1,0],[0,0,0,0,-1,0],[0]*6,[0]*6,
   [1,1,0,0,0,0],[0]*6]
A0=add(A,scale(L,-1))
ck('constant_intertwiner',mul(R,A0)==mul(H0,R))
ck('gate_coefficient_intertwiner',mul(R,L)==mul(D,R))
ck('six_independent',len(rref(R)[0])==6)
ck('gate_skew',tr(L)==scale(L,-1))
ck('closed_generator_skew',tr(A0)==scale(A0,-1))
Bg=[row[:] for row in m['B']]
for t in m['cells']: Bg[ix[(0,1,2)]][ix[t]]=Q(0)
ck('dynamic_mask_not_new_chain_boundary',mul(Bg,Bg)!=zeros(n,n))
ck('same_row_space_as_previous_six',len(rref(R+m['R6'])[0])==6)
# Stronger: each of the two face-cell incidences may be gated separately.
for i in range(2):
    Di=zeros(6,6); Di[i][4]=-1; Di[4][i]=1
    ck('separate_gate_'+str(i),mul(R,m['L1' if i==0 else 'L2'])==mul(Di,R))
# Shared gate must stay represented as a mode between decisions.
ck('mode_changes_derivative',D!=zeros(6,6))
ck('switch_order_matters',mul(H0,D)!=mul(D,H0))
# A common positive quadratic invariant is obtained from the row Gram matrix.
C=mul(R,tr(R)); inv_aug,_=rref([a+b for a,b in zip(C,eye(6))]); W=[row[6:] for row in inv_aug]
ck('gram_inverse',mul(C,W)==eye(6))
ck('metric_invariant_closed',add(mul(tr(H0),W),mul(W,H0))==zeros(6,6))
ck('metric_invariant_gate',add(mul(tr(D),W),mul(W,D))==zeros(6,6))
# Raw f/q snapshot cannot determine closed-mode q derivative either.
ck('minimal_common_record',m['results']['cells_shared_face']['ranks']==[3,6])
# Candidate visible guard opens if shared-face contribution to total cell stock is positive.
def guard(z): return int(-z[4][0]*(z[0][0]+z[1][0])>0)
base=add([[t] for t in I[ix[(0,1,2,3)]]],[[t] for t in I[ix[(0,1,2)]]])
u=add([[t] for t in I[ix[(0,1)]]],scale([[t] for t in I[ix[(1,2)]]],-1))
xp=add(base,u); xm=add(base,scale(u,-1))
zp=mul(R,xp); zm=mul(R,xm)
ck('hidden_guard_same_record',zp==zm)
ck('visible_guard_equal',guard(zp)==guard(zm))
gp=int(xp[ix[(0,1)]][0]>0); gm=int(xm[ix[(0,1)]][0]>0)
ck('hidden_guard_different_mode',gp!=gm)
Fp=mul(add(A0,scale(L,gp)),xp); Fm=mul(add(A0,scale(L,gm)),xm)
ck('hidden_guard_different_retained_future',mul(R,Fp)!=mul(R,Fm))
# Feedback delta is forced if baseline and perturbed state select different modes.
zb=zp; delta=scale(zp,Q(1,2)); gd=1; gb=0
lhs=add(mul(add(H0,scale(D,gd)),add(zb,delta)),scale(mul(add(H0,scale(D,gb)),zb),-1))
rhs=add(mul(add(H0,scale(D,gd)),delta),scale(mul(D,zb),gd-gb))
ck('different_schedule_delta_identity',lhs==rhs)
ck('different_schedule_forcing_nonzero',mul(D,zb)!=zeros(6,1))
out={'scope':'candidate dynamic interface mask; no physical or registry promotion',
 'record_order':['q1','q2','p1','p2','f','r'],'R':R,'H0':H0,'D':D,'gram':C,'metric':W,
 'hidden_guard_witness':{'plus':'e0123+e012+e01-e12','minus':'e0123+e012-e01+e12',
                       'shared_record':zp,'modes':[gp,gm],
                       'derivatives':[mul(R,Fp),mul(R,Fm)]},
 'checks':checks,'passed':sum(checks.values()),'total':len(checks),
 'baseline_passed':m['out']['passed']}
Path(__file__).with_name('gate_results.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print(json.dumps({'passed':out['passed'],'total':out['total'],'baseline_passed':out['baseline_passed'],
                  'gram':C,'hidden_guard_derivatives':out['hidden_guard_witness']['derivatives']},default=str,indent=2))
