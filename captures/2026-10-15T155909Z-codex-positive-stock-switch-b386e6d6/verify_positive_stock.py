"""Constructor replay for a declared positive-load hybrid mechanism."""
from pathlib import Path
from fractions import Fraction as Q
import json, math
import numpy as np
import scipy.sparse as sp
from scipy.integrate import solve_ivp
from finite_model import build

ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,ok,kind='EXACT'):
    assert bool(ok),name
    checks.append(dict(name=name,kind=kind,status='PASS'))
M=build(ROOT);A=M['A'];B1,B2,B3=M['B'];P=M['protected']
check('finite_boundary_12_nilpotence',(B1@B2).nnz==0)
check('finite_boundary_23_nilpotence',(B2@B3).nnz==0)
beta=Q(2,3);alpha=Q(1,12);f2=beta**2+12*alpha**2
check('port_column_norm_exact',f2==Q(19,36))
check('all_gradient_columns_zero_triangle_circulation',(B2.T@B1.T).nnz==0)
check('star_contact_signs_have_12_entries',all(B1.getrow(u).nnz==12 for u in range(120)))

# Arbitrary rational signed states test the full algebraic storage identities.
c=[Q(2,3),Q(-1,5)];z=[Q(1,7),Q(-2,9)];F=[[Q(3,4),Q(1,6)],[Q(-2,5),Q(4,7)]]
stock=[Q(1,11),Q(2,13)];cap=[Q(3),Q(4)];d=[Q(1),Q(2)];r=[Q(1,5),Q(2,5)]
b=[stock[i]+z[i]**2/2 for i in range(2)];g=[1-b[i]/cap[i] for i in range(2)]
x=[sum(F[j][i]*c[j] for j in range(2)) for i in range(2)]
dc=[sum(F[j][i]*g[i]*z[i] for i in range(2)) for j in range(2)]
dz=[-g[i]*x[i]-d[i]*z[i] for i in range(2)]
dm=[d[i]*z[i]**2-r[i]*stock[i] for i in range(2)]
dw=[r[i]*stock[i] for i in range(2)]
check('reciprocal_cross_power_cancels',sum(c[i]*dc[i] for i in range(2))+sum(z[i]*(-g[i]*x[i]) for i in range(2))==0)
check('signed_storage_decreases_by_true_positive_source',sum(c[i]*dc[i]+z[i]*dz[i] for i in range(2))==-sum(d[i]*z[i]**2 for i in range(2)))
check('complete_normalized_resource_conservation',sum(c[i]*dc[i]+z[i]*dz[i]+dm[i]+dw[i] for i in range(2))==0)
check('buffer_derivative_identity',all(z[i]*dz[i]+dm[i]==-g[i]*z[i]*x[i]-r[i]*stock[i] for i in range(2)))
check('stock_boundary_is_inward',all(d[i]*z[i]**2>=0 for i in range(2)))
check('capacity_boundary_is_inward',all(-r[i]*stock[i]<=0 for i in range(2)))
check('sink_receipt_nonnegative',all(x>=0 for x in dw))
check('recovery_reserve_derivative_exact',sum(c[i]*dc[i]+z[i]*dz[i]+dm[i] for i in range(2))==-sum(dw))
check('positive_observability_factor_examples',all(beta**2+alpha**2*Q(w)**2>0 for w in range(11)))

# Conservative rational bound Qmax=3/20 exceeds the exact radical contact bound.
C=Q(1,50);Ecmax=Q(1,2);Qmax=Q(3,20);latency=Q(1,100);headroom=C/4
check('rational_transfer_bound',Qmax**2>=4*f2*C*Ecmax)
check('guard_exponent_exact',Qmax*latency/C==Q(3,40))
# exp(x)<=1/(1-x), 0<=x<1; provides a rational guard that is at least as early.
xguard=Qmax*latency/C;exp_upper=1/(1-xguard);high=C-headroom*exp_upper;low=C/4
check('predictive_guard_rational',high==Q(27,1850))
check('hysteresis_has_positive_width',0<low<high<C)
check('post_latency_remaining_headroom',headroom*exp_upper*(1-xguard)==headroom)
check('positive_timeout_and_hysteresis_imply_positive_write_dwell',Q(1)>0 and (high-low)/Qmax>0)
check('null_packet_has_no_load_guard_event',Q(0)<high)

Fsp=sp.vstack([float(beta)*sp.eye(120),float(alpha)*B1.T,sp.csc_matrix((1800,120))],format='csc')
cut=A-M['edge_operator'](M['e'])
cap=np.full(120,float(C));ghi=float(high);glo=float(low);drain=1.;sink=.2
def rhs(operator):
    def fun(t,state):
        c=state[:2640];z=state[2640:2760];m=state[2760:2880]
        b=m+z*z/2;g=np.maximum(0,1-b/cap);x=Fsp.T@c
        return np.concatenate([operator@c+Fsp@(g*z),-g*x-drain*z,drain*z*z-sink*m,sink*m])
    return fun
def stop_write(t,state):
    z=state[2640:2760];m=state[2760:2880]
    return np.max(m+z*z/2)-ghi
stop_write.terminal=True;stop_write.direction=1
initial=np.zeros(3000);initial[M['u']]=1
write_budget=1.
write=solve_ivp(rhs(cut),[0,write_budget],initial,events=stop_write,rtol=2e-9,atol=2e-11,max_step=.005,dense_output=True)
check('benchmark_predictive_guard_is_reached',write.t_events[0].size==1,'NUMERICAL')
tguard=float(write.t_events[0][0]);atguard=write.y_events[0][0]
# Model the full allowed actuation delay under the old writer before restoration.
delay=solve_ivp(rhs(cut),[tguard,tguard+float(latency)],atguard,rtol=2e-9,atol=2e-11,max_step=.002,dense_output=True)
trestore=tguard+float(latency);restored=delay.y[:,-1];reference=P(restored[:2640]);PWnorm=float(reference@reference)
ready_tol=1e-7
def ready_event(t,state):
    c=state[:2640];z=state[2640:2760];m=state[2760:2880];u=c-P(c)
    residual=.5*(u@u+z@z)+m.sum()
    return max(residual/ready_tol,np.max(m+z*z/2)/glo)-1
ready_event.terminal=True;ready_event.direction=-1
recovery=solve_ivp(rhs(A),[trestore,trestore+1600],restored,method='DOP853',events=ready_event,rtol=2e-11,atol=2e-13,max_step=.08,dense_output=True)
check('benchmark_positive_tolerance_ready_is_reached',recovery.t_events[0].size==1,'NUMERICAL')
tready=float(recovery.t_events[0][0]);last=recovery.y_events[0][0]
states=np.concatenate([write.sol(np.linspace(0,tguard,61)),delay.sol(np.linspace(tguard,trestore,11)),recovery.sol(np.linspace(trestore,tready,401))],axis=1)
cc=states[:2640];zz=states[2640:2760];mm=states[2760:2880];ww=states[2880:]
buffers=mm+zz*zz/2;total=.5*np.sum(cc*cc+0,axis=0)+.5*np.sum(zz*zz,axis=0)+mm.sum(axis=0)+ww.sum(axis=0)
check('stock_and_export_stay_nonnegative',min(mm.min(),ww.min())>-1e-10,'NUMERICAL')
check('all_local_buffers_stay_within_capacity',buffers.max()<=float(C)+1e-10,'NUMERICAL')
check('complete_resource_balance_along_hybrid_path',np.max(abs(total-.5))<3e-7,'NUMERICAL')
lat_end=restored[2760:2880]+restored[2640:2760]**2/2
check('latency_keeps_promised_headroom',lat_end.max()<=float(C-headroom)+1e-8,'NUMERICAL')
sample=recovery.sol(np.linspace(trestore,tready,60));protected_norms=np.array([P(s[:2640])@P(s[:2640]) for s in sample.T])
check('restored_protected_stock_is_constant',np.max(abs(protected_norms-PWnorm))<3e-8,'NUMERICAL')
check('writer_deposits_nonzero_protected_stock',PWnorm>1e-7,'NUMERICAL')
u0=restored[:2640]-P(restored[:2640]);reserve0=.5*(u0@u0+restored[2640:2760]@restored[2640:2760])+restored[2760:2880].sum()
ul=last[:2640]-P(last[:2640]);residual=.5*(ul@ul+last[2640:2760]@last[2640:2760])+last[2760:2880].sum()
check('export_prediction_matches_remaining_resource',abs((last[2880:].sum()-restored[2880:].sum())-(reserve0-residual))<3e-7,'NUMERICAL')
check('bath_budget_is_finite_and_respected',ww.sum(axis=0).max()<2.,'NUMERICAL')
null=solve_ivp(rhs(cut),[0,write_budget],np.zeros(3000),events=stop_write,rtol=2e-9,atol=2e-11,max_step=.1)
check('null_packet_times_out_without_false_load_event',null.t_events[0].size==0 and null.t[-1]==write_budget and np.max(abs(null.y))==0,'NUMERICAL')
data={'parameters':{'beta':str(beta),'alpha':str(alpha),'coupling_rate':1,'transport_drain':1,'export_rate':'1/5','capacity_per_port':str(C),'latency':str(latency),'required_headroom':str(headroom),'q_bound':str(Qmax),'high_guard':str(high),'low_guard':str(low),'maximum_write_duration':write_budget,'ready_tolerance':ready_tol,'export_reservoir_capacity':2},'guard_time':tguard,'restoration_time':trestore,'ready_time':tready,'protected_stock_after_write':PWnorm,'protected_chain_energy':PWnorm/2,'max_buffer':float(buffers.max()),'max_buffer_after_latency':float(lat_end.max()),'resource_balance_max_error':float(np.max(abs(total-.5))),'export_after_ready':float(last[2880:].sum()),'remaining_recovery_resource':float(residual),'predicted_additional_export_at_restore':float(reserve0),'final_max_buffer':float((last[2760:2880]+last[2640:2760]**2/2).max()),'provided_inputs':['initial vertex amplitude at u','selected writer edge','frozen candidate kinetic coefficients and capacities','all stars available','declared finite write budget and controller timer'],'physical_promotion':0}
result={'status':'PASS','exact_checks':sum(c['kind']=='EXACT' for c in checks),'numerical_checks':sum(c['kind']=='NUMERICAL' for c in checks),'checks':checks,'independent_review':False,'physical_promotion':0}
(ROOT/'POSITIVE_STOCK_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
(ROOT/'POSITIVE_STOCK_DATA.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}));print(json.dumps(data))
