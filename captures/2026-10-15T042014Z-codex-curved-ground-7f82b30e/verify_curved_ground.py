#!/usr/bin/env python3
"""Constructor algebra and separately typed diagnostics for the CGS theorem."""
from pathlib import Path
import sympy as s
import numpy as np
from scipy.integrate import solve_ivp
import json,hashlib
from mode_model import graph
O=Path(__file__).resolve().parent;g=graph();B=g['B'];R=g['R'];C=g['C'];K=g['K'];edges=g['edges'];checks=[]
def zero(X):return all(s.simplify(v)==0 for v in X)
def check(name,ok):
 assert bool(ok),name
 checks.append(name);print('PASS',name,flush=True)
rho=s.sqrt(8+2*s.sqrt(10));L=16*(10+s.sqrt(10))/9
ratios=[s.Integer(1),rho/3,(1+s.sqrt(10))/3,4*(1+s.sqrt(10))/(3*rho)]
v=s.Matrix([ratios[len(t)-1]/s.sqrt(L) for t in g['simplices']]);T=s.zeros(15);U=[]
for e,(i,j) in enumerate(edges):T[i,j]=T[j,i]=1;U.append(-s.I*B[i,j])
D=s.zeros(15)
for e,(i,j) in enumerate(edges):D[i,j]=B[i,j]*U[e]
h=s.I*(D.H-D)
z=s.symbols('lambda')
check('unsigned_graph_characteristic',s.expand(T.charpoly().as_expr()-z**5*(z-2)**3*(z+2)**3*(z**4-16*z*z+24))==0)
# Actual complete factorization is recorded; Perron certification uses strictly positive v.
char=s.factor(T.charpoly().as_expr())
check('Perron_eigenvector',zero(T*v-rho*v))
check('Perron_normalization',s.simplify((v.T*v)[0]-1)==0)
check('Perron_strict_positivity',all(x.is_positive for x in ratios) and L.is_positive)
check('rho_characteristic_equation',s.simplify(rho**4-16*rho**2+24)==0)
check('twisted_h_equals_negative_adjacency',h==-T)
check('antifundamental_h_is_same_real_matrix',s.conjugate(h)==h)
for d in range(18):
 w=s.prod(U[e]**int(C[d,e]) for e in range(28) if C[d,e])
 check('diamond_minus_identity_'+str(d),s.simplify(w+1)==0)
check('pointwise_neutral_stationary_seed',zero(v.multiply_elementwise(v)-s.conjugate(v).multiply_elementwise(v)))
J=s.Matrix([2*B[i,j]*s.re(s.conjugate(v[i])*U[e]*v[j]+v[i]*U[e]*s.conjugate(v[j])) for e,(i,j) in enumerate(edges)])
check('matter_force_vanishes_at_seed',zero(J))
check('magnetic_force_vanishes_at_seed',zero(C.T*s.zeros(18,1)))
weights=s.diag(*[v[i]*v[j] for i,j in edges]);wmin=rho*(10-s.sqrt(10))/480
check('minimum_edge_weight_formula',s.simplify(v[0]*v[4]-wmin)==0)
check('level_weights_exceed_vertex_edge',ratios[1].is_positive and s.simplify(ratios[2]-1).is_positive and s.simplify(ratios[3]-1).is_positive and s.simplify(ratios[1]-1).is_positive)
Lw=R*weights*R.T;V=s.diag(*v)
check('ground_state_transform_matrix',zero(V.inv()*Lw*V.inv()-(rho*s.eye(15)-T)))
check('amplitude_form_only_constant_kernel',Lw.rank()==14 and Lw*s.ones(15,1)==s.zeros(15,1))
check('diamond_curl_kills_gauge_gradients',C*R.T==s.zeros(18,15))
kchar=s.factor(K.charpoly().as_expr());z=s.symbols('lambda')
check('exact_stiffness_spectrum',s.expand(kchar-z**14*(z-6)**2*(z*z-12*z+34)**3*(z*z-8*z+14)**3)==0)
check('stiffness_maximum_ordering',s.simplify(6+s.sqrt(2)-(4+s.sqrt(2)))==2 and s.sqrt(2).is_positive)
# Phase form: beta=eta+zeta, gamma=-eta+zeta, x=theta-R^T eta.
xb,gb,th=s.symbols('xb gb th',real=True);eta,zeta=s.symbols('eta zeta',real=True)
check('two_species_phase_quadratic_decomposition',s.expand(((eta+zeta)-th)**2+((-eta+zeta)+th)**2-2*((th-eta)**2+zeta**2))==0)
check('quadratic_phase_kernel_dimension',s.Matrix.vstack(s.Matrix.hstack(-R.T,s.eye(28),s.zeros(28,15)),s.Matrix.hstack(s.zeros(28,15),s.zeros(28),R.T)).rank()==42)
# Rational phase fixture for the universal ground transform, f arbitrary complex.
phases=[s.Integer(1),(3+4*s.I)/5,(-5+12*s.I)/13,s.I];u=[phases[e%4] for e in range(28)];f=s.Matrix([s.Rational(i+1,17)+s.I*s.Rational(i%3,11) for i in range(15)])
ht=s.zeros(15)
for e,(i,j) in enumerate(edges):ht[i,j]=-u[e];ht[j,i]=-s.conjugate(u[e])
Ltw=s.diag(*[Lw[i,i] for i in range(15)])
for e,(i,j) in enumerate(edges):Ltw[i,j]=-weights[e,e]*u[e];Ltw[j,i]=-weights[e,e]*s.conjugate(u[e])
check('nonlinear_ground_transform_unit_phase_fixture',zero(V.inv()*Ltw*V.inv()-(rho*s.eye(15)+ht)))
N,kappa=s.symbols('N kappa',positive=True);safe=4*N*wmin/(6+s.sqrt(2));curved=N*(rho-2)/18
check('positive_stability_interval',safe.is_positive)
check('curved_trial_beats_flat_at_half_cutoff',s.simplify(-2*rho*N+36*curved/2+4*N).is_negative)
report={'status':'PASS','type':'EXACT constructor algebra; universal variational and Lyapunov arguments in manuscript','check_count':len(checks),'checks':checks,'unsigned_graph_characteristic':str(char),'rho':str(rho),'Perron_level_ratios':[str(x) for x in ratios],'Perron_normalization_L':str(L),'minimum_edge_weight':str(wmin),'safe_scalar_kappa_per_N':str(safe/N),'safe_scalar_kappa_per_N_decimal_diagnostic':float(safe/N),'nonflat_ground_set_kappa_per_rN_bound':str(curved/N),'physical_promotion':0,'independent_review':'PENDING','verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'graph_sha256':hashlib.sha256((O/'mode_model.py').read_bytes()).hexdigest()}
(O/'CURVED_GROUND_EXACT_VERIFICATION_v0.1.json').write_text(json.dumps(report,indent=2)+'\n')
# Full unreduced temporal-gauge dynamics, both species. No stability projected into RHS.
Rn=np.array(R).astype(float);Cn=np.array(C).astype(float);vn=np.array(v.evalf()).astype(float).ravel();Un=np.array(U).astype(complex).ravel();bn=np.array([int(B[i,j]) for i,j in edges]);rho_n=float(rho);safe_n=float(safe/N)
def rhs(t,y,kappa):
 theta=y[:28].real;E=y[28:56].real;psi=y[56:71];chi=y[71:86];ue=Un*np.exp(1j*theta);hh=np.zeros((15,15),complex);J=np.zeros(28)
 for e,(i,j) in enumerate(edges):
  hh[i,j]=-1j*bn[e]*ue[e];hh[j,i]=hh[i,j].conjugate()
  J[e]=2*bn[e]*np.real(np.conj(psi[i])*ue[e]*psi[j]+chi[i]*ue[e]*np.conj(chi[j]))
 # All reference diamond phases are pi.
 return np.r_[E,kappa*Cn.T@np.sin(Cn@theta)-J,-1j*(hh+rho_n*np.eye(15))@psi,-1j*(hh.conjugate()+rho_n*np.eye(15))@chi]
def obs(y,kappa):
 theta=y[:28].real;E=y[28:56].real;psi=y[56:71];chi=y[71:86];ue=Un*np.exp(1j*theta);hh=np.zeros((15,15),complex)
 for e,(i,j) in enumerate(edges):hh[i,j]=-1j*bn[e]*ue[e];hh[j,i]=hh[i,j].conjugate()
 H=.5*E@E+kappa*np.sum(1+np.cos(Cn@theta))+np.vdot(psi,hh@psi).real+np.vdot(chi,hh.conjugate()@chi).real
 gauss=Rn@E-abs(psi)**2+abs(chi)**2
 # Gauge/phase invariant departure diagnostics, not a complete orbit-distance estimator.
 diag=max(np.max(abs(abs(psi)**2-vn**2)),np.max(abs(abs(chi)**2-vn**2)),np.linalg.norm(E),np.max(abs(np.exp(1j*Cn@theta)-1)))
 return H,np.vdot(psi,psi).real,np.vdot(chi,chi).real,np.max(abs(gauss)),diag
rng=np.random.default_rng(347810);theta_dir=rng.normal(size=28);theta_dir/=np.linalg.norm(theta_dir);matter_dir=rng.normal(size=15)+1j*rng.normal(size=15);matter_dir-=vn*np.vdot(vn,matter_dir);matter_dir/=np.linalg.norm(matter_dir)
campaigns=[]
for kval in [0,safe_n/2]:
 runs=[]
 for eps in [1e-2,5e-3,2.5e-3]:
  psi=vn+eps*matter_dir;psi/=np.linalg.norm(psi);chi=psi.conjugate();y0=np.r_[eps*theta_dir,np.zeros(28),psi,chi]
  sol=solve_ivp(lambda t,y:rhs(t,y,kval),(0,120),y0,method='DOP853',rtol=2e-10,atol=2e-12,t_eval=np.linspace(0,120,1201));assert sol.success
  oo=[obs(y,kval) for y in sol.y.T];H0=oo[0][0]
  row={'epsilon':eps,'time':120,'max_diagnostic':float(max(v[4] for v in oo)),'diagnostic_over_epsilon':float(max(v[4] for v in oo)/eps),'max_energy_absolute_drift':float(max(abs(v[0]-H0) for v in oo)),'max_norm_absolute_drift':float(max(max(abs(v[1]-1),abs(v[2]-1)) for v in oo)),'max_Gauss_absolute_residual':float(max(v[3] for v in oo))}
  assert row['max_energy_absolute_drift']<1e-7 and row['max_norm_absolute_drift']<1e-7 and row['max_Gauss_absolute_residual']<1e-7
  runs.append(row)
 assert runs[-1]['max_diagnostic']<runs[0]['max_diagnostic']/3
 campaigns.append({'kappa':kval,'N':1,'a':1,'runs':runs})
(O/'CURVED_GROUND_NUMERICAL_DIAGNOSTIC_v0.1.json').write_text(json.dumps({'status':'PASS','type':'NUMERICAL only; not empirical; finite horizon not proof of stability','method':'Full temporal-gauge dynamics in common (mu-rho) rotating frame; no Gauss or symmetry projection in RHS; two campaigns and three perturbation sizes','campaigns':campaigns,'physical_promotion':0},indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),'campaigns':campaigns},indent=2))
