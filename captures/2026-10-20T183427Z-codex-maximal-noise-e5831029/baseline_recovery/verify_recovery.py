"""Read-only postcheck of recovered baseline; no generation or estimation."""
from pathlib import Path
import hashlib,json,datetime
import numpy as np
P=Path(__file__).resolve().parent

def sha(p):
 h=hashlib.sha256()
 with p.open('rb')as f:
  for block in iter(lambda:f.read(1048576),b''):h.update(block)
 return h.hexdigest()

freeze=json.loads((P/'RECOVERY_FREEZE.json').read_text());r=json.loads((P/'RECOVERY_RECEIPT.json').read_text());raw=P/'ramp_clock_stress.i64le'
assert r['status']=='PASS_EXACT_BASELINE_RECOVERY' and r['new_estimator_calls']==0
assert r['recovery_freeze_sha256']==sha(P/'RECOVERY_FREEZE.json')
assert r['original_generation_row']==freeze['expected_original_generation_row']
assert sha(raw)==r['original_generation_row']['record_sha256']=='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59'
assert raw.stat().st_size==150321232 and raw.stat().st_mode&0o222==0
x=np.memmap(raw,dtype='<i8',mode='r',shape=(37,8191,62));minimum=int(x.min());maximum=int(x.max());assert max(abs(minimum),abs(maximum))==r['original_generation_row']['max_absolute_raw_integer'];assert minimum>-(1<<61)and maximum<(1<<61);readings=int(x.size);assert readings==18790154;del x
out={'status':'PASS_READ_ONLY_BASELINE_POSTCHECK','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_receipt_sha256':sha(P/'RECOVERY_RECEIPT.json'),'precheck_sha256':sha(P/'RECOVERY_PRECHECK.json'),'raw_sha256':sha(raw),'raw_bytes':150321232,'raw_shape':[37,8191,62],'raw_dtype':'<i8','mode':'0444','readings_checked':readings,'integer_minimum':minimum,'integer_maximum':maximum,'fresh_generation_row_matches_original':True,'new_estimator_calls':0,'new_raw_generations':0,'physical_promotion':0,'external_review':'PENDING'}
with(P/'RECOVERY_POSTCHECK.json').open('x')as f:json.dump(out,f,indent=2);f.write('\n')
allow=['README.md','RECOVERY_FREEZE.json','RECOVERY_PRECHECK.json','RECOVERY_RECEIPT.json','RECOVERY_POSTCHECK.json','REFERENCE_PROPOSAL.npz','recover_baseline.py','verify_recovery.py','prepare_recovery.py','recovery.log']
files=[]
for n in allow:
 p=P/n;assert p.is_file();files.append({'path':n,'sha256':sha(p),'size_bytes':p.stat().st_size})
inventory={'status':'EXPLICIT_BASELINE_RECOVERY_CAPTURE_ALLOWLIST','allowed_capture_files':allow+['OUTPUT_INVENTORY.json'],'files':files,'raw':{'path':'ramp_clock_stress.i64le','sha256':out['raw_sha256'],'size_bytes':150321232,'intentionally_omitted_from_capture':True},'new_estimator_calls':0,'physical_promotion':0}
with(P/'OUTPUT_INVENTORY.json').open('x')as f:json.dump(inventory,f,indent=2);f.write('\n')
print(json.dumps({'status':out['status'],'raw_sha256':out['raw_sha256'],'readings_checked':readings}))
