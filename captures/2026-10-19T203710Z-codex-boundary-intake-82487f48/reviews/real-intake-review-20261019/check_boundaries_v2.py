"""Same-team tiny intake-boundary controls; no real data, signing, keys or fits."""
import argparse,hashlib,importlib.util,json,shutil,sys,tempfile,subprocess,os
from pathlib import Path
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def put(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,sort_keys=True));return p
def load(root,name):
 spec=importlib.util.spec_from_file_location(name,root/'intake.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--implementation',required=True,type=Path);a=ap.parse_args();root=a.implementation.resolve();f=json.loads((P/'TEST_FREEZE_v2.json').read_text())
 for n,h in f['implementation_sha256'].items():assert sha(root/n)==h
 assert sha(__file__)==f['review_harness_sha256'];m=load(root,'intake_boundary_review');deny=json.loads((root/'KNOWN_SYNTHETIC_AUTHORITY.json').read_text());rows=[]
 with tempfile.TemporaryDirectory(prefix='ud-real-intake-negative-') as t:
  w=Path(t);bundle=w/'candidate';caller=w/'caller';bundle.mkdir();caller.mkdir()
  # Counterfactual test-only string, not generated credentials or a real authority.
  unknown='ab'*32;assert unknown not in deny['public_key_hex']
  policy={'version':'UD_TRUST_POLICY_v1','scope':'apparatus','keys':{'test_only_no_private_key':{'public_key_hex':unknown,'roles':['calibration','model','acquisition','lineage'],'principal':'NO_REAL_AUTHORITY_ASSERTED','algorithm':'Ed25519'}}}
  admission={'version':'UD_ANALYTIC_ADMISSION_v1','run_id':'counterfactual-routing-control','analytic_model_path':'MODEL.json'}
  packet={'provenance_kind':'apparatus_submission','files':{x:{'path':x+'.placeholder'} for x in ['raw_adc','prediction','timestamps','calibration']}}
  for name,value in [('ADMISSION.json',admission),('PACKET.json',packet),('CONTRACT.json',{}),('RECEIPTS.json',[]),('MODEL.json',{})]:put(bundle/name,value)
  for x in packet['files'].values():(bundle/x['path']).write_bytes(b'NOT_A_REAL_RECORD')
  policyfile=put(caller/'policy.json',policy)
  def request(path=None,**changes):
   r={'version':'UD_REAL_EVIDENCE_REQUEST_v1','pin_source':'independent_caller','evidence_kind':'independently_calibrated_apparatus','roles':['calibration','model','acquisition','lineage'],'bundle_path':str(bundle),'policy_path':str(policyfile),'expected_policy_sha256':sha(policyfile),'expected_admission_sha256':sha(bundle/'ADMISSION.json'),'verification_utc':'2026-10-19T20:00:00+00:00'};r.update(changes);return put(path or caller/'request.json',r)
  def check(name,expected,fn):
   out=fn();assert out['physical_promotion']==0 and out['physical_verdict']=='HOLD_UNQUALIFIED' and out['real_records_evaluated']==0 and out['actual_real_records_verified']==0
   assert out['status'].startswith('HOLD') and expected in out['blocking_items'];assert out['delegations']==0;rows.append({'control':name,'expected_block':expected,'outcome':out})
  check('missing caller pin','MISSING_CALLER_REQUEST_PIN',lambda:m.verify_request(str(request()),None))
  check('request inside candidate','REQUEST_INSIDE_CANDIDATE',lambda:m.verify_request(str(q:=request(bundle/'request.json')),sha(q)))
  link=caller/'request-symlink.json';link.symlink_to(bundle/'request.json');check('external request symlink to candidate','SYMLINK_ANCHOR',lambda:m.verify_request(str(link),sha(link)))
  inside=put(bundle/'policy.json',policy);check('policy inside candidate','POLICY_INSIDE_CANDIDATE',lambda:m.verify_request(str(q:=request(policy_path=str(inside))),sha(q)))
  synthetic=dict(policy);synthetic['scope']='synthetic_fixture';put(policyfile,synthetic);check('synthetic policy scope','SYNTHETIC_OR_UNSUPPORTED_REAL_POLICY',lambda:m.verify_request(str(q:=request()),sha(q)))
  relabel=json.loads(json.dumps(policy));relabel['keys']['test_only_no_private_key']['public_key_hex']=deny['public_key_hex'][0];put(policyfile,relabel);check('relabeled known fixture publickey','KNOWN_SYNTHETIC_PUBLIC_KEY_RELABELED',lambda:m.verify_request(str(q:=request()),sha(q)))
  put(policyfile,policy);syntheticpacket=dict(packet);syntheticpacket['provenance_kind']='synthetic_fixture';put(bundle/'PACKET.json',syntheticpacket);check('synthetic packet provenance','SYNTHETIC_OR_UNCLASSIFIED_PACKET',lambda:m.verify_request(str(q:=request()),sha(q)));put(bundle/'PACKET.json',packet)
  (bundle/'raw_adc.placeholder').unlink();check('missing raw member','MALFORMED_OR_MISSING_EXTERNAL_EVIDENCE',lambda:m.verify_request(str(q:=request()),sha(q)));(bundle/'raw_adc.placeholder').write_bytes(b'NOT_A_REAL_RECORD')
  # Copies only; original reviewed implementation bytes remain untouched.
  for label,filename,mutate,reason in [('changed delegate','verifier/base_record.py',lambda q:q.write_text(q.read_text()+'\n# boundary corruption control\n'),'PINNED_DELEGATE_CHANGED'),('changed denylist','KNOWN_SYNTHETIC_AUTHORITY.json',lambda q:q.write_text('{}'),'SYNTHETIC_DENYLIST_CHANGED'),('changed source bindings','SOURCE_BINDINGS.json',lambda q:q.write_text('{}'),'SOURCE_BINDINGS_CHANGED')]:
   copy=w/label.replace(' ','-');copy.mkdir()
   for n in f['implementation_sha256']:
    dest=copy/n;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(root/n,dest)
   mutate(copy/filename);other=load(copy,label.replace(' ','_'))
   q=request();check(label,reason,lambda other=other,q=q:other.verify_request(str(q),sha(q)))
  q=request();run=subprocess.run([sys.executable,'-O',str(root/'intake.py'),'--request',str(q)],capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'});assert run.returncode==0;out=json.loads(run.stdout);assert out['blocking_items']==['MISSING_CALLER_REQUEST_PIN'] and out['delegations']==0;rows.append({'control':'optimized interpreter missingpin','outcome':out})
  # Negative integration: all required filenames exist, but no valid record,
  # signatures, chronology or credentials exist. The actual pinned verifier HOLDs.
  q=request();out=m.verify_request(str(q),sha(q));(P/'DELEGATE_DIAGNOSTIC.json').write_text(json.dumps(out,indent=2));assert out['status']=='HOLD_DELEGATED_EVIDENCE' and out['delegations']==1 and out['candidate_requests_delegated']==1 and out['real_records_evaluated']==0 and out['actual_real_records_verified']==0 and out['delegated_result']['status']=='HOLD_AUTH_OR_ANALYTIC_EVIDENCE';rows.append({'control':'actual pinned verifier negative integration','outcome':out,'actual_real_records':0,'signatures_created':0})
 for n,h in f['implementation_sha256'].items():assert sha(root/n)==h
 result={'status':'PASS_TINY_SAME_TEAM_BOUNDARY_CONTROLS','rows':rows,'control_count':len(rows),'old_auth52_controls_rerun':0,'real_records':0,'signatures_created':0,'private_keys_generated':0,'fits_run':0,'actual_pinned_verifier_negative_delegations':1,'physical_promotion':0,'external_review':'PENDING'};(P/'BOUNDARY_RESULTS_v2.json').write_text(json.dumps(result,indent=2));print(json.dumps({'status':result['status'],'controls':len(rows),'real_records':0,'negative_delegations':1}))
if __name__=='__main__':main()
