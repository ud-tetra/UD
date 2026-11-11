from itertools import combinations, product
from fractions import Fraction
import sympy as S
V=tuple(range(5)); cells=[(0,1,2,3),(0,1,2,4)]
fs=sorted(set(f for c in cells for f in combinations(c,3)))
print('faces',fs)
D=S.zeros(len(fs),2)
for k,c in enumerate(cells):
 for j in range(4):
  f=tuple(c[:j]+c[j+1:]);D[fs.index(f),k]=(-1)**j * (1 if k==0 else -1)
print('D',D)
shared=fs.index((0,1,2)); aux=fs.index((0,1,3));
assert D[shared,0]==-1 and D[shared,1]==1
# ownership matrix w: 2 rows by 7 faces, weighted 1/n3(f)
w=S.zeros(2,len(fs))
for i,f in enumerate(fs):
 owners=[j for j,c in enumerate(cells) if set(f).issubset(c)]
 for j in owners:w[j,i]=S.Rational(1,len(owners))
assert all(sum(w[:,i])==1 for i in range(len(fs)))

def evolve(z,t,h):
 """ h is a face-cell contact matrix with 0/1 entries of shape 7x2"""
 M=S.matrix_multiply_elementwise(D,h)
 A=S.zeros(9)
 A[:7,7:]=-M
 A[7:,:7]=M.T
 eps=S.Rational(1,4)
 C=(S.eye(9)-eps*A/2).inv()*(S.eye(9)+eps*A/2)
 src=z.col_join(t);dst=C*src;zn=dst[:7,0];tn=dst[7:,0]
 mid=(src+dst)/2
 J=S.zeros(7,2)
 for f in range(7):
  for k in range(2):J[f,k]=2*eps*M[f,k]*mid[f]*mid[7+k]
 for f in range(7):assert S.expand(zn[f]**2-z[f]**2+sum(J[f,:]))==0
 for k in range(2):assert S.expand(tn[k]**2-t[k]**2-sum(J[:,k]))==0
 assert sum(x*x for x in list(zn)+list(tn))==sum(x*x for x in list(z)+list(t))
 own0=[sum(w[k,f]*z[f]**2 for f in range(7))+t[k]**2 for k in range(2)]
 own1=[sum(w[k,f]*zn[f]**2 for f in range(7))+tn[k]**2 for k in range(2)]
 for k in range(2):
  balance=sum(J[f,k]-w[k,f]*sum(J[f,:]) for f in range(7))
  assert S.expand(own1[k]-own0[k]-balance)==0
 assert sum(own1)==sum(own0)
 return zn,tn,J,own0,own1,C

# all face contacts off exact fixed; no dynamics whatsoever
z=S.zeros(7,1);z[aux]=1;z[shared]=1
t=S.zeros(2,1)
h=S.zeros(7,2)
zz,tt,J,a,b,C=evolve(z,t,h)
assert zz==z and tt==t and J==S.zeros(7,2)
# live unique face provides independently admissible event, shared face remains off
h[aux,0]=1
zz,tt,J,a,b,C=evolve(z,t,h)
print('phase 1 t0',tt[0], 'delta core',tt[0]**2,'owned',a,b)
assert tt[0]**2==S.Rational(256,4225)
assert zz[shared]==z[shared]
assert a==b and b==a
# candidate reset: positive actual nonshared face->cell core transfer permits shared contact next event
h2=h.copy()
h2[shared,0]=int(bool(tt[0]**2>t[0]**2))
assert h2[shared,0]==1 and h2[shared,1]==0
z2,t2,J2,o0,o1,C2=evolve(zz,tt,h2)
print('phase 2 shared J',J2[shared,0], 'owned deltas',[S.simplify(o1[k]-o0[k]) for k in range(2)])
assert J2[shared,0]!=0
assert S.simplify(o1[0]-o0[0]-J2[shared,0]/2)==0
assert S.simplify(o1[1]-o0[1]+J2[shared,0]/2)==0
# total face-core conservation, global exact
assert sum(o0)==sum(o1)
# gate static never resets from same initial joint state
z_other,t_other,J_other,_,_,_=evolve(zz,tt,h)
assert J_other[shared,0]==0
# completely empty face/cell carrier and globally blocked contacts cannot self-generate
nothing=S.zeros(7,1);vac=S.zeros(2,1)
zeroZ,zeroT,zeroJ,_,_,_=evolve(nothing,vac,S.zeros(7,2))
assert zeroZ==nothing and zeroT==vac and zeroJ==S.zeros(7,2)
# source-agnostic S4 symmetric action no unique selected face without state asymmetry
# multiplicity global formula unique for all simplices
simp=set()
for c in cells:
 for k in range(1,5):
  for sig in combinations(c,k):simp.add(sig)
assert len(simp)==23
for sig in simp:
 owners=[c for c in cells if set(sig).issubset(c)]
 assert sum(S.Rational(1,len(owners)) for c in owners)==1
print('PASS exact two-cell gluing, 23 unique simplices, shared ownership, candidate recovery, all-off no-go')
# Full 12-element automorphism group of two-face-glued carrier, with oriented faces/cells.
CONTACTS_SYM=[(f,k) for f in range(7) for k in range(2) if D[f,k]]
from itertools import permutations

def parity(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
num=0
for pp in permutations((0,1,2)):
 for qq in ((3,4),(4,3)):
  perm=pp+qq
  Q2=S.zeros(7);Q3=S.zeros(2)
  for i,face in enumerate(fs):
   mapped=tuple(perm[k] for k in face)
   j=fs.index(tuple(sorted(mapped)))
   Q2[j,i]=parity(mapped)
  signs=[1,-1]
  for i,c in enumerate(cells):
   mapped=tuple(perm[k] for k in c)
   j=cells.index(tuple(sorted(mapped)))
   Q3[j,i]=signs[i]*parity(mapped)*signs[j]
  assert Q2*D == D*Q3
  hn=S.zeros(7,2)
  for f,k in CONTACTS_SYM:
   hn[next(j for j in range(7) if Q2[j,f]!=0), next(j for j in range(2) if Q3[j,k]!=0)]=h2[f,k]
  assert S.matrix_multiply_elementwise(D,hn)==Q2*S.matrix_multiply_elementwise(D,h2)*Q3.T
  nz,nt,nJ,na,nb,_=evolve(Q2*zz,Q3*tt,hn)
  assert nz==Q2*z2 and nt==Q3*t2
  assert sorted(list(na))==sorted(list(o0))
  assert sorted(list(nb))==sorted(list(o1))
  num+=1
assert num==12
print('PASS all 12 signed two-cell automorphisms and equal-share owned-support covariance')
