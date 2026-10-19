"""Portable source-indexed proof replay; no estimator/SVD/alignment proposals."""
import argparse,json,shutil
from pathlib import Path
from datetime import datetime,timezone
import common,phase,controls
from common import P,sha
def source_checks(repo,f):
    for name,h in f['source_files'].items():
        assert name.startswith('ud-repo/');assert sha(repo/name[len('ud-repo/'):])==h,name
def main(repo,out):
    repo=Path(repo).resolve();out=Path(out).resolve();f=json.loads((P/'PROTOCOL_FREEZE.json').read_text());rf=json.loads((P/'REPLAY_FREEZE.json').read_text())
    for n,h in f['files'].items():assert sha(P/n)==h,n
    for n,h in rf['files'].items():assert sha(P/n)==h,n
    source_checks(repo,f);out.mkdir(parents=True,exist_ok=False);stage=out/'stage';stage.mkdir();(stage/'ud-repo').symlink_to(repo,target_is_directory=True);view=stage/'phase';view.mkdir()
    for name in [*f['files'],'PROTOCOL_FREEZE.json']:
        dest=view/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(P/name,dest)
    saved=(common.P,phase.P,controls.P)
    try:
        common.P=phase.P=controls.P=view
        controls.run();phase.run()
        assert json.loads((view/'CONTROLS.json').read_text())==json.loads((P/'CONTROLS.json').read_text())
        assert json.loads((view/'CERTIFICATE.json').read_text())==json.loads((P/'CERTIFICATE.json').read_text())
        # Only an isolated small copied source-input is corrupted; repository data untouched.
        q=view/'inputs/SOURCE_PHASE.json';expected=sha(q);q.write_bytes(q.read_bytes()+b'\n')
        try:common.freeze()
        except AssertionError as exc:
            assert exc.args[0]==('code/input','inputs/SOURCE_PHASE.json')
            rejection={'status':'ASSERTION_REJECTION','reason':str(exc),'expected_sha256':expected,'corrupted_fixture_sha256':sha(q)}
        else:raise AssertionError('corrupted target-source hash accepted')
    finally:common.P,phase.P,controls.P=saved
    for n,h in f['files'].items():assert sha(P/n)==h,n
    for n,h in rf['files'].items():assert sha(P/n)==h,n
    source_checks(repo,f)
    result={'status':'PASS_FULL_FOUR_SAVED_PHASE_AND_TEN_CONTROL_PORTABLE_REPLAY','phase_certificate_exact_equal':True,'ten_controls_exact_equal':True,'source_dependencies_checked':len(f['source_files']),'emitted_angles_checked':836,'source_hash_negative_control':rejection,'all_original_source_and_code_hashes_unchanged':True,'new_estimator_SVD_alignment_inverse_proposals':0,'raw_U_SVD_copies':0,'replay_freeze_sha256':sha(P/'REPLAY_FREEZE.json'),'completed_utc':datetime.now(timezone.utc).isoformat(),'scope':'Data-only immutable repository source indexing and exact finite proof replay, plus post-known-outcome isolated custody control. No raw measurements, fits, new policies or physical qualification.','external_review':'PENDING','physical_promotion':0}
    (out/'REPLAY_RECEIPT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--out',required=True);a=p.parse_args();main(a.repo,a.out)
