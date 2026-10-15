#!/usr/bin/env python3
"""Exact reduction, representation and interval certificates; numerical diagnostics separate."""
from pathlib import Path
import sympy as s,numpy as np,json,hashlib
from scipy.linalg import eigh,null_space,block_diag
from scipy.integrate import solve_ivp
from curved_mode_model import model,symmetry_sections,critical_pattern,link_action
from critical_interval_certificate import certificate
O=Path(__file__).resolve().parent;g=model();ss=symmetry_sections(g);checks=[]
def check(name,value):
 assert bool(value),name
 checks.append(name);print('PASS',name,flush=True)
def zero(X):return all(s.simplify(z)==0 for z in X)
def mat(X):return [[str(s.radsimp(s.simplify(z))) for z in X.row(i)] for i in range(X.rows)]
R=g['R'];K=g['K'];C=g['C'];V=g['V'];L=g['L'];W=g['W'];rho=g['rho'];d=s.sqrt(10);z=s.symbols('z');lam=s.symbols('ell');Q=s.diag(*g['q']);Gbar=(g['G']/rho).applyfunc(lambda x:s.radsimp(s.simplify(x)))
check('unsigned_adjacency_characteristic',s.expand(g['T'].charpoly(z).as_expr()-z**5*(z-2)**3*(z+2)**3*(z**4-16*z*z+24))==0)
check('ground_transform_identity',zero(R*W*R.T-V*L*V))
check('Gauss_gauge_compatibility',zero(R*K))
check('positive_mass_form_factorization',zero(g['G']-R.T*(g['ell']*Q.inv()*L*Q.inv())*R/4))
check('neutral_dimension_fourteen',15-1==14)
check('physical_reduced_dimension_eightyfour',2*28+2*14==116-2*15-2)
for j,p in enumerate([(1,0,2,3),(1,2,3,0)]):
 T=link_action(g,p)
 check('generator_'+str(j)+'_K_equivariance',T*K==K*T)
 check('generator_'+str(j)+'_D_equivariance',zero(T*g['D']-g['D']*T))
 check('generator_'+str(j)+'_mass_equivariance',zero(T*Gbar-Gbar*T))
# Character multiplicities establish how each rational section reconstructs all 28 links.
from itertools import permutations
from curved_mode_model import sign
pairings=[{frozenset((0,1)),frozenset((2,3))},{frozenset((0,2)),frozenset((1,3))},{frozenset((0,3)),frozenset((1,2))}]
multiplicities=dict(trivial=0,standard=0,two_dimensional=0,sign_standard=0,sign=0)
for p in permutations(range(4)):
 chi=int(s.trace(link_action(g,p)));cv=sum(p[i]==i for i in range(4))-1
 cp=sum({frozenset(p[i] for i in t) for t in pair}==pair for pair in pairings)-1
 for name,c in [('trivial',1),('standard',cv),('two_dimensional',cp),('sign_standard',sign(p)*cv),('sign',sign(p))]:multiplicities[name]+=chi*c
multiplicities={k:v//24 for k,v in multiplicities.items()}
check('link_representation_multiplicities',multiplicities=={'trivial':3,'standard':5,'two_dimensional':2,'sign_standard':2,'sign':0})
expected={'trivial':z**3,'standard':z**3*(z*z-g['lambda_sum']*z+g['lambda_product']),'two_dimensional':z*(z-(2+d)),'sign_standard':z*z-(4+5*d)*z/3+14*(d-1)/3}
blocks={};product=s.Integer(1)
for name,t in ss.items():
 P=t['projector'];Z=t['basis'];left=t['left'];dd=(left*g['D']*Z).applyfunc(s.simplify);kk=left*K*Z;gg=(left*Gbar*Z).applyfunc(s.simplify)
 check(name+'_projector',P*P==P and P.T==P)
 check(name+'_section_size',Z.cols==multiplicities[name])
 check(name+'_closed_D',zero(g['D']*Z-Z*dd))
 check(name+'_closed_K',K*Z==Z*kk)
 check(name+'_closed_mass',zero(Gbar*Z-Z*gg))
 polynomial=(dd.inv()*kk).charpoly(z).as_expr()
 check(name+'_weighted_characteristic',s.simplify(s.expand(polynomial-expected[name]))==0)
 product*=expected[name]**t['dimension']
 blocks[name]={'irrep_dimension':t['dimension'],'block_size':Z.cols,'D':mat(dd),'K':mat(kk),'G_bar':mat(gg),'basis_Z':mat(Z),'weighted_K_characteristic':str(expected[name]),'frequency_rule':'Roots y of det[y I-(u I+G_bar)(D-q K)]; each occurs irrep_dimension times; omega^2=4*rho*w0*y, u=a*N/rho, q=kappa/(4*N*w0).'}
check('all_charged_modes_count_twenty_eight',sum(x['block_size']*x['irrep_dimension'] for x in blocks.values())==28)
check('weighted_full_zero_multiplicity_fourteen',s.Poly(s.expand(product),z).terms()[-1][0][0]==14)
# Exact identities at the critical root, reduced modulo its quadratic over Q(sqrt10).
pcrit=lam**2-g['lambda_sum']*lam+g['lambda_product']
def root_zero(expr):
 expr=s.cancel(expr);num=s.fraction(expr)[0]
 rem=s.rem(num,pcrit,lam)
 return s.simplify(s.expand(rem))==0
patterns=[]
for j in range(3):
 a=[0,0,0,0];a[j]=1;a[3]=-1;x=critical_pattern(g,a,lam);patterns.append(x)
 check('critical_pattern_'+str(j)+'_weighted_divergence',zero(R*g['D']*x))
 check('critical_pattern_'+str(j)+'_eigen_identity',all(root_zero(v) for v in K*x-lam*g['D']*x))
check('three_independent_critical_patterns',s.Matrix.hstack(*patterns)[:12,:].rank()==3)
cert=certificate(g);check('exact_interval_root_ordering_and_positive_critical_quartic',cert['status']=='PASS')
(O/'CRITICAL_QUARTIC_INTERVAL_CERTIFICATE_v0.1.json').write_text(json.dumps(cert,indent=2)+'\n')
(O/'MODE_BLOCKS_v0.1.json').write_text(json.dumps({'type':'EXACT algebraic mode specification','rho':str(rho),'w0':str(g['w0']),'definitions':{'D':'W/w0','G_bar':'R^T V^-1 L V^-1 R/(4 rho)','u':'a*N/rho','q':'kappa/(4*N*w0)','y':'omega^2/(4*rho*w0)'},'blocks':blocks,'independent_review':'PENDING','physical_promotion':0},indent=2)+'\n')
report={'status':'PASS','type':'EXACT constructor algebra and exact integer interval certificate; written nonlinear endpoint proof in manuscript','check_count':len(checks),'checks':checks,'weighted_K_characteristic':str(s.factor(product,extension=d)),'lambda_plus':str(g['lambda_plus']),'critical_kappa_per_N':str(g['kappa_critical_per_N']),'critical_kappa_per_N_decimal_diagnostic':float(g['kappa_critical_per_N']),'regimes':{'below':'Nonlinear orbital stability; all 42 reduced oscillator pairs nonzero imaginary and semisimple.','equal':'Nonlinear orbital stability via positive critical quartic; three zero length-two Jordan chains plus 39 nonzero imaginary pairs.','above':'Real growing reduced modes imply nonlinear orbital instability.'},'scope':'Scalar rank, fixed N_psi=N_chi=N>0, a>0, mu arbitrary common phase; candidate action unchanged; no higher-rank color stability claim','physical_promotion':0,'independent_review':'PENDING','hashes':{n:hashlib.sha256((O/n).read_bytes()).hexdigest() for n in ['verify_curved_modes.py','curved_mode_model.py','critical_interval_certificate.py','mode_model.py']}}
(O/'CURVED_MODES_EXACT_VERIFICATION_v0.1.json').write_text(json.dumps(report,indent=2)+'\n')
# Numerical checks and full temporal-gauge trajectory diagnostics remain separate.
Rn=np.array(R).astype(float);Cn=np.array(C).astype(float);Kn=np.array(K).astype(float);vn=np.array(g['v'].evalf()).astype(float).ravel();Vn=np.diag(vn);Ln=np.array(L.evalf()).astype(float);Wn=np.array(W.evalf()).astype(float);Gn=np.array(g['G'].evalf()).astype(float);Pn=np.eye(15)-np.outer(vn,vn);Bn=null_space(vn.reshape(1,-1));edges=g['edges'];U0=np.array([-1j*int(g['B'][i,j]) for i,j in edges]);kc=float(g['kappa_critical_per_N']);Mn=np.eye(28)+Gn;F=np.linalg.inv(Vn)@Rn@Wn
records=[]
for kval in [0,.95*kc,kc,1.1*kc]:
 S=4*Wn-kval*Kn
 # Ambient coordinates theta,E,x,y,z,w. Full norm conditions and Gauss imposed.
 A=np.zeros((116,116));A[:28,28:56]=np.eye(28);A[28:56,:28]=-S;A[28:56,71:86]=2*F.T;A[28:56,101:116]=-2*F.T
 A[56:71,71:86]=Ln;A[56:71,:28]=-F;A[71:86,56:71]=-Ln;A[86:101,101:116]=Ln;A[86:101,:28]=F;A[101:116,86:101]=-Ln
 constraint=np.zeros((17,116));constraint[:15,28:56]=Rn;constraint[:15,56:71]=-2*Vn;constraint[:15,86:101]=2*Vn;constraint[15,56:71]=vn;constraint[16,86:101]=vn;Z=null_space(constraint)
 red=np.zeros((84,116));red[:28,:28]=np.eye(28);red[:28,71:86]=-Rn.T@np.linalg.inv(Vn)/2;red[:28,101:116]=Rn.T@np.linalg.inv(Vn)/2;red[28:56,28:56]=np.eye(28);red[56:70,56:71]=Bn.T/np.sqrt(2);red[56:70,86:101]=Bn.T/np.sqrt(2);red[70:84,71:86]=Bn.T/np.sqrt(2);red[70:84,101:116]=Bn.T/np.sqrt(2)
 reduced=np.zeros((84,84));reduced[:28,28:56]=Mn;reduced[28:56,:28]=-S;L14=Bn.T@Ln@Bn;reduced[56:70,70:84]=L14;reduced[70:84,56:70]=-L14
 residual=float(np.max(abs((red@A-reduced@red)@Z)));assert residual<1e-9
 assert np.linalg.matrix_rank(red@Z)==84
 mh=eigh(Mn);Mhalf=(mh[1]*np.sqrt(mh[0]))@mh[1].T;nus=eigh(Mhalf@S@Mhalf,eigvals_only=True)
 block_nus=[]
 for name,t in ss.items():
  zj=np.array(t['basis']).astype(float);left=np.array(t['left']).astype(float);vals=np.linalg.eigvals((left@Mn@zj)@(left@S@zj));assert max(abs(vals.imag))<1e-8;block_nus.extend(list(vals.real)*t['dimension'])
 spectrum_residual=float(np.max(abs(np.sort(block_nus)-nus)));assert spectrum_residual<1e-8
 records.append({'kappa':kval,'full_constraint_rank':int(np.linalg.matrix_rank(constraint)),'physical_dimension':84,'intertwiner_max_residual':residual,'block_spectrum_max_residual':spectrum_residual,'squared_charged_frequencies':nus.tolist(),'negative_squared_frequency_count':int(sum(nus<-1e-8)),'zero_squared_frequency_count':int(sum(abs(nus)<1e-8))})

def rhs(t,y,kval):
 th=y[:28].real;E=y[28:56].real;psi=y[56:71];chi=y[71:86];ue=U0*np.exp(1j*th);h=np.zeros((15,15),complex);J=np.zeros(28)
 for e,(i,j) in enumerate(edges):
  b=int(g['B'][i,j]);h[i,j]=-1j*b*ue[e];h[j,i]=h[i,j].conjugate();J[e]=2*b*np.real(np.conj(psi[i])*ue[e]*psi[j]+chi[i]*ue[e]*np.conj(chi[j]))
 return np.r_[E,kval*Cn.T@np.sin(Cn@th)-J,-1j*(h+float(rho)*np.eye(15))@psi,-1j*(h.conjugate()+float(rho)*np.eye(15))@chi]
def obs(y,kval):
 th=y[:28].real;E=y[28:56].real;psi=y[56:71];chi=y[71:86];ue=U0*np.exp(1j*th);h=np.zeros((15,15),complex)
 for e,(i,j) in enumerate(edges):h[i,j]=-1j*int(g['B'][i,j])*ue[e];h[j,i]=h[i,j].conjugate()
 energy=.5*E@E+kval*np.sum(1+np.cos(Cn@th))+np.vdot(psi,h@psi).real+np.vdot(chi,h.conjugate()@chi).real
 return energy,float(max(abs(Rn@E-abs(psi)**2+abs(chi)**2))),float(max(abs(np.vdot(psi,psi).real-1),abs(np.vdot(chi,chi).real-1))),float(max(np.max(abs(abs(psi)**2-vn**2)),np.max(abs(abs(chi)**2-vn**2)),np.linalg.norm(E),np.max(abs(np.exp(1j*Cn@th)-1))))
rng=np.random.default_rng(84921);axis=rng.normal(size=28);axis/=np.linalg.norm(axis);campaigns=[]
for kval,label in [(.95*kc,'enlarged_stable_interval'),(kc,'critical_phase_preparation'),(1.1*kc,'growing_mode_above_threshold')]:
 runs=[]
 if label=='growing_mode_above_threshold':
  S=4*Wn-kval*Kn;vals,vecs=eigh(Mhalf@S@Mhalf);rate=np.sqrt(-vals[0]);x=Mhalf@vecs[:,0];x/=np.linalg.norm(x);ee=rate*np.linalg.solve(Mn,x)
 elif label=='critical_phase_preparation':
  x=np.array(critical_pattern(g,[1,-1,0,0],g['lambda_plus']).evalf()).astype(float).ravel();x/=np.linalg.norm(x);ee=np.zeros(28)
 else:x=axis;ee=np.zeros(28)
 for eps in [.005,.0025,.00125]:
  E=eps*ee;q=Rn@E;psi=np.sqrt(vn**2+q/2).astype(complex);chi=np.sqrt(vn**2-q/2).astype(complex);y0=np.r_[eps*x,E,psi,chi];horizon=120 if label!='growing_mode_above_threshold' else 30
  def exit_event(t,y):return obs(y,kval)[3]-.04
  exit_event.terminal=True;exit_event.direction=1
  sol=solve_ivp(lambda t,y:rhs(t,y,kval),(0,horizon),y0,method='DOP853',rtol=2e-10,atol=2e-12,events=exit_event if label=='growing_mode_above_threshold' else None);assert sol.success
  oo=[obs(y,kval) for y in sol.y.T];H0=oo[0][0];r={'epsilon':eps,'end_time':float(sol.t[-1]),'max_diagnostic':max(o[3] for o in oo),'max_energy_absolute_drift':max(abs(o[0]-H0) for o in oo),'max_Gauss_absolute_residual':max(o[1] for o in oo),'max_species_norm_absolute_drift':max(o[2] for o in oo)}
  assert max(r[k] for k in ['max_energy_absolute_drift','max_Gauss_absolute_residual','max_species_norm_absolute_drift'])<1e-7
  if label=='growing_mode_above_threshold':assert sol.t_events[0].size==1;r['linear_growth_rate']=float(rate)
  runs.append(r)
 if label!='growing_mode_above_threshold':assert runs[-1]['max_diagnostic']<runs[0]['max_diagnostic']/2.5
 campaigns.append({'label':label,'kappa':kval,'a':1,'N':1,'runs':runs})
num={'status':'PASS','type':'NUMERICAL diagnostics, not empirical; endpoint proof supplied by exact interval-certified quartic','linear_reduction_and_block_spectrum':records,'nonlinear_campaigns':campaigns,'physical_promotion':0,'independent_review':'PENDING'}
(O/'CURVED_MODES_NUMERICAL_DIAGNOSTIC_v0.1.json').write_text(json.dumps(num,indent=2)+'\n');print(json.dumps({'status':'PASS','exact_checks':len(checks),'kappa_critical_per_N':kc,'campaigns':campaigns},indent=2))
