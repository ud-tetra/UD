"""Hash-bound saved-factor campaign replay plus v2 certificate; no proposer/SVD.

External independence cannot be self-attested by this program.
"""
import argparse,json,subprocess,sys,os,datetime
from pathlib import Path
from source_math import P,sha,freeze
from offline_intake import extract,safe_name

def intake(repo,out):
    f=freeze()['adversarial_capture'];root=repo/'captures'/f['id']
    assert sha(root/'MANIFEST.json')==f['manifest_sha256']
    archives=[]
    for e in json.loads((root/'MANIFEST.json').read_text())['files']:
        rel=safe_name(e['path']);prefix=Path('captures')/f['id']
        assert Path(str(rel)).is_relative_to(prefix)
        q=repo/str(rel)
        assert not q.is_symlink() and q.resolve().is_relative_to(root.resolve())
        assert q.stat().st_size==e['size_bytes'] and sha(q)==e['sha256']
        if q.suffix=='.zip':archives.append(q)
    assert len(archives)==10
    dest=out/'parent-package';summary=extract(sorted(archives),dest)
    return dest,summary

def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    freeze();out=args.out.absolute();assert not out.exists();out.mkdir(parents=True)
    receipt={'status':'RUNNING','started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
             'commands':[],'new_estimator_SVD_or_raw_generation':False,
             'reviewer_identity':None,'external_nonconstructor_review':'PENDING','physical_promotion':0}
    def go(cwd,cmd,tag):
        r=subprocess.run([sys.executable,*cmd],cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'})
        log=out/(tag+'.log');log.write_bytes(r.stdout)
        receipt['commands'].append({'tag':tag,'argv':cmd,'exit_code':r.returncode,'log_sha256':sha(log)})
        assert r.returncode==0,tag
    try:
        package,summary=intake(args.repo.resolve(),out);receipt['parent_intake']=summary
        go(package,['replay_package.py','--repo',str(args.repo.resolve()),'--out',str(out/'parent-replay')],'complete-parent-replay')
        go(P,['source_math.py','--replay'],'source-allowance')
        go(P,['validate.py','--campaign',str(out/'parent-replay'),'--replay'],'actual-v2')
        go(P,['controls.py'],'boundary-controls')
        freeze()
        receipt.update(status='PASS_COMPLETE_SAVED_FACTOR_AND_V2_REPLAY',cases=3,
                       original_policy_admitted=2,original_policy_HOLD=1,
                       numerical_rows_verified=True)
    except Exception as e:
        receipt.update(status='FAIL',error=type(e).__name__+': '+str(e));raise
    finally:
        receipt['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
        (out/'REPLAY_RECEIPT.json').write_text(json.dumps(receipt,indent=2))
    print(json.dumps(receipt),flush=True)

if __name__=='__main__':main()
