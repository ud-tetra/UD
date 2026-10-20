"""Independent active replay/diagnostic-version mathematical identity checks."""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent;W=P.parent
checks=[];pins={}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def ck(n,b):
 assert b,n
 checks.append({'id':n,'pass':True})
for case in ['boundary_pair_block','boundary_pair_rotating']:
 for name in ['CERTIFICATE.json','WITNESS.json.gz']:
  a=W/'c20_primary_v1_1'/case/name;b=W/'c20_replay_v1_1'/case/name
  ck(case+'_active_replay_'+name,a.read_bytes()==b.read_bytes());pins[str(a.relative_to(W))]=sha(a);pins[str(b.relative_to(W))]=sha(b)
 a=W/'c20_v1_primary'/case/'WITNESS.json.gz';b=W/'c20_primary_v1_1'/case/'WITNESS.json.gz';ck(case+'_v1_v1_1_witness_byte_identity',a.read_bytes()==b.read_bytes());pins[str(a.relative_to(W))]=sha(a)
 old=read(W/'c20_v1_primary'/case/'CERTIFICATE.json');new=read(W/'c20_primary_v1_1'/case/'CERTIFICATE.json')
 for field in ['protocol_sha256','seal_sha256']:old.pop(field);new.pop(field)
 ck(case+'_certificate_only_package_identity_changes',old==new)
result={'status':'PASS_ACTIVE_REPLAY_AND_DIAGNOSTIC_VERSION_MATH_IDENTITY','checks':checks,'count':len(checks),'active_scientific_files_byte_compared':4,'v1_to_v1_1_witnesses_byte_compared':2,'v1_to_v1_1_certificate_differences_only':['protocol_sha256','seal_sha256'],'source_sha256':pins,'excluded':['RESOURCE.json: host-dependent timing/RSS'],'mathematical_retractions':0,'new_fits':0,'physical_promotion':0}
with(P/'REPLAY_AND_VERSION_REVIEW.json').open('x')as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'status':result['status'],'checks':len(checks)}))
