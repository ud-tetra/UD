#!/usr/bin/env python3
"""Pin-check upstream evidence and rerun only fresh constructor verifiers in a temporary copy."""
from pathlib import Path
import argparse,subprocess,hashlib,json,tempfile,sys,os
C=Path(__file__).parent

def run(repo):
    index=json.loads((C/'EVIDENCE_INDEX.json').read_text());by={e['pr']:e for e in index['upstream']}
    def blob(ref,path):return subprocess.check_output(['git','show',ref+':'+path],cwd=repo)
    def sha(b):return hashlib.sha256(b).hexdigest()
    checked=0
    with tempfile.TemporaryDirectory(prefix='ud-review-reproduction-') as td:
        root=Path(td)
        for e in index['upstream']:
            raw=blob(e['commit'],e['manifest_path']);assert sha(raw)==e['manifest_sha256']
            manifest=json.loads(raw);assert manifest['files']==e['files'] and manifest['physical_promotion']==0
            for f in e['files']:
                data=blob(e['commit'],f['path'])
                assert sha(data)==f['sha256'] and len(data)==f['size_bytes']
                p=root/f['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data);checked+=1
        for s in index['source_files']:
            data=blob(s['commit'],s['path']);assert sha(data)==s['sha256'] and len(data)==s['size_bytes']
            p=root/s['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
        def path(pr,name):return root/by[pr]['capture']/name
        env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
        steps=[]
        def execute(pr,script,output,args=(),compare=True):
            target=path(pr,output);before=json.loads(target.read_text())
            proc=subprocess.run([sys.executable,str(path(pr,script)),*map(str,args)],cwd=root,env=env,capture_output=True,text=True,timeout=60)
            assert proc.returncode==0,proc.stderr
            after=json.loads(target.read_text())
            if compare:assert before==after,(pr,output,'regenerated output differs')
            steps.append({'pr':pr,'script':script,'exit_code':proc.returncode,'output':output,
                          'original_json_equal':True if compare else 'not required: original floating residual receipt retained',
                          'stdout':proc.stdout.strip(),'constructor_only':True})
        execute(350,'verify_components.py','RESULTS.json')
        execute(352,'verify_payload.py','VERIFICATION.json',compare=False)
        execute(354,'verify_reduction.py','CERTIFICATE.json')
        execute(354,'compare_replay.py','REPLAY_COMPARISON.json',[
            '--results',path(352,'RESULTS.json'),'--payload',path(352,'NUMERICAL_PAYLOAD.npz')])
        execute(355,'verify_reduction.py','CERTIFICATE.json')
        execute(356,'verify_certificate.py','CERTIFICATE.json')
        execute(358,'audit_replay.py','AUDIT.json',[
            '--payload',path(352,'NUMERICAL_PAYLOAD.npz'),'--results',path(352,'RESULTS.json'),
            '--receipt',path(352,'PRE_RUN_RECEIPT.json')])
    return {'status':'PASS_CONSTRUCTOR_REPRODUCTION','upstream_captures':len(by),'upstream_files_hash_checked':checked,
            'source_files_hash_checked':len(index['source_files']),'steps':steps,'physical_promotion':0,
            'independent_review':'NOT_PERFORMED','lane':'development — no registry entry',
            'meaning':'Pinned bytes verified; selected fresh constructor checks rerun in disposable copies. No promotion or blinded preregistration.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);args=p.parse_args()
    result=run(args.repo.resolve());(C/'REPRODUCTION.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='steps'}))
