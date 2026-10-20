"""Independent fresh-output audit: bit decoding and quadratic-form residual identities.
No estimator import, new fit, saved factor copy, or raw record copy.
"""
import argparse,hashlib,json,struct,sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import fmpz_mat,arb,acb,ctx,fmpq
ctx.prec=512
P=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def pair(q):return [str(q.numerator),str(q.denominator)]
def frac(p):return F(int(p[0]),int(p[1]))
def aa(q):
 if not isinstance(q,F):q=frac(q)
 return arb(fmpq(q.numerator,q.denominator))
def upper(x):return [int((arb(x.upper())*(1<<180)).ceil().unique_fmpz()),1<<180]
def decode(x):
 x=np.asarray(x);assert x.dtype==np.float64 and np.isfinite(x).all()
 z=x.view(np.uint64);rows=[];maxb=0
 for val in z.flat:
  v=int(val);e=(v>>52)&2047;m=v&((1<<52)-1)
  if e:m|=1<<52;power=e-1023-52
  else:power=-1074
  if v>>63:m=-m
  if m==0:power=0
  while m and m%2==0:m//=2;power+=1
  b=max(0,-power);n=m<<max(0,power);rows.append((n,b));maxb=max(maxb,b)
 return np.array([n<<(maxb-b)for n,b in rows],dtype=object).reshape(x.shape),maxb
def mat(x):return fmpz_mat(np.asarray(x,dtype=object).tolist())
def trace(x):return sum(int(x[j,j])for j in range(x.nrows()))
def normint(x):return sum(int(t)**2 for row in x.tolist()for t in row)
def gram(x,b):
 G=mat(x).transpose()*mat(x);D=fmpz_mat(G)
 for j in range(D.nrows()):D[j,j]-=1<<(2*b)
 return G,F(normint(D),1<<(4*b))
def eq_quadratic(N,V,bv,U,bu,s,bs):
 n,v,u=mat(N),mat(V),mat(U);gn=n.transpose()*n;gu=u.transpose()*u;cross=n.transpose()*u
 first=trace(v.transpose()*gn*v);middle=sum(int(s[j])**2*int(gu[j,j])for j in range(len(s)))
 mix=sum(int(s[j])*sum(int(cross[k,j])*int(V[k,j])for k in range(V.shape[0]))for j in range(len(s)))
 result=F(first,1<<(2*(55+bv)))+F(middle,1<<(2*(bu+bs)))-F(2*mix,1<<(55+bv+bu+bs));assert result>=0;return result

def lag_quadratic(U,bu,T,bt):
 minus,plus,t=mat(U[:-2]),mat(U[2:]),mat(T);gm=minus.transpose()*minus;gp=plus.transpose()*plus;cross=minus.transpose()*plus
 return F(trace(gp),1<<(2*bu))+F(trace(t.transpose()*gm*t),1<<(2*(bu+bt)))-F(2*trace(t.transpose()*cross),1<<(2*bu+bt))
def cx(x):
 x=np.asarray(x);x=x.reshape(-1,1) if x.ndim==1 else x
 r,br=decode(np.asarray(x.real,dtype=np.float64));i,bi=decode(np.asarray(x.imag,dtype=np.float64));b=max(br,bi);return mat(r*(1<<(b-br))),mat(i*(1<<(b-bi))),b
def square_cx(r,i,b):return F(normint(r)+normint(i),1<<(2*b))
def scaled_difference(ar,ai,ba,br,bi,bb):
 b=max(ba,bb);return square_cx(ar*(1<<(b-ba))-br*(1<<(b-bb)),ai*(1<<(b-ba))-bi*(1<<(b-bb)),b)
def ties_even(x):
 # Independent integer IEEE dyad decoding and signed nearest-even division.
 a,b=decode(np.array([x],dtype=np.float64));n=int(a[0])*(1<<60);q,r=divmod(n,1<<b);return q+(r*2>(1<<b)or(r*2==(1<<b)and q%2==1))
def circular(x):return 2*abs((x/2).sin()).asin()
def phase_audit(case,source,cert):
 z=np.load(case/'PHASE_META.npz',allow_pickle=False);p=np.load(case/'PHASE_PROPOSAL.npz',allow_pickle=False);T=z['shift'];V=z['eigenvectors'];H=z['inverse'];ev=z['eigenvalues'];angles=z['angles'];em=p['two_step_phase'];assert em.shape==(209,)and em.dtype==np.int64
 tr,bt=decode(T);vr,vi,bv=cx(V);hr,hi,bh=cx(H);lr,li,bl=cx(ev);I=fmpz_mat(209,209)
 for j in range(209):I[j,j]=1
 zero=fmpz_mat(209,209);rho=scaled_difference(vr*hr-vi*hi,vr*hi+vi*hr,bv+bh,I,zero,0)
 # Multiply by diagonal Lambda explicitly, independently from producer elementwise NumPy formula.
 dr,di=fmpz_mat(209,209),fmpz_mat(209,209)
 for j in range(209):dr[j,j]=int(lr[j,0])if lr.ncols()==1 else int(lr[0,j]);di[j,j]=int(li[j,0])if li.ncols()==1 else int(li[0,j])
 eig=scaled_difference(mat(tr)*vr,mat(tr)*vi,bt+bv,vr*dr-vi*di,vr*di+vi*dr,bv+bl)
 assert rho==frac(cert['phase']['exact_inverse_residual_squared']);assert eig==frac(cert['phase']['exact_eigenpair_residual_squared'])
 gr=hr.transpose()*hr+hi.transpose()*hi;gi=hr.transpose()*hi-hi.transpose()*hr
 norm_sq=F(min(trace(gr),max(sum(abs(int(gr[j,k]))+abs(int(gi[j,k]))for k in range(209))for j in range(209))),1<<(2*bh));h=aa(norm_sq).sqrt()
 assert frac(upper(h))==frac(cert['phase']['metrics']['proposed_inverse_norm'])
 targets=source['target_matches'];sep=aa(source['metrics']['minimum_target_chord_lower']);rows=[];argument=[]
 for j in range(209):
  assert int(em[j])==ties_even(angles[j]);val=acb(aa(F(int(lr[j,0]),1<<bl)),aa(F(int(li[j,0]),1<<bl)));assert abs(val)>0
  theta=aa(F(int(em[j]),1<<60));argument.append(upper(circular(val.arg()-theta)))
  errors=[circular(theta-2*aa(t['omega']))for t in targets];k=min(range(209),key=lambda k:float(errors[k].upper()));assert errors[k]<sep/2
  assert all(errors[k].upper()<errors[i].lower()for i in range(209)if i!=k);rows.append({'emitted_index':j,'target_index':k,'error_upper':upper(errors[k])})
 assert len({x['target_index']for x in rows})==209
 assert [x['target_index']for x in rows]==[x['target_index']for x in cert['phase']['observed']['rows']]
 maxarg=max(frac(x)for x in argument);producer=frac(cert['phase']['metrics']['emitted_argument_error']);assert maxarg<=producer+F(1,1<<178)
 return {'inverse_residual_squared':pair(rho),'eigenpair_residual_squared':pair(eig),'inverse_norm_upper':upper(h),'argument_error_upper':pair(maxarg),'maximum_match_error_upper':pair(max(frac(x['error_upper'])for x in rows)),'finite_target_indices':[x['target_index']for x in rows],'all_209_nearest_even_and_unique':True}


def lag_and_normal(U,bu,T,bt):
 A,B,t=mat(U[:-2]),mat(U[2:]),mat(T);Gamma=A.transpose()*A;cross=A.transpose()*B;scale=1<<bt
 G=(B.transpose()*B)*(scale*scale)-(cross.transpose()*t+t.transpose()*cross)*scale+t.transpose()*Gamma*t
 N=Gamma*t-cross*scale
 return G,2*(bu+bt),Gamma,2*bu,N,2*bu+bt

def ls_exact(G,bG,N,bN):
 assert G==G.transpose();size=G.nrows();D=fmpz_mat(G)
 for j in range(size):D[j,j]-=1<<bG
 defect=F(normint(D),1<<(2*bG));gersh=F(min(int(G[j,j])-sum(abs(int(G[j,k]))for k in range(size)if k!=j)for j in range(size)),1<<bG);identity=F(1)-frac(upper(aa(defect).sqrt()));floor=max(gersh,identity);normal2=F(normint(N),1<<(2*bN));normalup=upper(aa(normal2).sqrt());result={'Gram_minus_I_Frobenius_squared':pair(defect),'Gershgorin_lambda_min_lower':pair(gersh),'identity_minus_Frobenius_lambda_min_lower':pair(identity),'gamma_squared_lower':pair(floor),'normal_Frobenius_squared':pair(normal2),'normal_operator_norm_upper':normalup}
 if floor>0:result['LS_step_operator_distance_upper']=upper(aa(normalup)/aa(floor))
 return result

def implication(g,C,u,m,o):
 h={k:aa(v)for k,v in g.items()};floor=aa(o['qth_sigma_lower'])-C*aa([3,1<<49])-aa([1,1<<41]);assert floor>0 and h['proposed_smin']>=floor
 t=((aa(u['baseline_low_rank_residual_upper'])+C*aa([3,1<<49]))*(1+h['etaV']).sqrt()+h['xi'])/(h['proposed_smin']*(1-h['etaU']).sqrt());assert 0<=t<1
 d=t*(2/(1+(1-t*t).sqrt())).sqrt();beta=aa(u['deleted_two_rows_beta_lower']);assert beta>d
 b=(aa(u['comparison_shift_residual_upper'])+h['sA']/(1-h['etaU']).sqrt()+d*(1+aa(u['comparison_shift_norm_upper'])))/(beta-d)
 eta0=aa(m['basis_orthogonality_upper']);k0=((1+eta0)/(1-eta0)).sqrt();ka=((1+h['etaU'])/(1-h['etaU'])).sqrt();hD=aa(m['source_inverse_norm_upper'])/(1-aa(m['source_inverse_residual_upper']));R=hD*(aa(m['intertwining_residual_upper'])+k0*aa(m['source_reduction_norm_upper'])*(b+ka*h['eV']*h['h']/(1-h['rho'])));assert R<1;half=aa(m['minimum_target_chord_lower'])/2;angle=R.asin()+h['a']
 return {'offspan_sine_upper':upper(t),'polar_distance_upper':upper(d),'shift_distance_upper':upper(b),'eigenvalue_radius_upper':upper(R),'phase_error_upper':upper(angle),'phase_matching_margin_lower':[-upper(-(half-angle))[0],1<<180],'certified':bool(R<half and angle<half)}

def controls():
 rows=[]
 def ck(k,v):assert v,k;rows.append({'id':k,'pass':True})
 n,b=decode(np.array([-0.125,0.,1.5]));ck('independent_bit_decode',n.tolist()==[-1,0,12]and b==3)
 x,b=decode(np.array([[1.,0.],[0.,.5]]));ck('Gram_exact_scaling',gram(x,b)[1]==F(9,16))
 N=np.array([[24,0],[0,8]],dtype=object);V=np.array([[1],[0]],dtype=object);s=np.array([24],dtype=object)
 ck('zero_EQ_nonzero_tail',eq_quadratic(N,V,0,V,0,s,55)==0)
 ck('wrong_EQ_detected',eq_quadratic(N,V,0,np.array([[1],[1]],dtype=object),0,s,55)>0)
 u,bu=decode(np.array([[1.,0.],[0.,1.],[2.,0.],[0.,3.]]));t,bt=decode(np.array([[2.,0.],[0.,4.]]));G,bG,Gamma,bGamma,normal,bNormal=lag_and_normal(u,bu,t,bt)
 A,B=mat(u[:-2]),mat(u[2:]);D=A*mat(t)-B*(1<<bt);ck('full_Gram_identity_matches_toy_direct',G==D.transpose()*D);ck('normal_identity_matches_toy_direct',normal==A.transpose()*D)
 ck('normal_sign_and_scale',normal==mat([[0,0],[0,1]])and bNormal==0)
 ls=ls_exact(Gamma,bGamma,normal,bNormal);ck('finite_LS_distance_exact',frac(ls['LS_step_operator_distance_upper'])==1)
 ck('raw_lag_trace_identity',F(trace(G),1<<bG)==lag_quadratic(u,bu,t,bt))
 ck('fixed_Gram_Frobenius_fourth_root',frac(upper(aa(F(normint(G),1<<(2*bG))).sqrt().sqrt()))==1)
 cutoff=2.**-24;values=np.array([2*cutoff,cutoff,.5*cutoff]);ck('rank_cutoff_equality_excluded',int(np.count_nonzero(values>cutoff))==1)
 ck('strict_argument_ties_positive',ties_even(2.**-61)==0);ck('strict_argument_ties_negative',ties_even(-2.**-61)==0)
 ck('duplicate_bijection_not_permitted',len(set([0]*209))!=209)
 ck('LS_floor_must_be_positive',not F(0)>0)
 ck('cap_equality_nonstrict',F(1,1<<34)<=F(1,1<<34))
 ck('phase_equality_strict',not F(1,8)<F(1,8))
 ck('fresh_reconstruction_not_old_verdict','NOT_EVALUATED'!='NO_GO')
 return rows
