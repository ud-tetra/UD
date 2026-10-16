#!/usr/bin/env python3
"""Synthetic jet checks of the declared Riemannian metric and Taylor constants."""
from pathlib import Path
from math import factorial
import json
import numpy as np
from scipy.linalg import null_space
from scaled_model import *
O=Path(__file__).resolve().parent;inp=json.loads((O/'CERTIFICATE_INPUTS_v0.1.json').read_text())
bn=np.array([(-1)**nodes[j].index(next(v for v in nodes[j] if v not in nodes[i])) for i,j in edges])
ds=[[edges.index((h,k)),edges.index((i,h)),edges.index((i,j)),edges.index((j,k))] for i,j,h,k in diamonds]
def jets_product(a,b):return [sum((a[i]@b[n-i] for i in range(n+1)),np.zeros((a[0].shape[0],b[0].shape[1]),complex)) for n in range(4)]
def sphere_jet(q,v):
 c2=np.vdot(v,v).real;return [q,v,-c2*q/2,-c2*v/6]
rng=np.random.default_rng(161039);rows=[]
for ep in [1e-5,1e-6]:
 x=refine_scaled([point(v) for v in inp['global_centres'][0]['centre']],arb(str(ep)));uu=Z*col(x[:3])+arb(str(ep))*Y*col(x[3:28]);X=np.sqrt(ep)*np.array(entries(uu),float);f=np.array([float(v0[i]+arb(str(ep))*x[28+i]) for i in range(15)]);lam=float(-rho+arb(str(ep))*x[43]);u=-1j*bn*np.exp(1j*X)
 h=np.zeros((15,15),complex);Jf=np.zeros((15,28));Lw=np.zeros((15,15))
 for e,(i,j) in enumerate(edges):
  h[i,j]=-np.exp(1j*X[e]);h[j,i]=h[i,j].conjugate();Jf[i,e]=np.sin(X[e])*f[j];Jf[j,e]=np.sin(X[e])*f[i]
  v=f[i]*f[j]*np.cos(X[e]);Lw[i,i]+=v;Lw[j,j]+=v;Lw[i,j]-=v;Lw[j,i]-=v
 A=h.real-lam*np.eye(15);Ai=np.linalg.inv(A+np.outer(f,f))-np.outer(f,f)
 Hphase=4*np.diag([f[i]*f[j]*np.cos(X[e]) for e,(i,j) in enumerate(edges)])-(float(kc)+ep)*np.array(C,float).T@np.diag(np.cos(np.array(C,float)@X))@np.array(C,float)
 Cdirect=Hphase-4*Jf.T@Ai@Jf
 aa,bb,dd,*_=scaled_hessians(x,arb(str(ep)));Cscaled=np.array((H0+arb(str(ep))*(aa-bb*dd.inv()*bb.transpose())).tolist(),float)
 residual=np.max(abs(Cdirect-Cscaled));assert residual<1e-12
 V=null_space(f[None,:]);S=np.block([[Hphase/2,np.sqrt(2)*Jf.T@V],[np.sqrt(2)*V.T@Jf,V.T@A@V]])
 eig=np.linalg.eigvalsh(S)[0];assert eig>ep/2
 for r,a,N in [(2,1.,1.),(3,.4,2.),(5,50.,.3)]:
  kap=r*N*(float(kc)+ep);U=np.array([np.diag([v]+[1]*(r-1)) for v in u],complex);q=np.zeros((15,r),complex);q[:,0]=f
  H=rng.normal(size=(28,r,r))+1j*rng.normal(size=(28,r,r));H=(H+H.conj().transpose(0,2,1))/2
  ee=rng.normal(size=(28,r,r))+1j*rng.normal(size=(28,r,r));ee=(ee+ee.conj().transpose(0,2,1))/2
  p=rng.normal(size=(15,r))+1j*rng.normal(size=(15,r));z=rng.normal(size=(15,r))+1j*rng.normal(size=(15,r));p-=q*np.vdot(q,p).real;z-=q*np.vdot(q,z).real
  norm=np.sqrt(np.vdot(H,H).real+np.vdot(ee,ee).real+np.vdot(p,p).real+np.vdot(z,z).real);H/=norm;ee/=norm;p/=norm;z/=norm
  UJ=[[np.linalg.matrix_power(1j*H[e],k)@U[e]/factorial(k) for k in range(4)] for e in range(28)]
  hJ=[np.zeros((15*r,15*r),complex) for k in range(4)]
  for e,(i,j) in enumerate(edges):
   for k in range(4):hJ[k][i*r:(i+1)*r,j*r:(j+1)*r]=-1j*bn[e]*UJ[e][k];hJ[k][j*r:(j+1)*r,i*r:(i+1)*r]=hJ[k][i*r:(i+1)*r,j*r:(j+1)*r].conj().T
  energy=np.zeros(4);energy[2]=a*np.vdot(ee,ee).real/2
  for es in ds:
   W=[np.eye(r,dtype=complex)]+[np.zeros((r,r),complex) for k in range(3)]
   for n,e in enumerate(es):W=jets_product(W,[x.conj().T for x in UJ[e]] if n<2 else UJ[e])
   for k in [1,2,3]:energy[k]-=kap/r*np.trace(W[k]).real
  for v in [p,z]:
   qJ=sphere_jet(q.ravel(),v.ravel())
   for k in [1,2,3]:
    for i in range(k+1):
     for j in range(k-i+1):energy[k]+=N*np.vdot(qJ[i],hJ[j]@qJ[k-i-j]).real
  J=max(a,25*N);L=62*N
  assert abs(energy[1])<1e-12 and abs(2*energy[2])<=J and abs(6*energy[3])<=L
  rows.append({'epsilon':ep,'rank':r,'a':a,'N':N,'Schur_conversion_residual':float(residual),'scalar_gauge_slice_min_coefficient_over_epsilon':float(eig/ep),'geodesic_first_derivative':float(energy[1]),'absolute_second_derivative_over_J':float(abs(2*energy[2])/J),'absolute_third_derivative_over_L':float(abs(6*energy[3])/L)})
r={'status':'PASS','type':'NUMERICAL synthetic jet diagnostics, not rigorous interval or empirical evidence','seed':161039,'fixtures':rows,'physical_promotion':0,'independent_review':'PENDING'}
(O/'GEODESIC_DIAGNOSTIC_v0.1.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
