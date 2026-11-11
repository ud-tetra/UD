"""Exact circuit/module mapping and loaded two-channel apparatus checks."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations,product
import json,math,numpy as np
from scipy.linalg import expm
ROOT=Path(__file__).resolve().parent;checks=[]
def check(name,ok,kind='EXACT'):
 assert bool(ok),name
 checks.append({'name':name,'status':'PASS','kind':kind})
def rank(a):
 a=[[Q(int(x)) if not isinstance(x,Q) else x for x in row] for row in a];r=0
 for j in range(len(a[0])):
  p=next((i for i in range(r,len(a)) if a[i][j]),None)
  if p is None:continue
  a[r],a[p]=a[p],a[r];v=a[r][j];a[r]=[x/v for x in a[r]]
  for i in range(r+1,len(a)):
   v=a[i][j]
   if v:a[i]=[x-v*y for x,y in zip(a[i],a[r])]
  r+=1
  if r==len(a):break
 return r
def inv(a):
 n=len(a);z=[[Q(x) for x in row]+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
 for k in range(n):
  p=next(i for i in range(k,n) if z[i][k]);z[k],z[p]=z[p],z[k];v=z[k][k];z[k]=[x/v for x in z[k]]
  for i in range(n):
   if i!=k:
    v=z[i][k]
    if v:z[i]=[x-v*y for x,y in zip(z[i],z[k])]
 return np.array([row[n:] for row in z],dtype=object)
def charpoly(a):
 n=len(a);I=np.eye(n,dtype=object);B=I.copy();coef=[Q(1)]
 for k in range(1,n+1):
  AB=a@B;c=-sum(AB[i,i] for i in range(n))/Q(k);coef.append(c);B=AB+c*I
 return coef
def polymul(p,q):
 z=[Q(0)]*(len(p)+len(q)-1)
 for i,x in enumerate(p):
  for j,y in enumerate(q):z[i+j]+=x*y
 return z

tets=[(0,1,2,3),(0,1,2,4)];C=[sorted({s for t in tets for s in combinations(t,d+1)}) for d in range(4)];ids=[{s:i for i,s in enumerate(cs)} for cs in C];B=[]
for d in [1,2,3]:
 b=np.zeros((len(C[d-1]),len(C[d])),dtype=object)
 for j,s in enumerate(C[d]):
  for k in range(d+1):b[ids[d-1][s[:k]+s[k+1:]],j]=(-1)**k
 B.append(b)
B1,B2,B3=B;M=B3.T@B3;Mi=inv(M);shared=ids[2][(0,1,2)];es=np.eye(7,dtype=object)[:,shared]
check('physical_mesh_Gram_is_native_module',np.array_equal(M,np.array([[4,1],[1,4]],dtype=object)))
check('module_face_constraint',np.array_equal(B2@B3,np.zeros((9,2),dtype=object)))
check('shared_capacitor_generates_cross_interaction',np.array_equal(M,3*np.eye(2,dtype=object)+np.ones((2,2),dtype=object)))
A9=np.block([[np.zeros((7,7),dtype=object),-B3],[B3.T,np.zeros((2,2),dtype=object)]])
J9=np.block([[np.zeros((7,2),dtype=object),B3@Mi],[np.eye(2,dtype=object),np.zeros((2,2),dtype=object)]])
A4=np.block([[np.zeros((2,2),dtype=object),np.eye(2,dtype=object)],[-M,np.zeros((2,2),dtype=object)]])
H4=np.block([[np.eye(2,dtype=object),np.zeros((2,2),dtype=object)],[np.zeros((2,2),dtype=object),Mi]])
check('physical_module_embedding_rank_four',rank(J9)==4)
check('physical_first_order_intertwiner',np.array_equal(A9@J9,J9@A4))
check('physical_energy_pullback',np.array_equal(J9.T@J9,H4))
check('physical_static_offsets_dimension_five',7-rank(B3.T)==5)
q=np.array([Q(2,3),Q(-1,7)],dtype=object);v=np.array([Q(3,8),Q(-2,9)],dtype=object);state=np.r_[q,v]
check('physical_energy_example',(J9@state)@(J9@state)==state@H4@state)
read=np.zeros((2,9),dtype=object);read[0,shared]=1;read[1,:7]=(np.array([1,-1],dtype=object)@B3.T)
C4=read@J9
check('shared_face_readout_is_velocity_sum',list(C4[0])==[0,0,-Q(1,5),-Q(1,5)])
check('pickup_readout_is_velocity_difference',list(C4[1])==[0,0,1,-1])
check('two_channel_first_derivative_observability',rank(np.vstack([C4,C4@A4]))==4)
check('face_only_observability_rank_two',rank(np.vstack([C4[:1]@np.linalg.matrix_power(A4,k) for k in range(4)]))==2)
check('pickup_only_observability_rank_two',rank(np.vstack([C4[1:]@np.linalg.matrix_power(A4,k) for k in range(4)]))==2)
measure=np.r_[C4@state,C4@A4@state];yf,yp,dyf,dyp=measure
reconstructed=np.array([(dyf-dyp/3)/2,(dyf+dyp/3)/2,(-5*yf+yp)/2,(-5*yf-yp)/2],dtype=object)
check('derivative_state_reconstruction_exact',np.array_equal(reconstructed,state))

# Exact elementary inequalities supporting h=1/4 sampling and a deterministic noise bound.
check('sin_sqrt5_over4_above_half',5*91**2>192**2)
check('sin_sqrt3_over4_above_two_fifths',3*155**2>256**2)
check('qsum_noise_coefficient_below9',16*5<81)
check('qdiff_noise_coefficient_below3',Q(25,3)<9)
check('inherited_state_noise_bound_below9',2*6**2+Q(2*3**2,3)==78<81)
check('one_percent_capacitive_loading_shift_below_two_per_mille',Q(503,505)>Q(499,500)**2)

# Full finite-impedance readout: dimensionless verification benchmark L=C=Ls=1.
L=Q(1);Cc=Q(1);Ls=Q(1);mu=Q(1,10);Rs=Q(10);Gp=Q(1,100);Cp=Q(1,100)
Cb=np.eye(7,dtype=object)*Cc;Cb[shared,shared]+=Cp;CbI=inv(Cb);d=np.array([1,-1],dtype=object)
Lm=np.block([[L*np.eye(2,dtype=object),mu*d[:,None]],[mu*d[None,:],np.array([[Ls]],dtype=object)]])
check('pickup_inductance_positive_Schur',L*Ls-2*mu**2>0)
force=np.block([[B3.T@CbI,np.zeros((2,3),dtype=object)],[np.zeros((1,9),dtype=object),np.array([[-Rs]],dtype=object)]])
top=np.block([-Gp*np.outer(es,es)@CbI,-B3,np.zeros((7,1),dtype=object)])
Af=np.vstack([top,inv(Lm)@force]);Hf=np.block([[CbI,np.zeros((7,3),dtype=object)],[np.zeros((3,7),dtype=object),Lm]])
Dloss=np.zeros((10,10),dtype=object);Dloss[:7,:7]=Gp*CbI@np.outer(es,es)@CbI;Dloss[9,9]=Rs
check('full_loaded_passivity_identity',np.array_equal(Hf@Af+Af.T@Hf,-2*Dloss))
Cf=np.zeros((2,10),dtype=object);Cf[0,:7]=es@CbI;Cf[1,9]=Rs
Of=np.vstack([Cf@np.linalg.matrix_power(Af,k) for k in range(5)])
check('loaded_two_channel_observable_dimension_six',rank(Of)==6)
check('loaded_first_three_derivative_blocks_rank_six',rank(np.vstack([Cf,Cf@Af,Cf@Af@Af]))==6)
pp=[Q(101),Q(1),Q(503),Q(3)];pm=[Q(49),Q(500),Q(150),Q(1500)]
target=polymul([x/pp[0] for x in pp],[x/pm[0] for x in pm])+[Q(0)]*4
check('loaded_full_characteristic_factorization',charpoly(Af)==target)
check('common_mode_cubic_Routh_margin',L*Cc*Gp*(3*(Cc+Cp)+2*Cc)-L*Cc*(Cc+Cp)*3*Gp==2*L*Cc**2*Gp>0)
check('difference_cubic_Routh_margin',L*Rs*3*Ls/Cc-(L*Ls-2*mu**2)*3*Rs/Cc==6*Rs*mu**2/Cc>0)

# Numerical traces corroborate the exact physical map, two-sample formula and loaded loss.
sample_h=.25;w5=math.sqrt(5);w3=math.sqrt(3)
def decode(y0,y1):
 qs=w5*(y1[0]-math.cos(w5*sample_h)*y0[0])/math.sin(w5*sample_h)
 qd=-(y1[1]-math.cos(w3*sample_h)*y0[1])/(w3*math.sin(w3*sample_h))
 vs=-5*y0[0];vd=y0[1]
 return np.array([(qs+qd)/2,(qs-qd)/2,(vs+vd)/2,(vs-vd)/2])
statef=np.array(state,dtype=float);A4f=np.array(A4,dtype=float);C4f=np.array(C4,dtype=float)
y0=C4f@statef;y1=C4f@expm(A4f*sample_h)@statef
check('two_sample_reconstruction_numeric',np.linalg.norm(decode(y0,y1)-statef)<1e-12,'NUMERICAL')
noise_ratios=[]
for signs in product([-1,1],repeat=4):
 err=decode(y0+.001*np.array(signs[:2]),y1+.001*np.array(signs[2:]))-statef
 noise_ratios.append(float(math.sqrt(err@np.array(H4,dtype=float)@err)/.001))
check('all_noise_box_vertices_within_proved_bound',max(noise_ratios)<9,'NUMERICAL')
for t in [.2,.8,2.]:
 check('physical_trajectory_'+str(t),np.linalg.norm(expm(np.array(A9,dtype=float)*t)@np.array(J9,dtype=float)@statef-np.array(J9,dtype=float)@expm(A4f*t)@statef)<1e-12,'NUMERICAL')
rootsplus=np.roots([float(x) for x in pp]);rootsminus=np.roots([float(x) for x in pm])
check('both_loaded_channels_decay',max(rootsplus.real.max(),rootsminus.real.max())<0,'NUMERICAL')
Afnum=np.array(Af,dtype=float);Hnum=np.array(Hf,dtype=float)
start=np.r_[np.array((B3@Mi)@v,dtype=float),np.array(q,dtype=float),0.]
ages=np.linspace(0,100,1001);energies=[];lossrates=[]
for t in ages:
 x=expm(Afnum*t)@start;energies.append(float(x@Hnum@x/2));lossrates.append(float(x@np.array(Dloss,dtype=float)@x))
from scipy.integrate import quad
Dnum=np.array(Dloss,dtype=float)
def instantaneous_loss(t):
 x=expm(Afnum*t)@start
 return float(x@Dnum@x)
loss,quadrature_error=quad(instantaneous_loss,0,100,epsabs=1e-11,epsrel=1e-11,limit=500)
check('loaded_energy_monotone',np.max(np.diff(energies))<1e-12,'NUMERICAL')
check('loaded_energy_loss_integral',abs(energies[0]-energies[-1]-loss)<2e-7,'NUMERICAL')
check('adaptive_loss_quadrature_accuracy',quadrature_error<1e-9,'NUMERICAL')
encode=lambda a:[[str(x) for x in row] for row in a]
data={'B3':encode(B3),'shared_face_index':shared,'M':encode(M),'module_generator':encode(A4),'physical_module_embedding':encode(J9),'module_energy_metric':encode(H4),'ideal_readout':encode(C4),'loaded_generator':encode(Af),'loaded_energy_metric':encode(Hf),'loaded_readout':encode(Cf),'benchmark_parameters':{'L':str(L),'C':str(Cc),'L_secondary':str(Ls),'mutual_each_lobe':str(mu),'R_secondary':str(Rs),'probe_conductance':str(Gp),'probe_capacitance':str(Cp),'scope':'dimensionless constructor benchmark, not a component recommendation'},'common_cubic_integer_coefficients':[int(x) for x in pp],'difference_cubic_integer_coefficients':[int(x) for x in pm],'common_roots':[{'real':float(x.real),'imag':float(x.imag)} for x in rootsplus],'difference_roots':[{'real':float(x.real),'imag':float(x.imag)} for x in rootsminus],'sample_interval':'1/4 in normalized time','max_sample_noise_amplification_corrob':max(noise_ratios),'loaded_energy_initial':energies[0],'loaded_energy_final_at100':energies[-1],'integrated_loaded_dissipation':loss,'physical_promotion':0}
(ROOT/'PHYSICAL_MODULE_DATA.json').write_text(json.dumps(data,indent=2)+'\n')
result={'status':'PASS','exact_checks':sum(c['kind']=='EXACT' for c in checks),'numerical_checks':sum(c['kind']=='NUMERICAL' for c in checks),'checks':checks,'independent_review':False,'physical_promotion':0}
(ROOT/'PHYSICAL_MODULE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}));print(json.dumps({k:data[k] for k in ['common_roots','difference_roots','max_sample_noise_amplification_corrob','loaded_energy_initial','loaded_energy_final_at100']}))
