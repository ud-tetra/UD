"""Frozen metadata-only intake controls; never signing or fitting."""
import argparse,json,subprocess,sys,hashlib,os
from pathlib import Path
from make_controls_v2 import generate
P=Path(__file__).resolve().parent
def need(ok,reason):
    if not ok:raise RuntimeError(reason)
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);x=ap.parse_args();out=Path(x.out).resolve()
    need(out!=P and P not in out.parents,'OUTPUT_MUST_BE_NEW_EXTERNAL_DIRECTORY');out.mkdir(parents=True,exist_ok=False)
    freeze=json.loads((P/'PROTOCOL_FREEZE_v0.2.json').read_text())
    for n,h in freeze['files'].items():need(digest(P/n)==h,'FROZEN_FILE_CHANGED '+n)
    index=generate(out/'metadata_controls');need(len(index)==20 and len({r['id'] for r in index})==20,'CONTROL_COVERAGE')
    rows=[];env=dict(os.environ);env.pop('PYTHONPATH',None);env['PYTHONDONTWRITEBYTECODE']='1'
    for case in index:
        script=P/'intake_v2.py' if case['script']=='intake_v2.py' else out/'metadata_controls'/case['script']
        command=[sys.executable,str(script)]
        if case['request'] is not None:command+=['--request',str(out/'metadata_controls'/case['request'])]
        if case['expected_request_sha256'] is not None:command+=['--expected-request-sha256',case['expected_request_sha256']]
        completed=subprocess.run(command,capture_output=True,text=True,env=env,check=False);need(completed.returncode==0,'CONTROL_PROCESS_FAILED '+case['id']);value=json.loads(completed.stdout)
        need(value['status']==case['expected_status'],'CONTROL_STATUS '+case['id'])
        if case['expected_reason'] is not None:need(value['blocking_items']==[case['expected_reason']],'CONTROL_REASON '+case['id'])
        need(value['delegations']==case['expected_delegations'],'DELEGATION_SCOPE '+case['id'])
        need(value['real_records_evaluated']==value['actual_real_records_verified']==value['actual_hardware_acquisitions_verified']==value['physical_promotion']==0,'REAL_OR_PHYSICAL_SCOPE')
        need(value['physical_verdict']=='HOLD_UNQUALIFIED','PHYSICAL_HOLD');rows.append({'id':case['id'],'result':value})
    # Security gates must remain active under optimized Python.
    optimized=[]
    for name in ['absent_real_evidence','known_fixture_public_key_relabelled']:
        case=next(c for c in index if c['id']==name);cmd=[sys.executable,'-O',str(P/'intake_v2.py')]
        if case['request'] is not None:cmd+=['--request',str(out/'metadata_controls'/case['request']),'--expected-request-sha256',case['expected_request_sha256']]
        c=subprocess.run(cmd,capture_output=True,text=True,env=env,check=False);need(c.returncode==0,'OPTIMIZED_PROCESS');value=json.loads(c.stdout);need(value==next(r['result'] for r in rows if r['id']==name),'OPTIMIZED_GATE_CHANGED');optimized.append({'id':name,'same_result_under_python_O':True})
    result={'status':'PASS_FROZEN_METADATA_PREFLIGHT_CONTROLS','rows':rows,'controls':len(rows),'optimized_controls':optimized,'actual_real_records_evaluated':0,'actual_hardware_acquisitions':0,'new_signing_keys':0,'new_signatures':0,'new_fits':0,'metadata_only_routing_probes':1,'unchanged_verifier_placeholder_handoffs':sum(r['result']['delegations'] for r in rows),'real_authentication_path_evaluated':False,'protocol_sha256':digest(P/'PROTOCOL_FREEZE_v0.2.json'),'physical_promotion':0,'external_review':'PENDING'}
    (out/'CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    (out/'ACTUAL_INTAKE_RESULT.json').write_text(json.dumps(rows[0]['result'],indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['rows','optimized_controls']}))
if __name__=='__main__':main()
