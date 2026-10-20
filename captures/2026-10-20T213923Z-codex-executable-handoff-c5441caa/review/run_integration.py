#!/usr/bin/env python3
"""Frozen small-input integration and preoutput failure checks; actual pinned CLIs."""
import hashlib,json,os,resource,shutil,subprocess,sys
from pathlib import Path
P=Path(__file__).resolve().parent;BASE=P.parent;RUN=BASE/'c22_runner';REPO=BASE/'ud-repo';EX=P/'executions';F=P/'fixtures'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def snapshot():
 return {str(p.relative_to(P)):sha(p) for p in F.rglob('*') if p.is_file() and not p.is_symlink()}
def limits():resource.setrlimit(resource.RLIMIT_AS,(3*1024**3,3*1024**3));resource.setrlimit(resource.RLIMIT_CPU,(40,40))
assert (RUN/'SEAL.json').is_file()
EX.mkdir(exist_ok=False);pins={n:sha(RUN/n) for n in ['run_submission.py','DEPENDENCIES.json','PROTOCOL.json','SEAL.json']};before=snapshot()
# Isolated dependency copy for a pre-output source-pin test. The intended producer is never changed.
config=json.loads((RUN/'DEPENDENCIES.json').read_text());mirror=P/'dependency_mirror';mirror.mkdir(exist_ok=False)
for role in config['roles'].values():
 for rel in role['files']:
  dest=mirror/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(REPO/rel,dest)
entry=mirror/config['roles']['identity']['entry'];entry.write_bytes(entry.read_bytes()+b'\n# Deliberate isolated source-pin negative fixture.\n')
cases=[]
for n in ['exact_q1','distinct_exact_q1','numerical_hold','hash_mismatch','missing_field','unknown_field','relative_escape','symlink_record']:
 cases.append({'name':n,'manifest':F/n/'manifest.json','out':EX/n,'repo':REPO,'expected':'NUMERICAL_PASS_PROVENANCE_HOLD' if n in ['exact_q1','distinct_exact_q1'] else ('HOLD_NUMERICAL_STEP' if n=='numerical_hold' else 'HOLD_INTAKE_OR_SETUP')})
cases += [{'name':'existing_output','manifest':F/'exact_q1/manifest.json','out':F/'existing_output','repo':REPO,'expected':'HOLD_INTAKE_OR_SETUP'}, {'name':'output_is_input','manifest':F/'exact_q1/manifest.json','out':F/'exact_q1/N.npy','repo':REPO,'expected':'HOLD_INTAKE_OR_SETUP'}, {'name':'source_pin_changed','manifest':F/'exact_q1/manifest.json','out':EX/'source_pin_changed','repo':mirror,'expected':'HOLD_INTAKE_OR_SETUP'}]
rows=[];count=0
for c in cases:
 existed=c['out'].exists();r=subprocess.run([sys.executable,str(RUN/'run_submission.py'),'--repo',str(c['repo']),'--manifest',str(c['manifest']),'--out',str(c['out'])],capture_output=True,text=True,timeout=60,preexec_fn=limits,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1'})
 data=json.loads(r.stdout.strip().splitlines()[-1]);assert data['workflow_status']==c['expected'],(c['name'],r.returncode,r.stdout,r.stderr);count+=1
 assert r.returncode==(0 if c['expected']=='NUMERICAL_PASS_PROVENANCE_HOLD' else 2);count+=1
 if c['expected']=='HOLD_INTAKE_OR_SETUP':
  assert c['out'].exists()==existed;count+=1
  assert not (EX/c['name']/'ROLLUP.json').exists();count+=1
  stages=[];roll=None
 else:
  roll=json.loads((c['out']/'ROLLUP.json').read_text());assert roll['workflow_status']==c['expected'];count+=1
  stages=[s['role']for s in roll['stages_invoked']];assert stages==(['identity','numerical','audit'] if c['expected']=='NUMERICAL_PASS_PROVENANCE_HOLD'else ['identity','numerical']);count+=1
  assert (c['out']/'audit').exists()==('audit'in stages);count+=1
  for k,v in {'independent_acquisition':'NOT_ESTABLISHED','fresh_preparation':'NOT_ESTABLISHED','provenance_status':'HOLD_PROVENANCE_NOT_ESTABLISHED','physical_promotion':0,'external_promotion_review':'PENDING','all_input_backend_conformance':'OPEN','new_estimator_calls':0}.items():assert roll[k]==v;count+=1
  screen=json.loads((c['out']/'identity/SCREEN.json').read_text());assert screen['identity_relation']=='UNLISTED_FINGERPRINT';count+=1
  if 'audit'in stages:
   aud=json.loads((c['out']/'audit/CERTIFICATE.json').read_text());assert aud['status']=='PASS_ALL_SIX_EXACT_CRT_AND_FRESH_SCALAR_CERTIFICATE';count+=1
   assert all(x['status']=='PASS_EXACT_ALL_ENTRY_CRT'for x in aud['matrix_checks'].values());count+=1
   assert all(aud['scalar_checks']['gates'].values());count+=1
 assert snapshot()==before;count+=1
 row={'case':c['name'],'returncode':r.returncode,'workflow_status':data['workflow_status'],'stages_invoked':stages,'pass':True,'stdout':r.stdout,'stderr':r.stderr,'rollup_sha256':sha(c['out']/'ROLLUP.json')if roll else None};rows.append(row);print(json.dumps({k:row[k]for k in ['case','returncode','workflow_status','stages_invoked','pass']}),flush=True)
assert {n:sha(RUN/n) for n in pins}==pins
result={'status':'PASS_FROZEN11_C22_INTEGRATION_CASES','case_count':len(rows),'check_count':count,'source_pins':pins,'results':rows,'all_generated_inputs_synthetic':True,'root_pinned_sources_unchanged':True,'input_sentinel_bytes_unchanged':True,'estimator_calls':0,'external_promotion_review':'PENDING','physical_promotion':0}
(P/'INTEGRATION_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'check_count':count}))
