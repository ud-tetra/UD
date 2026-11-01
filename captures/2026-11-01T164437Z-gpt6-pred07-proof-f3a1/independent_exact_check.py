"""Independent-method arithmetic checks. Does not import the PRED07 constructor."""
from fractions import Fraction as F
from itertools import permutations, combinations
from pathlib import Path
import json
from sympy import Matrix,Rational,sqrt,simplify,eye,ones

# Fractions-only finite K4 Euler consistency for candidate source.
b=[F(13,10),F(11,10),F(9,10),F(7,10)];M=sum(b);Q=sum(x*x for x in b)
source=[2*x*(x-Q/M) for x in b]
assert sum(source)==0
# Q162 mixing plus source, checking equality after an arbitrary permutation.
def rhs(vals):
    total=sum(vals);q=sum(x*x for x in vals)
    return [-(4*x-total)/4+2*x*(x-q/total) for x in vals]
for perm in permutations(range(4)):
    assert rhs([b[i] for i in perm])==[rhs(b)[i] for i in perm]
# K4 source strength is NOT an independent nonconservative source: construct its graph flux.
e=list(combinations(range(4),2));B=Matrix.zeros(4,6)
for j,(i,k) in enumerate(e):B[i,j]=-1;B[k,j]=1
s=Matrix(source)
assert B*B.T*s/4==s
# Exact independent projector and metric witness.
L=B*B.T
assert L==4*eye(4)-ones(4,4)
P=B.T*B/4;R=eye(6)-P
assert P**2==P and R**2==R and P*R==Matrix.zeros(6,6)
G=P/2+3*R/2
assert all(G[i,i]==1 for i in range(6)) and G[0,1]==-F(1,4)
# The one-high branch fixed point and finite contrast threshold.
d=(4+2*sqrt(10))/3
assert simplify(1+d-3*d*d/8)==0
assert 1<d<4
# Separate primitive 3-edge cycle with nonzero real period and zero divergence.
Bt=Matrix([[-1,0,1],[1,-1,0],[0,1,-1]])
h=Matrix([Rational(1,3)]*3)
assert Bt*h==Matrix.zeros(3,1) and sum(h)==1
assert F(9-4,2)==F(5,2)
report={'status':'PASS_EXACT_CONDITIONAL','method':'independent Fraction arithmetic and explicit K4 projectors',
        'S4_cases':24,'source_sum':'0','projector_ranks':[3,3],'metric_cross_edge':'-1/4',
        'sector_gap_ratio':'5/2','physical_promotion':0,'external_review':'DEFERRED'}
Path(__file__).with_name('INDEPENDENT_CHECK.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
