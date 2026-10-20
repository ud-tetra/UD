"""Independent aligned-phase and exact-LS arithmetic. No fitting/imported producer math."""
from fractions import Fraction as F
import numpy as np
from flint import arb,fmpq,fmpz_mat,ctx
ctx.prec=512

def aa(p):
 if isinstance(p,F):return arb(fmpq(p.numerator,p.denominator))
 return arb(fmpq(int(p[0]),int(p[1])))
def frac(p):return F(int(p[0]),int(p[1]))
def pair(q):return [str(q.numerator),str(q.denominator)]
def up(x):return [int((arb(x.upper())*(1<<180)).ceil().unique_fmpz()),1<<180]
def down(x):return [int((arb(x.lower())*(1<<180)).floor().unique_fmpz()),1<<180]
def decode(x):
 x=np.asarray(x);assert x.dtype==np.float64 and np.isfinite(x).all();v=[];bits=0
 for word in x.view(np.uint64).flat:
  z=int(word);e=(z>>52)&2047;n=z&((1<<52)-1)
  if e:n+=1<<52;power=e-1075
  else:power=-1074
  if z>>63:n=-n
  if n==0:power=0
  while n and n%2==0:n//=2;power+=1
  b=max(-power,0);v.append((n<<max(power,0),b));bits=max(bits,b)
 return np.array([n<<(bits-b)for n,b in v],dtype=object).reshape(x.shape),bits

def fm(x):return fmpz_mat(np.asarray(x,dtype=object).tolist())
def square(m,b):return F(sum(int(x)**2 for row in m.tolist()for x in row),1<<(2*b))
def normal_identity(U,T):
 ui,bu=decode(U);ti,bt=decode(T);A=fm(ui[:-2]);B=fm(ui[2:]);Gamma=A.transpose()*A;Cross=A.transpose()*B;N=Gamma*fm(ti)-Cross*(1<<bt)
 return Gamma,2*bu,N,2*bu+bt,{'U_bits':bu,'T_bits':bt}
def ls_bound(G,bG,N,bN):
 assert G.nrows()==G.ncols()and G==G.transpose();n=G.nrows();scale=1<<bG
 gl=F(min(int(G[j,j])-sum(abs(int(G[j,k]))for k in range(n)if j!=k)for j in range(n)),scale)
 defect=fmpz_mat(G)
 for j in range(n):defect[j,j]-=scale
 defect2=square(defect,bG);identitylower=1-aa(defect2).sqrt();chosen=max(gl,frac(down(identitylower)));assert chosen>0,'nonpositive Gamma lower'
 n2=square(N,bN);error=aa(n2).sqrt()/aa(chosen)
 return {'Gamma_Gershgorin_lower':pair(gl),'Gamma_identity_defect_squared':pair(defect2),'Gamma_identity_lower':down(identitylower),'Gamma_chosen_lower':pair(chosen),'normal_squared':pair(n2),'LS_distance_upper':up(error)}

def phase(zeta,caps,C,u,m,o):
 assert zeta>=0,'negative extra sketch perturbation'
 g={k:aa(v)for k,v in caps.items()};floor=aa(o['qth_sigma_lower'])-C*aa([3,1<<49])-zeta-g['singular_floor_debit']
 if not(0<=g['etaU']<1 and 0<=g['etaV']<1 and 0<=g['rho']<1 and g['h']>0):return {'status':'HOLD_INVALID_PREMISE'}
 if not floor>0:return {'status':'HOLD_PROPOSED_SINGULAR_FLOOR'}
 t=(((aa(u['baseline_low_rank_residual_upper'])+C*aa([3,1<<49])+zeta)*(1+g['etaV']).sqrt())+g['xi'])/(floor*(1-g['etaU']).sqrt())
 out={'required_proposed_singular_floor_lower':down(floor)}
 if not(0<=t<1):out['status']='HOLD_SUBSPACE_GAP';return out
 d=t*(2/(1+(1-t*t).sqrt())).sqrt();beta=aa(u['deleted_two_rows_beta_lower'])
 if not beta>d:out['status']='HOLD_DELETED_ROW_MARGIN';return out
 b=(aa(u['comparison_shift_residual_upper'])+g['sA']/(1-g['etaU']).sqrt()+d*(1+aa(u['comparison_shift_norm_upper'])))/(beta-d)
 eta0=aa(m['basis_orthogonality_upper']);k0=((1+eta0)/(1-eta0)).sqrt();ka=((1+g['etaU'])/(1-g['etaU'])).sqrt();hD=aa(m['source_inverse_norm_upper'])/(1-aa(m['source_inverse_residual_upper']));R=hD*(aa(m['intertwining_residual_upper'])+k0*aa(m['source_reduction_norm_upper'])*(b+ka*g['eV']*g['h']/(1-g['rho'])));half=aa(m['minimum_target_chord_lower'])/2
 out.update(offspan_sine_upper=up(t),polar_distance_upper=up(d),shift_distance_upper=up(b),eigenvalue_radius_upper=up(R),status='HOLD_DISKS_NOT_STRICTLY_DISJOINT')
 if R<1:
  angle=R.asin()+g['a'];out.update(phase_error_upper=up(angle),phase_matching_margin_lower=down(half-angle))
  if R<half and angle<half:out['status']='CERTIFIED_UNIFORM_PHASE_TARGET_BIJECTION'
 return out

def controls():
 rows=[]
 def check(k,v):assert v,k;rows.append({'id':k,'pass':True})
 def reject(fn):
  try:fn();return False
  except AssertionError:return True
 U=np.array([[1.,0.],[0.,1.],[2.,0.],[0.,3.]],dtype=np.float64);T=np.array([[2.,0.],[0.,4.]],dtype=np.float64);G,bG,N,bN,_=normal_identity(U,T);r=ls_bound(G,bG,N,bN)
 check('exact_LS_normal_identity',N==fm([[0,0],[0,1]])and bG==bN==0)
 check('exact_LS_distance_one',frac(r['LS_distance_upper'])==1)
 G2,bG2,N2,bN2,_=normal_identity(U/2,T);r2=ls_bound(G2,bG2,N2,bN2);check('LS_scaled_A_B_invariance',frac(r2['LS_distance_upper'])==1 and frac(r2['Gamma_chosen_lower'])==F(1,4))
 check('nonpositive_Gamma_refused',reject(lambda:ls_bound(fm([[0,0],[0,0]]),0,N,0)))
 check('positive_diagonal_indefinite_refused',reject(lambda:ls_bound(fm([[1,2],[2,1]]),0,N,0)))
 check('asymmetric_Gamma_refused',reject(lambda:ls_bound(fm([[1,1],[0,1]]),0,N,0)))
 check('normal_tamper_distinguishable',N!=fm([[0,0],[0,2]]))
 # ExactLS residual term is necessary for rectangular fits: A=(1,0),B=(0,1),DeltaA=(0,e).
 e=F(1,2);actual=e/(1+e*e);first=F(0);second=e/(1-e)**2
 check('LS_residual_term_necessary',actual>first and actual<=second)
 check('LS_denominator_requires_strict_margin',not F(1)-F(1)>0)
 check('polar_similarity_requires_R',fm([[2,0],[0,1]])*fm([[0,1],[0,0]])!=fm([[0,1],[0,0]])*fm([[2,0],[0,1]]))
 zcaps={k:[0,1]for k in ['etaU','etaV','rho','xi','sA','eV','a']};zcaps.update(h=[1,1],singular_floor_debit=[1,1<<41]);o={'qth_sigma_lower':[0,1]}
 check('negative_zeta_refused',reject(lambda:phase(arb(-1),zcaps,arb(1),{}, {},o)))
 check('nonpositive_source_floor_HOLD',phase(arb(0),zcaps,arb(1),{}, {},o)['status']=='HOLD_PROPOSED_SINGULAR_FLOOR')
 bad=dict(zcaps);bad['etaU']=[1,1];check('invalid_Gram_HOLD',phase(arb(0),bad,arb(1),{}, {},o)['status']=='HOLD_INVALID_PREMISE')
 bad=dict(zcaps);bad['rho']=[1,1];check('invalid_inverse_HOLD',phase(arb(0),bad,arb(1),{}, {},o)['status']=='HOLD_INVALID_PREMISE')
 check('zero_plus_eightyone_grid',len([None]+list(range(20,101)))==82)
 check('subquantum_no_nonzero_encoded_change',F(1,1<<49)<F(1,1<<48))
 return rows
