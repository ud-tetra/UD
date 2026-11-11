#!/usr/bin/env python3
"""Independent stdlib Fraction replay: Q167 prospective signed gate, K4 support Cayley.

This is a second implementation written by the same constructor, NOT outside review.
"""
from fractions import Fraction as Q
E=[(u,v) for u in range(4) for v in range(u+1,4)]

def solve(M,b):
 n=len(b);a=[[Q(c) for c in row]+[Q(v)] for row,v in zip(M,b)]
 for k in range(n):
  pivot=next(i for i in range(k,n) if a[i][k]!=0)
  a[k],a[pivot]=a[pivot],a[k]
  fac=a[k][k];a[k]=[z/fac for z in a[k]]
  for i in range(n):
   if i!=k:
    m=a[i][k]
    if m:a[i]=[z-m*w for z,w in zip(a[i],a[k])]
 return [row[-1] for row in a]

def ready(x,y):return [(x[v]-x[u])*y[k] for k,(u,v) in enumerate(E)]
def norm(x):return sum((z*z for z in x),Q())
def transition(x,y,rho,r):
 h=[int(z>0) for z in ready(x,y)]
 # Cayley midpoint: (I + 1/64 BHB.T) xm = x + (1/8) BH y
 D=[[Q(0) for _ in range(6)] for _ in range(4)]
 for k,(u,v) in enumerate(E):D[u][k]=-h[k];D[v][k]=h[k]
 K=[[Q(int(i==j))+Q(1,64)*sum(D[i][k]*D[j][k] for k in range(6)) for j in range(4)] for i in range(4)]
 rhs=[x[i]+Q(1,8)*sum(D[i][k]*y[k] for k in range(6)) for i in range(4)]
 xm=solve(K,rhs)
 ym=[y[k]-Q(1,8)*sum(D[i][k]*xm[i] for i in range(4)) for k in range(6)]
 xp=[2*xm[i]-x[i] for i in range(4)]
 yp=[2*ym[k]-y[k] for k in range(6)]
 # Signed flux rho += B1 j and reciprocal r exchange
 j=[-Q(h[k],4)*(rho[v]-rho[u]) for k,(u,v) in enumerate(E)]
 p=rho[:]
 for k,(u,v) in enumerate(E):p[u]-=j[k];p[v]+=j[k]
 s=[Q(r[i]-p[i],4) for i in range(4)]
 rho1=[p[i]+s[i] for i in range(4)];r1=[r[i]-s[i] for i in range(4)]
 return xp,yp,rho1,r1,h,j

x=list(map(Q,[-3,-4,-1,-2]));y=list(map(Q,[-3,1,-2,-1,-3,1]));r=list(map(Q,[1,1,1,0]));rho=list(map(Q,[1,0,0,0]))
init_support=norm(x)+norm(y);init_stock=sum(rho)+sum(r)
seq=[];qs=[];nonzero_j=0
for k in range(8):
 q=ready(x,y)[1];qs.append(int(q>0)-int(q<0))
 xp,yp,rb,r2,h,j=transition(x,y,rho,r)
 seq.append(''.join(map(str,h)))
 assert norm(xp)+norm(yp)==init_support
 assert sum(rb)+sum(r2)==init_stock and min(rb+r2)>=0
 nonzero_j+=int(any(j))
 x,y,rho,r=xp,yp,rb,r2
assert init_support==55 and init_stock==4
assert seq==['110000','110000','110000','101000','001000','011000','011000','001000']
assert qs[0]>0 and qs[3]<0 and qs[5]>0
assert nonzero_j==8
# all-off from negative prospective products; no support update possible
z=[Q(v) for v in [3,2,1,0]]; w=[Q(1)]*6
assert not any(t>0 for t in ready(z,w))
zn,wn,_,_,gate,_=transition(z,w,[Q(1),Q(0),Q(0),Q(0)],[Q(1)]*4)
assert gate==[0]*6 and zn==z and wn==w
print('PASS pure Fraction: 8 events, exact 10-state support norm 55, stock total 4')
print('gate sequence',seq)
print('edge02 signs',qs,'8 nonzero signed burden redistribution events')
print('all-off absorbing; independent implementation, same constructor; physical promotion 0')
