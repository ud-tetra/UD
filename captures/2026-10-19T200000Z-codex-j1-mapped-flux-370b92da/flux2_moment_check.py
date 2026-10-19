"""Independent analytic reference moments and mapped constant-flux normalization checks."""
import sys
sys.dont_write_bytecode=True
from flux2 import *
from red_mesh import determinant
checks=0
for i in range(5):
 for j in range(5-i):
  for k in range(5-i-j):
   e=(i,j,k);expected=F(6,(k+1)*(j+k+2)*(i+j+k+3));assert sum(RI(cell,e) for cell in range(8))==expected;checks+=1
assert checks==35
G=[[F(1),F(1,2),F(0)],[F(0),F(2),F(1,2)],[F(1),F(0),F(1)]];T=inv(G);o=(F(1,3),F(-2,5),F(3,7));io=tuple(-v for v in mv(T,o));g=tr(G);mt=[[metric(a,b) for b in g] for a in g];vol=abs(determinant(G));B=whole_gram(tuple(x for row in mt for x in row),vol)
for axis,weight in enumerate([F(1),F(1),F(1,2)]):
 c=[F(0)]*15;c[4*axis]=1;local=transform(c,io,T,G);assert quad(B,local)==vol*weight
print(json.dumps({'status':'PASS','degree4_reference_partition_identities':checks,'nonorthogonal_mapped_constant_flux_norm_checks':3,'scope':'Reference child moments match analytic ordered-tetrahedron moments; affine-map metric/volume and coefficient transform preserve three physical coordinate constant-flux norms. Constructor checks only.','independent_review':False,'physical_promotion':0},indent=2))
