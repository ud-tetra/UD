"""Exact Gershgorin/trace upper bound on the Euclidean operator norm."""
from fractions import Fraction as F
from flint import arb
from proof_math import fm,arr

def pair(x):return [x.numerator,x.denominator]
def gram_norm(integer_matrix,bits):
 R=fm(integer_matrix);G=arr(R.transpose()*R)
 trace=sum(int(G[j,j]) for j in range(G.shape[0]));assert trace>=0
 row=max(sum(abs(int(x)) for x in G[j]) for j in range(G.shape[0]))
 chosen=min(trace,row);sq=F(chosen,1<<(2*bits));bound=arb(sq.numerator).sqrt()/arb(sq.denominator).sqrt()
 return bound,{'Gram_dimension':G.shape[0],'residual_scale_bits':bits,'trace_squared_bound':pair(F(trace,1<<(2*bits))),'Gershgorin_squared_bound':pair(F(row,1<<(2*bits))),'chosen_squared_bound':pair(sq),'choice':'min(trace, max absolute row sum), both exact PSD eigenvalue upper bounds','physical_promotion':0}
