#!/usr/bin/env python3
"""Frozen portability controls. Only temporary staging writes; report on stdout."""
from pathlib import Path
import hashlib,json,subprocess,tempfile,shutil,sys,os
HERE=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    if not __debug__: raise RuntimeError("Run controls without -O")
    freeze=json.loads((HERE/'PORTABILITY_FREEZE_v0.2.json').read_text())
    for item in freeze['files']:
        p=HERE/item['path']
        assert p.stat().st_size==item['bytes'] and sha(p)==item['sha256']
    old=json.loads((HERE/'MANIFEST.json').read_text())
    inputs=json.loads((HERE/'INPUT_BINDINGS.json').read_text())['inputs']
    new=json.loads((HERE/'INPUT_BINDINGS_v0.2.json').read_text())['inputs']
    before={p.name:sha(p) for p in HERE.iterdir() if p.is_file()}
    receipts=[]
    with tempfile.TemporaryDirectory(prefix='renamed-ud-audit-') as td:
        temp=Path(td)
        audit=temp/'entirely-renamed-audit'
        checkout=temp/'entirely-renamed-checkout'
        gov=temp/'canonical-governance'
        audit.mkdir(); checkout.mkdir(); gov.mkdir()
        names=[x['path'] for x in old['files']]+['MANIFEST.json','INPUT_BINDINGS_v0.2.json','verify_audit_v2.py']
        for name in names: shutil.copyfile(HERE/name,audit/name)
        for x,b in zip(inputs,new):
            target=(checkout if b['role']=='repository' else gov)/b['relative_path']
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(x['path'],target)
        def run(name,repo=checkout,governance=gov,expected='PASS',reason=None,optimized=False):
            args=[sys.executable]+(['-O'] if optimized else [])+[str(audit/'verify_audit_v2.py'),'--repo',str(repo)]
            if governance is not None: args+=['--governance-root',str(governance)]
            env=dict(os.environ); env['PYTHONDONTWRITEBYTECODE']='1'
            result=subprocess.run(args,cwd=temp,capture_output=True,text=True,env=env)
            payload=json.loads(result.stdout)
            assert payload['status']==expected,(name,result.returncode,payload,result.stderr)
            assert result.returncode==(0 if expected=='PASS' else 2)
            assert payload['absolute_path_fallback_used'] is False
            if reason: assert payload.get('reason','').startswith(reason),(name,payload)
            receipts.append({'control':name,'expected':expected,'status':payload['status'],
                             'reason':payload.get('reason'),'absolute_path_fallback_used':False})
        run('relocated_valid_roots')
        empty_repo=temp/'empty-checkout'; empty_repo.mkdir()
        run('wrong_repo_no_original_fallback',repo=empty_repo,expected='HOLD',reason='HOLD_MISSING_DECLARED_INPUT:repository')
        run('missing_governance_no_original_fallback',governance=None,expected='HOLD',reason='HOLD_MISSING_GOVERNANCE_ROOT')
        empty_gov=temp/'empty-governance'; empty_gov.mkdir()
        run('wrong_governance_no_original_fallback',governance=empty_gov,expected='HOLD',reason='HOLD_MISSING_DECLARED_INPUT:governance')
        item=next(x for x in new if x['role']=='repository' and x['relative_path'].endswith('REQUEST_TEMPLATE.json'))
        path=checkout/item['relative_path']; original=path.read_bytes(); path.write_bytes(original+b'\n')
        run('repository_hash_mutation',expected='HOLD',reason='HOLD_DECLARED_INPUT_HASH:repository')
        path.write_bytes(original)
        gp=gov/'UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md'; originalgov=gp.read_bytes();gp.write_bytes(originalgov+b'\n')
        run('governance_hash_mutation',expected='HOLD',reason='HOLD_DECLARED_INPUT_HASH:governance')
        gp.write_bytes(originalgov)
        outside=temp/'outside-copy'; outside.write_bytes(original); path.unlink(); path.symlink_to(outside)
        run('repository_symlink_escape',expected='HOLD',reason='HOLD_INPUT_ESCAPES_DECLARED_ROOT')
        path.unlink();path.write_bytes(original)
        outsidegov=temp/'outside-governance-copy'; outsidegov.write_bytes(originalgov); gp.unlink();gp.symlink_to(outsidegov)
        run('governance_symlink_escape',expected='HOLD',reason='HOLD_INPUT_ESCAPES_DECLARED_ROOT')
        gp.unlink();gp.write_bytes(originalgov)
        run('optimized_python_refused',expected='HOLD',reason='HOLD_OPTIMIZED_PYTHON_ASSERTIONS_DISABLED',optimized=True)
        altered=audit/'README.md'; altered.write_bytes(altered.read_bytes()+b'\n')
        run('original_artifact_tamper',expected='HOLD',reason='HOLD_ORIGINAL_ARTIFACT_HASH:README.md')
    after={p.name:sha(p) for p in HERE.iterdir() if p.is_file()}
    assert before==after,"Source audit directory changed during controls"
    print(json.dumps({'status':'PASS','control_count':len(receipts),'controls':receipts,
                      'execution_scope':'Renamed temporary audit plus minimal relocated checkout; no original-path fallback; stdout-only verifier',
                      'original_files_changed':False,'raw_records_opened':0,'new_fits':0,
                      'calibration_evidence_verified':False,'physical_promotion':0},indent=2))
if __name__=='__main__': main()

