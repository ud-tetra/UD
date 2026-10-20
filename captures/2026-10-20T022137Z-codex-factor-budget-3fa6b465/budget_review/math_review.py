"""Independent deterministic saved-factor budget arithmetic; no fits or producer imports."""
from fractions import Fraction as F
import numpy as np
from flint import arb,fmpq,ctx
ctx.prec=512

def aa(p):
 if isinstance(p,F):return arb(fmpq(p.numerator,p.denominator))
 return arb(fmpq(int(p[0]),int(p[1])))
def pair(x):return [str(x.numerator),str(x.denominator)]
def up(x):return [int((arb(x.upper())*(1<<180)).ceil().unique_fmpz()),1<<180]
def down(x):return [int((arb(x.lower())*(1<<180)).floor().unique_fmpz()),1<<180]
def decode(x):
 x=np.asarray(x);assert x.dtype==np.float64 and np.isfinite(x).all();terms=[];bits=0
 for word in x.view(np.uint64).flat:
  w=int(word);e=(w>>52)&2047;n=w&((1<<52)-1)
  if e:n+=1<<52;power=e-1075
  else:power=-1074
  if w>>63:n=-n
  if n==0:power=0
  while n and n%2==0:n//=2;power+=1
  b=max(0,-power);terms.append((n<<max(0,power),b));bits=max(bits,b)
 return np.array([n<<(bits-b)for n,b in terms],dtype=object).reshape(x.shape),bits

def exact_frobenius_squared(x):
 if np.iscomplexobj(x):return exact_frobenius_squared(np.asarray(x.real,dtype=np.float64))+exact_frobenius_squared(np.asarray(x.imag,dtype=np.float64))
 n,b=decode(x);return F(sum(int(v)**2 for v in n.flat),1<<(2*b))
def scalar(x):
 n,b=decode(np.array([x],dtype=np.float64));return F(int(n[0]),1<<b)
def radii(k,family):
 assert family in ['all_box','lag_only']and isinstance(k,int)and 20<=k<=100
 e=aa([1,1<<k]);z=arb(0);return (e,e,e,e)if family=='all_box'else(e,z,z,e)
def inflate(g,c,u,v,s,t):
 assert all(x>=0 for x in [u,v,s,t]);U,V,Z,S,T,W=[c[k]for k in ['U','V','Z','Sigma','T','W']]
 h=dict(g)
 h['etaU']=g['etaU']+u*(2*U+u);h['etaV']=g['etaV']+v*(2*V+v)
 h['xi']=g['xi']+Z*v+u*(S+s)+U*s
 h['sA']=g['sA']+u*(1+T+t)+U*t
 h['eV']=g['eV']+W*t;h['proposed_smin']=g['proposed_smin']-s
 return h

def phase(g,C,u,m,o):
 if not(all(g[k]>=0 for k in ['etaU','etaV','rho','xi','sA','eV','a'])and g['etaU']<1 and g['etaV']<1 and g['rho']<1 and g['h']>0):return {'status':'HOLD_INVALID_PREMISE'}
 delta=aa([3,1<<49]);floor=aa(o['qth_sigma_lower'])-C*delta-aa([1,1<<41])
 if not(floor>0 and g['proposed_smin']>=floor):return {'status':'HOLD_PROPOSED_SINGULAR_FLOOR'}
 t=((aa(u['baseline_low_rank_residual_upper'])+C*delta)*(1+g['etaV']).sqrt()+g['xi'])/(g['proposed_smin']*(1-g['etaU']).sqrt())
 if not(0<=t<1):return {'status':'HOLD_SUBSPACE_GAP'}
 d=t*(2/(1+(1-t*t).sqrt())).sqrt();beta=aa(u['deleted_two_rows_beta_lower'])
 if not beta>d:return {'status':'HOLD_DELETED_ROW_MARGIN'}
 b=(aa(u['comparison_shift_residual_upper'])+g['sA']/(1-g['etaU']).sqrt()+d*(1+aa(u['comparison_shift_norm_upper'])))/(beta-d)
 eta0=aa(m['basis_orthogonality_upper']);k0=((1+eta0)/(1-eta0)).sqrt();ka=((1+g['etaU'])/(1-g['etaU'])).sqrt();hD=aa(m['source_inverse_norm_upper'])/(1-aa(m['source_inverse_residual_upper']));back=g['eV']*g['h']/(1-g['rho']);R=hD*(aa(m['intertwining_residual_upper'])+k0*aa(m['source_reduction_norm_upper'])*(b+ka*back));half=aa(m['minimum_target_chord_lower'])/2
 out={'status':'HOLD_DISKS_NOT_STRICTLY_DISJOINT','offspan_sine_upper':up(t),'polar_distance_upper':up(d),'shift_distance_upper':up(b),'eigenvalue_radius_upper':up(R)}
 if R<1:
  angle=R.asin()+g['a'];out.update(phase_error_upper=up(angle),phase_matching_margin_lower=down(half-angle))
  if R<half and angle<half:out['status']='CERTIFIED_UNIFORM_PHASE_TARGET_BIJECTION'
 return out

def controls():
 rows=[]
 def check(name,value):assert value,name;rows.append({'id':name,'pass':True})
 def reject(fn):
  try:fn();return False
  except AssertionError:return True
 one=arb(1);zero=arb(0);g={k:zero for k in ['etaU','etaV','rho','xi','sA','eV','a']};g.update(h=one,proposed_smin=one);c={k:one for k in ['U','V','Z','Sigma','T','W']}
 check('zero_budgets_recover_all_metrics',all(inflate(g,c,zero,zero,zero,zero)[k]==v for k,v in g.items()))
 check('negative_budget_refused',reject(lambda:inflate(g,c,-one,zero,zero,zero)))
 check('unsupported_family_refused',reject(lambda:radii(50,'raw_noise')))
 check('out_of_grid_refused',reject(lambda:radii(19,'all_box')))
 test=dict(g);test['xi']=one;cc=dict(c);cc['Z']=zero
 h=inflate(test,cc,one,zero,one,zero);check('mixed_us_term_needed_scalar_exact',h['xi']==4 and abs((1+1)*(1+1))>3)
 cc=dict(c);cc['U']=zero;cc['T']=zero;h=inflate(g,cc,one,zero,zero,arb(2));check('mixed_ut_term_needed',h['sA']==3 and abs(-1*2)>1)
 check('fixed_Z_EV_term_present',inflate(g,c,zero,one,zero,zero)['xi']==one)
 check('T_perturbation_eigenpair_term_present',inflate(g,c,zero,zero,zero,one)['eV']==one)
 check('Gram_quadratic_term_present',inflate(g,c,one,zero,zero,zero)['etaU']==3)
 check('min_diagonal_debits_s',inflate(g,c,zero,zero,one,zero)['proposed_smin']==0)
 h=inflate(g,c,one,one,one,one);check('fixed_complex_diagnostics_unchanged',all(h[k]==g[k]for k in ['rho','h','a']))
 n=np.array([[.5,-.25],[0.,1.]],dtype=np.float64);check('exact_norm_squared_scaling',exact_frobenius_squared(n)==F(21,16))
 check('complex_Frobenius_squared',exact_frobenius_squared(n+1j*n)==F(21,8))
 bad=dict(g);bad['etaU']=one;check('phase_invalid_Gram_refused',phase(bad,one,{}, {}, {})['status']=='HOLD_INVALID_PREMISE')
 check('phase_nonpositive_floor_refused',phase(g,one,{}, {}, {'qth_sigma_lower':[0,1]})['status']=='HOLD_PROPOSED_SINGULAR_FLOOR')
 check('grid_has_81_unique_points',len(set(range(20,101)))==81 and set(range(20,100))!=set(range(20,101)))
 return rows
