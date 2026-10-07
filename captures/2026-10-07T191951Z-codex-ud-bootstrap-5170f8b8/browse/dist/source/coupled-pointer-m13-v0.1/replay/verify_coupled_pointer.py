#!/usr/bin/env python3
"""Constructor replay: exact finite support/costs; small-N numerical witnesses.
Large-N guarantees rely on the accompanying analytical proof, not simulation.
"""
import itertools,json,math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.integrate import solve_ivp,quad
ROOT=Path(__file__).resolve().parents[1]
I=np.eye(2,dtype=complex);X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex);Z=np.diag([1,-1]).astype(complex)
pa={'I':I,'X':X,'Y':Y,'Z':Z}; exact=[];nums=[]
def word(s):
    a=np.array([[1]],complex)
    for c in s:a=np.kron(a,pa[c])
    return a
def anti(a,b):return sum(x!='I' and y!='I' and x!=y for x,y in zip(a,b))%2==1
def check(name,b):assert bool(b),name;exact.append(name)
def close(name,a,b,tol=4e-10):
    d=np.asarray(a)-np.asarray(b);e=float(np.linalg.norm(d.ravel()))
    assert e<tol,(name,e);nums.append({'name':name,'residual':e,'tolerance':tol})
def bound(name,observed,cap,tol=4e-10):
    assert observed<=cap+tol,(name,observed,cap)
    nums.append({'name':name,'observed':float(observed),'upper':float(cap),'tolerance':tol})
def pureD(a,b):
    return float(np.abs(np.linalg.eigvalsh(np.outer(a,a.conj())-np.outer(b,b.conj()))).sum()/2)
def terms(n):
    w=['Y'+'I'*n+'Y']
    for j in range(n):
        s=['I']*(n+2);s[j+1]='X';w.append(''.join(s))
    for j in range(n):
        s=['I']*(n+2);s[0]=s[j+1]='Z';w.append(''.join(s))
    return w
def main():
    rng=np.random.default_rng(1313)
    for n in range(1,7):
        w=terms(n);coeff=[F(3)]+[F(2)]*n+[F(1,n)]*n
        check(f'N={n}: complete support at most two',all(sum(c!='I' for c in s)<=2 for s in w))
        check(f'N={n}: supports grouped once',len({tuple(i for i,c in enumerate(s) if c!='I') for s in w})==len(w))
        check(f'N={n}: L=2N+1',len(w)==2*n+1)
        C=sum((coeff[i]*coeff[j] for i,j in itertools.combinations(range(len(w)),2) if anti(w[i],w[j])),F())
        check(f'N={n}: C=G(Omega+kappa)',C==5)
        B=sum((F(s.count('X'))+F(3*s.count('Y'),2)+sum(c!='I' for c in s)-1 for s in w),F())
        check(f'N={n}: literal B/pi=2N+4',B==2*n+4)
    instances=[]
    for name,q,a,b,threshold in [('toy-window',52,20,14,F(11,100)),('timer-debit',134,50,34,F(1,5000))]:
        n=2**q;G=F(2**a);O=F(2**b);sqrtN=2**(q//2)
        init=O/(2*G);orient=O/G;adiabatic=4*G/O**2;fluct=5*G/(4*sqrtN)
        amplitude=init+orient+adiabatic+fluct;outward=F(3,2)*amplitude
        check(name+': exact square root and factor count',sqrtN**2==n and n+2>n)
        check(name+': individual finite support caps',max(O,F(1),G/n)==O)
        check(name+': strict outward joint threshold',outward<threshold)
        expected=F(45,512) if q==52 else F(75,2**20)
        check(name+': expected rational joint certificate',outward==expected)
        check(name+': mean and variance positive finite',G>0 and O**2+n>0)
        instances.append({'name':name,'clock_spin_count':str(n),'N_prime_factorization':f'2^{q}',
            'binary_factor_count':str(n+2),'clock_dimension':f'2^(2^{q}+1)',
            'joint_dimension':f'2^(2^{q}+2)','G_over_kappa':str(G),'Omega_over_kappa':str(O),
            'g_over_kappa':str(G/n),'initial_eigenvector_debit':str(init),
            'window_orientation_debit':str(orient),'following_debit':str(adiabatic),
            'finite_clock_fluctuation_debit':str(fluct),'wrong_pointer_amplitude_bound':str(amplitude),
            'outward_joint_bound':str(outward),'threshold':str(threshold),
            'h_cap_over_kappa':str(O),'J_cap_over_kappa':str(O+n+G),
            'energy_mean_over_kappa':str(G),'energy_variance_over_kappa_squared':str(O**2+n),
            'L':str(2*n+1),'C_over_kappa_squared':str(G*(O+1)),'B_over_pi':str(2*n+4),
            'large_state_propagation_executed':False})
    check('sqrt2 outward factor3/2',F(2)<F(3,2)**2)
    check('4+pi<8 via22/7',4+F(22,7)<8)
    check('fluctuation integral coefficient5/4',(F(2)+F(1,2))/2==F(5,4))
    e=F(1,5000);rr=e/8;G=2048/e**3;O=rr*G;sqrtN=10*G/e
    check('arbitrary epsilon following coefficient1/8',4*G/O**2==e/8)
    check('arbitrary epsilon fluctuation coefficient1/8',5*G/(4*sqrtN)==e/8)
    check('arbitrary epsilon outward21/32',F(3,2)*(3*rr/2+e/8+e/8)==F(21,32)*e)
    for n in range(1,5):
        dimC=2**(n+1);dim=2*dimC
        W=np.kron(np.diag([1,0]),np.eye(2**n*2))+np.kron(np.diag([0,1]),np.kron(np.eye(2**n),Z@X))
        wx=word('X'+'I'*(n+1));ypyb=word('Y'+'I'*n+'Y')
        check(f'N={n}: exact dressing of pointer X',np.array_equal(W@wx@W.conj().T,ypyb))
        check(f'N={n}: dressing unitary',np.array_equal(W@W.conj().T,np.eye(dim)))
        hc=3*word('X'+'I'*(n+1));h=3*ypyb
        for j in range(n):
            sx=['I']*(n+2);sx[j+1]='X';sz=['I']*(n+2);sz[0]=sz[j+1]='Z'
            x,z=word(''.join(sx)),word(''.join(sz))
            check(f'N={n} spin{j}: remaining clock terms commute W',np.array_equal(W@x,x@W) and np.array_equal(W@z,z@W))
            hc+=2*x+z;h+=2*x+z
        check(f'N={n}: exact full generator conjugation',np.array_equal(W@hc@W.conj().T,h))
        c0=np.eye(dimC,dtype=complex)[:,0];clockh=hc[::2,::2]
        psi=rng.normal(size=4)+1j*rng.normal(size=4);psi/=np.linalg.norm(psi)
        start=np.kron(c0,psi)
        for t in [F(1,7),F(1,2),F(3,4)]:
            tt=float(t);chi=expm(-1j*tt*clockh)@c0
            actual=np.kron(expm(-1j*tt*h),I)@start
            close(f'N={n} t={t}: spectator propagator dressing',actual,np.kron(W,I)@np.kron(chi,psi))
            target=np.kron(chi,np.kron(Z@X,I)@psi)
            p=float(np.linalg.norm(chi[:dimC//2])**2);cap=math.sqrt(max(0,2*p-p*p))
            bound(f'N={n} t={t}: full entangled input distance',pureD(actual,target),cap)
            s=np.kron(c0,np.array([1,0],complex));v=expm(-1j*tt*h)@s
            close(f'N={n} t={t}: full-state supremum attained by work0',pureD(v,np.kron(chi,np.array([0,1],complex))),cap)
            # Product-clock residual norm; pointer may itself be arbitrary.
            z=np.array([1,0],complex);cj=expm(-2j*tt*X)@z;cjprod=np.array([1],complex)
            for j in range(n):cjprod=np.kron(cjprod,cj)
            ptr=np.array([1,1j])/math.sqrt(2);product=np.kron(ptr,cjprod)
            mf=3*word('X'+'I'*n)+n*math.cos(4*tt)*word('Z'+'I'*n)
            for j in range(n):
                sx=['I']*(n+1);sx[j+1]='X';mf+=2*word(''.join(sx))
            close(f'N={n} t={t}: exact product fluctuation norm',np.linalg.norm((clockh-mf)@product),math.sqrt(n)*abs(math.sin(4*tt)))
        hstart=np.kron(c0,np.array([1,0],complex));mean=np.vdot(hstart,h@hstart).real
        var=np.vdot(h@hstart,h@hstart).real-mean**2
        close(f'N={n}: initial mean and variance',[mean,var],[n,9+4*n])
    # Numerical following witnesses for moderate, actually propagated parameters.
    k=1.;G=1024.;O=128.;end=2*math.pi/3
    rhs=lambda t,s:-1j*(O*X+G*math.cos(2*t)*Z)@s
    grid=np.linspace(0,end,301)
    sol=solve_ivp(rhs,(0,end),np.array([1,0],complex),t_eval=grid,rtol=2e-11,atol=2e-12)
    assert sol.success
    norms=np.sum(abs(sol.y)**2,axis=0)
    close('moderate mean-field propagated state normalization',norms,np.ones(len(grid)),tol=2e-7)
    pointercap=3*O/(2*G)+4*G/O**2
    window=grid>=math.pi/3
    bound('moderate mean-field window pointer bound',float(max(abs(sol.y[0,window]))),pointercap)
    amax=k*G/(2*O**2)
    theta=lambda t:math.atan2(O,G*math.cos(2*t))
    ff=lambda t:k*O*G*math.sin(2*t)/(O**2+G**2*math.cos(2*t)**2)
    aa=lambda t:ff(t)/(2*math.sqrt(O**2+G**2*math.cos(2*t)**2))
    av=np.array([aa(t) for t in grid]);tv=sum(abs(np.diff(av)))
    bound('integration-by-parts endpoint and variation cap',abs(aa(end))+tv,4*amax)
    integral=quad(lambda t:abs(ff(t)),0,end,points=[math.pi/2],epsabs=1e-10)[0]
    bound('angle total variation f-integral cap',integral,math.pi)
    integralclock=quad(lambda t:abs(math.sin(2*t)),0,end,points=[math.pi/2],epsabs=1e-12)[0]
    close('clock integral at upper window endpoint',integralclock,5/4)
    receipt={'status':'PASS','exact_checks':len(exact),'numerical_checks':len(nums),'exact':exact,'numerical':nums,
        'instances':instances,'ideal_toy_window_status':'CERTIFIED_BY_ANALYTICAL_UPPER_BOUND',
        'large_state_propagation_executed':False,'full_controller_status':'OPEN',
        'wbs_status':{'5.2':'coupled pair-only compressed-ZX family constructed with certified toy window; full source word open',
        '4.3 / 5.3':'complete clock/work/spectator window proof with finite fluctuation cost; full bank open',
        '1.3 / 4.1':'explicit finite enormous toy resource envelopes; preparation supplied; full sizing open',
        '3.1 / 3.2':'general-N structured L/Lambda/C/B derived; retained full operator open',
        '8':'constructor replay and provenance complete; independent review pending'},
        'independent_review':'PENDING','physical_promotion':0}
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
