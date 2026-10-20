import json,hashlib,subprocess
from pathlib import Path
R=Path('/workspace/scratch/f3d1c2f040c9/ud-repo');W=R.parent/'c15_campaign';P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
f=json.loads((P/'EXPOSURE_FREEZE.json').read_text());assert sha(Path(__file__))==f['code_sha256'];cf=json.loads((W/'CAMPAIGN_FREEZE.json').read_text());assert sha(W/'CAMPAIGN_FREEZE.json')==f['campaign_freeze_sha256'];rows=[]
for name in cf['case_order']:
 p=W/'cases'/name;assert sha(p/'FREEZE.json')==cf['case_freeze_sha256'][name];assert not(p/'FIT_INTENT.json').exists();d=json.loads((p/'DATA_FREEZE.json').read_text());h=d['record']['record_sha256'];v=subprocess.run(['git','grep','-l','-F',h,f['prior_commit'],'--','*.json','*.md','*.py'],cwd=R,capture_output=True,text=True);assert v.returncode in(0,1);rows.append({'case':name,'record_sha256':h,'prior_text_digest_matches':v.stdout.splitlines(),'exit_code':v.returncode,'data_freeze_sha256':sha(p/'DATA_FREEZE.json')})
assert len({x['record_sha256']for x in rows})==2
out={'status':'PASS_BOUNDED_NO_PRIOR_DIGEST_MATCH_AND_TWO_DISTINCT'if all(not x['prior_text_digest_matches']for x in rows)else'HOLD_PRIOR_DIGEST_MATCH','rows':rows,'prior_commit':f['prior_commit'],'scope':'Committed JSON/Markdown/Python at pinned main only; no global novelty or historical absence claim','new_estimator_calls':0,'physical_promotion':0}
with(P/'EXPOSURE_RECEIPT.json').open('x')as g:json.dump(out,g,indent=2);g.write('\n')
print(out['status'])
