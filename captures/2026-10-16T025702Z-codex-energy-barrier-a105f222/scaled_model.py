"""Regularized full stationary system and its rigorous Arb enclosure."""
from math import factorial
from geometry import *
Vlev=[arb(1),rho/3,(1+D0)/3,4*(1+D0)/(3*rho)];ell0=16*(10+D0)/9
v0=[Vlev[len(t)-1]/ell0.sqrt() for t in nodes];K=Cmat.transpose()*Cmat
H0=diag([4*v0[i]*v0[j] for i,j in edges])-kc*K
P=arb_mat(28,28)
for i in range(28):P[i,i]=1
P-=Z*(Z.transpose()*Z).inv()*Z.transpose()
pivots=[0,1,3];columns=[i for i in range(28) if i not in pivots];Y=arb_mat([[P[i,j] for j in columns] for i in range(28)]);HY=H0*Y

def ipow(a,n):
 out=arb(1)
 for _ in range(n):out*=a
 return out

def regular(z,shift,N=18):
 """sum (-1)^(n+1) z^n/(2n+shift)! and its z derivative, with geometric tail."""
 assert z.abs_upper()<4
 out=arb(0);der=arb(0);pow=arb(1)
 for n in range(N):
  coeff=arb((-1)**(n+1))/factorial(2*n+shift);out+=coeff*pow
  if n:der+=coeff*n*ipow(z,n-1)
  pow*=z
 tail=2*ipow(arb(4),N)/factorial(2*N+shift);dtail=2*N*ipow(arb(4),N-1)/factorial(2*N+shift)
 return out+ball(tail.upper()),der+ball(dtail.upper())

def eval_scaled(x,t,jac=True,dt=False):
 b=x[:3];cc=x[3:28];ss=x[28:43];lam=x[43]
 yc=entries(Y*col(cc));u=entries(Z*col(b)+t*col(yc));f=[v0[i]+t*ss[i] for i in range(15)];ph=entries(Cmat*col(u));cu=entries(Cmat*col(yc))
 U=arb_mat([[Z[i,j] if j<3 else t*Y[i,j-3] for j in range(28)] for i in range(28)])
 Fn=entries(HY*col(cc)-K*col(u));En=[rho*ss[i]-lam*f[i] for i in range(15)];J=arb_mat(44,44);Ju=arb_mat(28,28);Eu=arb_mat(15,28);Gt=[zero]*44
 for e,(i,j) in enumerate(edges):
  a=u[e];aa=v0[i]*ss[j]+ss[i]*v0[j]+t*ss[i]*ss[j];S,Sz=regular(t*a*a,3);Co,Cz=regular(t*a*a,2);ff=f[i]*f[j]
  Fn[e]+=4*aa*a+4*ff*ipow(a,3)*S
  En[i]-=ss[j]+a*a*Co*f[j];En[j]-=ss[i]+a*a*Co*f[i]
  if jac:
   Ju[e,e]=4*aa+4*ff*(3*a*a*S+2*t*ipow(a,4)*Sz)
   J[e,28+i]=4*f[j]*(a+t*ipow(a,3)*S);J[e,28+j]=4*f[i]*(a+t*ipow(a,3)*S)
   Eu[i,e]=-f[j]*(2*a*Co+2*t*ipow(a,3)*Cz);Eu[j,e]=-f[i]*(2*a*Co+2*t*ipow(a,3)*Cz)
   J[28+i,28+j]=-1-t*a*a*Co;J[28+j,28+i]=-1-t*a*a*Co
  if dt:
   a1=yc[e];z1=a*a+2*t*a*a1
   Gt[e]+=4*(ss[i]*ss[j]*a+aa*a1)+4*((ss[i]*f[j]+f[i]*ss[j])*ipow(a,3)*S+ff*(3*a*a*a1*S+ipow(a,3)*Sz*z1))
   Gt[28+i]-=(2*a*a1*Co+a*a*Cz*z1)*f[j]+a*a*Co*ss[j]
   Gt[28+j]-=(2*a*a1*Co+a*a*Cz*z1)*f[i]+a*a*Co*ss[i]
 for d in range(18):
  a=ph[d];S,Sz=regular(t*a*a,3);fac=(kc+t)*ipow(a,3)*S;der=(kc+t)*(3*a*a*S+2*t*ipow(a,4)*Sz)
  for e in range(28):
   if C[d][e]:
    Fn[e]-=C[d][e]*fac
    if jac:
     for j in range(28):
      if C[d][j]:Ju[e,j]-=C[d][e]*der*C[d][j]
    if dt:Gt[e]-=C[d][e]*(ipow(a,3)*S+(kc+t)*(3*a*a*cu[d]*S+ipow(a,3)*Sz*(a*a+2*t*a*cu[d])))
 if jac:
  Ju-=K;Jtop=Ju*U;Jbot=Eu*U
  for i in range(28):
   for j in range(28):J[i,j]=Jtop[i,j]+(HY[i,j-3] if j>=3 else 0)
  for i in range(15):
   for j in range(28):J[28+i,j]=Jbot[i,j]
   J[28+i,28+i]=rho-t*lam;J[28+i,43]=-f[i];J[43,28+i]=2*f[i]
 Fn+=En+[2*sum(v0[i]*ss[i] for i in range(15))+t*sum(a*a for a in ss)]
 if dt:
  kt=entries(K*col(yc))
  for e in range(28):Gt[e]-=kt[e]
  for i in range(15):Gt[28+i]-=lam*ss[i]
  Gt[43]=sum(a*a for a in ss)
 return col(Fn),J,col(Gt)

def refine_scaled(x,t):
 x=[midpoint(a) if isinstance(a,arb) else point(str(a)) for a in x]
 for _ in range(5):
  F,J,_=eval_scaled(x,t);step=entries(J.inv()*F);x=[midpoint(a-b) for a,b in zip(x,step)]
 return x

def validate_scaled(x,ti,verbose=False):
 tm=ti.mid();Fc,Jc,_=eval_scaled(x,tm);inv=Jc.inv();A=arb_mat([[midpoint(t) for t in row] for row in inv.tolist()]);Ft,_,Gti=eval_scaled(x,ti,False,True)
 vals=entries(A*Fc+(A*Gti)*(ti-tm));weights=[arb(1)]*3+[arb(1000)]*25+[arb(10)]*15+[arb(100)]
 eta=maxupper([vals[i]/weights[i] for i in range(44)]);rad=2*eta+arb('1e-25')
 for attempt in range(4):
  if verbose:print('RADIUS',float(rad),flush=True)
  rr=[rad*w for w in weights];X=[a+ball(r.upper()) for a,r in zip(x,rr)];_,J,Gt=eval_scaled(X,ti,True,True)
  M=arb_mat(44,44)
  for i in range(44):M[i,i]=1
  M-=A*J;q=maxupper([sum(M[i,j].abs_upper()*rr[j] for j in range(44))/rr[i] for i in range(44)]);inc=maxupper([(vals[i].abs_upper()+sum(M[i,j].abs_upper()*rr[j] for j in range(44)))/rr[i] for i in range(44)])
  if verbose:print('SCALED',float(rad),float(q),float(inc),flush=True)
  if q<arb('9/10') and inc<arb('99/100'):
   dermax=maxupper([v/weights[i] for i,v in enumerate(entries(A*Gt))])/(1-q)
   return {'X':X,'r':rr,'q':q,'inc':inc,'weights':weights,'derivative_weighted_bound':dermax,'A':A,'M':M,'x':x,'parameter':ti}
  rad*=2
 return None

def congruence(A):
 import numpy as np
 vals,V=np.linalg.eigh(np.array([[float(A[i,j].mid()) for j in range(A.ncols())] for i in range(A.nrows())]));T=V/np.sqrt(abs(vals));T=arb_mat([[point(str(t)) for t in row] for row in T]);B=T.transpose()*A*T
 signs=[];margin=[]
 for i in range(B.nrows()):
  off=sum(B[i,j].abs_upper() for j in range(B.nrows()) if i!=j)
  if not B[i,i].abs_lower()>off:return None
  signs.append(B[i,i]<0);margin.append(B[i,i].abs_lower()-off)
 return {'inertia':sum(signs),'T':T,'B':B,'margin':min(t.lower() for t in margin)}

def certified_inverse(A,positive=True):
 c=congruence(A)
 if c is None or (positive and c['inertia']!=0):raise ValueError('congruence failed')
 return c['T']*c['B'].inv()*c['T'].transpose()

def scaled_hessians(x,t):
 cc=x[3:28];ss=x[28:43];u=entries(Z*col(x[:3])+t*Y*col(cc));f=[v0[i]+t*ss[i] for i in range(15)];phi=entries(Cmat*col(u));kap=kc+t
 wc=[];ws=[];wa=[]
 for e,(i,j) in enumerate(edges):
  a=u[e];S,_=regular(t*a*a,3);Co,_=regular(t*a*a,2);ff=f[i]*f[j]
  wc.append(ff*(1+t*a*a*Co));ws.append(ff*a*(1+t*a*a*S));wa.append(v0[i]*ss[j]+ss[i]*v0[j]+t*ss[i]*ss[j]+ff*a*a*Co)
 cm=[]
 for a in phi:
  Co,_=regular(t*a*a,2);cm.append(a*a*Co)
 A=4*diag(wa)-K-kap*Cmat.transpose()*diag(cm)*Cmat
 Si=diag([1/(a*a) for a in f]);Rt=Rmat.transpose();Qt=Qd.transpose();Ar=arb_mat([[abs(i) for i in row] for row in R]);J=Rt*Si*Rmat;Jp=Ar.transpose()*Si*Rmat
 B=diag(ws)*Ar.transpose()*Si*Qd
 D=Qt*Si*Rmat*diag(wc)*Rt*Si*Qd/4
 eye=arb_mat(28,28)
 for i in range(28):eye[i,i]=1
 P=eye+J.transpose()*diag(wc)*J/4
 Q=-Jp.transpose()*diag(ws)*Rt*Qd
 T=4*Qt*Rmat*diag(wc)*Rt*Qd
 return A,B,D,P,Q,T

def configuration_inertia(x,t):
 A,B,D,_,_,_=scaled_hessians(x,t)
 try:
  Di=certified_inverse(D);Tr=A-B*Di*B.transpose();Fast=Y.transpose()*(H0+t*Tr)*Y;Fi=certified_inverse(Fast)
  Cr=Z.transpose()*Tr*Z-t*Z.transpose()*Tr*Y*Fi*Y.transpose()*Tr*Z;c=congruence(Cr)
  return None if c is None else c['inertia']
 except (ValueError,ZeroDivisionError):return None

def sector_arrays(name,source):
 import numpy as np
 B=arb_mat([[arb(t) for t in row] for row in source[name]['phase_basis']]);Bd=arb_mat([[arb(t) for t in row] for row in source[name]['density_basis']])
 z=arb_mat([[Z[i,0]] for i in range(28)]) if name=='radial' else arb_mat([[(Z[i,1]+Z[i,2])/arb(2).sqrt()] for i in range(28)])
 proj=B-z*(z.transpose()*B)/(z.transpose()*z)[0,0]
 _,_,piv=__import__('scipy.linalg',fromlist=['qr']).qr(np.array(proj.tolist(),float),pivoting=True);sel=list(piv[:B.ncols()-1]);W=arb_mat([[proj[i,int(j)] for j in sel] for i in range(28)]);S=arb_mat([[z[i,0]]+[W[i,j] for j in range(W.ncols())] for i in range(28)]);Sd=S*(S.transpose()*S).inv();Bdd=Bd*(Bd.transpose()*Bd).inv()
 return S,Sd,Bd,Bdd

def sector_spectral(x,t,w,arrays):
 S,Sd,Bd,Bdd=arrays
 # Full analytic blocks with Qd removed from the density factors.
 A,B0,D0p,P,Q0,T0=scaled_hessians(x,t);Dfull=Qd*D0p*Qd.transpose();Bfull=B0*Qd.transpose();Qfull=Q0*Qd.transpose();Tfull=Qd*T0*Qd.transpose()
 A=S.transpose()*A*S;B=S.transpose()*Bfull*Bd;D=Bd.transpose()*Dfull*Bd;P=Sd.transpose()*P*Sd;Q=Sd.transpose()*Qfull*Bdd;T=Bdd.transpose()*Tfull*Bdd
 try:
  Pi=certified_inverse(P);Wi=certified_inverse(T-t*Q.transpose()*Pi*Q);U=Pi+t*Pi*Q*Wi*Q.transpose()*Pi;V=-Pi*Q*Wi;Bb=B-t*w*V;Tr=A-w*U-Bb*certified_inverse(D-t*w*Wi)*Bb.transpose()
  m=S.ncols();F=arb_mat([[ (S.transpose()*H0*S)[i,j]+t*Tr[i,j] for j in range(1,m)] for i in range(1,m)]);Fi=certified_inverse(F)
  vf=arb_mat([[Tr[0,j] for j in range(1,m)]]);val=Tr[0,0]-t*(vf*Fi*vf.transpose())[0,0]
  if val.contains(0):return None
  return {'negative':int(val<0),'margin':val.abs_lower()}
 except (ValueError,ZeroDivisionError):return None
