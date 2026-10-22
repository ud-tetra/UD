# THM-534 v1.2 compact exact proof replay (SymPy)
from itertools import combinations
import sympy as s
cells=[(0,1,2,3),(0,1,2,4)]
faces=sorted({f for c in cells for f in combinations(c,3)})
D=s.zeros(7,2)
for k,c in enumerate(cells):
 for j in range(4):
  D[faces.index(c[:j]+c[j+1:]),k]=(-1)**j*(1 if k==0 else -1)
w=s.zeros(2,7)
for f,F in enumerate(faces):
 owners=[k for k,c in enumerate(cells) if set(F)<=set(c)]
 for k in owners:w[k,f]=s.Rational(1,len(owners))
def step(z,t,h):
 M=s.matrix_multiply_elementwise(D,h);A=s.zeros(9)
 A[:7,7:]=-M;A[7:,:7]=M.T
 C=(s.eye(9)-A/8).inv()*(s.eye(9)+A/8)
 old=z.col_join(t);new=C*old;mid=(old+new)/2
 J=s.Matrix(7,2,lambda f,k:M[f,k]*mid[f]*mid[7+k]/2)
 for f in range(7):
  assert new[f]**2-z[f]**2==-sum(J[f,:])
 for k in range(2):
  assert new[7+k]**2-t[k]**2==sum(J[:,k])
 own=lambda a:[a[7+k]**2+sum(w[k,f]*a[f]**2 for f in range(7)) for k in range(2)]
 before,after=own(old),own(new)
 for k in range(2):
  assert after[k]-before[k]==sum(J[f,k]-w[k,f]*sum(J[f,:]) for f in range(7))
 return new[:7,0],new[7:,0],J,before,after
z=s.zeros(7,1);z[0]=1;z[1]=1;t=s.zeros(2,1);h=s.zeros(7,2)
assert step(z,t,h)[:2]==(z,t)
h[1,0]=1;z1,t1,J,a,b=step(z,t,h)
assert t1[0]==s.Rational(16,65)
assert a==b==[s.Rational(3,2),s.Rational(1,2)]
h[0,0]=1;z2,t2,J2,u,v=step(z1,t1,h)
assert J2[0,0]==-s.Rational(61824,511225)
assert [v[k]-u[k] for k in range(2)]==[J2[0,0]/2,-J2[0,0]/2]
assert sum(u)==sum(v)
print('PASS: exact midpoint, 23-simplex Kminus ownership, reopened shared-face transfer')
print('OPEN: independently sourced reset; physical promotion 0')
