"""Stage pinned dependencies and deliberately replay the counterexample proof; zero fits."""
import argparse,json,hashlib,shutil,zipfile,subprocess,sys,os
from pathlib import Path
P=Path(__file__).resolve().parent
def digest(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        while b:=f.read(1<<20):h.update(b)
    return h.hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--baseline',required=True);ap.add_argument('--out',required=True);x=ap.parse_args()
    repo=Path(x.repo).resolve();baseline=Path(x.baseline).resolve();out=Path(x.out).resolve()
    assert out!=P and P not in out.parents;out.mkdir(parents=True,exist_ok=False)
    fr=json.loads((P/'COUNTEREXAMPLE_REPLAY_FREEZE.json').read_text())
    for name,h in fr['files'].items():assert digest(P/name)==h,name
    stage=out/'sources';stage.mkdir();target=stage/'strict-family-review-20261019'
    # Read-only witness hardlinks; isolated hostile controls unlink before mutation.
    shutil.copytree(P/'counterexample',target,copy_function=os.link,ignore=shutil.ignore_patterns('__pycache__','*.pyc','.*'))
    rows=json.loads((P/'COUNTEREXAMPLE_SOURCE_INDEX.json').read_text())['sources']
    for row in rows:
        dest=(stage/row['target']).resolve();assert stage.resolve() in dest.parents;dest.parent.mkdir(parents=True,exist_ok=True)
        if row['kind']=='caller_baseline':
            assert digest(baseline)==row['sha256'];dest.symlink_to(baseline)
        elif row['kind']=='repository_file':
            src=repo/row['source_path'];manifest=repo/'captures'/Path(row['source_path']).parts[1]/'MANIFEST.json'
            assert digest(src)==row['sha256'] and digest(manifest)==row['source_manifest_sha256'];os.link(src,dest)
        else:
            archive=repo/row['archive'];manifest=repo/'captures'/row['capture']/'MANIFEST.json'
            assert digest(archive)==row['archive_sha256'] and digest(manifest)==row['manifest_sha256']
            with zipfile.ZipFile(archive) as z:
                assert z.namelist().count(row['member'])==1;b=z.read(row['member'])
            assert len(b)==row['size_bytes'] and hashlib.sha256(b).hexdigest()==row['sha256'];dest.write_bytes(b)
        assert digest(dest)==row['sha256']
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    subprocess.run([sys.executable,str(target/'replay_controls.py'),'--out',str(out/'checks'),'--baseline',str(baseline)],env=env,check=True)
    r=json.loads((out/'checks/REPLAY_AND_CONTROLS.json').read_text());assert r['saved_factor_result_exact_equal'] and len(r['controls'])==3
    for name,h in fr['files'].items():assert digest(P/name)==h,name
    summary={'status':'PASS_PORTABLE_COUNTEREXAMPLE_REPLAY','source_dependencies_checked':len(rows),'raw_scalar_checks':r['raw_replay']['raw_scalars_checked'],'projection_entries':r['raw_replay']['projection_entries_recomputed'],'hostile_controls':3,'saved_counterexample_exactly_reproduced':True,'new_estimator_fits':0,'physical_promotion':0}
    (out/'PORTABLE_REPLAY.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
if __name__=='__main__':main()
