"""Exact graph and linearized operators for the declared GHT action."""
from itertools import combinations
import sympy as s

def graph():
    simplices=[t for k in range(1,5) for t in combinations(range(4),k)]
    B=s.zeros(15)
    for j,t in enumerate(simplices):
        if len(t)>1:
            for k in range(len(t)):B[simplices.index(t[:k]+t[k+1:]),j]=(-1)**k
    edges=[(i,j) for i in range(15) for j in range(15) if B[i,j]]
    R=s.zeros(15,28)
    for e,(i,j) in enumerate(edges):R[i,e]=1;R[j,e]=-1
    diamonds=[]
    for i,t in enumerate(simplices):
        for k,w in enumerate(simplices):
            if len(w)==len(t)+2 and set(t)<set(w):
                j,h=[j for j in range(15) if B[i,j] and B[j,k]]
                diamonds.append((i,j,h,k))
    C=s.zeros(18,28)
    for row,(i,j,h,k) in enumerate(diamonds):
        for pair,sign in [((i,j),1),((j,k),1),((i,h),-1),((h,k),-1)]:C[row,edges.index(pair)]+=sign
    k=s.Matrix([1]*4+[0]*11);S=s.diag(*k);M=s.zeros(15,28)
    for e,(i,j) in enumerate(edges):M[i,e]=-B[i,j]*k[j];M[j,e]=-B[i,j]*k[i]
    return {'simplices':simplices,'edges':edges,'diamonds':diamonds,'B':B,'A':B.T-B,'R':R,'C':C,'K':C.T*C,'k':k,'S':S,'M':M}

def scalar(g,a=1,kappa=1,alpha=1):
    """116 real coordinates (theta,E,x,u,y,v), mu-rotating frame."""
    A=g['A'];M=alpha*g['M'];S=alpha*g['S'];R=g['R'];K=g['K']
    th=slice(0,28);E=slice(28,56);x=slice(56,71);u=slice(71,86);y=slice(86,101);v=slice(101,116)
    L=s.zeros(116);L[th,E]=a*s.eye(28);L[E,th]=-kappa*K
    L[E,x]=2*M.T;L[E,u]=2*M.T;L[x,x]=A;L[u,u]=-A
    L[y,y]=A;L[v,v]=-A;L[y,th]=M;L[v,th]=M
    G=s.zeros(15,116);G[:,E]=R;G[:,x]=-2*S;G[:,u]=2*S
    T=s.zeros(116,15);T[th,:]=R.T;T[y,:]=S;T[v,:]=-S
    return L,G,T

def transverse(g,a=1,kappa=1,alpha=1):
    """One off-diagonal color: 86 complex coordinates (beta,epsilon,p,q)."""
    A=g['A'];M=alpha*g['M'];S=alpha*g['S'];R=g['R']
    b=slice(0,28);e=slice(28,56);p=slice(56,71);q=slice(71,86)
    L=s.zeros(86);L[b,e]=a*s.eye(28);L[e,b]=-kappa*g['K'];L[e,p]=M.T
    L[p,q]=A;L[q,p]=A;L[q,b]=2*s.I*M
    G=s.zeros(15,86);G[:,e]=R;G[:,q]=-S
    T=s.zeros(86,15);T[b,:]=R.T;T[p,:]=2*s.I*S
    return L,G,T

def reduction(g):
    """Coulomb projectors and 86-coordinate scalar reduced dynamics, alpha=1.

    Coordinates (theta_T,E_T,p,q,eta,zeta); constrained subspaces are explicit.
    The ambient presentation has dimensions 28+28+4*15; its invariant domain
    theta_T,E_T in ker R and q,zeta in k-perp has dimension 86.
    """
    R=g['R'];k=g['k'];S=g['S'];A=g['A'];M=g['M'];K=g['K']
    J=s.ones(15)/15;Lplus=(R*R.T+J).inv()-J
    PT=s.eye(28)-R.T*Lplus*R;P0=s.eye(15)-k*k.T/4
    return Lplus,PT,P0

def fast_rank(M):
    from sympy.polys.matrices import DomainMatrix
    return DomainMatrix.from_Matrix(M,extension=True).to_field().rank()
