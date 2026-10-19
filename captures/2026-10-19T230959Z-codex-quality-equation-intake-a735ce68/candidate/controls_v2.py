"""Frozen v0.2 controls; synthetic complete declarations are not scientific evidence."""
import copy,hashlib,json,subprocess,sys
from pathlib import Path
import check_request_v2 as c
D=Path(__file__).resolve().parent

def run():
 t=json.loads((D/'CANDIDATE_REQUEST_v0.2.json').read_text());full=json.loads((D/'SYNTHETIC_COMPLETE_DECLARATION_v0.2.json').read_text());rows=[]
 def trial(name,base,mutate,expected):
  x=copy.deepcopy(base);mutate(x);r=c.evaluate(x)
  assert r['status']==expected,(name,r)
  assert r['raw_access_authorized'] is False and r['qualification_blockers_closed']==0 and r['physical_promotion']==0
  rows.append({'name':name,'pass':True,'status':r['status']})
 invalid='HOLD_INVALID_REQUEST_METADATA';hold='HOLD_INCOMPLETE_UNVERIFIED_REQUEST';complete='DECLARATIONS_COMPLETE_EXTERNAL_REVIEW_REQUIRED'
 trial('actual_candidate_null_request_HOLD',t,lambda x:None,hold)
 trial('all_ten_wiring_evidence_slots_completeable',full,lambda x:None,complete)
 trial('candidate_specific_complete_domain_not_old_1000',full,lambda x:None,complete)
 trial('CH1_bool_not_integer1',full,lambda x:x['channel_roles_filename_only'][0].update(channel=True),invalid)
 trial('scope_channel_bool_not_integer1_deep_const',full,lambda x:x['calibration']['joint_error']['scope']['covered_channel_numbers'].__setitem__(0,True),invalid)
 trial('scope_false_not_numeric0_deep_const',full,lambda x:x['calibration']['joint_error']['scope']['covered_channel_numbers'].__setitem__(0,False),invalid)
 trial('role_bool_not_text',full,lambda x:x['channel_roles_filename_only'][0].update(role=True),invalid)
 trial('known_record_bool_not_integer',full,lambda x:x.update(known_records=True),invalid)
 trial('scope_record_bool_not_integer',full,lambda x:x['calibration']['joint_error']['scope'].update(record_count=True),invalid)
 trial('old_scope_string_refused',full,lambda x:x['calibration']['joint_error'].update(scope='ALL_1000_RECORDS_EACH_CROPPED_16184_VECTOR'),invalid)
 trial('candidate_scope_wrong_PID_refused',full,lambda x:x['calibration']['joint_error']['scope'].update(source_persistent_id='old-source'),invalid)
 trial('crop_outside_manifest_refused',full,lambda x:x['calibration']['joint_error']['scope'].update(crop_stop_exclusive=2),invalid)
 trial('empty_crop_refused',full,lambda x:x['calibration']['joint_error']['scope'].update(crop_start_inclusive=1),invalid)
 trial('group_count_exceeds_records_refused',full,lambda x:x['calibration']['joint_error']['scope'].update(group_count=2),invalid)
 trial('record_count_custody_disagreement_refused',full,lambda x:x.update(known_records=2),invalid)
 trial('group_count_custody_disagreement_refused',full,lambda x:x.update(known_groups=2),invalid)
 trial('missing_independent_manifest_returns_HOLD',full,lambda x:x['calibration']['joint_error']['scope'].update(custodian_manifest_evidence=None),hold)
 trial('missing_channel10_wiring_returns_HOLD',full,lambda x:x['channel_roles_filename_only'][9].update(verified_wiring=None),hold)
 trial('CH9_CH10_role_swap_refused',full,lambda x:x['channel_roles_filename_only'][8].update(role='site5'),invalid)
 trial('CH9_empty_cannot_be_numerical_zero',full,lambda x:x['channel_roles_filename_only'][8].update(role=0),invalid)
 trial('fresh_confirmation_claim_refused',full,lambda x:x.update(purpose='FRESH_CONFIRMATION'),invalid)
 trial('fresh_comparison_design_refused',full,lambda x:x['physical_model_comparison'].update(comparison_design='FRESH_INDEPENDENT_UNSEEN_SOURCE_REQUIRED'),invalid)
 trial('erase_exposure_refused',full,lambda x:x['exposure'].update(public_notebook_exact_path_used=False),invalid)
 trial('erase_Jexp_exposure_refused',full,lambda x:x['exposure'].update(public_candidate_derived_parameter_use=False),invalid)
 trial('drive_label_is_not_calibrated_interval',full,lambda x:x['drive'].update(actual_amplitude_interval_V='0.050'),invalid)
 trial('drive_label_is_not_zero_drive',full,lambda x:x['drive'].update(filename_tag='Vdrv=0.000V'),invalid)
 trial('self_authorization_refused',full,lambda x:x.update(raw_download_authorized_by_this_metadata=True),invalid)
 trial('physical_promotion_refused',full,lambda x:x.update(physical_promotion=1),invalid)
 trial('unknown_field_refused',full,lambda x:x.update(calibrated=True),invalid)
 trial('malformed_evidence_hash_refused',full,lambda x:x['channel_roles_filename_only'][0]['verified_wiring'].update(sha256='fake'),invalid)
 trial('null_count_remains_unknown_HOLD',full,lambda x:x.update(known_records=None),hold)
 trial('NaN_Python_input_refused',full,lambda x:x.update(known_records=float('nan')),invalid)
 for label,b in [('duplicate_top_key',b'{"source":{},"source":{}}'),('duplicate_nested_key',b'{"source":{"x":1,"x":2}}'),('NaN_token',b'{"x":NaN}'),('Infinity_token',b'{"x":Infinity}'),('negative_Infinity_token',b'{"x":-Infinity}')]:
  try:c.strict_loads(b)
  except ValueError:rows.append({'name':label,'pass':True,'status':'HOLD_INVALID_JSON'})
  else:raise AssertionError(label)
 for a,b in [(True,1),([True],[1]),({'channel':True},{'channel':1}),([False],[0])]:assert not c.deep_equal(a,b)
 rows.append({'name':'recursive_type_sensitive_const_and_enum_equality','pass':True})
 # Real CLI input pin and complete-null behaviors, no temporary record/evidence files.
 for name in ['CANDIDATE_REQUEST_v0.2.json','SYNTHETIC_COMPLETE_DECLARATION_v0.2.json']:
  p=D/name;pin=hashlib.sha256(p.read_bytes()).hexdigest()
  r=subprocess.run([sys.executable,str(D/'check_request_v2.py'),str(p),'--sha256',pin],capture_output=True,text=True,check=True)
  expected=hold if name.startswith('CANDIDATE') else complete
  q=json.loads(r.stdout);assert q['status']==expected and q['raw_access_authorized']is False
  rows.append({'name':'actual_CLI_'+name,'pass':True,'status':q['status']})
 p=D/'CANDIDATE_REQUEST_v0.2.json';r=subprocess.run([sys.executable,str(D/'check_request_v2.py'),str(p),'--sha256','0'*64],capture_output=True,text=True)
 assert r.returncode!=0 and 'HOLD_REQUEST_DIGEST_MISMATCH'in r.stderr
 rows.append({'name':'actual_CLI_digest_mismatch_refused','pass':True})
 # File references remain strings only. No evidence opening API is used by this checker.
 trial('nonexistent_URI_complete_declaration_still_unverified',full,lambda x:x['channel_roles_filename_only'][0]['verified_wiring'].update(uri='file:///does-not-exist-and-must-not-be-opened'),complete)
 return {'artifact_type':'PRE_RAW_METADATA_CONTROLS_v0.2','count':len(rows),'controls':rows,'all_pass':True,'actual_null_request':c.evaluate(t),'synthetic_complete_declaration':c.evaluate(full),'physical_promotion':0,'new_raw_downloads':0,'new_fits':0,'author_code_executed':False}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
