"""Pin current producer bytes, exact-power receipts, and hostile write guards."""
import hashlib,json,subprocess,sys,tempfile
from pathlib import Path
import numpy as np
from flint import fmpz_mat
P=Path(__file__).resolve().parent
ROOT=P.parent
PROD=ROOT/'phase-uniform-20261019'
REPO=ROOT/'ud-repo'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 f=json.loads((P/'ADDITIONAL_FREEZE.json').read_text())
 for rel,digest in f['files'].items():assert sha(ROOT/rel)==digest
 source=json.loads((PROD/'INPUT_BINDINGS.json').read_text())
 for row in source['files']:
  assert sha(PROD/row['local_path'])==sha(REPO/row['repository_path'])==row['sha256']
 frozen=json.loads((PROD/'FREEZE_v2.json').read_text())
 for rel,digest in frozen['files'].items():assert sha(PROD/rel)==digest
 null=json.loads((PROD/'inputs/NULL_VECTOR.json').read_text())['vector']
 A=np.zeros((2294,321),dtype=np.int64)
 A[:,:160]=2*np.random.default_rng(172026).choice([-1.,1.],(2294,160)).astype(np.int64)
 A[:len(null),160]=null
 A[:,161:]=2*np.random.default_rng(184052).choice([-1.,1.],(2294,160)).astype(np.int64)
 G=fmpz_mat((A.T@A).tolist()); cert=json.loads((ROOT/'phase-uniform-primary-20261019/CERTIFICATE.json').read_text())
 powers=[]
 for receipt in cert['sketch']['power_bounds']:
  k=receipt['power'];W=G**k
  exact=max(sum(abs(int(W[i,j])) for j in range(321)) for i in range(321))
  assert str(exact)==receipt['exact_max_absolute_row_sum'];powers.append(k)
 assert powers==[1,2,4,8,16,32]
 assert hashlib.sha256(np.array(G.tolist(),dtype='<i8').tobytes()).hexdigest()==cert['sketch']['Gram_int64le_sha256']
 guardrows=[]
 with tempfile.TemporaryDirectory(prefix='phase-review-guard-',dir=ROOT) as t:
  t=Path(t);outer=t/'outer';inner=outer/'inner';stage=inner/'producer';stage.mkdir(parents=True)
  (outer/'MANIFEST.json').write_text('{}');(inner/'MANIFEST.json').write_text('{}')
  staged=stage/'certify_v2.py';staged.write_bytes((PROD/'certify_v2.py').read_bytes())
  (t/'link_inside').symlink_to(inner,target_is_directory=True)
  elsewhere=t/'elsewhere';elsewhere.mkdir();(inner/'link_outside').symlink_to(elsewhere,target_is_directory=True)
  cases=[('inside_self',stage/'new'),('inside_inner_capture',inner/'sibling'),('inside_outer_capture',outer/'sibling'),('ancestor_of_source',t),('symlink_target_inside',t/'link_inside/new'),('symlink_lexical_inside',inner/'link_outside/new')]
  for name,out in cases:
   cmd=[sys.executable,str(staged),'--repo',str(REPO),'--out',str(out)]
   completed=subprocess.run(cmd,capture_output=True,text=True,env={'PYTHONDONTWRITEBYTECODE':'1','OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1'})
   assert completed.returncode!=0 and 'HOLD ' in completed.stderr,(name,completed.returncode,completed.stderr)
   assert not (out/'CERTIFICATE.json').exists()
   guardrows.append(dict(id=name,status='REFUSED_BEFORE_OUTPUT_OR_SOURCE_BINDING',returncode=completed.returncode))
 # Exactly integer support patterns for squared lattice length<=2.
 count=1+2*62+4*(62*61//2);assert count==7689
 result=dict(status='PASS_SOURCE_BINDINGS_SIX_POWERS_AND_SIX_HOSTILE_GUARDS',power_exponents=powers,input_bindings=len(source['files']),guards=guardrows,per_vector_lattice_patterns=count,lattice_extension='All integer records with each squared norm <3q^2 coincide with closed3q/2 ball; no boundary3q^2 claim',new_fits=0,new_SVD_or_eigenvalue_calls=0,external_review='PENDING',physical_promotion=0)
 (P/'ADDITIONAL_REVIEW.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(dict(status=result['status'],powers=len(powers),guards=len(guardrows),patterns=count)))
if __name__=='__main__':main()
