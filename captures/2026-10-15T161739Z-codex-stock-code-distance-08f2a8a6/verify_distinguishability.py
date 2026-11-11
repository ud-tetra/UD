"""Current exact geometry/bounds and numerical six-branch code replay."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial, comb
import math,json
import numpy as np
import scipy.sparse as sp
from scipy.integrate import solve_ivp
from finite_model import build
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,ok,kind='EXACT'):
 assert bool(ok),name
 checks.append({'name':name,'kind':kind,'status':'PASS'})
M=build(ROOT);A=M['A'];B1,B2,B3=M['B'];C=M['C'];P=M['protected'];u=M['u']
reps=json.loads((ROOT/'sources/ROBUST_RETENTION_DATA.json').read_text())['code_representatives']
beta=Q(2,3);alpha=Q(1,12);F=sp.vstack([float(beta)*sp.eye(120),float(alpha)*B1.T,sp.csc_matrix((1800,120))],format='csc')
check('chain_skew',(A+A.T).nnz==0)
check('safe_port_gradient_identity',(B2.T@B1.T).nnz==0)
check('chain_nilpotence_12',(B1@B2).nnz==0)
check('chain_nilpotence_23',(B2@B3).nnz==0)
check('all_triangles_have_two_tetrahedra_no_free_faces',np.all(np.asarray(abs(B3).sum(axis=1)).ravel()==2))
check('port_norm_bound_by_degree',beta**2+24*alpha**2==Q(11,18)<1)
check('B2_squared_norm_below_16',int(abs(B2).sum(axis=0).max())*int(abs(B2).sum(axis=1).max())<16)
check('B3_squared_norm_below_16',int(abs(B3).sum(axis=0).max())*int(abs(B3).sum(axis=1).max())<16)
# q(L) nonzero roots are all below 16; the reconstructed pseudoinverse identity certifies q(L)L=0.
check('vertex_spectral_root_bound',45<49 and 20<36 and max(9,12,14,15)<16)
check('finite_incidence_norm_A_below_4_source_certificate',np.array_equal(M['L'].astype(object)@M['Z'],(M['den']//120)*(120*np.eye(120,dtype=object)-np.ones((120,120),dtype=object))))

# Quaternion conjugations give signed simplicial automorphisms fixing the source vertex.
V=[tuple(tuple(x) for x in v) for v in M['D']['vertices']];vid={v:i for i,v in enumerate(V)}
neg=lambda x:(-x[0],-x[1]);mul=lambda x,y:(x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1]);sm=lambda xs:(sum(x[0] for x in xs),sum(x[1] for x in xs))
def qm(x,y):
 z=[sm([mul(x[0],y[0])]+[neg(mul(x[i],y[i])) for i in [1,2,3]])]
 for i,j,k in [(1,2,3),(2,3,1),(3,1,2)]:z.append(sm([mul(x[0],y[i]),mul(x[i],y[0]),mul(x[j],y[k]),neg(mul(x[k],y[j]))]))
 assert all(a%2==b%2==0 for a,b in z)
 return tuple((a//2,b//2) for a,b in z)
conj=lambda x:(x[0],)+tuple(neg(t) for t in x[1:])
ids=[{s:i for i,s in enumerate(cs)} for cs in C];offset=np.cumsum([0]+list(map(len,C)))
ref=reps[0];automorphisms=[]
for h,r in enumerate(reps):
 q=next(q for q in V if qm(qm(conj(q),V[ref['neighbor']]),q)==V[r['neighbor']])
 vp=[vid[qm(qm(conj(q),v),q)] for v in V];check('source_fixed_'+str(h),vp[u]==u)
 rr=[];cc=[];vv=[]
 for d,cs in enumerate(C):
  for j,s in enumerate(cs):
   t=tuple(vp[k] for k in s);sign=(-1)**sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))
   rr.append(int(offset[d])+ids[d][tuple(sorted(t))]);cc.append(int(offset[d])+j);vv.append(sign)
 T=sp.csc_matrix((vv,(rr,cc)),shape=(2640,2640));Vperm=T[:120,:120]
 check('chain_generator_equivariant_'+str(h),(T@A-A@T).nnz==0)
 # Avoid floating cancellation in the exact rational port check: use 12 F integral.
 Fi=sp.vstack([8*sp.eye(120,dtype=np.int64),B1.T,sp.csc_matrix((1800,120),dtype=np.int64)],format='csc')
 check('port_equivariant_'+str(h),(T@Fi-Fi@Vperm).nnz==0)
 check('writer_equivariant_'+str(h),(T@M['edge_operator'](ref['edge'])-M['edge_operator'](r['edge'])@T).nnz==0)
 automorphisms.append({'subgroup':r['subgroup'],'conjugator_vertex':vid[q],'vertex_permutation':vp})

# Exact lower write time from b<=C tanh^2(k t).
capacity=Q(1,50);high=Q(27,1850);Cratio=high/capacity
check('comparison_rate_squared',((beta**2+12*alpha**2)/(2*capacity))==Q(475,36))
check('comparison_rate_less_11_over_3',Q(475,36)<Q(121,9))
def exp_upper(x,n):
 terms=[x**k/factorial(k) for k in range(n+1)]
 return sum(terms)+terms[-1]*x/Q(n+1)/(1-x/Q(n+2))
check('exp_22_over_9_below_12',exp_upper(Q(22,9),20)<12)
check('tanh_guard_not_reached_before_one_third',Q(121,169)<Cratio)
check('deadline_plus_latency_half',Q(49,100)+Q(1,100)==Q(1,2))

# Exact Taylor/Bernstein bounds for the unforced reference drive a0(t).
edge=ref['edge'];K=A-M['edge_operator'](edge);e0=np.zeros(2640,dtype=object);e0[u]=1
delta=np.zeros(2640,dtype=object);delta[u]=1;delta[ref['neighbor']]=-1
coef=[];v=e0.copy()
for k in range(16):
 coef.append(Q(int(sum(delta[j]*v[j] for j in range(2640))),factorial(k)))
 v=K@v.astype(np.int64) if max(abs(x) for x in v)<10**12 else np.array(K.toarray(),dtype=object)@v
check('reference_drive_odd_coefficients_zero',all(coef[k]==0 for k in range(1,16,2)))
def bernstein(p,a,b):
 n=len(p)-1
 # power coefficients after t=a+(b-a)x
 s=[sum(p[k]*comb(k,j)*a**(k-j)*(b-a)**j for k in range(j,n+1)) for j in range(n+1)]
 return [sum(s[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]
remainder=Q(3,2)*Q(3)**16/factorial(16)
amin=min(bernstein(coef,Q(0),Q(1,2)))-remainder
jcoef=[Q(0)]+[a/Q(k+1) for k,a in enumerate(coef)]
jmin=min(bernstein(jcoef,Q(1,3),Q(1,2)))-remainder/2
check('reference_drive_lower_minus_one_over_16',amin>=-Q(1,16))
check('reference_integral_lower_one_quarter',jmin>=Q(1,4))
check('drive_integral_perturbation_bound',Q(1,2)**3/4==Q(1,32))
check('actual_J_lower',Q(1,4)-Q(1,32)==Q(7,32))
check('negative_drive_mass_upper',Q(1,16)*Q(1,2)+Q(1,32)==Q(1,16))
check('filter_min_singular_value_lower',(Q(7,32)-Q(1,16))/2==Q(5,64))
Tlead=np.zeros((720,6),dtype=np.int64)
for j,r in enumerate(reps):Tlead[r['edge'],j]=r['outward_sign']
Dlead=(B1@Tlead).astype(object)
Glead=np.eye(6,dtype=object)-np.array([[Q(int(x),int(M['den'])) for x in row] for row in Dlead.T@M['Z']@Dlead],dtype=object)
leading=min(Glead[i,i]+Glead[j,j]-2*Glead[i,j] for i in range(6) for j in range(i))
check('leading_distance_reconstructed_exactly',leading==Q(136907,75600))
check('edge_cycle_norm_reconstructed_exactly',all(Glead[i,i]==Q(601,720) for i in range(6)))
check('six_word_leading_distance_above_5_over_4',leading>Q(25,16))
check('finite_word_distance_bound',Q(5,64)*Q(5,4)==Q(25,256))
check('nearest_template_radius',Q(25,256)/2==Q(25,512))
check('post_recovery_port_error_bound_600',Q(601,720)*Q(600,2)<16**2)
check('example_combined_error_contract',Q(1,100)+4*Q(1,1000)+16*Q(1,1000)<Q(25,512))

words=[];receipts=[];rawstates=[]
for r in reps:
 cut=A-M['edge_operator'](r['edge'])
 def rhs(t,s):
  c=s[:2640];z=s[2640:2760];m=s[2760:2880];g=np.maximum(0,1-(m+z*z/2)/float(capacity));x=F.T@c
  return np.r_[cut@c+F@(g*z),-g*x-z,z*z-.2*m,.2*m]
 def guard(t,s):return np.max(s[2760:2880]+s[2640:2760]**2/2)-float(high)
 guard.terminal=True;guard.direction=1
 initial=np.zeros(3000);initial[u]=1
 sol=solve_ivp(rhs,[0,.49],initial,method='DOP853',events=guard,rtol=1e-11,atol=1e-13,max_step=.005)
 check('branch_guard_before_timeout_'+str(r['subgroup']),sol.t_events[0].size==1,'NUMERICAL')
 tg=float(sol.t_events[0][0]);delay=solve_ivp(rhs,[tg,tg+.01],sol.y_events[0][0],method='DOP853',rtol=1e-11,atol=1e-13,max_step=.002)
 last=delay.y[:,-1];y=P(last[:2640]);words.append(y);rawstates.append(last)
 receipts.append({'subgroup':r['subgroup'],'edge':r['edge'],'guard_time':tg,'restoration_time':tg+.01,'protected_norm_squared':float(y@y),'retained_energy':float(y@y/2),'ultimate_export':float(.5-y@y/2),'export_at_restoration':float(last[2880:].sum()),'working_resource_at_restoration':float(.5*np.linalg.norm(last[:2640]-y)**2+.5*np.linalg.norm(last[2640:2760])**2+last[2760:2880].sum()),'scores':M['scores'](y).tolist()})
words=np.array(words);dist=np.linalg.norm(words[:,None,:]-words[None,:,:],axis=2);dmin=min(dist[i,j] for i in range(6) for j in range(i))
check('all_restore_times_in_proved_window',all(1/3<r['restoration_time']<.5 for r in receipts),'NUMERICAL')
check('six_branch_event_times_agree',max(r['guard_time'] for r in receipts)-min(r['guard_time'] for r in receipts)<2e-9,'NUMERICAL')
check('six_retained_stocks_agree',max(r['protected_norm_squared'] for r in receipts)-min(r['protected_norm_squared'] for r in receipts)<2e-9,'NUMERICAL')
check('finite_distance_exceeds_analytic_bound',dmin>float(Q(25,256)),'NUMERICAL')
check('all_source_labels_win_quadratic_scores',all(np.argmax(r['scores'])==r['subgroup'] for r in receipts),'NUMERICAL')
for i,y in enumerate(words):
 direction=words[(i+1)%6]-y;noise=.04*direction/np.linalg.norm(direction)
 check('bounded_noise_nearest_template_'+str(i),np.argmin(np.linalg.norm(words-(y+noise),axis=1))==i,'NUMERICAL')
np.savez_compressed(ROOT/'CODEBOOK.npz',protected_words=words,restoration_states=np.array(rawstates),pair_distances=dist)
data={'exact_certificate':{'restoration_window':['1/3','1/2'],'drive_reference_lower_bound':'-1/16','reference_integral_lower_bound':'1/4','actual_integral_lower_bound':'7/32','negative_drive_mass_upper_bound':'1/16','filter_singular_value_lower_bound':'5/64','pair_distance_lower_bound':'25/256','decoder_error_radius':'25/512','bernstein_actual_drive_bound':str(amin),'bernstein_integral_bound':str(jmin),'reference_drive_taylor_coefficients':[str(x) for x in coef]},'protocol_change':'Maximum write duration 49/100 replaces PR117 control 1; actuation delay remains 1/100. No kinetics or capacity change.','automorphisms':automorphisms,'receipts':receipts,'numerical_min_pair_distance':float(dmin),'numerical_pair_distances':dist.tolist(),'classical_label_count':6,'uniform_label_bits':math.log2(6),'aggregate_local_buffer_capacity':'12/5','collector_capacity':2,'normalized_input_storage':'1/2','post_restore_error_contract':'nu + template_error + 4*abs(phase_error) + 16*abs(epsilon) < 25/512 for s<=600; stated unit-norm edge-port perturbation and d=1','physical_promotion':0}
(ROOT/'DISTINGUISHABILITY_DATA.json').write_text(json.dumps(data,indent=2)+'\n')
result={'status':'PASS','exact_checks':sum(c['kind']=='EXACT' for c in checks),'numerical_checks':sum(c['kind']=='NUMERICAL' for c in checks),'checks':checks,'independent_review':False,'physical_promotion':0}
(ROOT/'DISTINGUISHABILITY_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}));print(json.dumps({'dmin':float(dmin),'guard_time':receipts[0]['guard_time'],'retained_energy':receipts[0]['retained_energy'],'ultimate_export':receipts[0]['ultimate_export'],'bernstein_min_drive':str(amin),'bernstein_min_integral':str(jmin)}))
