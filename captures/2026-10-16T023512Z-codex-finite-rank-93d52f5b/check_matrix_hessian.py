#!/usr/bin/env python3
"""Synthetic full-matrix diagnostics. Floating results are not proof certificates."""
from pathlib import Path
import json
import numpy as np
from scipy.linalg import expm,eigh
from scaled_model import *
O=Path(__file__).resolve().parent
inp=json.loads((O/'CERTIFICATE_INPUTS_v0.1.json').read_text())
bn=np.array([(-1)**nodes[j].index(next(x for x in nodes[j] if x not in nodes[i])) for i,j in edges])
ds=[[edges.index((h,k)),edges.index((i,h)),edges.index((i,j)),edges.index((j,k))] for i,j,h,k in diamonds]
h0=np.zeros((15,15),complex)
for e,(i,j) in enumerate(edges):h0[i,j]=-1j*bn[e];h0[j,i]=1j*bn[e]
assert np.max(abs(eigh(h0,eigvals_only=True)-np.array([-2]*7+[0]+[2]*7)))<1e-12
def profile(k,eps):
 x=refine_scaled([point(s) for s in inp['global_centres'][k-1]['centre']],arb(str(eps)))
 u=Z*col(x[:3])+arb(str(eps))*Y*col(x[3:28])
 X=np.sqrt(eps)*np.array([float(z) for z in entries(u)])
 f=np.array([float(v0[i]+arb(str(eps))*x[28+i]) for i in range(15)])
 lam=float(-rho+arb(str(eps))*x[43]);return X,f,lam
def jet_product(a,b):
 return [sum((a[i]@b[k-i] for i in range(k+1)),np.zeros_like(a[0])) for k in range(3)]
def magnetic_coefficient(U,beta,kappa):
 r=U.shape[1];J=[]
 for e in range(28):
  H=np.zeros((r,r),complex);H[1:,0]=beta[e];H[0,1:]=beta[e].conjugate()
  J.append([U[e],1j*H@U[e],-.5*H@H@U[e]])
 result=0.
 for es in ds:
  w=[np.eye(r,dtype=complex),np.zeros((r,r),complex),np.zeros((r,r),complex)]
  for p,e in enumerate(es):
   j=J[e];j=[x.conj().T for x in j] if p<2 else j;w=jet_product(w,j)
  result-=kappa/r*np.trace(w[2]).real
 return result
def energy(U,E,p,z,a,kappa):
 r=U.shape[1];v=a/2*sum(np.trace(x@x).real for x in E)
 for es in ds:v+=kappa*(1-np.trace(U[es[0]].conj().T@U[es[1]].conj().T@U[es[2]]@U[es[3]]).real/r)
 for e,(i,j) in enumerate(edges):v+=2*bn[e]*(np.vdot(p[i],U[e]@p[j]).imag+np.vdot(z[i],U[e]@z[j]).imag)
 return float(v)
rng=np.random.default_rng(161026);rows=[]
for k,eps,r,N,a in [(1,1e-5,2,1.,1.),(1,5e-6,3,2.,.4),(2,1e-5,3,1.,1.),(3,1e-5,2,1.,1.)]:
 X,f,lam=profile(k,eps);u=-1j*bn*np.exp(1j*X);kap=r*N*(float(kc)+eps)
 U=np.array([np.diag([ue]+[1]*(r-1)) for ue in u],complex)
 E0=np.zeros_like(U);p0=np.zeros((15,r),complex);p0[:,0]=np.sqrt(N)*f
 beta=(rng.normal(size=(28,r-1))+1j*rng.normal(size=(28,r-1)))/8
 Q=(rng.normal(size=(15,r-1))+1j*rng.normal(size=(15,r-1)))/8
 ee=(rng.normal(size=(28,r-1))+1j*rng.normal(size=(28,r-1)))/8
 qm=magnetic_coefficient(U,beta,kap)
 scalar_sum=sum(magnetic_coefficient(U[:,:2,:2],beta[:,j:j+1],2*N*(float(kc)+eps)) for j in range(r-1))
 assert abs(qm-scalar_sum)<1e-13
 pred=a*np.vdot(ee,ee).real+sum(np.vdot(Q[:,j],(h0-lam*np.eye(15))@Q[:,j]).real for j in range(r-1))
 pred+=sum(2*N*f[i]*f[j]*np.cos(X[e])*np.vdot(beta[e],beta[e]).real for e,(i,j) in enumerate(edges))+qm
 values=[];step=2e-4
 for sign in [-1,1]:
  t=sign*step;U1=[];E1=[]
  for e in range(28):
   H=np.zeros((r,r),complex);H[1:,0]=beta[e];H[0,1:]=beta[e].conjugate();U1.append(expm(1j*t*H)@U[e])
   G=np.zeros((r,r),complex);G[1:,0]=ee[e];G[0,1:]=ee[e].conjugate();E1.append(t*G)
  p=p0.copy();z=p0.copy();fac=np.sqrt(1-t*t*np.vdot(Q,Q).real/(2*N));p[:,0]*=fac;z[:,0]*=fac
  p[:,1:]=t*Q/np.sqrt(2);z[:,1:]=-t*Q/np.sqrt(2)
  values.append(energy(np.array(U1),np.array(E1),p,z,a,kap))
 observed=(sum(values)-2*energy(U,E0,p0,p0,a,kap))/(2*step**2)
 assert abs(observed-pred)<2e-6
 # Reconstruct the Hermitian magnetic matrix in one inactive color by polarization.
 U2=U[:,:2,:2];kap2=2*N*(float(kc)+eps);Mmag=np.zeros((28,28),complex)
 def q(v):return magnetic_coefficient(U2,v[:,None],kap2)
 eye=np.eye(28);di=np.array([q(v) for v in eye]);np.fill_diagonal(Mmag,di)
 for i in range(28):
  for j in range(i+1,28):
   re=(q(eye[i]+eye[j])-di[i]-di[j])/2;im=-(q(eye[i]+1j*eye[j])-di[i]-di[j])/2
   Mmag[i,j]=re+1j*im;Mmag[j,i]=re-1j*im
 S=Mmag+np.diag([2*N*f[i]*f[j]*np.cos(X[e]) for e,(i,j) in enumerate(edges)])
 Ru=np.zeros((15,28),complex)
 for e,(i,j) in enumerate(edges):Ru[i,e]=1;Ru[j,e]=-u[e]
 FI=np.diag(1/f);M=a*np.eye(28)+Ru.conj().T@FI@(h0-lam*np.eye(15))@FI@Ru/(2*N)
 mv,V=eigh(M);mh=(V*np.sqrt(mv))@V.conj().T;omega2=eigh(mh@S@mh,eigvals_only=True)
 assert eigh(S,eigvals_only=True)[0]>N/16 and omega2[0]>a*N/16
 assert np.linalg.norm(Mmag,2)<3*N/200
 rows.append({'family_k':k,'epsilon':eps,'rank':r,'N':N,'a':a,'quadratic_predicted':float(pred),'quadratic_observed':observed,'absolute_difference':abs(observed-pred),'magnetic_additivity_residual':abs(qm-scalar_sum),'magnetic_operator_norm_over_N':float(np.linalg.norm(Mmag,2)/N),'link_energy_min_eigenvalue_over_N':float(eigh(S,eigvals_only=True)[0]/N),'minimum_color_squared_frequency_over_aN':float(omega2[0]/(a*N))})
report={'status':'PASS','type':'NUMERICAL synthetic diagnostic; neither interval proof nor empirical data','central_difference_step':2e-4,'seed':161026,'fixtures':rows,'physical_promotion':0,'independent_review':'PENDING'}
(O/'MATRIX_HESSIAN_DIAGNOSTIC_v0.1.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
