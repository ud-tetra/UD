"""Independent operator-route arithmetic. No fitting or producer arithmetic imports."""
from fractions import Fraction as F
import hashlib,json
import numpy as np
from flint import fmpz_mat,arb,fmpq,ctx
ctx.prec=512

def bitdecode(x):
 x=np.asarray(x);assert x.dtype==np.float64 and np.isfinite(x).all();decoded=[];scale=0
 for word in x.view(np.uint64).flat:
  w=int(word);e=(w>>52)&2047;m=w&((1<<52)-1)
  if e:m+=1<<52;p=e-1075
  else:p=-1074
  if w>>63:m=-m
  if not m:p=0
  while m and m%2==0:m//=2;p+=1
  b=max(-p,0);decoded.append((m<<max(p,0),b));scale=max(scale,b)
 return np.array([m<<(scale-b)for m,b in decoded],dtype=object).reshape(x.shape),scale

def fm(a):return fmpz_mat(np.asarray(a,dtype=object).tolist())
def matrix_rows(m):return [[str(int(x))for x in row]for row in m.tolist()]
def digest(m,b):return hashlib.sha256((json.dumps({'denominator_power_two':b,'rows':matrix_rows(m)},sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
def fraction(p):return F(int(p[0]),int(p[1]))
def pair(q):return [str(q.numerator),str(q.denominator)]
def aa(q):
 if not isinstance(q,F):q=fraction(q)
 return arb(fmpq(q.numerator,q.denominator))
def up(x):return [int((arb(x.upper())*(1<<180)).ceil().unique_fmpz()),1<<180]
def down(x):return [int((arb(x.lower())*(1<<180)).floor().unique_fmpz()),1<<180]

def quadratic_gram(U,T):
 ui,bu=bitdecode(U);ti,bt=bitdecode(T);A,B,t=fm(ui[:-2]),fm(ui[2:]),fm(ti);cross=A.transpose()*B;gA=A.transpose()*A;gB=B.transpose()*B;scale=1<<bt
 # This exact identity is E^T E, E = U[2:] - U[:-2]T.
 G=gB*(scale*scale)-(cross.transpose()*t+t.transpose()*cross)*scale+t.transpose()*gA*t
 assert G.nrows()==G.ncols()==T.shape[0]
 return G,2*(bu+bt),{'basis_denominator_power_two':bu,'shift_denominator_power_two':bt,'Gram_origin':'quadratic identity equal to exact residual E^T E'}

def exact_bounds(G,b):
 assert b>=0 and G.nrows()==G.ncols()and G.nrows()>0
 n=G.nrows();assert G==G.transpose(),'nonsymmetric candidate'
 assert all(G[j,j]>=0 for j in range(n)),'negative diagonal excludes Gram provenance'
 tr=sum(int(G[j,j])for j in range(n));rows=[sum(abs(int(G[j,k]))for k in range(n))for j in range(n)];gs=max(rows)
 # PSD is established by exact equality with the residual Gram, not assumed for arbitrary symmetric input.
 return {'trace':F(tr,1<<b),'Gershgorin':F(gs,1<<b),'operator_squared_upper':F(min(tr,gs),1<<b),'largest_diagonal_lower':F(max(int(G[j,j])for j in range(n)),1<<b),'maximizing_rows':[j for j,v in enumerate(rows)if v==gs]}

def admit(expected,candidate,b,cap,completed):
 assert completed,'premature pass refused'
 assert cap>0,'nonpositive cap refused'
 assert expected==candidate,'candidate is not the exact source-bound residual Gram'
 bounds=exact_bounds(candidate,b)
 return bounds['operator_squared_upper']<=cap*cap

def expression(g,C,u,m,o):
 etaU,etaV,rho=[aa(g[k])for k in ['etaU','etaV','rho']];assert 0<=etaU<1 and 0<=etaV<1 and 0<=rho<1
 noise=aa([3,1<<49]);floor=aa(o['qth_sigma_lower'])-C*noise-aa([1,1<<41]);assert floor>0 and aa(g['proposed_smin'])>=floor
 t=((aa(u['baseline_low_rank_residual_upper'])+C*noise)*(1+etaV).sqrt()+aa(g['xi']))/(aa(g['proposed_smin'])*(1-etaU).sqrt());assert 0<=t<1
 d=t*(2/(1+(1-t*t).sqrt())).sqrt();beta=aa(u['deleted_two_rows_beta_lower']);assert beta>d
 shift=(aa(u['comparison_shift_residual_upper'])+d*(1+aa(u['comparison_shift_norm_upper']))+aa(g['sA'])/(1-etaU).sqrt())/(beta-d)
 eta0=aa(m['basis_orthogonality_upper']);k0=((1+eta0)/(1-eta0)).sqrt();ka=((1+etaU)/(1-etaU)).sqrt();hD=aa(m['source_inverse_norm_upper'])/(1-aa(m['source_inverse_residual_upper']));Delta=aa(g['eV'])*aa(g['h'])/(1-rho)
 R=hD*(aa(m['intertwining_residual_upper'])+k0*aa(m['source_reduction_norm_upper'])*(shift+ka*Delta));half=aa(m['minimum_target_chord_lower'])/2;assert R<1;angle=R.asin()+aa(g['a'])
 return {'required_singular_floor_lower':down(floor),'offspan_sine_upper':up(t),'polar_distance_upper':up(d),'shift_distance_upper':up(shift),'eigenvalue_radius_upper':up(R),'phase_error_upper':up(angle),'phase_matching_margin_lower':down(half-angle),'pointwise_disjoint_and_angle_gate':bool(R<half and angle<half)}

def controls():
 rows=[]
 def check(name,value):assert value,name;rows.append({'id':name,'pass':True})
 def rejected(call):
  try:call();return False
  except AssertionError:return True
 I=fm([[1,0],[0,1]]);indef=fm([[1,2],[2,1]])
 check('indefinite_unbound_matrix_rejected',rejected(lambda:admit(I,indef,0,F(4),True)))
 check('nonpositive_zero_cap_rejected',rejected(lambda:admit(I,I,0,F(0),True)))
 check('nonpositive_negative_cap_rejected',rejected(lambda:admit(I,I,0,F(-1),True)))
 check('overcap_rejected',not admit(I,I,0,F(1,2),True))
 check('exact_boundary_accepted',admit(I,I,0,F(1),True))
 check('prematurepass_rejected',rejected(lambda:admit(I,I,0,F(1),False)))
 nonsym=fm([[1,1],[0,1]]);check('symmetry_failure_rejected',rejected(lambda:admit(nonsym,nonsym,0,F(2),True)))
 tamper=fm([[1,0],[0,2]]);check('same_shape_tamper_rejected',rejected(lambda:admit(I,tamper,0,F(2),True)))
 negative=fm([[-1,0],[0,1]]);check('negative_diagonal_rejected',rejected(lambda:admit(negative,negative,0,F(2),True)))
 check('scaling_squared_denominator',exact_bounds(I,4)['operator_squared_upper']==F(1,16))
 U=np.array([[.5,0],[0,.5],[.5,.5],[1.,.5]],dtype=np.float64);T=np.array([[.5,0],[0,1.]],dtype=np.float64)
 G,b,_=quadratic_gram(U,T);ui,bu=bitdecode(U);ti,bt=bitdecode(T);E=fm(ui[2:])*(1<<bt)-fm(ui[:-2])*fm(ti)
 check('quadratic_identity_matches_direct_synthetic',G==E.transpose()*E and b==2*(bu+bt))
 check('trace_is_Frobenius_squared',exact_bounds(G,b)['trace']==sum(F(int(x)**2,1<<b)for row in E.tolist()for x in row))
 # Rank-two diagonal example distinguishes operator from Frobenius admission.
 check('operator_pass_with_Frobenius_overcap',admit(I,I,0,F(1),True)and exact_bounds(I,0)['trace']>1)
 return rows
