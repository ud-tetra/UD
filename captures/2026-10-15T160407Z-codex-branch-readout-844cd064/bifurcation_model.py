"""Exact critical-amplitude geometry and numerical full energy derivatives.

The carrier is fixed. These are phase-amplitude patterns, not geometric deformations.
"""
import sympy as sp
import numpy as np
from scipy.linalg import eigh,null_space
from curved_mode_model import model,critical_pattern

HADAMARD=sp.Matrix([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])/2

def critical_algebra():
    g=model();z=sp.symbols('Lambda');poly=z*z-g['lambda_sum']*z+g['lambda_product']
    Z=sp.Matrix.hstack(*(critical_pattern(g,list(HADAMARD[:,j]),z) for j in range(3)))
    def red(e):
        num,den=sp.fraction(sp.cancel(e));assert z not in den.free_symbols
        return sp.radsimp(sp.simplify(sp.rem(num,poly,z)/den))
    gram=(Z.T*g['K']*Z).applyfunc(red);gamma=gram[0,0]
    return g,Z,z,red,gamma,gram

def numerical_model(g):
    mat=lambda x:np.array(x.evalf()).astype(float)
    D=mat(g['D']);K=mat(g['K']);C=mat(g['C']);R=mat(g['R']);dd=np.diag(D)
    weighted=K/np.sqrt(dd[:,None]*dd[None,:]);vals,vec=eigh(weighted)
    Y=vec[:,np.where(vals>1e-9)[0][:-3]]/np.sqrt(dd[:,None])
    Z=mat(sp.Matrix.hstack(*(critical_pattern(g,list(HADAMARD[:,j]),g['lambda_plus']) for j in range(3))))
    basis=np.column_stack([Z,Y]);edges=g['edges'];kc=float(g['kappa_critical_per_N'])
    def energy(theta,kappa,N=1):
        h=np.zeros((15,15),complex)
        for e,(i,j) in enumerate(edges):h[i,j]=-np.exp(1j*theta[e]);h[j,i]=h[i,j].conjugate()
        lam,f=eigh(h);v=f[:,0];phase=np.vdot(mat(g['v']).ravel(),v);v*=np.conj(phase)/abs(phase)
        first=np.zeros((15,28),complex);bond=np.zeros(28,complex)
        for e,(i,j) in enumerate(edges):
            ex=np.exp(1j*theta[e]);first[i,e]=-1j*ex*v[j];first[j,e]=1j*ex.conjugate()*v[i];bond[e]=np.conj(v[i])*ex*v[j]
        gaps=lam[1:]-lam[0];inverse=(f[:,1:]/gaps)@f[:,1:].conj().T
        gradient=4*N*bond.imag-kappa*C.T@np.sin(C@theta)
        Hessian=4*N*np.diag(bond.real)-4*N*(first.conj().T@inverse@first).real-kappa*C.T@(np.cos(C@theta)[:,None]*C)
        value=2*N*lam[0]+kappa*np.sum(1+np.cos(C@theta))
        return float(value),gradient,Hessian,v,float(lam[0])
    density_basis=null_space(np.ones((1,15)));unsigned=abs(R)
    def reduced_energy(X,sigma,E,zeta,kappa,a=1):
        n=(sigma+R@E)/2;m=(sigma-R@E)/2;rz=R.T@zeta
        assert min(n)>0 and min(m)>0
        out=a*np.dot(E,E)/2+kappa*np.sum(1+np.cos(C@X))
        for e,(i,j) in enumerate(edges):out-=2*(np.sqrt(n[i]*n[j])*np.cos(X[e]-rz[e])+np.sqrt(m[i]*m[j])*np.cos(X[e]+rz[e]))
        return float(out)
    def reversible_blocks(X,sigma,kappa,a=1):
        density=sigma/2;rootd=np.sqrt(density);Sinv=np.diag(1/density);bond=np.array([rootd[i]*rootd[j] for i,j in edges]);Wc=np.diag(bond*np.cos(X));Ws=np.diag(bond*np.sin(X));Qd=density_basis
        J=R.T@Sinv@R;Jplus=unsigned.T@Sinv@R
        Hxx=4*Wc-kappa*C.T@(np.cos(C@X)[:,None]*C)
        Hxd=Ws@unsigned.T@Sinv@Qd
        Hdd=Qd.T@Sinv@R@Wc@R.T@Sinv@Qd/4
        HEE=a*np.eye(28)+J.T@Wc@J/4
        HEz=-Jplus.T@Ws@R.T@Qd
        Hzz=4*Qd.T@R@Wc@R.T@Qd
        return np.block([[Hxx,Hxd],[Hxd.T,Hdd]]),np.block([[HEE,HEz],[HEz.T,Hzz]])
    return {'basis':basis,'critical_basis':Z,'complement':Y,'C':C,'R':R,'D':D,'K':K,'kc':kc,'energy':energy,'v':mat(g['v']).ravel(),'M':np.eye(28)+mat(g['G']),'density_basis':density_basis,'reduced_energy':reduced_energy,'reversible_blocks':reversible_blocks}
