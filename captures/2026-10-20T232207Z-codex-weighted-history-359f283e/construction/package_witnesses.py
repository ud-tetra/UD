from pathlib import Path
import gzip,json,math,functools,zipfile,hashlib
import numpy as np
from scipy.sparse import csr_matrix
from flint import nmod_mat
P=Path('/workspace/scratch/f3d1c2f040c9');O=P/'c26_work'
with zipfile.ZipFile(O/'UPPER_WITNESSES.zip','w',compression=zipfile.ZIP_DEFLATED,compresslevel=9)as z:
 for f in sorted((O/'upper').glob('*.gz')):
  d=json.loads(gzip.decompress(f.read_bytes()));bs=[];ds=[]
  for row in d['basis_rows']:
   a=list(map(int,row));g=functools.reduce(math.gcd,a);g=g if int(d['denominator'])>0 else -g;bs.append([str(x//g)for x in a]);ds.append(str(int(d['denominator'])//g))
  d['basis_rows']=bs;d['row_denominators']=ds;d.pop('denominator');d['membership_identity']='For each j: V[:,piv]*B[:,j] with rowwise denominators equals V[:,j]; B[:,piv]=diag(row_denominators)'
  info=zipfile.ZipInfo(f.stem.removesuffix('.json')+'.json',date_time=(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED
  z.writestr(info,(json.dumps(d,separators=(',',':'))+'\n').encode())
with np.load(O/'OPERATORS.npz',allow_pickle=False)as z:G=z['G'];C=z['C0'];MW=z['MW'];CW=z['CW'];J=z['J']
rec=[];p=1009
for label,A,U in [('nominal',G,C),('weighted',MW,CW),('augmented_nominal',G,np.vstack([C,np.eye(600,dtype=np.int64)[J]]))]:
 v=U.copy()%p;rows=[];op=csr_matrix(A)
 for j in range(600):rows.append(v);v=(op@v.T).T%p
 H=np.vstack(rows);T=nmod_mat(H.T.tolist(),p);E,r=T.rref();ri=[next(j for j in range(H.shape[0])if E[i,j])for i in range(r)]
 V=nmod_mat(H[ri].tolist(),p);E,r2=V.rref();assert r2==r;ci=[next(j for j in range(600)if E[i,j])for i in range(r)]
 det=int(nmod_mat(H[np.ix_(ri,ci)].tolist(),p).det());assert det
 rec.append({'case':label,'prime':p,'rows_time_major':ri,'columns':ci,'determinant_mod_prime':det,'rank_lower':r,'seed_rows':len(U),'powers_checked':600,'max_selected_power':max(ri)//len(U)})
 print(label,r,det,flush=True)
(O/'LOWER_WITNESSES.json').write_text(json.dumps({'status':'NONZERO_MODULAR_MINORS','witnesses':rec},indent=2)+'\n')
print('archive bytes', (O/'UPPER_WITNESSES.zip').stat().st_size)
