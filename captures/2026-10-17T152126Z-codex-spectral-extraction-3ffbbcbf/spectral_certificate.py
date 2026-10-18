"""Rigorous one-sided projection certificate for the exact data Hankel spectrum."""
from fractions import Fraction as F
from flint import arb,ctx,fmpz_mat
import numpy as np
from hankel_exact import upper_entries
ctx.prec=512
def pair(x):x=F(x);return [x.numerator,x.denominator]
def a(x):x=F(x);return arb(x.numerator)/x.denominator
def bound(x,up,bits=160):
 z=(x*2**bits).upper() if up else (x*2**bits).lower()
 return F(int((z.ceil() if up else z.floor()).fmpq()),2**bits)
def root_pair_bounds(sq):
 if sq<0:raise ValueError('Negative squared spectral bound')
 x=a(sq).sqrt();return pair(bound(x,False)),pair(bound(x,True))

def verified_core_diagonalization(gc,gcden,r,G_norm):
 """Floating eigensystem is only a proposal. Exact residual and polar correction prove every bound."""
 G=np.zeros((r,r),dtype=np.float64);GN=fmpz_mat(r,r)
 for (i,j),n in upper_entries(gc,r):
  n=int(n);GN[i,j]=n;GN[j,i]=n;G[i,j]=G[j,i]=float(F(n,gcden))
 values,Q=np.linalg.eigh(G);qden=2**60;dden=2**80
 Qint=np.rint(Q*qden).astype(np.int64);QN=fmpz_mat(Qint.tolist())
 Dint=[int(round(float(t)*dden)) for t in values]
 gram=QN.transpose()*QN
 eta_num=sum((int(gram[i,j])-(qden*qden if i==j else 0))**2 for i in range(r) for j in range(r))
 eta2=F(eta_num,qden**4);eta=bound(a(eta2).sqrt(),True)
 if eta>=F(1,2):raise ArithmeticError('Core eigenvector proposal not sufficiently orthogonal')
 R=GN*QN
 res_num=0
 for i in range(r):
  for j in range(r):
   v=int(R[i,j])*dden-int(QN[i,j])*Dint[j]*gcden;res_num+=v*v
 res2=F(res_num,(gcden*qden*dden)**2)
 D_norm=max(abs(F(t,dden)) for t in Dint)
 # Q=US, U orthogonal, ||S-I||<=eta/(1+sqrt(1-eta)).
 ss=(1+a(eta)).sqrt();ds=a(eta)/(1+(1-a(eta)).sqrt())
 radius=bound(a(G_norm*eta)+a(res2).sqrt()*ss+a(D_norm)*ds*(ss+1),True)
 return sorted([F(t,dden) for t in Dint],reverse=True),radius,{
  'method':'Exact eigen-residual and polar correction; floating eigensystem untrusted',
  'eigenvector_Gram_defect_squared':pair(eta2),'eigen_residual_frobenius_squared':pair(res2),
  'individual_eigenvalue_radius':pair(radius)}

def certify(energy,gv,gvden,gc,gcden,r,threshold,condition_cap=2029):
 """C=HV, gv=V^TV, gc=C^TC, supplied from exact data-dependent construction.
 This numerical proof proves properties of the numeric record, not its physical provenance.
 """
 if r<1 or gvden<=0 or gcden<=0 or threshold<=0:raise ValueError('Invalid proof parameters')
 eta_num=0;diag=[0]*r
 for (i,j),value in upper_entries(gv,r):
  if not 0<=i<=j<r:raise ValueError('Gram index outside candidate basis')
  diff=int(value)-(gvden if i==j else 0);eta_num+=(1 if i==j else 2)*diff*diff
  if i==j:diag[i]=1
 # Sparse matrices omit zero diagonal entries; include their distance fromidentity.
 eta_num+=sum(1-d for d in diag)*gvden**2
 eta2=F(eta_num,gvden**2);eta=bound(a(eta2).sqrt(),True)
 common={'status':'HOLD','physical_promotion':0,'independent_review':'pending',
  'candidate_rank':r,'exact_Hankel_frobenius_squared':pair(energy),'candidate_Gram_defect_squared':pair(eta2),
  'candidate_Gram_defect_upper':pair(eta),'full_Hankel_materialized':False,
  'scope':'Exact encoded numeric record only; no hardware, model-family or hidden-state certification'}
 if eta>=1:return {**common,'reason':'Candidate Gram defect not belowone'}
 d=[0]*r;off=[0]*r
 for (i,j),value in upper_entries(gc,r):
  if not 0<=i<=j<r:raise ValueError('Gram index outside candidate basis')
  value=int(value)
  if i==j:d[i]=value
  else:off[i]+=abs(value);off[j]+=abs(value)
 if min(d)<0:raise ValueError('Negative Gram diagonal')
 trace=F(sum(d),gcden)
 residual2=F(energy)-trace/(1+eta)
 if residual2<0:raise ValueError('Inconsistent core/energy inputs; exact construction must be used')
 offmax=max(off);sorted_d=sorted(d,reverse=True)
 eigen_d=[F(t,gcden) for t in sorted_d];radius=F(offmax,gcden)
 lower2=max(F(0),eigen_d[-1]-radius)/(1+eta)
 upper2=(eigen_d[0]+radius)/(1-eta)+residual2
 coreproof={'method':'Symmetric offdiagonal row-sum bound','individual_eigenvalue_radius':pair(radius)}
 # A rotated but valid signal basis need not be diagonally dominant.
 # When the tail is already small, verify a proposed core eigensystem exactly.
 if residual2<threshold**2 and (lower2<=threshold**2 or upper2>=condition_cap**2*lower2):
  try:eigen_d,radius,coreproof=verified_core_diagonalization(gc,gcden,r,F(sorted_d[0]+offmax,gcden))
  except (ArithmeticError,np.linalg.LinAlgError,OverflowError):return {**common,'reason':'Core eigenvector proposal could not be verified; HOLD'}
  lower2=max(F(0),eigen_d[-1]-radius)/(1+eta)
  upper2=(eigen_d[0]+radius)/(1-eta)+residual2
 signature=lower2>threshold**2 and residual2<threshold**2
 cond_ok=lower2>0 and upper2<condition_cap**2*lower2
 lo,_=root_pair_bounds(lower2);_,hi=root_pair_bounds(upper2);_,tail=root_pair_bounds(residual2)
 bands=[]
 for value in eigen_d:
  l=max(F(0),value-radius)/(1+eta)
  u=(value+radius)/(1-eta)+residual2
  low,_=root_pair_bounds(l);_,high=root_pair_bounds(u);bands.append([low,high])
 result={**common,'status':'CERTIFIED_NUMERIC_RECORD_SIGNATURE' if signature and cond_ok else 'HOLD',
  'reason':'Count and condition gates verified' if signature and cond_ok else 'Insufficient core or residual gap; do not change the frozen gate',
  'projection_tail_frobenius_squared_upper':pair(residual2),
  'projected_core_trace_squared_norm':pair(trace),'core_offdiagonal_row_sum_upper':pair(F(offmax,gcden)),
  'verified_core_spectral_bounds':coreproof,
  'sigma_r_lower_squared':pair(lower2),'sigma_1_upper_squared':pair(upper2),
  'sigma_r_plus1_upper_squared':pair(residual2),'sigma_1_interval':[bands[0][0],hi],
  'sigma_r_interval':[lo,bands[-1][1]],'sigma_r_plus1_interval':[[0,1],tail],
  'individual_retained_singular_intervals':bands,'selection_threshold':pair(threshold),
  'count_above_threshold_certified':r if signature else None,
  'condition_below_declared_cap':bool(cond_ok),'condition_cap':condition_cap,
  'condition_squared_upper':pair(upper2/lower2) if lower2>0 else None,
  'right_signal_subspace_sine_squared_upper':pair(min(F(1),residual2/lower2)) if signature else None,
  'numerical_operator_error_upper':[0,1],
  'numerical_error_reason':'Direct validated enclosures of the exact encodedH; no floating approximateH or unverified SVD is used'}
 return result
