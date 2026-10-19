"""Compose pinned offline witness/raw replay with the uniform admission proof."""
import argparse,datetime,hashlib,json,os,shutil,subprocess,sys
from pathlib import Path
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def command(args,cwd,log,steps):
 with log.open('xb') as f:r=subprocess.run([sys.executable,*args],cwd=cwd,stdout=f,stderr=subprocess.STDOUT,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'})
 steps.append({'argv':[sys.executable,*args],'exit_code':r.returncode,'log':log.name,'log_sha256':sha(log)})
 if r.returncode:raise RuntimeError('replay failed: '+log.name)
def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--raw',action='store_true');p.add_argument('--reuse-evidence',type=Path);x=p.parse_args();out=x.out.absolute();assert not out.exists(),'new output directory required'
 # Root envelope/package checks before importing/launching any retained numerical source.
 m=json.loads((P/'PACKAGE_MANIFEST.json').read_text())
 for e in m['files']:
  r=Path(e['path']);assert not r.is_absolute() and '..' not in r.parts;q=P/r
  assert q.stat().st_size==e['size_bytes'] and sha(q)==e['sha256'],e['path']
 out.mkdir(parents=True);steps=[];receipt={'status':'RUNNING','reviewer_identity':None,'external_nonconstructor_review':'PENDING','physical_promotion':0,'steps':steps,'new_estimator_runs':0,'new_SVD_runs':0,'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  if x.reuse_evidence:
   prior=x.reuse_evidence.resolve();old=json.loads((prior/'RUN_RECEIPT.json').read_text());allowed=[sha(P/'reviewer/offline_replay.py'),sha(P/'reviewer/offline_replay_v2.py')]
   assert old['status']=='PASS_CONSTRUCTOR_REPLAY_ONLY' and old['runner_sha256'] in allowed
   if x.raw:assert old['mode']=='raw'
   for c in old['commands']:assert c['returncode']==0 and sha(prior/c['log'])==c['log_sha256']
   receipt['prior_evidence_receipt_sha256']=sha(prior/'RUN_RECEIPT.json');receipt['new_raw_reconstruction_in_this_invocation']=False
   receipt['prior_empty_command_logs']=[c['tag'] for c in old['commands'] if (prior/c['log']).stat().st_size==0]
   # Recheck full saved witnesses with fail-closed v2 markers, regardless of old stdout.
   evidence=out/'rechecked-evidence';command([str(P/'reviewer/offline_replay_v2.py'),'--repo',str(x.repo.resolve()),'--out',str(evidence)],P,out/'strict-witness-recheck.log',steps)
   receipt['reused_raw_scope']='Prior frozenrunner raw recovery/Grams, with new strict fullwitness verification here'
  else:
   evidence=out/'evidence';command([str(P/'reviewer/offline_replay_v2.py'),'--repo',str(x.repo.resolve()),'--out',str(evidence),*(['--raw'] if x.raw else [])],P,out/'offline-evidence.log',steps);receipt['new_raw_reconstruction_in_this_invocation']=x.raw
  stage=evidence/'uniform-output-work';assert not stage.exists(),'new proof staging path required'
  shutil.copytree(P,stage,ignore=shutil.ignore_patterns('__pycache__','ACTUAL_ADMISSION.json','CONTROLS.json'))
  command(['uniform.py','--replay'],stage,out/'uniform-implication.log',steps)
  command(['lineage.py'],stage,out/'lineage.log',steps)
  command(['actual.py'],stage,out/'actual-gates.log',steps)
  assert json.loads((stage/'ACTUAL_ADMISSION.json').read_text())==json.loads((P/'ACTUAL_ADMISSION.json').read_text())
  command(['controls.py'],stage,out/'admission-controls.log',steps)
  assert json.loads((stage/'CONTROLS.json').read_text())==json.loads((P/'CONTROLS.json').read_text())
  receipt.update(status='PASS_CONSTRUCTOR_REVIEW_ONLY',mode='raw_plus_admission' if x.raw else 'witness_plus_admission',phase_error_strict_upper=3.079e-7,quantifier='Every eligible returned output satisfying frozen gates; not universal solver success',scope='Exact witness/implication/actualgate replay; sourceconstants remain explicit pinned parent dependencies')
 except Exception as e:receipt.update(status='FAIL',error=type(e).__name__+': '+str(e));raise
 finally:
  receipt['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();(out/'REVIEW_RECEIPT.json').write_text(json.dumps(receipt,indent=2))
 print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
