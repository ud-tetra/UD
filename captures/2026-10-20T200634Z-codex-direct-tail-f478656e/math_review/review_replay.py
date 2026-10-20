"""Independent byte comparison of zero-fit tail Gram scientific replays."""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent;W=P.parent
rows=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for case in ['boundary_pair_block','boundary_pair_rotating']:
 for name in ['CERTIFICATE.json','TAIL_WITNESS.json.gz']:
  a=W/'c19_primary'/case/name;b=W/'c19_replay'/case/name
  assert a.read_bytes()==b.read_bytes(),(case,name)
  rows.append({'case':case,'file':name,'primary_and_replay_sha256':sha(a),'bytes_identical':True})
j={'status':'PASS_INDEPENDENT_ROOT_TAIL_SCIENTIFIC_REPLAY_BYTE_COMPARISON','files':rows,'scientific_files_compared':len(rows),'excluded':['RESOURCE.json: host-dependent elapsed time and peak RSS'],'root_pipeline_executed_by_this_reviewer':False,'new_fits':0,'physical_promotion':0}
with(P/'REPLAY_REVIEW.json').open('x')as f:json.dump(j,f,indent=2);f.write('\n')
print(json.dumps({'status':j['status'],'scientific_files':len(rows)}))
