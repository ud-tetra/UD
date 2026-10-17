"""Adversarial input checks for the new exact witness checker, not new spectral replays."""
from pathlib import Path
import tempfile,shutil,subprocess,json,hashlib,sys
P=Path(__file__).resolve().parent;rows=[]
for case in ['clean','altered_relation_rebound_hash','wrong_baseline_binding','changed_frozen_contract']:
 with tempfile.TemporaryDirectory() as t:
  d=Path(t);(d/'inputs').mkdir()
  for n in ['certify_blind_family.py','CAMPAIGN_FREEZE.json','NULL_VECTOR.json']:shutil.copyfile(P/n,d/n)
  for n in ['BASELINE_CERTIFICATE.json','FROZEN_CONTRACT.json']:shutil.copyfile(P/'inputs'/n,d/'inputs'/n)
  if case=='altered_relation_rebound_hash':
   q=d/'NULL_VECTOR.json';v=json.loads(q.read_text());v['vector'][0]+=1;q.write_text(json.dumps(v));q=d/'CAMPAIGN_FREEZE.json';v=json.loads(q.read_text());v['null_vector_sha256']=hashlib.sha256((d/'NULL_VECTOR.json').read_bytes()).hexdigest();q.write_text(json.dumps(v))
  elif case=='wrong_baseline_binding':
   q=d/'inputs/BASELINE_CERTIFICATE.json';v=json.loads(q.read_text());v['input_sha256']['record']='0'*64;q.write_text(json.dumps(v))
  elif case=='changed_frozen_contract':
   q=d/'inputs/FROZEN_CONTRACT.json';q.write_text(q.read_text()+' ')
  r=subprocess.run([sys.executable,str(d/'certify_blind_family.py')],capture_output=True,text=True)
  assert (r.returncode==0)==(case=='clean'),(case,r.stdout,r.stderr)
  rows.append({'case':case,'accepted':r.returncode==0,'expected':case=='clean','pass':True})
(P/'WITNESS_TEST_RESULTS.json').write_text(json.dumps({'status':'PASS','tests':rows},indent=2)+'\n');print(json.dumps(rows))
