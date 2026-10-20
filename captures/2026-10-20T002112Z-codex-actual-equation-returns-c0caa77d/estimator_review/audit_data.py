"""Independent pre-fit rank-one projection audit; no estimator or new raw file."""
import argparse,json,hashlib
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
SHA=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 a=argparse.ArgumentParser();a.add_argument('--repo',required=True);a.add_argument('--baseline',required=True);args=a.parse_args();repo=Path(args.repo).resolve();base=Path(args.baseline).resolve();f=json.loads((P/'DATA_AUDIT_FREEZE.json').read_text());assert SHA(Path(__file__))==f['code_sha256']
 for name,h in f['repo_sources'].items():assert SHA(repo/name)==h,name
 assert SHA(base)==f['baseline_sha256'] and base.stat().st_size==37*8191*62*8
 old=json.loads((repo/f['old_certificate']).read_text());v=np.zeros(2294,np.int64);small=json.loads((repo/f['null_path']).read_text())['vector'];v[:len(small)]=small
 # Independent construction reads the pinned fixed RNG definitions, not producer functions.
 oldS=np.random.default_rng(172026).choice([-1.,1.],(2294,160)).astype(np.int64);newS=np.random.default_rng(184052).choice([-1.,1.],(2294,160)).astype(np.int64);A=np.column_stack([2*oldS,v,2*newS]);Y=np.memmap(base,dtype='<i8',mode='r',shape=(37,8191,62));X=np.asarray(Y.transpose(1,2,0).reshape(8191,2294),dtype=np.int64)
 partial=max(abs(int(X.min())),abs(int(X.max())))*max(int(x)for x in np.abs(A).sum(axis=0));assert partial<2**63;N0=X@A;del X
 u=np.ones(8191,np.int64);u[1::2]=-1;rows=[]
 for count in [1,2]:
  w=np.zeros((62,37),np.int64)
  for prep in range(37):
   available=set(range(62))
   for k in range(count):
    ch=max(available,key=lambda c:(abs(int(v[c*37+prep])),-c));available.remove(ch);w[ch,prep]=1 if int(v[ch*37+prep])>=0 else -1
  flat=w.reshape(-1);prior=old['rows'][count-1];assert hashlib.sha256(flat.astype('<i8').tobytes()).hexdigest()==prior['w_int64le_sha256'];rawhash=hashlib.sha256();changed=0;normmax=0;scalars=0
  for prep in range(37):
   before=np.array(Y[prep],dtype=np.int64,copy=True);delta=u[:,None]*w[:,prep][None,:];lo=int(before.min());hi=int(before.max());assert lo>-2**63+2 and hi<2**63-2;after=before+delta
   got=after-before;assert np.array_equal(got,delta);norms=np.einsum('ij,ij->i',got,got);assert np.all(norms==count);rawhash.update(after.astype('<i8').tobytes());changed+=int(np.count_nonzero(got));normmax=max(normmax,int(norms.max()));scalars+=got.size
  # Exact rank-one linear update is a different projection association from raw matrix multiply.
  b=flat@A;N=N0+u[:,None]*b[None,:];maximum=max(abs(int(N.min())),abs(int(N.max())));assert maximum<2**53
  ih=hashlib.sha256(N.astype('<i8').tobytes()).hexdigest();zh=hashlib.sha256((N.astype(float)/2.**55).astype('<f8').tobytes()).hexdigest();assert rawhash.hexdigest()==prior['raw_int64le_sha256']
  rows.append({'case':prior['id'],'raw_sha256':rawhash.hexdigest(),'w_sha256':prior['w_int64le_sha256'],'local_vector_integer_squared_norm_max':normmax,'local_vector_count':303067,'scalar_differences_checked':scalars,'changed_scalars':changed,'integer_projection_sha256':ih,'dyadic_projection_sha256':zh,'projection_entries':int(N.size),'maximum_integer_projection':maximum})
 result={'status':'PASS_INDEPENDENT_LINEAR_UPDATE_DATA_AUDIT','rows':rows,'code_freeze_sha256':SHA(P/'DATA_AUDIT_FREEZE.json'),'baseline_sha256':f['baseline_sha256'],'baseline_integer_partial_bound':partial,'new_estimator_calls':0,'new_raw_files':0,'physical_promotion':0,'external_review':'PENDING','scope':'Both existing fixed raw recipe identities/membership and exact projection hashes, computed before current floating output access. No fit, frame, or phase arithmetic here.'}
 out=P/'DATA_AUDIT_RECEIPT.json';assert not out.exists();out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'rows':[{k:r[k]for k in ['case','raw_sha256','integer_projection_sha256']}for r in rows]}),flush=True)
if __name__=='__main__':main()
