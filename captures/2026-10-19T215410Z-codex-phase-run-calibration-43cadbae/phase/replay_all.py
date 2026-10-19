"""Portable full raw/projection and exact saved-proof replay; ZERO new fits."""
import argparse,json,os
from pathlib import Path
import common,driver,replay_saved

def run(repo,baseline,out):
    os.environ['UD_REPO']=str(Path(repo).resolve());P=common.P;common.freeze();out=Path(out).resolve()
    assert out!=P and P not in out.parents and out not in P.parents
    for anc in P.parents:
        if (anc/'MANIFEST.json').exists():assert out!=anc and anc not in out.parents
    out.mkdir(parents=True,exist_ok=False);view=out/'raw';view.mkdir()
    for n in ['CONTRACT.json','PROTOCOL_FREEZE.json','DATA_FREEZE.json']:(view/n).symlink_to(P/n)
    driver.P=view;driver.replay_raw(str(Path(baseline).resolve()));replay_saved.run(out/'saved')
    common.freeze();receipt={'status':'PASS_PORTABLE_FULL_RAW_PROJECTION_AND_SAVED_FACTOR_REPLAY','raw_replay_sha256':common.sha(view/'RAW_REPLAY.json'),'saved_replay_sha256':common.sha(out/'saved/REPLAY_RECEIPT.json'),'new_estimator_SVD_eigenvalue_inverse_alignment_calls':0,'scope':'One complete four-record raw/projection regeneration and exact saved-proof replay; no new estimator or proposals.','physical_promotion':0};(out/'REPLAY_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--baseline',required=True);p.add_argument('--out',required=True);x=p.parse_args();run(x.repo,x.baseline,x.out)
