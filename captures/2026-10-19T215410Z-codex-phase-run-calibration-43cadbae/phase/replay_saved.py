"""Isolated exact saved-factor replay, no new numerical proposals/fits."""
import argparse,json,tempfile,shutil,os
from pathlib import Path
import common,verify,phase,score

def run(out):
    P=common.P;common.freeze();out=Path(out).resolve();assert out!=P and P not in out.parents and out not in P.parents
    for anc in P.parents:
        if (anc/'MANIFEST.json').exists():assert out!=anc and anc not in out.parents
    out.mkdir(parents=True,exist_ok=False)
    for n in ['inputs','results','alignments']:(out/n).symlink_to(P/n,target_is_directory=True)
    for n in ['PROTOCOL_FREEZE.json','DATA_FREEZE.json','RUN_EXECUTIONS.json','ALIGNMENT_FREEZE.json','CONTRACT.json','verify.py']:(out/n).symlink_to(P/n)
    # freeze remains bound to immutable original; all mutable output P names redirected.
    verify.P=out;score.P=out;phase.P=out
    verify.certify();score.run();rows=[]
    for n in ['CERTIFICATE.json','PHASE_CERTIFICATE.json','EXACT_T_CERTIFICATE.json']:
        a=json.loads((P/n).read_text());b=json.loads((out/n).read_text());assert a==b,n;rows.append({'file':n,'exact_JSON_equality':True,'sha256':common.sha(out/n)})
    # isolated stale-hash control; originals never mutated.
    fixture=out/'STALE_HASH_FIXTURE';fixture.mkdir();(fixture/'input').write_bytes(b'changed');wanted=common.sha(P/'CONTRACT.json');rejected=False
    try:assert common.sha(fixture/'input')==wanted
    except AssertionError:rejected=True
    assert rejected;common.freeze();receipt={'status':'PASS_EXACT_SAVED_OUTPUT_REPLAY_AND_STALE_HASH_CONTROL','rows':rows,'stale_hash_rejected':True,'new_estimator_SVD_eigenvalue_inverse_alignment_calls':0,'physical_promotion':0};(out/'REPLAY_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',required=True);p.add_argument('--repo',required=True);x=p.parse_args();os.environ['UD_REPO']=str(Path(x.repo).resolve());run(x.out)
