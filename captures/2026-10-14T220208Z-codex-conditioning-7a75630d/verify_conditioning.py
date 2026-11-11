from pathlib import Path
import json,math,hashlib
import sympy as s
import numpy as np
from scipy.linalg import expm
from scipy.stats import chi2

root=Path(__file__).resolve().parent
source=root/'baseline'
x=s.symbols('x');tau=s.Rational(1,2);results={};matrices={}
for name in ['two_face','five_star','five_chain']:
 d=json.loads((source/f'{name}_certificate.json').read_text());A=s.Matrix(d['copy_generator']);E=s.Matrix(d['aggregation']);nu=[sum(E[i,:]) for i in range(E.rows)]
 P=E.T*s.diag(*[1/s.Integer(t) for t in nu])*E;H=P+tau*tau*A.T*P*A
 cp=s.factor(H.charpoly(x).as_expr());eig=np.linalg.eigvalsh(np.array(H.tolist(),float));lam=float(eig[0])
 if name=='two_face':
  expected=(x-2)**14*(x-1)*(4*x-7)*(4*x*x-8*x+1)**7/s.Integer(65536)
  assert s.expand(cp-expected)==0
  exact_min=1-s.sqrt(3)/2;gain=1+s.sqrt(3)
  assert s.simplify(gain**2*exact_min)==1
 elif name=='five_star':
  # Exact factor-root check: every displayed quadratic has roots 1 +- sqrt(1-c/a).
  exact_min=1-s.sqrt(15)/4;gain=s.sqrt(2)*(s.sqrt(5)+s.sqrt(3))
  assert s.simplify(gain**2*exact_min)==1
  for factor,mult in s.factor_list(cp)[1]:
   if s.degree(factor,x)==1:
    assert s.solve(factor,x)[0]>=exact_min
   elif s.degree(factor,x)==2:
    assert s.simplify(factor.coeff(x)+2*factor.coeff(x,2))==0
    a0=factor.coeff(x,2);c0=factor.coeff(x,0)
    assert c0/a0>=s.Rational(1,16)
   else:raise AssertionError('unexpected factor')
 else:exact_min=None;gain=None
 lo={'two_face':s.Rational(13,100),'five_star':s.Rational(31,1000),'five_chain':s.Rational(241,10000)}[name]
 L,D=(H-lo*s.eye(A.rows)).LDLdecomposition()
 assert all(D[i,i]>0 for i in range(A.rows))
 assert L*D*L.T==H-lo*s.eye(A.rows)
 if name=='five_chain':
  hi=s.Rational(243,10000);sq=s.Poly(cp,x).sqf_part();assert s.polys.polytools.count_roots(sq,0,lo)==0 and s.polys.polytools.count_roots(sq,lo,hi)==1
  factor=64*x**4-256*x**3+280*x*x-48*x+1
  assert s.rem(s.Poly(cp,x),s.Poly(factor,x)).is_zero
  assert s.polys.polytools.count_roots(factor,lo,hi)==1
 Q=np.diag([1/math.sqrt(float(t)) for t in nu])@np.array(E.tolist(),float);An=np.array(A.tolist(),float)
 M=np.vstack([Q,.5*Q@An]);u,sv,vt=np.linalg.svd(M,full_matrices=False)
 eps=.01;e=eps*u[:,-1];err=np.linalg.pinv(M)@e
 assert abs(np.linalg.norm(err)-eps/sv[-1])<1e-11
 assert np.linalg.norm(An@An@An+4*An)<1e-12
 # Exact sampled derivative versus a direct matrix exponential; no derivative-free assumption.
 for h in [.01,.2,math.pi/4]:
  Bh=Q@(expm(h*An)-expm(-h*An))/(2*h)
  f=math.sin(2*h)/(2*h)
  assert np.linalg.norm(Bh-f*Q@An,2)<1e-12
  I1=Q.T@Q+2*h*h*Bh.T@Bh
  I2=np.array(P.tolist(),float)+(math.sin(2*h)**2/2)*An.T@np.array(P.tolist(),float)@An
  assert np.linalg.norm(I1-I2,2)<1e-12
  assert np.linalg.eigvalsh(np.array(P.tolist(),float)+.5*An.T@np.array(P.tolist(),float)@An-I1)[0]>-1e-12
 results[name]={'state_dimension':A.rows,'visible_dimension':E.rows,'tau':'1/2',
  'minimum_gram_eigenvalue_exact':str(exact_min) if exact_min is not None else 'smallest root of 64x^4-256x^3+280x^2-48x+1',
  'minimum_gram_eigenvalue_numeric':lam,'absolute_noise_gain_exact':str(gain) if gain is not None else None,
  'absolute_noise_gain_numeric':1/math.sqrt(lam),'condition_number_numeric':math.sqrt(float(eig[-1])/lam),
  'certified_gram_lower_bound':str(lo),'ldl_positive_pivots':A.rows,
  'characteristic_polynomial':str(cp),'sharp_noise_witness':'PASS',
  'centered_difference_and_retained_fisher_checks':'PASS'}
 matrices[name]={'A':An,'Q':Q,'M':M,'P':np.array(P.tolist(),float)}
 (root/f'{name}_conditioning_certificate.json').write_text(json.dumps({'gram':H.tolist(),'lower_bound':str(lo),'ldl_pivots':[str(D[i,i]) for i in range(A.rows)],'characteristic_polynomial':str(cp)},default=str,indent=2)+'\n')

# Nonuniform scaling alone cannot improve information if covariance is transported.
d=matrices['two_face'];M=d['M'];N=M.shape[0];n=M.shape[1]
Sigma=np.eye(N);Sigma[0,1]=Sigma[1,0]=.3
S=np.diag([1.]*d['Q'].shape[0]+[7.]*d['Q'].shape[0])
I=M.T@np.linalg.solve(Sigma,M);Is=(S@M).T@np.linalg.solve(S@Sigma@S.T,S@M)
assert np.linalg.norm(I-Is,2)<1e-12
GLS=np.linalg.solve(I,M.T@np.linalg.inv(Sigma));C=np.linalg.inv(I)
assert np.linalg.norm(GLS@Sigma@GLS.T-C,2)<1e-11
assert np.linalg.norm(GLS@M-np.eye(n),2)<1e-11

# A fixed norm-two family can still make the snapshot/derivative readout singular.
data=json.loads((source/'two_face_certificate.json').read_text());base=s.Matrix(data['copy_generator']);E=s.Matrix(data['aggregation']);
flat=[f for k in range(1,5) for f in __import__('itertools').combinations((0,1,2,3),k)]+[f for k in range(1,5) for f in __import__('itertools').combinations((0,1,2,4),k)]
hvec=np.zeros(30);hvec[flat.index((0,1,2))]=1/math.sqrt(2);hvec[15+flat[15:].index((0,1,2))]=-1/math.sqrt(2)
family=[]
for small in [1.,.1,.01]:
 A=np.array(base.tolist(),float)
 for off in (0,15):A[off+10:off+14,off+14]*=small;A[off+14,off+10:off+14]*=small
 Q=d['Q'];Mt=np.vstack([Q,.5*Q@A]);witness=np.linalg.norm(Mt@hvec)
 assert abs(witness-.5*small)<1e-12
 assert abs(np.linalg.norm(A,2)-2)<1e-12
 family.append({'cell_exchange_weight':small,'min_singular_value_numeric':float(np.linalg.svd(Mt,compute_uv=False)[-1]),'certified_upper_bound':small/2})

# A declared small generator mismatch obeys the full-state reconstruction bound.
v=np.arange(1,31,dtype=float);v/=np.linalg.norm(v);Dg=np.zeros((30,30));Dg[0,1]=.001;Dg[1,0]=-.001
Mbar=np.vstack([d['Q'],.5*d['Q']@(d['A']+Dg)]);gamma=np.linalg.svd(Mbar,compute_uv=False)[-1]
eh=np.linalg.pinv(Mbar)@(d['M']@v)-v
assert np.linalg.norm(eh)<=.5*np.linalg.norm(Dg,2)/gamma+1e-12
# Finite precision, jitter and centered-remainder witnesses in the declared model.
q=.01;jitter=.001;signal=d['Q']@v;rounded=np.round(signal/q)*q
assert np.linalg.norm(rounded-signal)<=math.sqrt(len(signal))*q/2+1e-12
assert np.linalg.norm(d['Q']@(expm(jitter*d['A'])@v-v))<=2*jitter+1e-12
h=.02;noise=.001*np.ones(len(signal))/math.sqrt(len(signal))
Dh=(d['Q']@expm(h*d['A'])@v+noise-d['Q']@expm(-h*d['A'])@v+noise)/(2*h)
assert np.linalg.norm(Dh-d['Q']@d['A']@v)<=.001/h+8*h*h/6+1e-12
report={'status':'PASS','models':results,'coordinate_covariance_invariance':'PASS','GLS_covariance_identity':'PASS',
 'fixed_norm_ill_conditioning_family':family,'generator_mismatch':'PASS','quantization_jitter_and_difference_remainder':'PASS',
 'gaussian_95_percent_radius_for_two_cell_whitened_model':math.sqrt(chi2.ppf(.95,30)/np.linalg.eigvalsh(I)[0]),
 'scope':'exact spectra/LDL/Sturm certificates and separate floating fixtures; no empirical noise or physical cost',
 'physical_promotion':0}
(root/'CONDITIONING_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
