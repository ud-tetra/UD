"""Portable zero-fit replay entrypoint, including all five frozen logic controls."""
import argparse,json
from pathlib import Path
from datetime import datetime,timezone
from common import P,sha,freeze
import controls
import replay
def main(baseline,out,controls_only=False):
    freeze();f=json.loads((P/'REPLAY_ALL_FREEZE.json').read_text())
    for n,h in f['files'].items():assert sha(P/n)==h,n
    out=Path(out);out.mkdir(parents=True,exist_ok=False);c=out/'logical_controls';c.mkdir();original=controls.P
    try:controls.P=c;controls.run()
    finally:controls.P=original
    assert json.loads((c/'CONTROLS.json').read_text())==json.loads((P/'CONTROLS.json').read_text())
    if not controls_only:replay.main(baseline,out/'proof')
    for n,h in f['files'].items():assert sha(P/n)==h,n
    result={'status':'PASS_LOGICAL_CONTROLS_ONLY' if controls_only else 'PASS_FULL_ZERO_FIT_DIRECTIONAL_REPLAY_AND_FIVE_LOGIC_CONTROLS','five_logic_controls_exact_equal':True,'full_proof_replay_executed':not controls_only,'new_estimator_runs':0,'new_proposer_calls':0,'new_SVD_runs':0,'wrapper_freeze_sha256':sha(P/'REPLAY_ALL_FREEZE.json'),'completed_utc':datetime.now(timezone.utc).isoformat(),'physical_promotion':0};(out/'ALL_REPLAY_RECEIPT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--baseline',required=True);p.add_argument('--out',required=True);p.add_argument('--controls-only',action='store_true');a=p.parse_args();main(a.baseline,a.out,a.controls_only)
