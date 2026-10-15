"""Full neutral stationary equations in the gauge where ground-state matter is positive.
Arb balls enclose all arithmetic; SciPy/SymPy are used only to propose centres.
"""
from itertools import combinations
from fractions import Fraction
from flint import arb,arb_mat,fmpq,ctx
ctx.prec=192
nodes=[t for n in range(1,5) for t in combinations(range(4),n)]
edges=[(i,j) for i,u in enumerate(nodes) for j,v in enumerate(nodes) if len(v)==len(u)+1 and set(u)<set(v)]
R=[[int(i==a)-int(i==b) for a,b in edges] for i in range(15)]
diamonds=[];C=[]
for i,u in enumerate(nodes):
 for k,v in enumerate(nodes):
  if len(v)==len(u)+2 and set(u)<set(v):
   j,h=[j for j,w in enumerate(nodes) if len(w)==len(u)+1 and set(u)<set(w)<set(v)]
   diamonds.append((i,j,h,k));row=[0]*28
   for e,sgn in [((i,j),1),((j,k),1),((i,h),-1),((h,k),-1)]:row[edges.index(e)]=sgn
   C.append(row)
Cmat=arb_mat(C);Rmat=arb_mat(R);D0=arb(10).sqrt();rho=(8+2*D0).sqrt();lp=(28+17*D0+(866-128*D0).sqrt())/18;w0=rho*(10-D0)/480;kc=4*w0/lp
H=arb_mat([[fmpq(v,2) for v in row] for row in [[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]]])
c=(1+D0)/3;hh=(8-D0)/3;gg=-lp+(5+4*D0)/3
Z=[]
for i,j in edges:
 lo=nodes[i];added=next(t for t in nodes[j] if t not in lo);row=[]
 for k in range(3):
  aa=[H[u,k] for u in range(4)]
  row.append(aa[lo[0]]+3*aa[added] if len(lo)==1 else gg*sum(aa[u] for u in lo)+(2*gg-4/c)*aa[added] if len(lo)==2 else 4*(1-c*gg)/hh*aa[added])
 Z.append(row)
Z=arb_mat(Z);L=Cmat*Z;Gamma=(L.transpose()*L)[0,0];Bmap=L.transpose()/Gamma
zero=arb(0)
def col(x):return arb_mat([[v] for v in x])
def entries(x):return [x[i,0] for i in range(x.nrows())]
def point(v):
 q=Fraction(str(v));return arb(fmpq(q.numerator,q.denominator))
def midpoint(v):return point(v.mid().str(70,radius=False))
def ball(rad):return arb(0,rad)
def bounds(x,digits=18):
 # Decimal reporting endpoints are rounded out by one final decimal unit.
 scale=10**digits;return [str((x*scale).lower().floor().fmpz())+'/'+str(scale),str((x*scale).upper().ceil().fmpz())+'/'+str(scale)]
def maxupper(xs):return max(x.abs_upper() for x in xs)
Qd=arb_mat(15,14)
for j in range(14):
 n=j+1;den=arb(n*(n+1)).sqrt()
 for i in range(n):Qd[i,j]=1/den
 Qd[n,j]=-n/den

def diag(vals):return arb_mat([[v if i==j else 0 for j in range(len(vals))] for i,v in enumerate(vals)])
def block(A,B,C,D):
 m=A.nrows();n=D.nrows();out=arb_mat(m+n,m+n)
 for i in range(m):
  for j in range(m):out[i,j]=A[i,j]
  for j in range(n):out[i,m+j]=B[i,j]
 for i in range(n):
  for j in range(m):out[m+i,j]=C[i,j]
  for j in range(n):out[m+i,m+j]=D[i,j]
 return out

