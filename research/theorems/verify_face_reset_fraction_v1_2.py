"""Exact independent stdlib Fraction matrix audit: two glued tetrahedra, 256 face-cell contact masks."""
from fractions import Fraction as Q
from itertools import product
FACES=[(0,1,2),(0,1,3),(0,1,4),(0,2,3),(0,2,4),(1,2,3),(1,2,4)]
CELLS=[(0,1,2,3),(0,1,2,4)]
# second 3-cell oriented negatively to oppose the first on shared face
D=[[Q(-1),Q(1)],[Q(1),Q(0)],[Q(0),Q(-1)],
   [Q(-1),Q(0)],[Q(0),Q(1)],[Q(1),Q(0)],[Q(0),Q(-1)]]
CONTACTS=[(f,k) for f in range(7) for k in range(2) if D[f][k]]
assert len(CONTACTS)==8
W=[[Q(0) for _ in range(7)] for _ in range(2)]
for f, face in enumerate(FACES):
    own=[k for k,c in enumerate(CELLS) if set(face).issubset(c)]
    for k in own:W[k][f]=Q(1,len(own))

def linear_solve(A,b):
    A=[list(A[i])+[b[i]] for i in range(len(b))]
    n=len(b)
    for c in range(n):
        k=next(j for j in range(c,n) if A[j][c])
        A[c],A[k]=A[k],A[c]
        z=A[c][c];A[c]=[a/z for a in A[c]]
        for r in range(n):
            if r==c:continue
            f=A[r][c]
            if f:A[r]=[A[r][j]-f*A[c][j] for j in range(n+1)]
    return [A[i][-1] for i in range(n)]

def evolve(z,t,mask):
    M=[[D[f][k]*mask[f][k] for k in range(2)] for f in range(7)]
    A=[[Q(0) for _ in range(9)] for _ in range(9)]
    for f,k in CONTACTS:
        A[f][7+k]=-M[f][k];A[7+k][f]=M[f][k]
    eps=Q(1,4);u=z+t
    L=[[Q(int(i==j))-eps*A[i][j]/2 for j in range(9)] for i in range(9)]
    rhs=[u[i]+eps*sum(A[i][j]*u[j] for j in range(9))/2 for i in range(9)]
    n=linear_solve(L,rhs)
    mid=[(u[i]+n[i])/2 for i in range(9)]
    J=[[2*eps*M[f][k]*mid[f]*mid[7+k] for k in range(2)] for f in range(7)]
    for f in range(7):assert n[f]**2-z[f]**2==-sum(J[f])
    for k in range(2):assert n[7+k]**2-t[k]**2==sum(J[f][k] for f in range(7))
    own0=[t[k]**2+sum(W[k][f]*z[f]**2 for f in range(7)) for k in range(2)]
    own1=[n[7+k]**2+sum(W[k][f]*n[f]**2 for f in range(7)) for k in range(2)]
    for k in range(2):
        assert own1[k]-own0[k]==sum(J[f][k]-W[k][f]*sum(J[f]) for f in range(7))
    assert sum(own0)==sum(own1)
    return n[:7],n[7:],J,own0,own1

z=[Q(0)]*7;z[0]=1;z[1]=1;t=[Q(0)]*2
h=[[Q(0)]*2 for _ in range(7)]
assert evolve(z,t,h)[:2]==(z,t)
h[1][0]=1
z1,t1,J,a,b=evolve(z,t,h)
assert t1[0]==Q(16,65) and t1[0]**2==Q(256,4225)
assert a==b==[Q(3,2),Q(1,2)]
next_h=[row.copy() for row in h];next_h[0][0]=Q(int(t1[0]**2>t[0]**2))
z2,t2,J2,a2,b2=evolve(z1,t1,next_h)
assert J2[0][0]==Q(-61824,511225)
assert b2[0]-a2[0]==J2[0][0]/2
assert b2[1]-a2[1]==-J2[0][0]/2
assert evolve(z1,t1,h)[2][0][0]==0

# Exhaustive mask test; binary contact assignments over all 8 face-cell incidences.
positive_shared=0
for bits in product((0,1),repeat=8):
    mask=[[Q(0)]*2 for _ in range(7)]
    for (f,k),b in zip(CONTACTS,bits):mask[f][k]=Q(b)
    zn,tn,Js,own0,own1=evolve(z,t,mask)
    if Js[0][0]:positive_shared+=1
assert positive_shared>0
print('PASS 256 binary face-to-cell contact masks, exact per-face/per-cell midpoint receipts, global norm and equal-share owned content')
print('PASS conditional unique-face->cell reset witness, J_shared=',J2[0][0], 'owned delta=',[b2[i]-a2[i] for i in range(2)])
print('PASS globally all-off absorbing, no self-reset without admitted higher-degree contact')
