from pathlib import Path
from collections import defaultdict
import json,zipfile,time,hashlib
import numpy as np
from scipy.sparse import csr_matrix
from flint import nmod_mat
P=Path('/workspace/scratch/f3d1c2f040c9');R=P/'ud-repo';O=P/'c26_work';O.mkdir(exist_ok=True)
Z=R/'captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/recovered/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.zip'
with zipfile.ZipFile(Z)as z:C=json.loads(z.read('sources/COMPLEX_AND_ACTION.json'));M=json.loads(z.read('modular_results.json'))
S=[[tuple(s)for s in g]for g in C['simplices']];fi={s:i for i,s in enumerate(S[2])};B=np.zeros((1200,600),dtype=np.int64)
for j,s in enumerate(S[3]):
 for k in range(4):B[fi[s[:k]+s[k+1:]],j]=(-1)**k
G=B.T@B;C0=B[[i-840 for i in M['observed_indices']if 840<=i<2040]];J=json.loads((P/'c26_plan.json').read_text())['tetrahedron_indices'];d=np.full(600,2,dtype=np.int64);d[J]=3;MW=d[:,None]*G*d[None,:];CW=C0*d[None,:]
np.savez(O/'OPERATORS.npz',G=G,C0=C0,MW=MW,CW=CW,J=J)
rows=[]
for label,A,U in [('nominal',G,C0),('weighted',MW,CW),('augmented_nominal',G,np.vstack([C0,np.eye(600,dtype=np.int64)[J]]))]:
 for prime in[1009]:
  start=time.perf_counter();op=csr_matrix(A);powers=[];v=U.copy()%prime
  for j in range(600):powers.append(v);v=(op@v.T).T%prime
  H=np.vstack(powers);rank=nmod_mat(H.tolist(),prime).rank();rec={'case':label,'prime':prime,'rows':len(H),'columns':600,'powers':600,'modular_rank':rank,'elapsed_seconds':time.perf_counter()-start};rows.append(rec);print(json.dumps(rec),flush=True)
(O/'SCREEN.json').write_text(json.dumps({'status':'MODULAR_LOWER_BOUNDS_ONLY','rows':rows,'physical_promotion':0},indent=2)+'\n')
