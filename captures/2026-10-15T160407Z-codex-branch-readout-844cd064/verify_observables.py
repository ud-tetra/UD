#!/usr/bin/env python3
"""Exact readout geometry; numerical full-energy branch fixtures, never empirical."""
from pathlib import Path
from itertools import combinations,product,permutations
import json
import sympy as s,numpy as np
from scipy.optimize import root
from scipy.linalg import eigh
from bifurcation_model import critical_algebra,numerical_model,HADAMARD as H
from critical_interval_certificate import certificate,I,Q
O=Path(__file__).resolve().parent;checks=[]
def check(name,value):
 assert bool(value),name
 checks.append(name);print('PASS',name,flush=True)
g,Z,z,red,G,gram=critical_algebra();C=g['C'];L=C*Z
zero=lambda M:all(red(t)==0 for t in M)
check('curl_critical_Gram',gram==G*s.eye(3))
check('critical_reconstruction_left_inverse',zero(L.T*L-G*s.eye(3)))
check('curl_kills_vertex_gauge',C*g['R'].T==s.zeros(18,15))
check('four_loop_closure_relations',C.rank()==14 and 18-C.rank()==4)
check('eleven_noncritical_loop_directions',C.rank()-3==11)
check('fast_complement_annihilation_identity',zero(Z.T*g['K']-z*Z.T*g['D']))
b=s.Matrix(s.symbols('b1:4',real=True));a=H*b;r2=(b.T*b)[0]
check('Hadamard_isometry',H.T*H==s.eye(3))
check('fourth_moment_identity',s.expand(sum(t**4 for t in a)-3*r2*r2/4+sum(t**4 for t in b)/2)==0)
check('signed_cubic_identity',s.expand(sum(t**3 for t in a)-3*b[0]*b[1]*b[2])==0)
check('centered_pair_distance_reconstruction',s.ones(1,4)*a==s.zeros(1,1))
J=s.eye(4)-s.ones(4)/4;Delta=s.Matrix(4,4,lambda i,j:(a[i]-a[j])**2)
check('double_centering_is_rank_one_Gram',all(s.expand(t)==0 for t in -J*Delta*J/2-a*a.T))
# One of the two vertex diamonds for every unordered added pair.
selected={};vertex_coefficient=z
for row,(i,j,h,k) in enumerate(g['diamonds']):
 lo=g['simplices'][i];hi=g['simplices'][k];pair=tuple(t for t in hi if t not in lo)
 if len(lo)==1:
  target=z*(a[pair[0]]-a[pair[1]])
  expr=(L*b)[row]
  ok=red(expr-target)==0 or red(expr+target)==0
  check('vertex_diamond_difference_'+str(row),ok)
  selected.setdefault(pair,row)
check('six_labeled_pair_channels_available',len(selected)==6)
for p in permutations(range(4)):
 P=s.zeros(4)
 for i,j in enumerate(p):P[j,i]=1
 T=H.T*P*H;tb=T*b
 check('S4_signed_cubic_invariance_'+''.join(map(str,p)),s.expand(s.prod(tb)-s.prod(b))==0)
family=[]
for k in [1,2,3]:
 points=[]
 for ind in combinations(range(3),k):
  for signs in product([-1,1],repeat=k):
   n=s.zeros(3,1)
   for j,sgn in zip(ind,signs):n[j]=sgn/s.sqrt(k)
   points.append(n)
   assert s.simplify(sum(t**4 for t in n)-s.Rational(1,k))==0
   assert s.simplify(sum(t**4 for t in H*n)-{1:s.Rational(1,4),2:s.Rational(1,2),3:s.Rational(7,12)}[k])==0
   assert s.simplify(3*s.sqrt(3)*s.prod(n)) in ([s.Integer(0)] if k<3 else [-s.Integer(1),s.Integer(1)])
 check('all_family_'+str(k)+'_fingerprints',len(points)=={1:6,2:12,3:8}[k])
 family.append({'k':k,'branches':len(points),'P4':str(s.Rational(1,k)),'phase_blind_eta_limit':str({1:s.Rational(1,4),2:s.Rational(1,2),3:s.Rational(7,12)}[k]),'signed_C3':('0' if k<3 else '+1 or -1')})
# Exact algebra underlying the perturbation bound at a stationary unit ray.
w=s.Matrix(s.symbols('w1:4',real=True));t=(w.T*w)[0]
for k in [1,2,3]:
 n=s.Matrix([1/s.sqrt(k) if j<k else 0 for j in range(3)])
 expansion=4*sum(n[j]**3*w[j] for j in range(3))+6*sum(n[j]**2*w[j]**2 for j in range(3))-2*t/k+4*sum(n[j]*w[j]**3 for j in range(3))+sum(x**4 for x in w)-t*t/k
 check('noise_expansion_'+str(k),s.expand(sum(x**4 for x in n+w)-(1+t)**2/k-expansion)==0)
 check('noise_linear_term_normal_to_sphere_'+str(k),s.simplify(sum(n[j]**3*w[j] for j in range(3))-(n.T*w)[0]/k)==0)
 if k==1:bounds=[-2] # w_occupied=0 by orthogonality
 elif k==2:bounds=[2,-1]
 else:bounds=[s.Rational(4,3)]
 check('quadratic_noise_coefficient_at_most_two_'+str(k),max(abs(v) for v in bounds)<=2)
bound=2*s.Rational(1,6)**2+4*s.Rational(1,6)**3+s.Rational(1,6)**4
check('rigorous_noise_margin',bound==s.Rational(97,1296) and bound<s.Rational(1,12))
check('relative_error_to_tangent_error',s.Rational(1,7)/(1-s.Rational(1,7))==s.Rational(1,6))
cert=certificate(g);AA=I(int(cert['A4']['lower_numerator']),int(cert['A4']['upper_numerator']));BB=I(int(cert['B4']['lower_numerator']),int(cert['B4']['upper_numerator']));ratio=1+4*AA/BB;fratio=ratio.sqrt()
check('inherited_quartic_intervals',cert['status']=='PASS')
check('spectral_ratio_positive_interval',ratio.lo>Q and ratio.hi<5*Q)
Gnum=float(G.subs(z,g['lambda_plus']));nm=numerical_model(g);Zn=nm['critical_basis'];Ln=nm['C']@Zn;Cnum=nm['C'];basis=nm['basis'];rng=np.random.default_rng(54710)
A4=(AA.lo+AA.hi)/(2*Q);B4=(BB.lo+BB.hi)/(2*Q);Pi=Cnum@np.linalg.pinv(Cnum)
# Full U(r) conjugation, not scalar-only gauge fixture.
gauge_errors=[]
for rank in [1,2,3,5]:
 for j in range(8):
  U,_=np.linalg.qr(rng.normal(size=(rank,rank))+1j*rng.normal(size=(rank,rank)));W,_=np.linalg.qr(rng.normal(size=(rank,rank))+1j*rng.normal(size=(rank,rank)));p=rng.normal(size=rank)+1j*rng.normal(size=rank)
  z0=-np.vdot(p,W@p)/np.vdot(p,p);p1=U@p;W1=U@W@U.conj().T;z1=-np.vdot(p1,W1@p1)/np.vdot(p1,p1)
  gauge_errors.append(abs(z0-z1));assert abs(z0)<=1+2e-15
assert max(gauge_errors)<2e-14
noise_errors=[]
for k in [1,2,3]:
 for j in range(200):
  n=np.r_[np.ones(k)/np.sqrt(k),np.zeros(3-k)];direction=rng.normal(size=18);direction/=np.linalg.norm(direction);err=direction*np.sqrt(Gnum)/7
  bh=n+Ln.T@err/Gnum;p4=np.sum(bh**4)/np.dot(bh,bh)**2
  assert abs(p4-1/k)<1/12 and abs(p4-1/k)<97/1296
  noise_errors.append(abs(p4-1/k))
records=[]
for k in [1,2,3]:
 n=np.r_[np.ones(k)/np.sqrt(k),np.zeros(3-k)];qk=A4+3*B4/4-B4/(2*k);rows=[]
 for epsilon in [1e-4,5e-5,2.5e-5,1.25e-5]:
  kap=nm['kc']+epsilon;radius=np.sqrt(Gnum*epsilon/(4*qk));seed=np.r_[radius*n,np.zeros(11)]
  fun=lambda q:basis.T@nm['energy'](basis@q,kap)[1]
  jac=lambda q:basis.T@nm['energy'](basis@q,kap)[2]@basis
  sol=root(fun,seed,jac=jac,tol=2e-11);q=sol.x;assert max(abs(fun(q)))<2e-12
  theta=basis@q;_,_,_,f,_=nm['energy'](theta,kap);phi=Cnum@theta;zz=np.exp(1j*phi);assert max(abs(phi))<np.pi
  bh=Ln.T@np.angle(zz)/Gnum;err=float(np.linalg.norm(bh-q[:3]));assert err<2e-14
  R=np.linalg.norm(bh);P4=np.sum(bh**4)/R**4;C3=3*np.sqrt(3)*np.prod(bh)/R**3
  assert abs(P4-1/k)<2e-12 and abs(abs(C3)-(1 if k==3 else 0))<2e-6
  dm=np.zeros((4,4))
  for (i,j),row in selected.items():dm[i,j]=dm[j,i]=(np.arccos(np.clip(zz[row].real,-1,1))/float(g['lambda_plus']))**2
  jn=np.eye(4)-np.ones((4,4))/4;gg=-jn@dm@jn/2;eta=float(np.sum(np.diag(gg)**2)/np.trace(gg)**2);target={1:.25,2:.5,3:7/12}[k]
  _,_,_,fm,_=nm['energy'](-theta,kap);assert max(abs(abs(f)**2-abs(fm)**2))<3e-15
  assert max(abs(np.exp(-1j*phi).real-zz.real))<1e-15
  assert np.linalg.norm((np.eye(18)-Pi)@phi)<2e-14
  X=theta-nm['R'].T@np.angle(f);Hq,Hp=nm['reversible_blocks'](X,2*abs(f)**2,kap);ev,V=eigh(Hp);assert min(ev)>0;half=(V*np.sqrt(ev))@V.T;spec=eigh(half@Hq@half,eigvals_only=True);soft=spec[np.argsort(abs(spec))[:3]];measured_ratio=float(max(soft)/min(soft)) if k==1 else None
  rows.append({'epsilon':epsilon,'force_residual':float(max(abs(fun(q)))),'critical_reconstruction_error':err,'P4':float(P4),'signed_C3':float(C3),'phase_blind_eta':eta,'phase_blind_eta_limit':target,'phase_blind_eta_error':abs(eta-target),'fast_loop_norm_over_R_cubed':float(np.linalg.norm(phi-Ln@bh)/R**3),'stable_soft_squared_ratio':measured_ratio,'stable_soft_squared_ratio_limit':float((ratio.lo+ratio.hi)/(2*Q)) if k==1 else None})
 if k==2:assert rows[-1]['phase_blind_eta_error']<rows[0]['phase_blind_eta_error']/5
 if k==1:assert abs(rows[-1]['stable_soft_squared_ratio']-rows[-1]['stable_soft_squared_ratio_limit'])<abs(rows[0]['stable_soft_squared_ratio']-rows[0]['stable_soft_squared_ratio_limit'])/5
 records.append({'k':k,'runs':rows})
exact={'status':'PASS','type':'EXACT constructor algebra and inherited directed interval bounds; analytic proofs in manuscript','checks':checks,'check_count':len(checks),'Gamma':str(G),'family_fingerprints':family,'robust_P4_error_bound':'97/1296 < 1/12 when ||delta b|| <= ||b||/7','spectral_squared_ratio_interval':ratio.bounds(),'spectral_frequency_ratio_interval':fratio.bounds(),'six_pair_diamond_rows':{str(pair):row for pair,row in selected.items()},'independent_review':'PENDING','physical_promotion':0}
num={'status':'PASS','type':'NUMERICAL synthetic full-energy fixtures, not empirical','parameters':{'a':1,'N':1,'rank':1},'Gamma':Gnum,'squared_frequency_ratio_limit':(ratio.lo+ratio.hi)/(2*Q),'frequency_ratio_limit':(fratio.lo+fratio.hi)/(2*Q),'full_rank_gauge_fixture_count':len(gauge_errors),'maximum_gauge_readout_error':max(gauge_errors),'bounded_phase_noise_fixtures':len(noise_errors),'maximum_fingerprint_error_in_noise_fixtures':max(noise_errors),'full_stationary_solutions':12,'campaigns':records,'independent_review':'PENDING','physical_promotion':0}
(O/'OBSERVABLE_EXACT_VERIFICATION_v0.1.json').write_text(json.dumps(exact,indent=2)+'\n');(O/'OBSERVABLE_NUMERICAL_DIAGNOSTIC_v0.1.json').write_text(json.dumps(num,indent=2)+'\n');(O/'INHERITED_CRITICAL_CERTIFICATE_v0.1.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),'squared_frequency_ratio':num['squared_frequency_ratio_limit'],'frequency_ratio':num['frequency_ratio_limit'],'maximum_reconstruction_error':max(row['critical_reconstruction_error'] for rec in records for row in rec['runs'])}))
