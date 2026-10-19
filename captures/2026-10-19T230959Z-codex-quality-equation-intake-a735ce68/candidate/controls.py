"""Frozen metadata controls. Synthetic mutations are not evidence responses."""
import copy,hashlib,json,subprocess,sys
from pathlib import Path
import check_request as c
D=Path(__file__).resolve().parent

def run():
    t=json.loads((D/'CANDIDATE_REQUEST_v0.1.json').read_text());rows=[]
    def control(name,mutate,predicate):
        x=copy.deepcopy(t);mutate(x);r=c.evaluate(x);ok=predicate(r)
        if not ok:raise AssertionError((name,r))
        rows.append({'name':name,'pass':ok,'status':r['status'],'raw_access_authorized':r['raw_access_authorized']})
    bad=lambda r:r['status']=='HOLD_INVALID_REQUEST_METADATA' and not r['raw_access_authorized']
    hold=lambda r:r['status']=='HOLD_INCOMPLETE_UNVERIFIED_REQUEST' and not r['raw_access_authorized'] and r['qualification_blockers_closed']==0
    control('actual_null_request_stays_hold',lambda x:None,hold)
    control('old_CH9_CH10_mapping_refused',lambda x:x['channel_roles_filename_only'][8].update(role='site5'),bad)
    control('empty_channel_not_assumed_zero',lambda x:x['channel_roles_filename_only'][8].update(verified_wiring=0),bad)
    control('fresh_confirmation_claim_refused',lambda x:x.update(purpose='FRESH_CONFIRMATION'),bad)
    control('path_retarget_refused',lambda x:x['source'].update(path='05-21/old.gz'),bad)
    control('PID_retarget_refused',lambda x:x['source'].update(persistent_id='doi:example/new'),bad)
    control('published_MD5_change_refused',lambda x:x['source']['checksum'].update(value='0'*32),bad)
    control('bytecount_bool_refused',lambda x:x['source'].update(bytes=True),bad)
    control('erase_public_exposure_refused',lambda x:x['exposure'].update(public_notebook_exact_path_used=False),bad)
    control('erase_derived_parameter_exposure_refused',lambda x:x['exposure'].update(public_candidate_derived_parameter_use=False),bad)
    control('erase_local_noninspection_refused',lambda x:x['exposure'].update(local_raw_inspected=True),bad)
    control('drive_label_not_actual_amplitude',lambda x:x['drive'].update(actual_amplitude_interval_V='0.050'),bad)
    control('drive_label_not_zero_drive',lambda x:x['drive'].update(filename_tag='Vdrv=0.000V'),bad)
    control('no_implicit_record_count',lambda x:x.update(known_records=0),bad)
    control('no_implicit_group_count',lambda x:x.update(known_groups=False),bad)
    control('unknown_raw_hash_not_MD5',lambda x:x.update(raw_sha256='3fc592443a1c117ab4a9503e01d5a92c'),bad)
    control('self_release_refused',lambda x:x.update(raw_download_authorized_by_this_metadata=True),bad)
    control('self_physical_promotion_refused',lambda x:x.update(physical_promotion=1),bad)
    control('unknown_field_refused',lambda x:x.update(fresh=True),bad)
    control('missing_model_freeze_refused',lambda x:x.pop('pre_raw_freeze'),bad)
    control('forged_URI_does_not_establish_evidence',lambda x:x['exposure'].update(independent_custody_review={'uri':'file:///must-not-be-opened','sha256':'0'*64,'reviewer_or_authority':'SYNTHETIC_CONTROL_ONLY','scope':'synthetic declared reference'}),hold)
    # Public source audit is a concrete code-text predicate, not an executed notebook claim.
    src=json.loads((D/'SOURCE_CELLS.json').read_text());cells={i['index']:i['source'] for i in src['cells']['figures']}
    assert t['source']['path'] in cells[10]
    assert 'data[[0,1,2,3,4,5,6,7,9]' in cells[10]
    assert 'Jexp' in cells[22] and 'shotidx = 209' in cells[17]
    assert all(f'Fig {n}' in cells[i] for i,n in [(23,7),(25,4),(32,8)])
    rows.append({'name':'exact_candidate_source_dependency_and_channel_selection','pass':True})
    # Caller pin changes are rejected by the real CLI before parsing, not a standalone comparison.
    request=D/'CANDIDATE_REQUEST_v0.1.json'
    proc=subprocess.run([sys.executable,str(D/'check_request.py'),str(request),'--sha256','0'*64],capture_output=True,text=True)
    assert proc.returncode!=0 and 'HOLD_REQUEST_DIGEST_MISMATCH' in proc.stderr
    rows.append({'name':'actual_CLI_wrong_input_digest_refused','pass':True})
    b=request.read_bytes();pin=hashlib.sha256(b).hexdigest()
    proc=subprocess.run([sys.executable,str(D/'check_request.py'),str(request),'--sha256',pin],capture_output=True,text=True,check=True)
    cli=json.loads(proc.stdout);assert hold(cli) and cli==c.evaluate(t)
    rows.append({'name':'actual_CLI_null_request_digest_and_HOLD','pass':True})
    return {'artifact_type':'FROZEN_PRE_RAW_METADATA_CONTROLS','controls':rows,'count':len(rows),'all_pass':True,'actual_request_result':c.evaluate(t),'source_and_code_only':True,'new_raw_downloads':0,'new_fits':0,'author_code_executed':False,'physical_promotion':0}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
