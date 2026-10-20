from pathlib import Path
import json,zipfile
from collections import defaultdict
import numpy as np
from scipy.linalg import eigh,svd
P=Path('/workspace/scratch/f3d1c2f040c9');O=P/'c27_work'
Z=P/'ud-repo/captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/recovered/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.zip'
with zipfile.ZipFile(Z)as z:S=json.loads(z.read('sources/COMPLEX_AND_ACTION.json'))['simplices'];obs=json.loads(z.read('modular_results.json'))['observed_indices']
S=[[tuple(s)for s in g]for g in S];ix=[{s:i for i,s in enumerate(g)}for g in S];Bs=[]
for k in [1,2,3]:
 B=np.zeros((len(S[k-1]),len(S[k])))
 for j,s in enumerate(S[k]):
  for m in range(k+1):B[ix[k-1][s[:m]+s[m+1:]],j]=(-1)**m
 Bs.append(B)
off=[0,120,840,2040];ob=[np.array([i-off[k]for i in obs if off[k]<=i<off[k]+len(S[k])])for k in range(4)]
Qcols=[];omega=[];pairs=[]
# zero harmonic grade0
q=np.zeros((2640,1));q[:120]=1/np.sqrt(120);Qcols.append(q);omega.append(0.)
for k in [1,2,3]:
 B=Bs[k-1].copy()
 if k==3:
  D=np.ones(600);D[[0,9,227,432,447,582,538,347,332,141]]=1.5;B*=D[None,:]
  z=np.load(O/'SCREEN.npz',allow_pickle=False);V=z['U'];w=z['omega'];U=B@V/w[None,:]
 else:
  vals,U0=eigh(B@B.T);groups=[]
  for i in np.flatnonzero(vals>1e-8):
   if not groups or abs(vals[i]-vals[groups[-1][0]])>1e-7:groups.append([i])
   else:groups[-1].append(i)
  us=[];ws=[]
  for inds in groups:
   E=U0[:,inds];Z,s,W=svd(E[ob[k-1]],full_matrices=False);r=sum(s>1e-8)
   us.append(E@W[:r].T);ws.extend([np.sqrt(np.mean(vals[inds]))]*r)
  U=np.hstack(us);w=np.array(ws);V=B.T@U/w[None,:]
 n=len(w);print('channel',k,n,flush=True)
 start=len(omega);qu=np.zeros((2640,n));qv=np.zeros((2640,n));qu[off[k-1]:off[k]]=U;qv[off[k]:off[k]+len(S[k])]=V;Qcols.extend([qu,qv]);omega.extend(w.tolist()+w.tolist());pairs.extend([(start+i,start+n+i,float(w[i]))for i in range(n)])
Q=np.hstack(Qcols);assert Q.shape==(2640,1999);Y=Q[obs];K=np.zeros((2640,2640))
for k,B in enumerate(Bs,1):
 if k==3:B=B*D[None,:]
 K[off[k-1]:off[k],off[k]:off[k]+len(S[k])]=B;K[off[k]:off[k]+len(S[k]),off[k-1]:off[k]]=-B.T
T=np.zeros((1999,1999))
for u,v,w in pairs:T[u,v]=w;T[v,u]=-w
print('Qerr',np.linalg.norm(Q.T@Q-np.eye(1999)),'E',np.linalg.norm(K@Q-Q@T),flush=True)
# Reorder to uniform a,b pair indexing including zero with b=0
ui=[0]+[x[0]for x in pairs];vi=[0]+[x[1]for x in pairs];w=np.array([0.]+[x[2]for x in pairs]);A=Y[:,ui];B=Y[:,vi].copy();B[:,0]=0
M=4096;th=w/2
# finite geometric average stable at zero
geom=lambda t:np.exp(1j*(M-1)*t/2)*np.sinc(M*t/(2*np.pi))/np.sinc(t/(2*np.pi))
diff=geom(th[:,None]-th[None,:]);add=geom(th[:,None]+th[None,:]);cc=(diff.real+add.real)/2;ss=(diff.real-add.real)/2;cs=(add.imag-diff.imag)/2;sc=cs.T
AA=A.T@A;AB=A.T@B;BA=AB.T;BB=B.T@B
# initialu: A cos - B sin; initialv:A sin+B cos
Huu=AA*cc-AB*cs-BA*sc+BB*ss;Hvv=AA*ss+AB*sc+BA*cs+BB*cc;Huv=AA*cs+AB*cc-BA*ss-BB*sc
H=np.block([[Huu,Huv[:,1:]],[Huv[:,1:].T,Hvv[1:,1:]]]);vals,Z=eigh(H);print('FULL GRAM',vals[:15],vals[-1],'kappa',np.sqrt(vals[-1]/vals[0]),flush=True)
order=ui+vi[1:];Q=Q[:,order];Y=Y[:,order];ww=w.tolist()+w[1:].tolist()
np.savez(O/'FULL_SCREEN.npz',Q=Q,frequencies=w,Gram=H,Gram_values=vals,Gram_vectors=Z,ordered_readout=Y)
(O/'FULL_SCREEN.json').write_text(json.dumps({'status':'NUMERICAL_SCREEN_ONLY_NOT_CERTIFICATE','rank':1999,'gram_min':float(vals[0]),'gram_max':float(vals[-1]),'kappa':float(np.sqrt(vals[-1]/vals[0])),'distinct_positive_frequencies_1e-7':int(1+sum(np.diff(np.sort(w[1:]))>1e-7)),'physical_promotion':0},indent=2)+'\n')
