"""Exact retained equation/Gram and prospectively fixed lag/LS matrix witnesses."""
from fractions import Fraction as F
import numpy as np
from flint import fmpz_mat
from common import a,up,need
from numeric_math import encode

def saved_rank(s):
 s=np.asarray(s);need(s.dtype==np.float64 and s.ndim==1 and np.isfinite(s).all(),'saved singular array must be finite binary64')
 cutoff=F(1,1<<24);values=[F(*float(x).as_integer_ratio())for x in s]
 need(all(x!=cutoff for x in values),'HOLD saved singular value equals exact cutoff')
 return sum(x>cutoff for x in values)

def fm(x):return fmpz_mat(np.asarray(x,dtype=object).tolist())
def pair(x):return [str(x.numerator),str(x.denominator)]
def fraction(p):return F(int(p[0]),int(p[1]))
def sqnorm(M,b):return F(sum(int(x)**2 for row in M.tolist()for x in row),1<<(2*b))
def norm_upper(squared):return up(a(pair(squared)).sqrt())
def gram_sq(X,b):
 G=fm(X).transpose()*fm(X)
 for j in range(G.nrows()):G[j,j]-=1<<(2*b)
 return sqnorm(G,2*b)

def matrices(Ui,Ti,bU,bT):
 q=Ui.shape[1];lag=fmpz_mat(q,q);Gamma=fmpz_mat(q,q);normal=fmpz_mat(q,q);tm=fm(Ti);rawsq=F(0)
 for begin in range(0,len(Ui)-2,512):
  end=min(len(Ui)-2,begin+512);A=fm(Ui[begin:end]);B=fm(Ui[begin+2:end+2]);D=A*tm-B*(1<<bT);lag+=D.transpose()*D;Gamma+=A.transpose()*A;normal+=A.transpose()*D;rawsq+=sqnorm(D,bU+bT)
 need(rawsq==F(sum(int(lag[j,j])for j in range(q)),1<<(2*(bU+bT))),'lag trace identity')
 return lag,Gamma,normal,rawsq

def matrix_bounds(lag,Gamma,normal,bU,bT):
 # The ONLY lag operator route is sqrt(||lag Gram||F), never route search.
 gram_F_sq=sqnorm(lag,2*(bU+bT));lagupper=up(a(pair(gram_F_sq)).sqrt().sqrt());E=fmpz_mat(Gamma);q=Gamma.nrows()
 for j in range(q):E[j,j]-=1<<(2*bU)
 gammaDefect=sqnorm(E,2*bU);gersh=F(min(int(Gamma[i,i])-sum(abs(int(Gamma[i,j]))for j in range(q)if j!=i)for i in range(q)),1<<(2*bU));identity=F(1)-fraction(norm_upper(gammaDefect));floor=max(gersh,identity);normal_sq=sqnorm(normal,2*bU+bT);normalUpper=norm_upper(normal_sq)
 ls={'status':'HOLD_NO_POSITIVE_LS_GRAM_FLOOR','Gram_denominator_bits':2*bU,'normal_denominator_bits':2*bU+bT,'Gram_minus_I_Frobenius_squared':pair(gammaDefect),'Gershgorin_lambda_min_lower':pair(gersh),'identity_minus_Frobenius_lambda_min_lower':pair(identity),'gamma_squared_lower':pair(floor),'normal_Frobenius_squared':pair(normal_sq),'normal_operator_norm_upper':normalUpper}
 if floor>0:ls.update(status='CERTIFIED_FINITE_SAVED_LS_STEP_DISTANCE',LS_step_operator_distance_upper=up(a(normalUpper)/a(pair(floor))))
 return {'route':'PRESELECTED_GRAM_FROBENIUS_ONLY','residual_denominator_bits':bU+bT,'Gram_Frobenius_squared':pair(gram_F_sq),'operator_norm_upper':lagupper},ls

def measure(N,U,s,vt,T):
 need(U.shape==(8191,209)and vt.shape==(321,321)and s.shape==(321,)and T.shape==(209,209),'fixed output shapes');need(np.isfinite(s).all()and np.all(s[:-1]>=s[1:])and np.all(s>=0),'singular values finite sorted nonnegative')
 Ui,bU=encode(U);Vi,bV=encode(vt[:209,:].T.copy());si,bS=encode(s[:209].copy());Ti,bT=encode(T);eq=F(0);vm=fm(Vi)
 for begin in range(0,8191,512):
  end=min(8191,begin+512);left=fm(N[begin:end])*vm;right=fm(Ui[begin:end]*si[None,:]);bits=max(55+bV,bU+bS);D=left*(1<<(bits-55-bV))-right*(1<<(bits-bU-bS));eq+=sqnorm(D,bits)
 gu=gram_sq(Ui,bU);gv=gram_sq(Vi,bV);lag,Gamma,normal,rawsq=matrices(Ui,Ti,bU,bT);lagbound,ls=matrix_bounds(lag,Gamma,normal,bU,bT)
 result={'etaU':norm_upper(gu),'etaV':norm_upper(gv),'xi':norm_upper(eq),'sA':lagbound['operator_norm_upper'],'proposed_smin':list(float(s[208]).as_integer_ratio()),'exact_squared':{'left_Gram_F':pair(gu),'right_Gram_F':pair(gv),'singular_equation_F':pair(eq),'raw_lag_F':pair(rawsq)},'lag':lagbound,'LS':ls,'retained_equation_norm':'Exact dyadic Frobenius upper bounds operator; no reconstruction tail charged','readable':{'etaU':float(a(norm_upper(gu))),'etaV':float(a(norm_upper(gv))),'xi':float(a(norm_upper(eq))),'lag_operator_upper':float(a(lagbound['operator_norm_upper'])),'proposed_smin':float(s[208]),'LS_step_distance_upper':None if ls['status'].startswith('HOLD')else float(a(ls['LS_step_operator_distance_upper']))}}
 payload={'U_denominator_bits':bU,'T_denominator_bits':bT,'lag_Gram_denominator_bits':2*(bU+bT),'LS_Gram_denominator_bits':2*bU,'LS_normal_denominator_bits':2*bU+bT,'matrix_shape':[209,209],'lag_Gram_integer_numerators':[[str(int(v))for v in row]for row in lag.tolist()],'LS_Gram_integer_numerators':[[str(int(v))for v in row]for row in Gamma.tolist()],'LS_normal_integer_numerators':[[str(int(v))for v in row]for row in normal.tolist()]}
 return result,payload
