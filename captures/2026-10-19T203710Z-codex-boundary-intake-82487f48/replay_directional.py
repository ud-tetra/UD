"""Stage pinned sources and deliberately replay four saved outputs; no estimator fits."""
import argparse, hashlib, json, os, shutil, subprocess, sys, zipfile
from pathlib import Path
P=Path(__file__).resolve().parent
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        while b:=f.read(1<<20):h.update(b)
    return h.hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--baseline',required=True);ap.add_argument('--out',required=True);x=ap.parse_args()
    repo=Path(x.repo).resolve();base=Path(x.baseline).resolve();out=Path(x.out).resolve()
    assert out!=P and P not in out.parents;out.mkdir(exist_ok=False,parents=True)
    freeze=json.loads((P/'PORTABLE_DIRECTIONAL_FREEZE.json').read_text())
    for n,h in freeze['files'].items():assert sha(P/n)==h,n
    stage=out/'sources';stage.mkdir();target=stage/'directional-admission-work-20261019'
    shutil.copytree(P/'directional',target,copy_function=os.link,ignore=shutil.ignore_patterns('__pycache__','*.pyc','.*'))
    sources=json.loads((P/'DIRECTIONAL_SOURCE_INDEX.json').read_text())['sources']
    for row in sources:
        dst=(stage/row['target']).resolve();assert stage.resolve() in dst.parents;dst.parent.mkdir(parents=True,exist_ok=True)
        if row['kind']=='caller_baseline':
            assert sha(base)==row['sha256'];dst.symlink_to(base)
        elif row['kind']=='repository_file':
            src=repo/row['source_path'];manifest=repo/'captures'/Path(row['source_path']).parts[1]/'MANIFEST.json'
            assert sha(src)==row['sha256'] and sha(manifest)==row['source_manifest_sha256'];os.link(src,dst)
        else:
            archive=repo/row['archive'];manifest=repo/'captures'/row['capture']/'MANIFEST.json'
            assert sha(archive)==row['archive_sha256'] and sha(manifest)==row['manifest_sha256']
            with zipfile.ZipFile(archive) as z:
                assert z.namelist().count(row['member'])==1;b=z.read(row['member'])
            assert len(b)==row['size_bytes'] and hashlib.sha256(b).hexdigest()==row['sha256'];dst.write_bytes(b)
        assert sha(dst)==row['sha256']
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    subprocess.run([sys.executable,str(target/'replay_all.py'),'--baseline',str(base),'--out',str(out/'checks')],env=env,check=True)
    for n,h in freeze['files'].items():assert sha(P/n)==h,n
    result={'status':'PASS_PORTABLE_FOUR_DIRECTIONAL_SAVED_OUTPUT_REPLAY','source_dependencies_checked':len(sources),'new_estimator_fits':0,'scope':'Data-only source staging and deliberate replay of saved exact witnesses, fixed logical controls, full raw/projection reconstruction and hash rejection; no phase/hardware qualification','physical_promotion':0}
    (out/'PORTABLE_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
