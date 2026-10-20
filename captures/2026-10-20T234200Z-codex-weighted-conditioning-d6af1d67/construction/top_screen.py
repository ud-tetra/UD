from pathlib import Path
import json,zipfile,gzip
import numpy as np
from scipy.linalg import eigh,svd,qr
P=Path('/workspace/scratch/f3d1c2f040c9');O=P/'c27_work';O.mkdir(exist_ok=True)
with np.load(P/'c26_work/OPERATORS.npz',allow_pickle=False)as z:G=z['G'];C=z['C0'];MW=z['MW'];CW=z['CW'];J=z['J']
factors=json.loads((P/'c26_work/FACTOR_CERTIFICATE.json').read_text())['factors'];ev,V=eigh(G.astype(float));blocks=[];offset=0
for f in factors:
 cs=f['coefficients_ascending'];r=f['augmented_upper']
 if not r:continue
 roots=np.polynomial.polynomial.polyroots(cs)
 for root in roots:
  assert abs(root.imag)<1e-8;inds=np.flatnonzero(abs(ev-root.real)<1e-7);E=V[:,inds];U=np.vstack([C,np.eye(600)[J]]);A=U@E
  Z,s,W=svd(A,full_matrices=False);rank=r//(len(cs)-1);assert rank<=len(s)and s[rank-1]>1e-9
  blocks.append(E@W[:rank].T)
Q=np.hstack(blocks);assert Q.shape==(600,444);print('Qerr',np.linalg.norm(Q.T@Q-np.eye(444)),flush=True)
T=Q.T@MW@Q;vals,U=eigh(T);print('minvals',vals[:8],flush=True);I=vals>1e-9;assert sum(I)==443
U=Q@U[:,I];om=np.sqrt(vals[I])/2;E=(CW@U)/np.sqrt(vals[I])[None,:];# R2 BD u /omega
# scalar sums for4096 samples j/2
M=4096;theta=om/2
def geom(t):
 return np.exp(1j*(M-1)*t/2)*np.sinc(M*t/(2*np.pi))/np.sinc(t/(2*np.pi))
minus=geom(theta[:,None]-theta[None,:]);plus=geom(theta[:,None]+theta[None,:]);EE=E.T@E
CC=EE*(minus.real+plus.real)/2;SS=EE*(minus.real-plus.real)/2
CS=EE*(plus.imag-minus.imag)/2 # cos_i sin_j: sin(a+b)+sin(b-a)
H=np.block([[CC,CS],[CS.T,SS]]);s,Z=eigh(H)
print('gram extremes',s[:20],s[-1],flush=True)
energy=np.sum(E*E,axis=0);ix=np.argsort(energy);print('small modal energies',[(int(i),float(om[i]),float(energy[i]))for i in ix[:15]],flush=True)
np.savez(O/'SCREEN.npz',W=Q,U=U,omega=om,E=E,gram_values=s,gram_vectors=Z,top_modal_energies=energy)
(O/'SCREEN.json').write_text(json.dumps({'status':'NUMERICAL_SCREEN_ONLY_NOT_CERTIFICATE','W_orthogonality_error':float(np.linalg.norm(Q.T@Q-np.eye(444))),'gram_min':float(s[0]),'gram_max':float(s[-1]),'small_modal_indices':ix[:20].tolist(),'small_modal_energies':energy[ix[:20]].tolist(),'small_modal_omega':om[ix[:20]].tolist(),'physical_promotion':0},indent=2)+'\n')
