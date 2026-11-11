"""Self-contained exact reduction, sampled observer certificate and circuit write budget."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,isqrt,sqrt
import json,math,platform
import numpy as np
from scipy.linalg import expm,eigh
ROOT=Path(__file__).resolve().parent;checks=[]
def ck(n,v,k='EXACT'):
 assert bool(v),n
 checks.append({'name':n,'type':k,'status':'PASS'})
def mat(x):return np.array([[F(v) for v in row] for row in x],dtype=object)
def inv(a):
 n=len(a);a=np.hstack([a.copy(),np.eye(n,dtype=object)])
 for j in range(n):
  k=next(k for k in range(j,n) if a[k,j]);a[[k,j]]=a[[j,k]];a[j]=a[j]/a[j,j]
  for k in range(n):
   if k!=j:a[k]=a[k]-a[k,j]*a[j]
 return a[:,n:]
def positive(a):
 a=a.copy()
 for j in range(len(a)):
  if a[j,j]<=0:return False
  for k in range(j+1,len(a)):
   for l in range(k,len(a)):
    a[k,l]=a[k,l]-a[k,j]*a[j,l]/a[j,j];a[l,k]=a[k,l]
 return True
class IV:
 def __init__(self,a,b=None):self.lo=F(a);self.hi=F(a if b is None else b)
 def __add__(self,v):
  v=iv(v);return IV(self.lo+v.lo,self.hi+v.hi)
 __radd__=__add__
 def __neg__(self):return IV(-self.hi,-self.lo)
 def __sub__(self,v):return self+-iv(v)
 def __rsub__(self,v):return iv(v)+-self
 def __mul__(self,v):
  v=iv(v);a=[x*y for x in (self.lo,self.hi) for y in (v.lo,v.hi)];return IV(min(a),max(a))
 __rmul__=__mul__
 def __truediv__(self,v):
  v=iv(v);assert v.lo*v.hi>0;return self*IV(1/v.hi,1/v.lo)
 def __rtruediv__(self,v):return iv(v)/self
 def __pow__(self,n):
  assert n==2
  return self*self

def iv(x):return x if isinstance(x,IV) else IV(x)
def make(p):
 L,C,Cs,Ls,mu,Rs,Gp,r=[p[k] for k in ['L','C','Cs','Ls','mu','Rs','Gp','r']];de=L*Ls-2*mu**2;g=Gp/Cs
 A=np.array([[0,0,-3,0,0,0],[0,-g,1,0,0,0],[1/(L*C),-2/(L*Cs),-r/L,0,0,0],[0,0,0,0,-3,0],[0,0,0,Ls/(C*de),-Ls*r/de,2*mu*Rs/de],[0,0,0,-mu/(C*de),mu*r/de,-L*Rs/de]],dtype=object)
 G=np.diag([1/(6*C),1/Cs,L/2,1/(6*C),L/2,Ls]).astype(object);G[4,5]=G[5,4]=mu
 B=np.array([[0,0],[0,0],[1/L,0],[0,0],[0,Ls/de],[0,-mu/de]],dtype=object)
 Cmat=np.array([[0,1/Cs,0,0,0,0],[0,0,0,0,0,Rs]],dtype=object)
 loss=np.diag([0,Gp/Cs**2,r/2,0,r/2,Rs]).astype(object)
 # Normalize zeros too: an integer zero divided by two would otherwise be a float.
 return tuple(np.array([[x if isinstance(x,IV) else F(x) for x in row] for row in m],dtype=object) for m in (A,G,B,Cmat,loss))
p={k:F(v) for k,v in {'L':1,'C':1,'Cs':'101/100','Ls':1,'mu':'1/10','Rs':10,'Gp':'1/100','r':'1/100'}.items()}
A,G,B,C,Dloss=make(p);Gi=inv(G)
ck('six_state_energy_positive',positive(G));ck('six_state_passivity',np.array_equal(G@A+A.T@G,-2*Dloss))
port=np.zeros((6,2),dtype=object);port[2,0]=port[4,1]=F(1,2)
ck('drive_input_power_identity',np.array_equal(G@B,port))
# Reconstruct the minimum-energy physical state and four static exclusive offsets.
B3=mat([[-1,-1],[1,0],[0,1],[-1,0],[0,-1],[1,0],[0,1]])
P=np.zeros((6,10),dtype=object);R=np.zeros((10,6),dtype=object)
P[1,0]=1;P[2,7]=P[2,8]=1;P[4,7]=1;P[4,8]=-1;P[5,9]=1
R[0,1]=1;R[7,2]=R[8,2]=F(1,2);R[7,4]=F(1,2);R[8,4]=-F(1,2);R[9,5]=1
for i in range(1,7):
 j=0 if B3[i,0] else 1;sgn=B3[i,j];P[0,i]=sgn;P[3,i]=sgn*(1 if j==0 else -1)
 R[i,0]=sgn/6;R[i,3]=sgn*(1 if j==0 else -1)/6
Cb=np.eye(7,dtype=object);Cb[0,0]=p['Cs'];CbI=inv(Cb);d=mat([[1],[-1]])
Lm=np.block([[p['L']*np.eye(2,dtype=object),p['mu']*d],[p['mu']*d.T,mat([[p['Ls']]])]])
force=np.block([[B3.T@CbI,-p['r']*np.eye(2,dtype=object),np.zeros((2,1),dtype=object)],[np.zeros((1,9),dtype=object),mat([[-p['Rs']]])]])
top=np.hstack([-p['Gp']*np.diag([1,0,0,0,0,0,0])@CbI,-B3,np.zeros((7,1),dtype=object)])
A10=np.vstack([top,inv(Lm)@force]);G10=np.block([[CbI,np.zeros((7,3),dtype=object)],[np.zeros((3,7),dtype=object),Lm]])
ck('exact_reduction_left_inverse',np.array_equal(P@R,np.eye(6,dtype=object)))
ck('exact_reduction_generator',np.array_equal(P@A10,A@P))
ck('exact_dynamic_embedding',np.array_equal(A10@R,R@A))
ck('exact_energy_pullback',np.array_equal(R.T@G10@R,G))
ck('four_static_offsets',np.array_equal(A10@(np.eye(10,dtype=object)-R@P),np.zeros((10,10),dtype=object)))
# Three samples, no differentiation: exact rational Taylor/positive-definiteness certificate.
W2=np.diag([p['Cs'],p['Ls']/p['Rs']**2]).astype(object)
a=F(11);c=F(11,10);N=100;times=[F(0),F(1),F(2)]
frobA=sum((Gi@A.T@G@A)[i,i] for i in range(6));frobC=sum((Gi@C.T@W2@C)[i,i] for i in range(6))
ck('energy_generator_norm_below11',frobA<a*a)
# The two row energies are orthogonal, allowing the sharper spectral bound.
Cg=C@Gi@C.T;ck('energy_output_rows_orthogonal',Cg[0,1]==Cg[1,0]==0)
ck('energy_output_norm_below11over10',max(W2[i,i]*Cg[i,i] for i in range(2))<c*c)
def taylor(t):
 E=np.eye(6,dtype=object);term=E.copy()
 for n in range(1,N+1):term=term@A*t/n;E+=term
 return E
Es=[taylor(t) for t in times];O=np.vstack([C@E for E in Es]);Wstack=np.kron(np.eye(3,dtype=object),W2)
alpha=F(21,1000);rem=(a*2)**(N+1)/factorial(N+1)
ck('rational_sample_Gram_margin',positive(O.T@Wstack@O-alpha**2*G))
ck('Taylor_observer_remainder_below1over1000',3*c*c*rem**2<F(1,1000)**2)
sigma=F(1,50);ck('certified_observer_sigma_lower_bound',alpha-F(1,1000)==sigma)
# Independent relative parameter boxes, including input impedance.
eta=F(1,100000);boxes={k:IV(v*(1-eta),v*(1+eta)) for k,v in p.items()};Ai,Giv,Bi,Ci,_=make(boxes)
def errors(m,m0):
 return np.array([[max(abs(iv(x).lo-m0[i,j]),abs(iv(x).hi-m0[i,j])) for j,x in enumerate(row)] for i,row in enumerate(m)],dtype=object)
EA=errors(Ai,A);EC=errors(Ci,C);EG=errors(Giv,G);EB=errors(Bi,B)
def metric_frob(E,H,K):
 # bound tr(K Delta^T H Delta) using an entrywise error envelope
 n,m=E.shape
 return sum(abs(H[i,k]*K[j,l])*E[k,j]*E[i,l] for i in range(n) for k in range(n) for j in range(m) for l in range(m))
dA=F(1,2000);dC=F(1,50000);dG=F(1,30000)
Aerr2=metric_frob(EA,G,Gi);Cerr2=metric_frob(EC,W2,Gi);Gerr2=metric_frob(EG,Gi,Gi)
dB=F(1,10000);Berr2=metric_frob(EB,G,np.eye(2,dtype=object))
ck('interval_parameter_generator_bound',Aerr2<dA*dA)
ck('interval_parameter_output_bound',Cerr2<dC*dC)
ck('interval_parameter_energy_metric_bound',Gerr2<dG*dG)
ck('interval_parameter_write_input_bound',Berr2<dB*dB)
ck('interval_passivity_and_capacitance',boxes['Cs'].lo>boxes['C'].hi and boxes['L'].lo*boxes['Ls'].lo>2*boxes['mu'].hi**2)
qexp=1/(1-2*dA);kappa=c*(qexp-1)+dC*qexp;rho=F(1,500)
ck('stacked_model_error_bound',3*kappa*kappa<rho*rho)
ck('robust_observability_margin',sigma-rho==F(9,500))
# Retention for original four-coordinate target preparation, probes always connected.
P4=mat([[0,0,'3/5','3/5'],[0,0,'-1/5','-1/5'],[1,1,0,0],[0,0,1,-1],[1,-1,0,0],[0,0,0,0]])
G4=P4.T@G@P4;ET=Es[-1];beta=F(24,25)
ck('prepared_subspace_nominal_retention_certificate',positive(P4.T@ET.T@G@ET@P4-(beta+F(1,1000))*G4))
ck('retention_Taylor_remainder',2*rem+rem**2<F(1,1000))
ck('sqrt_retention_lower_witness',F(979,1000)**2<beta)
robust_ret=(1-dG)/(1+dG)*(F(979,1000)-(qexp-1))**2
ck('prepared_subspace_robust_retention_above95percent',robust_ret>F(19,20))
cone_ret=(1-dG)/(1+dG)*((F(979,1000)-(qexp-1)-qexp*F(1,1000))/(1+F(1,1000)))**2
ck('write_error_cone_retention_above95percent',cone_ret>F(19,20))
# Polynomial exact finite-time write; constant + relative uncertainty is not assumed compensated.
def trim(a):
 a=list(a)
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def add(*aa):
 z=[F(0)]*max(map(len,aa))
 for a0 in aa:
  for i,x in enumerate(a0):z[i]+=x
 return trim(z)
def scale(a,k):return trim([k*x for x in a])
def mul(a,b):
 z=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return trim(z)
def der(a):return trim([i*x for i,x in enumerate(a)][1:] or [F(0)])
def integ(a):return [F(0)]+[x/(i+1) for i,x in enumerate(a)]
def val(a,t):return sum(x*t**i for i,x in enumerate(a))
def area(a,T=F(1)):return val(integ(a),T)
T=F(1);g=p['Gp']/p['Cs'];de=p['L']*p['Ls']-2*p['mu']**2
# x(0)=x'(0)=x(T)=integral(x)=0; x'(T)=1.
Hx=mat([[1,0,0,0,0],[0,1,0,0,0],[1,1,1,1,1],[0,1,2,3,4],['1','1/2','1/3','1/4','1/5']])
x=list(inv(Hx)@np.array([0,0,0,1,0],dtype=object));S=add(der(x),scale(x,g));z=add(scale(x,-3),scale(integ(x),-3*g))
# J(0)=J(T)=0, integral J=-mu/Rs, weighted integral J=Ls*mu/Rs^2.
Hj=mat([[1,0,0,0],[1,1,1,1],['1','1/2','1/3','1/4'],['1/2','1/6','1/12','1/20']])
J=list(inv(Hj)@np.array([0,0,-p['mu']/p['Rs'],p['Ls']*p['mu']/p['Rs']**2],dtype=object))
D=scale(add(scale(J,p['Ls']),scale(integ(J),p['Rs'])),-1/p['mu']);w=scale(integ(D),-3)
Us=add(scale(der(S),p['L']),scale(S,p['r']),scale(z,-1/p['C']),scale(x,2/p['Cs']))
Ud=add(scale(der(J),-de/p['mu']),scale(w,-1/p['C']),scale(J,-p['L']*p['Rs']/p['mu']),scale(D,p['r']))
polys=[z,x,S,w,D,J];controls=[Us,Ud]
ck('write_initial_zero',all(val(a0,F(0))==0 for a0 in polys))
target=[0,0,1,0,1,0];ck('write_target_reached_exactly',[val(a0,T) for a0 in polys]==target)
for i in range(6):
 rhs=add(*[scale(polys[j],A[i,j]) for j in range(6)],*[scale(controls[j],B[i,j]) for j in range(2)])
 ck('write_ODE_component_'+str(i),trim(der(polys[i]))==trim(rhs))
Ep=[F(0)];Lp=[F(0)]
for i in range(6):
 for j in range(6):
  Ep=add(Ep,scale(mul(polys[i],polys[j]),G[i,j]/2))
  Lp=add(Lp,scale(mul(polys[i],polys[j]),Dloss[i,j]))
Pp=scale(add(mul(S,Us),mul(D,Ud)),F(1,2))
ck('write_power_balance_polynomial',trim(der(Ep))==trim(add(Pp,scale(Lp,-1))))
heat=area(Lp);net=area(Pp);targetE=val(Ep,T)
ck('write_net_work_exact',net==heat+targetE and targetE==F(1,2))
loss_parts={'probe':area(scale(mul(x,x),p['Gp']/p['Cs']**2)),'pickup':area(scale(mul(J,J),p['Rs'])),'drive_resistance':area(scale(add(mul(S,S),mul(D,D)),p['r']/2))}
ck('write_all_declared_losses_accounted',sum(loss_parts.values())==heat and all(x>=0 for x in loss_parts.values()))
P2=area(mul(Pp,Pp));b=F(isqrt((T*P2).numerator//(T*P2).denominator)+1)
ck('gross_positive_work_upper_bound',(2*((b+net)/2)-net)**2>=T*P2)
def rootup(x,denom=10**6):
 n=isqrt((x*denom**2).numerator//(x*denom**2).denominator)+1
 return F(n,denom)
stored_root=rootup(2*T*area(Ep));drive_root=rootup(T*area(add(mul(Us,Us),mul(Ud,Ud))))
write_err=(dA*stored_root+dB*drive_root)/(1-dA*T)
ck('write_uncertainty_norm_bounds',stored_root**2>2*T*area(Ep) and drive_root**2>T*area(add(mul(Us,Us),mul(Ud,Ud))))
ck('write_endpoint_uncertainty_below_one_per_mille',write_err<F(1,1000))
seed=np.array(target,dtype=object)
ck('binary_seed_sample_gain_certificate',seed@O.T@Wstack@O@seed>F(501,1000)**2)
ck('binary_seed_actual_nominal_gain_above_half',F(501,1000)-F(1,1000)==F(1,2))
ck('write_read_model_radius_below1over200',rho+(2*c+rho)*F(1,1000)<F(1,200))
ck('binary_amplitude_six_noise_units_suffices',(F(1,2)-F(1,200))*6>F(5,2))
BinGram=B.T@G@B
ck('nominal_drive_power_operator_norm',BinGram[0,1]==BinGram[1,0]==0 and max(BinGram[0,0],BinGram[1,1])<F(3,4)**2)
extra_work=F(1,1000)*F(3,4)*drive_root
ck('uncertain_gross_source_work_below_four_fifths',(b+net)/2+extra_work<F(4,5))
# Numerical corroborations; the certificates above do not rely on these singular values.
Af=np.array(A,dtype=float);Gf=np.array(G,dtype=float);Cf=np.array(C,dtype=float);Gvals,V=eigh(Gf);Gs=(V*np.sqrt(Gvals))@V.T;Gis=(V/np.sqrt(Gvals))@V.T;Ws=np.diag(np.sqrt(np.diag(np.array(W2,dtype=float))))
Abar=Gs@Af@Gis;Cbar=Ws@Cf@Gis;On=np.vstack([Cbar@expm(Abar*float(t)) for t in times]);sv=np.linalg.svd(On,compute_uv=False)
ck('sample_min_singular_numeric',sv[-1]>float(sigma),'NUMERICAL')
e0=np.array([.3,-.2,.4,.1,-.3,.05]);truth=On@e0;est=np.linalg.lstsq(On,truth,rcond=None)[0]
ck('six_state_sample_reconstruction',np.linalg.norm(est-e0)<1e-12,'NUMERICAL')
E2=expm(Af*2);ret=eigh(np.array(P4,dtype=float).T@E2.T@Gf@E2@np.array(P4,dtype=float),np.array(G4,dtype=float),eigvals_only=True)
ck('prepared_retention_numeric',ret.min()>float(beta),'NUMERICAL')
# Each uncertainty-box corner corroborates the analytic entrywise interval enclosure.
from itertools import product
max_model=0.;max_A=0.;max_C=0.
max_write=0.;Uco=np.zeros((2,6))
for i,a0 in enumerate(controls):Uco[i,:len(a0)]=np.array(a0,dtype=float)
mono=np.zeros((6,6))
for i in range(1,6):mono[i,i-1]=i
augstart=np.r_[np.zeros(6),1.,np.zeros(5)]
for signs in product([-1,1],repeat=len(p)):
 pp={k:v*(1+eta*s) for (k,v),s in zip(p.items(),signs)};at,gt,bt,ct,dt=make(pp);at=np.array(at,dtype=float);ct=np.array(ct,dtype=float)
 ot=np.vstack([Ws@ct@expm(at*float(t))@Gis for t in times]);max_model=max(max_model,np.linalg.norm(ot-On,2));max_A=max(max_A,np.linalg.norm(Gs@(at-Af)@Gis,2));max_C=max(max_C,np.linalg.norm(Ws@(ct-Cf)@Gis,2))
 aug=np.block([[at,np.array(bt,dtype=float)@Uco],[np.zeros((6,6)),mono]])
 max_write=max(max_write,np.linalg.norm(Gs@((expm(aug)@augstart)[:6]-np.array(target,dtype=float))))
ck('all256_parameter_corners_model_bound',max_model<float(rho),'NUMERICAL')
ck('all256_parameter_corners_generator_bound',max_A<float(dA) and max_C<float(dC),'NUMERICAL')
ck('all256_parameter_corners_write_bound',max_write<float(write_err),'NUMERICAL')
roots=np.polynomial.polynomial.polyroots(np.array(Pp,dtype=float));knots=[0.]+sorted(float(t.real) for t in roots if abs(t.imag)<1e-7 and 0<t.real<1)+[1.]
pos=neg=0.
for lo,hi in zip(knots[:-1],knots[1:]):
 work=float(val(integ(Pp),hi)-val(integ(Pp),lo))
 if work>=0:pos+=work
 else:neg-=work
ck('gross_positive_minus_recovered_equals_net',abs(pos-neg-float(net))<1e-9,'NUMERICAL')
ck('gross_positive_work_inside_analytic_bounds',float(net)<=pos<=float((b+net)/2),'NUMERICAL')
from scipy.integrate import quad
start=np.array(target,dtype=float)
lossread,err=quad(lambda t:float((expm(Af*t)@start)@np.array(Dloss,dtype=float)@(expm(Af*t)@start)),0,2,epsabs=1e-12)
Eread=float((E2@start)@Gf@(E2@start)/2)
ck('read_energy_identity',abs(.5-Eread-lossread)<1e-10,'NUMERICAL')
# Evaluate write profile endpoints using a high-order numerical integrator.
from scipy.integrate import solve_ivp
uv=lambda t:np.array([float(val(a0,t)) for a0 in controls])
sol=solve_ivp(lambda t,z:Af@z+np.array(B,dtype=float)@uv(t),(0,1),np.zeros(6),method='DOP853',rtol=1e-11,atol=1e-12)
ck('finite_write_trajectory_numeric',np.linalg.norm(sol.y[:,-1]-start)<1e-8,'NUMERICAL')
enc=lambda m:[[str(x) for x in row] for row in m]
data={'parameters':{k:str(v) for k,v in p.items()},'scope':'dimensionless constructor benchmark; no component recommendation','state_order':['z','x','S','w','D','J'],'A6':enc(A),'G6':enc(G),'B6':enc(B),'C6':enc(C),'reduction_6_from10':enc(P),'embedding_10_from6':enc(R),'prepared_embedding_6_from4':enc(P4),'observer_certificate':{'sample_times':['0','1','2'],'Taylor_degree':N,'generator_energy_norm_upper':str(a),'output_energy_norm_upper':str(c),'truncated_sigma_lower':str(alpha),'certified_sigma_lower':str(sigma),'parameter_relative_box':str(eta),'delta_A_upper':str(dA),'delta_C_upper':str(dC),'delta_G_relative_upper':str(dG),'delta_B_upper':str(dB),'stacked_model_error_upper':str(rho),'robust_sigma_margin':str(sigma-rho),'min_singular_numeric':float(sv[-1]),'condition_number_numeric':float(sv[0]/sv[-1]),'all_corner_model_error_max':max_model},'retention_certificate':{'nominal_prepared_energy_fraction_lower':str(beta),'uncertain_prepared_energy_fraction_lower':'19/20','nominal_eigenvalues_numeric':ret.tolist()},'write':{'endpoint_uncertainty_upper':str(write_err),'endpoint_uncertainty_corner_max':max_write,'uncertain_gross_work_upper':'4/5','binary_code_amplitude_in_noise_units':'6','binary_code_retained_energy_fraction_lower':'19/20','binary_code_gross_work_upper_in_noise_squared_units':'144/5','state_time_integral_norm_upper':str(stored_root),'input_time_integral_norm_upper':str(drive_root),'duration':'1','target6':target,'state_polynomials_ascending':[[str(v) for v in a0] for a0 in polys],'drive_sum_polynomial_ascending':[str(v) for v in Us],'drive_difference_polynomial_ascending':[str(v) for v in Ud],'target_energy':str(targetE),'heat':{k:str(v) for k,v in loss_parts.items()},'net_port_work':str(net),'gross_positive_work_numeric':pos,'recovered_port_work_numeric':neg,'gross_positive_work_upper':str((b+net)/2),'read_energy_after2_numeric':Eread,'read_heat_over2_numeric':lossread},'physical_promotion':0}
(ROOT/'LOADED_OBSERVER_DATA.json').write_text(json.dumps(data,indent=2)+'\n')
result={'status':'PASS','exact_checks':sum(c['type']=='EXACT' for c in checks),'numerical_checks':sum(c['type']=='NUMERICAL' for c in checks),'checks':checks,'physical_promotion':0,'independent_review':'PENDING'}
(ROOT/'LOADED_OBSERVER_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}));print(json.dumps({'sigma_numeric':float(sv[-1]),'condition_number':float(sv[0]/sv[-1]),'uncertainty_A_Frob_bound':sqrt(float(Aerr2)),'uncertainty_C_Frob_bound':sqrt(float(Cerr2)),'uncertainty_G_bound':sqrt(float(Gerr2)),'net_write':str(net),'heat':{k:str(v) for k,v in loss_parts.items()},'gross_write':pos,'returned_write':neg,'gross_upper':str((b+net)/2),'retention':ret.tolist(),'read_heat':lossread}))
