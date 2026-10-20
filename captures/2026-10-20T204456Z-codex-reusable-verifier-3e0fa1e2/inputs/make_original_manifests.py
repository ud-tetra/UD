from pathlib import Path
import hashlib,json,numpy as np
root=Path('/workspace/scratch/f3d1c2f040c9')
source=root/'ud-repo/captures/2026-10-20T183427Z-codex-maximal-noise-e5831029'
def row(p):return {'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
for short in ['block','rotating']:
 case='boundary_pair_'+short
 n=root/'c18_work'/case/'N.npy'
 run=source/'campaign/cases'/case/'results'/case
 record=row(n);record.update(payload_sha256=hashlib.sha256(np.load(n,allow_pickle=False).tobytes(order='C')).hexdigest(),dyadic_exponent=55)
 spec={'schema_version':'1.0','record':record,'svd':row(run/'SVD_META.npz'),'left_chunks':[]}
 for j,(a,b) in enumerate([(0,2731),(2731,5462),(5462,8191)]):
  r=row(run/f'U_{j}.npz');r.update(start=a,stop=b);spec['left_chunks'].append(r)
 (root/f'c20_{short}_manifest.json').write_text(json.dumps(spec,indent=2,sort_keys=True)+'\n')
 print(short,record['payload_sha256'])
