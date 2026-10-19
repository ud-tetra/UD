"""Independent post-v1-finding review of prospectively frozen packet v0.2.
Source/schema/metadata only. No waveform, model, authority verification or URI access.
"""
import copy,hashlib,importlib.util,json,subprocess,sys
from pathlib import Path
D=Path(sys.argv[1]).resolve();R=Path(sys.argv[2]).resolve()
def H(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 spec=importlib.util.spec_from_file_location('checker_v2',D/'check_request_v2.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
 t=json.loads((D/'CANDIDATE_REQUEST_v0.2.json').read_text());s=c.load_schema();f=json.loads((D/'SYNTHETIC_COMPLETE_DECLARATION_v0.2.json').read_text());rows=[]
 def add(name,ok,detail=''):rows.append({'name':name,'pass':bool(ok),'detail':detail})
 def safe(r):return all(r[k] is False for k in ['raw_access_authorized','calibration_verified','evidence_authenticity_verified','physical_model_verified']) and r['physical_promotion']==0 and r['qualification_blockers_closed']==0
 def test(name,base,fn):
  x=copy.deepcopy(base);fn(x);r=c.evaluate(x);add(name,safe(r) and r['status']=='HOLD_INVALID_REQUEST_METADATA',r['schema_errors'])
 rt=c.evaluate(t);rf=c.evaluate(f)
 add('actual_candidate_stays_HOLD',safe(rt) and rt['status']=='HOLD_INCOMPLETE_UNVERIFIED_REQUEST',{'missing_leaves':rt['unsupplied_count'],'independent_blockers':128})
 add('complete_synthetic_declaration_reaches_unverified_only',safe(rf) and rf['status']=='DECLARATIONS_COMPLETE_EXTERNAL_REVIEW_REQUIRED' and rf['unsupplied_count']==0,rf['status'])
 test('bool_channel_refused',t,lambda x:x['channel_roles_filename_only'][0].update(channel=True))
 test('float_channel_refused_by_explicit_integer_type',t,lambda x:x['channel_roles_filename_only'][0].update(channel=1.0))
 test('CH9_site5_refused',t,lambda x:x['channel_roles_filename_only'][8].update(role='site5'))
 test('wrong_CH10_identity_refused',t,lambda x:x['channel_roles_filename_only'][9].update(channel=9))
 test('wiring_bool_not_evidence',t,lambda x:x['channel_roles_filename_only'][0].update(verified_wiring=True))
 test('release_request_refused',f,lambda x:x.update(raw_download_authorized_by_this_metadata=True))
 test('truth_promotion_refused',f,lambda x:x.update(physical_promotion=1))
 test('confirmatory_scope_refused',f,lambda x:x.update(purpose='FRESH_CONFIRMATION'))
 test('erase_parameter_exposure_refused',f,lambda x:x['exposure'].update(public_candidate_derived_parameter_use=False))
 test('filename_amplitude_not_calibration_interval',t,lambda x:x['drive'].update(actual_amplitude_interval_V='0.050V'))
 test('legacy_joint_scope_string_refused',f,lambda x:x['calibration']['joint_error'].update(scope='ALL_1000_RECORDS_EACH_CROPPED_16184_VECTOR'))
 test('counts_disagree_refused',f,lambda x:x.update(known_records=x['known_records']+1))
 test('group_count_disagree_refused',f,lambda x:x.update(known_groups=x['known_groups']+1))
 test('empty_crop_refused',f,lambda x:x['calibration']['joint_error']['scope'].update(crop_stop_exclusive=x['calibration']['joint_error']['scope']['crop_start_inclusive']))
 test('crop_exceeds_sample_count_refused',f,lambda x:x['calibration']['joint_error']['scope'].update(crop_stop_exclusive=x['calibration']['joint_error']['scope']['samples_per_record']+1))
 # No evidence URI is dereferenced while evaluating complete fabricated references.
 import builtins,socket
 oo=builtins.open;ss=socket.socket;pr=Path.read_bytes
 def refuse(*a,**k):raise AssertionError('Unexpected evidence/raw/network access')
 try:
  builtins.open=refuse;socket.socket=refuse;Path.read_bytes=refuse
  rn=c.evaluate(f,schema=s)
 finally:builtins.open=oo;socket.socket=ss;Path.read_bytes=pr
 add('fake_complete_evidence_not_opened',rn==rf,'File/network entry points denied during in-memory evaluation.')
 for name,b in [('duplicate_key',b'{"x":1,"x":2}'),('NaN',b'{"x":NaN}'),('Infinity',b'{"x":Infinity}')]:
  try:c.strict_loads(b);ok=False
  except ValueError:ok=True
  add('strict_JSON_'+name,ok,'Parser path only; no file/evidence read.')
 proc=subprocess.run([sys.executable,str(D/'check_request_v2.py'),str(D/'SYNTHETIC_COMPLETE_DECLARATION_v0.2.json'),'--sha256',H(D/'SYNTHETIC_COMPLETE_DECLARATION_v0.2.json')],capture_output=True,text=True)
 add('actual_CLI_complete_fake_still_unverified',proc.returncode==0 and json.loads(proc.stdout)==rf,'Correct request pin proves custody only.')
 proc=subprocess.run([sys.executable,str(D/'check_request_v2.py'),str(D/'CANDIDATE_REQUEST_v0.2.json'),'--sha256','0'*64],capture_output=True,text=True)
 add('actual_CLI_wrong_pin_refused',proc.returncode!=0 and 'HOLD_REQUEST_DIGEST_MISMATCH' in proc.stderr)
 old=json.loads((D/'CANDIDATE_REQUEST_v0.1.json').read_text());old_s=json.loads((D/'REQUEST_SCHEMA_v0.1.json').read_text());a=copy.deepcopy(t['calibration']);b=copy.deepcopy(old['calibration']);a['joint_error']['scope']=b['joint_error']['scope'];add('calibration_template_only_scope_changed',a==b)
 a=copy.deepcopy(s['properties']['calibration']);b=copy.deepcopy(old_s['properties']['calibration']);a['properties']['joint_error']['properties']['scope']=b['properties']['joint_error']['properties']['scope'];add('calibration_schema_only_scope_changed',a==b)
 a=copy.deepcopy(s['properties']['physical_model_comparison']);b=copy.deepcopy(old_s['properties']['physical_model_comparison']);a['properties']['comparison_design']['enum']=b['properties']['comparison_design']['enum'];add('physical_model_template_preserved_schema_only_retrospective_tightening',t['physical_model_comparison']==old['physical_model_comparison'] and a==b and s['properties']['physical_model_comparison']['properties']['comparison_design']['enum']==['RETROSPECTIVE_EXISTING_PUBLIC_ONLY',None], 'The only schema delta removes fresh-confirmatory designation for this publicly exposed candidate.')
 freeze=json.loads((D/'FREEZE_v0.2.json').read_text());add('new_frozen_inputs_intact',all((D/x['path']).stat().st_size==x['bytes'] and H(D/x['path'])==x['sha256'] for x in freeze['files']))
 add('old_manifest_intact',H(D/'MANIFEST.json')==freeze['old_manifest_sha256'])
 oldmanifest=json.loads((D/'MANIFEST.json').read_text());records=oldmanifest.get('files',[]);add('old_manifest_files_intact',all((D/x['path']).stat().st_size==x.get('bytes',x.get('size_bytes')) and H(D/x['path'])==x['sha256'] for x in records))
 return {'artifact_type':'SAME_TEAM_REVIEW_OF_APPEND_ONLY_PACKET_V0_2','controls':rows,'count':len(rows),'all_pass':all(x['pass'] for x in rows),'actual_null_leaf_count':rt['unsupplied_count'],'null_leaf_count_is_not_independent_blockers':True,'original_qualification_blockers_unresolved':128,'physical_promotion':0,'new_raw_downloads':0,'new_fits':0,'author_code_executed':False,'external_review':'PENDING','review_independence':'Separate same-team agent; not external.'}
if __name__=='__main__':print(json.dumps(main(),indent=2,sort_keys=True))
