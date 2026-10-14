from pathlib import Path
import json,math
import numpy as np
import sympy as s
from scipy.linalg import expm

root=Path(__file__).resolve().parent
r,p=s.symbols('r p',real=True)
assert s.expand(1-(1-r+r*p)**2)==s.expand(2*r*(1-p)-r*r*(1-p)**2)
assert s.expand(1-(1-2*r)**2)==s.expand(4*r*(1-r))
assert s.expand(1-(1-r)**2)==s.expand(2*r-r*r)
tol=2e-12;counts={'fresh_terminal_joint_and_marginal':0,'arbitrary_input_envelope':0,'generator_mismatch':0}
max_residual=0.
counts['fresh_nonterminal_and_failure_probability']=0

def clock(N,rate=1.):
    H=np.zeros((N+1,N+1))
    for j in range(N):H[j,j+1]=H[j+1,j]=rate*math.sqrt((j+1)*(N-j))
    return H

def distance(a,b):
    a=a/np.linalg.norm(a);b=b/np.linalg.norm(b)
    return float(np.linalg.norm(b-a*np.vdot(a,b)))

# Body S,O,L,M,E,Y, all qubits. Source and spectator Y form a Bell pair.
psi=np.zeros(64,complex);psi[0]=1/math.sqrt(2);psi[33]=1/math.sqrt(2)
J=np.zeros((64,64))
for i in range(64):
    S,O,L,M,E,Y=[(i>>j)&1 for j in (5,4,3,2,1,0)]
    target=(O<<5)+(S<<4)+((L^1)<<3)+((M^1)<<2)+((E^1)<<1)+Y
    J[target,i]=1
assert np.array_equal(J@J,np.eye(64))
assert abs(np.vdot(psi,J@psi))<tol
for N in (1,2,4):
 for t in (0.,math.pi/8,math.pi/4,math.pi/2,3*math.pi/4,math.pi):
    c=expm(-1j*t*clock(N))[:,0];rr=abs(c[0])**2
    actual=np.kron(c,J@psi);actual[:64]=c[0]*psi
    target=np.kron(c,J@psi)
    dj=distance(actual,target)
    reduced=rr*np.outer(psi,psi.conj())+(1-rr)*np.outer(J@psi,(J@psi).conj())
    db=np.linalg.eigvalsh(reduced-np.outer(J@psi,(J@psi).conj()))
    dm=float(np.sum(abs(db))/2)
    residual=max(abs(dj-math.sqrt(max(0.,2*rr-rr*rr))),abs(dm-rr))
    assert residual<tol
    max_residual=max(max_residual,residual);counts['fresh_terminal_joint_and_marginal']+=1

# General involution with both eigenspaces; scan admitted expectation values.
Jn=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]],float)
for pp in (0.,.2,.5,1.):
 for rr in (.1,.5,.9):
    v=np.array([math.sqrt(pp),0,math.sqrt(1-pp),0],complex)
    assert abs(np.vdot(v,Jn@v)-pp)<tol
    c=np.array([math.sqrt(rr),math.sqrt(1-rr)])
    a=np.concatenate([c[0]*v,c[1]*(Jn@v)])
    b=np.kron(c,Jn@v)
    assert abs(distance(a,b)-math.sqrt(max(0.,1-(1-rr+rr*pp)**2)))<tol
    no_capture=float(sum(abs(a[i])**2 for i in (0,2,4,6)))
    assert abs(no_capture-(pp+(1-pp)*rr))<tol
    counts['fresh_nonterminal_and_failure_probability']+=1
for rr in (0.,.01,.1,.25,.5,.75,1.):
 for xx in (-1.,-.5,0.,.5,1.):
    val=math.sqrt(max(0.,1-(1-rr+rr*xx)**2))
    bound=2*math.sqrt(rr*(1-rr)) if rr<=.5 else 1.
    assert val<=bound+tol
    counts['arbitrary_input_envelope']+=1

# Small dressed-clock mismatch with a retained spectator, no assumed freshness.
J2=np.array([[0.,1.],[1.,0.]])
rho0=np.array([1,0,0,1],complex)/math.sqrt(2) # body / spectator Bell vector
for N in (1,3):
    Hq=clock(N);V=np.kron(np.diag([1]+[0]*N),np.eye(2))+np.kron(np.diag([0]+[1]*N),J2)
    H0=V@np.kron(Hq,np.eye(2))@V.T
    mismatch=.03*np.kron(np.eye(N+1),np.diag([1.,-1.]))
    Ha=H0+mismatch
    initial=np.kron(np.eye(N+1)[:,0],rho0)
    for t in (.1,.5,1.,math.pi/2):
        actual=np.kron(expm(-1j*t*Ha),np.eye(2))@initial
        c=expm(-1j*t*Hq)[:,0];rr=abs(c[0])**2
        target=np.kron(c,np.kron(J2,np.eye(2))@rho0)
        bound=min(1.,.03*t+(2*math.sqrt(rr*(1-rr)) if rr<=.5 else 1.))
        assert distance(actual,target)<=bound+tol
        counts['generator_mismatch']+=1

report={'status':'PASS','symbolic_identities':3,'numeric_checks':counts,'tolerance':tol,
 'largest_fresh_fixture_residual':max_residual,'retained_spectator':'source/spectator Bell pair',
 'scope':'small constructor fixtures and symbolic identities; no independent review, interval certificate or apparatus-acquisition test',
 'physical_promotion':0}
(root/'APPARATUS_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
