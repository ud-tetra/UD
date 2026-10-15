#!/usr/bin/env python3
"""Higher-rank algebra; separate finite matrix and full nonlinear diagnostics."""
from pathlib import Path
import sympy as s,numpy as np,json,hashlib
from scipy.linalg import eigh,expm,null_space
from scipy.integrate import solve_ivp
from higher_rank_model import color_model,color_sections,twisted_action
from critical_interval_certificate import certificate
O=Path(__file__).resolve().parent;g=color_model();ss=color_sections(g);checks=[]
def check(n,v):assert bool(v),n;checks.append(n);print('PASS',n,flush=True)
def zero(X):return all(s.simplify(s.radsimp(s.expand(z)))==0 for z in X)
def mat(X):return [[str(s.radsimp(s.simplify(z))) for z in X.row(i)] for i in range(X.rows)]
Ru=g['Ru'];W=g['W'];V=g['V'];L0=g['L0'];rho=g['rho'];F=g['F_perp_N1'];Gp=g['G_perp'];C=g['C'];R=g['R'];K=g['K'];z=s.symbols('z')
h0=s.I*g['A'];P=s.eye(15)-g['k']*g['k'].T/4
check('inactive_positive_spectrum',h0*h0==4*P and h0*g['k']==s.zeros(15,1))
check('rho_exceeds_two',s.simplify(rho**2-4).is_positive)
check('twisted_ground_identity',zero(Ru*W*Ru.H-V*L0*V))
inv0=g['k']*g['k'].T/(4*rho)+(rho*s.eye(15)-h0)*P/(rho*rho-4)
check('full_row_rank_twisted_incidence',zero(L0*inv0-s.eye(15)))
check('force_gauge_intertwiner',zero(F*Ru.H+s.I*L0*V))
check('Gauss_evolution_identity',zero(Ru*F.H-s.I*V*L0))
check('Hermitian_transverse_mass',Gp==Gp.H)
check('exact_transverse_mass_coefficient',zero(2*rho*g['Q0_perp']-g['ell']*s.diag(*g['q']).inv()*L0*s.diag(*g['q']).inv()))
for j,p in enumerate([(1,0,2,3),(1,2,3,0)]):
 node,link=twisted_action(g,p)
 check('generator_'+str(j)+'_connection_incidence',node*Ru==Ru*link)
 check('generator_'+str(j)+'_signed_L0',node*L0==L0*node)
 check('generator_'+str(j)+'_mode_mass',zero(link*Gp-Gp*link))
 check('generator_'+str(j)+'_weight',zero(link*g['D']-g['D']*link))
# Universal second-order off-diagonal magnetic Hessian, one symbolic beta per link.
xx=s.symbols('x0:28',real=True);yy=s.symbols('y0:28',real=True)
series=[]
for e,u in enumerate(g['u']):
 H=s.Matrix([[0,xx[e]-s.I*yy[e]],[xx[e]+s.I*yy[e],0]]);U=s.diag(u,1)
 series.append([U,s.I*H*U,-H*H*U/2])
def mul(a,b):return [sum((a[j]*b[k-j] for j in range(k+1)),s.zeros(2)) for k in range(3)]
for d,(i,j,h,k) in enumerate(g['diamonds']):
 a=g['edges'].index((i,j));b=g['edges'].index((j,k));c=g['edges'].index((i,h));dd=g['edges'].index((h,k));out=[s.eye(2),s.zeros(2),s.zeros(2)]
 for e,dag in [(dd,True),(c,True),(a,False),(b,False)]:out=mul(out,[v.H for v in series[e]] if dag else series[e])
 check('diamond_'+str(d)+'_offdiagonal_magnetic_Hessian_zero',s.simplify(s.expand(s.re(s.trace(out[2]))))==0)
blocks={};total=0
for name,t in ss.items():
 P=t['projector'];Z=t['basis'];left=t['left'];D=(left*g['D']*Z).applyfunc(s.simplify);G=(left*Gp*Z).applyfunc(s.simplify)
 check(name+'_projector',P*P==P and P.T==P)
 check(name+'_section_degree',Z.cols=={'trivial':1,'standard':3,'two_dimensional':2,'sign_standard':4,'sign':2}[name])
 check(name+'_closed_weight',zero(g['D']*Z-Z*D))
 check(name+'_closed_mass',zero(Gp*Z-Z*G))
 total+=Z.cols*t['irrep_dimension'];blocks[name]={'degree':Z.cols,'irrep_dimension':t['irrep_dimension'],'D':mat(D),'G_perp':mat(G),'basis':mat(Z)}
check('complex_color_mode_count_twenty_eight',total==28)
check('real_color_mode_count_fifty_six',2*total==56)
# Re-run the inherited exact integer certificate to retain critical endpoint provenance.
cert=certificate(g);check('inherited_scalar_critical_quartic_certificate',cert['status']=='PASS')
(O/'INHERITED_CRITICAL_CERTIFICATE_v0.1.json').write_text(json.dumps(cert,indent=2)+'\n')
report={'status':'PASS','type':'EXACT constructor algebra; nonlinear all-rank conclusion supplied by written energy proof','check_count':len(checks),'checks':checks,'color_mode_rule':'omega^2=2*rho*w0*y, det[y I-(b I+G_perp_j)D_j]=0; b=a*N/rho; each root irrep_dimension times as a complex oscillator and twice as real pairs per inactive color','blocks':blocks,'full_rank_stability':{'rank_one':'0<=kappa<=kappa_star(N)','rank_at_least_two':'0<kappa<=r*kappa_star(N)','zero_stiffness_rank_at_least_two':'Exact unused-color holonomy drift; individual embedded orbit unstable','above_upper_boundary':'Exact active scalar embedding gives nonlinear instability'},'residual_constraint':'The color/vacuum mode list is a linear symplectic slice before the residual global U(r-1) zero-moment quotient. No smooth full reduced stratum or unconditional independent-mode count is asserted. Energy stability is proved on the larger fixed-norm surface.','independent_review':'PENDING','physical_promotion':0,'hashes':{n:hashlib.sha256((O/n).read_bytes()).hexdigest() for n in ['verify_higher_rank.py','higher_rank_model.py','curved_mode_model.py','critical_interval_certificate.py','mode_model.py']}}
(O/'HIGHER_RANK_EXACT_VERIFICATION_v0.1.json').write_text(json.dumps(report,indent=2)+'\n')
# Complex linear Gauss reduction, one inactive color, a=N=1.
Rn=np.array(R).astype(float);Cn=np.array(C).astype(float);Run=np.array(Ru).astype(complex);Wn=np.array(W).astype(float);Vn=np.array(V.evalf()).astype(float);L0n=np.array(L0.evalf()).astype(complex);Fn=np.array(F.evalf()).astype(complex);Gpn=np.array(Gp.evalf()).astype(complex);Mn=np.eye(28)+float(rho)*Gpn;Sn=2*Wn
A=np.zeros((86,86),complex);A[:28,28:56]=np.eye(28);A[28:56,:28]=-Sn;A[28:56,56:71]=-np.sqrt(2)*Fn.conj().T;A[56:71,71:86]=-1j*L0n;A[71:86,56:71]=-1j*L0n;A[71:86,:28]=-1j*np.sqrt(2)*Fn
G=np.zeros((15,86),complex);G[:,28:56]=Run;G[:,71:86]=-np.sqrt(2)*Vn;Z=null_space(G)
Q=np.zeros((56,86),complex);Q[:28,:28]=np.eye(28);Q[:28,56:71]=1j*Run.conj().T@np.linalg.inv(Vn)/np.sqrt(2);Q[28:,28:56]=np.eye(28);Lr=np.zeros((56,56),complex);Lr[:28,28:]=Mn;Lr[28:,:28]=-Sn
linear_residual=float(np.max(abs((Q@A-Lr@Q)@Z)));assert linear_residual<1e-9
vals,vec=eigh(Mn);mh=(vec*np.sqrt(vals))@vec.conj().T;nus=eigh(mh@Sn@mh,eigvals_only=True);assert nus[0]>0
small=[]
for name,t in ss.items():
 zn=np.array(t['basis']).astype(float);left=np.array(t['left']).astype(float);ev=np.linalg.eigvals((left@Mn@zn)@(left@Sn@zn));assert max(abs(ev.imag))<1e-8;small.extend(list(ev.real)*t['irrep_dimension'])
block_residual=float(np.max(abs(np.sort(small)-nus)));assert block_residual<1e-8
# General matrix Hamiltonian and exact canonical forces, not a projected color model.
edges=g['edges'];diamonds=[]
for i,j,h,k in g['diamonds']:diamonds.append([edges.index((h,k)),edges.index((i,h)),edges.index((i,j)),edges.index((j,k))])
v=np.array(g['v'].evalf()).astype(float).ravel();u=np.array(g['u']).astype(complex).ravel();bn=np.array([int(g['B'][i,j]) for i,j in edges]);kc=float(g['kappa_critical_per_N'])
def unpack(y,r):
 n=28*r*r;return y[:n].reshape(28,r,r),y[n:2*n].reshape(28,r,r),y[2*n:2*n+15*r].reshape(15,r),y[2*n+15*r:].reshape(15,r)
def base(r):
 U=np.array([np.diag([u[e]]+[1]*(r-1)) for e in range(28)],complex);E=np.zeros_like(U);p=np.zeros((15,r),complex);p[:,0]=v;return U,E,p,p.copy()
def energy(U,E,p,ch,kappa):
 r=U.shape[1];e=.5*sum(np.trace(x@x).real for x in E)
 for es in diamonds:
  a,b,c,d=es;W=U[a].conj().T@U[b].conj().T@U[c]@U[d];e+=kappa*(1-np.trace(W).real/r)
 for n,(i,j) in enumerate(edges):e+=2*bn[n]*(np.vdot(p[i],U[n]@p[j]).imag+np.vdot(ch[i].conjugate(),U[n]@ch[j].conjugate()).imag)
 return float(e)
def flow(t,y,r,kappa):
 U,E,p,ch=unpack(y,r);h=np.zeros((15*r,15*r),complex);force=np.zeros_like(U);zz=ch.conjugate()
 for e,(i,j) in enumerate(edges):
  h[i*r:(i+1)*r,j*r:(j+1)*r]=-1j*bn[e]*U[e];h[j*r:(j+1)*r,i*r:(i+1)*r]=1j*bn[e]*U[e].conj().T
  z=U[e]@(np.outer(p[j],p[i].conjugate())+np.outer(zz[j],zz[i].conjugate()));force[e]+=bn[e]*(z+z.conj().T)
 for es in diamonds:
  factors=[U[es[0]].conj().T,U[es[1]].conj().T,U[es[2]],U[es[3]]]
  for k,e in enumerate(es):
   pre=np.eye(r,dtype=complex);post=np.eye(r,dtype=complex)
   for j in range(k):pre=pre@factors[j]
   for j in range(k+1,4):post=post@factors[j]
   if k<2:z=post@pre@factors[k];sg=-1
   else:z=factors[k]@post@pre;sg=1
   force[e]+=kappa/r*sg*(z-z.conj().T)/(2j)
 return np.r_[(1j*E@U).ravel(),(-force).ravel(),(-1j*(h+float(rho)*np.eye(15*r))@p.ravel()),(-1j*(h.conjugate()+float(rho)*np.eye(15*r))@ch.ravel())]
def obs(y,r,kappa):
 U,E,p,ch=unpack(y,r);G=-np.einsum('ia,ib->iab',p,p.conjugate())+np.einsum('ia,ib->iab',ch.conjugate(),ch)
 for e,(i,j) in enumerate(edges):G[i]+=E[e];G[j]-=U[e].conj().T@E[e]@U[e]
 unitarity=max(np.linalg.norm(x.conj().T@x-np.eye(r)) for x in U);gauss=float(np.max(abs(G)));norm=max(abs(np.vdot(p,p).real-1),abs(np.vdot(ch,ch).real-1))
 diag=max(float(np.max(abs(np.sum(abs(p)**2,axis=1)-v*v))),float(np.max(abs(np.sum(abs(ch)**2,axis=1)-v*v))),float(np.linalg.norm(E)))
 for es in diamonds:
  a,b,c,d=es;W=U[a].conj().T@U[b].conj().T@U[c]@U[d];diag=max(diag,abs(np.trace(W).real-(r-2)))
 return energy(U,E,p,ch,kappa),gauss,norm,unitarity,diag
rng=np.random.default_rng(570913);fixtures=[]
for r in [2,3]:
 U,E,p,ch=base(r);y=np.r_[U.ravel(),E.ravel(),p.ravel(),ch.ravel()];f=flow(0,y,r,r*kc)
 assert max(abs(f))<1e-12;fixtures.append({'rank':r,'equilibrium_max_residual':float(max(abs(f)))})
 # Hessian in a generic off-diagonal direction. Norm-preserving matter retraction.
 bet=rng.normal(size=28)+1j*rng.normal(size=28);pm=rng.normal(size=15)+1j*rng.normal(size=15);zm=rng.normal(size=15)+1j*rng.normal(size=15)
 pred=(np.vdot(pm,L0n@pm)+np.vdot(zm,L0n@zm)+2*np.sqrt(2)*np.vdot((pm+zm)/np.sqrt(2),Fn@bet).real+2*np.vdot(bet,Wn@bet)).real
 eps=2e-4;values=[]
 for sg in [-1,1]:
  U1=[]
  for e in range(28):H=np.zeros((r,r),complex);H[1,0]=sg*eps*bet[e];H[0,1]=H[1,0].conjugate();U1.append(expm(1j*H)@U[e])
  pp=p.copy();cc=ch.copy();pp[:,0]*=np.sqrt(1-eps*eps*np.vdot(pm,pm).real);cc[:,0]*=np.sqrt(1-eps*eps*np.vdot(zm,zm).real);pp[:,1]=sg*eps*pm;cc[:,1]=sg*eps*zm.conjugate();values.append(energy(np.array(U1),E,pp,cc,7.1))
 num=(sum(values)-2*energy(U,E,p,ch,7.1))/(2*eps*eps);err=abs(num-pred);assert err<5e-3;fixtures[-1]['offdiagonal_Hessian_absolute_error']=float(err)
campaigns=[]
for fraction in [.95,1.0]:
 runs=[];r=2;kappa=r*kc*fraction
 for eps in [.005,.0025]:
  U,E,p,ch=base(r)
  # Same seed direction at both amplitudes, including unused-color and off-diagonal fields.
  rr=np.random.default_rng(4107)
  for e in range(28):
   H=np.zeros((r,r),complex);H[1,0]=rr.normal()+1j*rr.normal();H[0,1]=H[1,0].conjugate();H[1,1]=rr.normal();U[e]=expm(1j*eps*H/10)@U[e]
  p[:,1]=eps*(rr.normal(size=15)+1j*rr.normal(size=15))/10;p/=np.linalg.norm(p);ch=p.conjugate();y0=np.r_[U.ravel(),E.ravel(),p.ravel(),ch.ravel()];sol=solve_ivp(lambda t,y:flow(t,y,r,kappa),(0,30),y0,method='DOP853',rtol=3e-10,atol=3e-12);assert sol.success
  oo=[obs(y,r,kappa) for y in sol.y.T];h0=oo[0][0];row={'epsilon':eps,'rank':r,'time':30,'max_invariant_diagnostic':max(x[4] for x in oo),'max_energy_absolute_drift':max(abs(x[0]-h0) for x in oo),'max_Gauss_residual':max(x[1] for x in oo),'max_norm_residual':max(x[2] for x in oo),'max_unitarity_residual':max(x[3] for x in oo)};assert max(row[x] for x in ['max_energy_absolute_drift','max_Gauss_residual','max_norm_residual','max_unitarity_residual'])<2e-7;runs.append(row)
 assert runs[-1]['max_invariant_diagnostic']<runs[0]['max_invariant_diagnostic']/1.5
 campaigns.append({'kappa_fraction_of_rank_scaled_threshold':fraction,'runs':runs})
num={'status':'PASS','type':'NUMERICAL diagnostic only; no empirical data','linear_Gauss_intertwiner_residual':linear_residual,'color_block_spectrum_residual':block_residual,'squared_color_frequencies_aN1':nus.tolist(),'matrix_fixtures':fixtures,'full_nonlinear_campaigns':campaigns,'physical_promotion':0,'independent_review':'PENDING'}
(O/'HIGHER_RANK_NUMERICAL_DIAGNOSTIC_v0.1.json').write_text(json.dumps(num,indent=2)+'\n');print(json.dumps({'status':'PASS','exact_checks':len(checks),'campaigns':campaigns},indent=2))
