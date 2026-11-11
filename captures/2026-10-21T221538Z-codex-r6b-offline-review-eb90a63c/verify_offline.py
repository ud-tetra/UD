#!/usr/bin/env python3
"""Reproduce pinned constructor checks from staged bytes; no git or network calls."""
from pathlib import Path
import hashlib,json,sys,tempfile,shutil,subprocess,os,argparse
C=Path(__file__).parent

def verify(output):
    integrity=json.loads((C/'BUNDLE_FILES.json').read_text())
    for f in integrity['files']:
        p=C/f['path'];assert p.stat().st_size==f['size_bytes']
        assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256'],f['path']
    idx=json.loads((C/'EVIDENCE_INDEX.json').read_text());by={e['pr']:e for e in idx['upstream']};checked=0
    for e in idx['upstream']:
        m=C/'evidence'/e['manifest_path'];raw=m.read_bytes()
        assert hashlib.sha256(raw).hexdigest()==e['manifest_sha256']
        assert json.loads(raw)['files']==e['files']
        for f in e['files']:
            p=C/'evidence'/f['path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256']
            assert p.stat().st_size==f['size_bytes'];checked+=1
    for f in idx['source_files']:
        p=C/'evidence'/f['path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256']
    env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
    steps=[]
    with tempfile.TemporaryDirectory(prefix='r6b-offline-verified-copy-') as td:
        root=Path(td);shutil.copytree(C/'evidence',root,dirs_exist_ok=True)
        def path(pr,name):return root/by[pr]['capture']/name
        def execute(pr,script,out,args=(),same=True):
            target=path(pr,out);before=json.loads(target.read_text())
            proc=subprocess.run([sys.executable,str(path(pr,script)),*map(str,args)],cwd=root,env=env,capture_output=True,text=True,timeout=60)
            if proc.returncode:raise RuntimeError(proc.stderr)
            after=json.loads(target.read_text())
            if same:assert before==after,(pr,out,'regenerated JSON differs')
            steps.append({'pr':pr,'script':script,'exit_code':proc.returncode,'output':out,
                          'exact_original_json_equal':True if same else None,'stdout':proc.stdout.strip()})
        execute(350,'verify_components.py','RESULTS.json')
        execute(352,'verify_payload.py','VERIFICATION.json',same=False)
        execute(354,'verify_reduction.py','CERTIFICATE.json')
        execute(354,'compare_replay.py','REPLAY_COMPARISON.json',['--results',path(352,'RESULTS.json'),'--payload',path(352,'NUMERICAL_PAYLOAD.npz')])
        execute(355,'verify_reduction.py','CERTIFICATE.json')
        execute(356,'verify_certificate.py','CERTIFICATE.json')
        execute(358,'audit_replay.py','AUDIT.json',['--payload',path(352,'NUMERICAL_PAYLOAD.npz'),'--results',path(352,'RESULTS.json'),'--receipt',path(352,'PRE_RUN_RECEIPT.json')])
    result={'status':'PASS_REPRODUCTION_ONLY','physical_promotion':0,'reviewer_identity':None,
            'independent_proof_review':'NOT_ESTABLISHED_BY_SCRIPT_EXECUTION','upstream_files_hash_checked':checked,
            'upstream_manifests_hash_checked':len(by),'source_files_hash_checked':len(idx['source_files']),
            'steps':steps,'meaning':'Current executor reproduces pinned constructor checks; add separate attributed review findings.'}
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='steps'}))
    return result
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=C/'REPRODUCTION.json');a=p.parse_args();verify(a.output)
