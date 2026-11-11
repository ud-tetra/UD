"""New exact checks of selected recovered claims, not imported code execution."""
from fractions import Fraction as F
import json
def matmul(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def transpose(a):return list(map(list,zip(*a)))
def fidelity(x,t):
 y=[sum(a*b for a,b in zip(row,x)) for row in t]
 return sum(a*b for a,b in zip(x,y))**2/(sum(a*a for a in x)*sum(a*a for a in y))
# THM-565a's permitted ONB contains w=(1,-1,0)/sqrt2.
# H=(ones*w^T+w*ones^T)/sqrt6, so <e1|H|e2>=0.
w=[1,-1,0];h=[[w[i]+w[j] for j in range(3)] for i in range(3)]
assert h[0][1]==0 and h[2][1]==-1
# Columns of Y: (0,-1)/sqrt6 and (2,-1)/sqrt18.
c1=[0,-1];c2=[2,-1]
g=[[F(c1[i]*c1[j],6)+F(c2[i]*c2[j],18) for j in range(2)] for i in range(2)]
assert g==[[F(2,9),F(-1,9)],[F(-1,9),F(2,9)]]
trace=g[0][0]+g[1][1];det=g[0][0]*g[1][1]-g[0][1]*g[1][0]
assert trace==F(4,9) and det==F(1,27)
assert F(1,3)+F(1,9)==trace and F(1,3)*F(1,9)==det
assert (F(1,3)-F(1,9))/(F(1,3)+F(1,9))==F(1,2)
# THM-LS1 counterexample in an orthonormal two-eigenvector subspace of T.
t=[[F(1),F(0)],[F(0),F(1,2)]]
r=fidelity([F(1),F(1)],t);r2=fidelity([F(2),F(1)],t)
assert r==F(9,10) and r2==F(81,85) and r!=r2
# Joint S/star sectors are not thereby invariant under transport.
tp=[[F(i==j,2)+F(1,6) for j in range(3)] for i in range(3)]
d=[[F((1,-1,1)[i] if i==j else 0) for j in range(3)] for i in range(3)]
td=matmul(tp,d);dt=matmul(d,tp);assert td[0][1]-dt[0][1]==F(-1,3)
print(json.dumps({'status':'PASS','constructor_only':True,'THM565a':'Universal nonzero-entry claim falsified by admissible standard ONB; existence of nonzero coupling retained','Y_YYt':[[str(v) for v in row] for row in g],'Y_singular_values_squared':['1/3','1/9'],'singular_value_ratio_squared':3,'angle_abs_cosine_bound':'1/2 under real orthogonal column rotations','determinant_scope':'absolute determinant invariant; sign can flip with ONB orientation','THMLS1':{'original_fidelity':str(r),'after_U_diag_2_1_fixed_metric':str(r2),'repair':'unitary changes with fixed metric; general invertible changes require transported metric'},'transport_star_commutator_12':'-1/3 in Pplus basis','physical_promotion':0},indent=2))
