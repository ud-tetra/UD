"""Full frozen-record/projection and exact saved-factor replay; zero new fits."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,shutil
from pathlib import Path
from datetime import datetime,timezone
from common import P,sha,freeze
import driver
import verify as proof
from estimator import project
def main(baseline,out):
    f=freeze();sf=json.loads((P/'REPLAY_FREEZE.json').read_text())
    for n,h in sf['files'].items():assert sha(P/n)==h,n
    out=Path(out);out.mkdir(exist_ok=False);data=json.loads((P/'DATA_FREEZE.json').read_text());projs=json.loads((P/'PROJECTION_REPLAYS.json').read_text())['rows'];rawrows=[]
    for record,old in zip(data['records'],projs):
        fd,raw,fresh=driver.memrecord(baseline,record['integer_amplitude'])
        try:
            assert fresh==record;N,p=project(raw);assert p==old['projection'];rawrows.append({'case':record['case'],'record_sha256':sha(raw),'scalars_rechecked':18790154,'vectors_rechecked':303067,'projection_entries_recomputed':int(N.size),'projection':p});del N
        finally:os.close(fd)
    # Fresh external view: hardlink immutable NPZ data, copy only small metadata.
    view=out/'saved_factor_view';view.mkdir();(view/'results').mkdir();(view/'alignments').mkdir();(view/'inputs').mkdir()
    for n in ['RUN_EXECUTIONS.json','DATA_FREEZE.json','PROTOCOL_FREEZE.json','ALIGNMENT_FREEZE.json','verify.py']:shutil.copyfile(P/n,view/n)
    for p in (P/'inputs').iterdir():shutil.copyfile(p,view/'inputs'/p.name)
    for p in (P/'alignments').iterdir():os.link(p,view/'alignments'/p.name)
    for record in data['records']:
        source=P/'results'/record['case'];dest=view/'results'/record['case'];dest.mkdir()
        for p in source.iterdir():
            if p.suffix=='.npz':os.link(p,dest/p.name)
            else:shutil.copyfile(p,dest/p.name)
    originalP=proof.P;originalfreeze=proof.freeze
    def replay_freeze():
        f=freeze().copy();f['reference_basis_sources']={k:str(P.parent/v) for k,v in f['reference_basis_sources'].items()};return f
    try:proof.P=view;proof.freeze=replay_freeze;proof.certify()
    finally:proof.P=originalP;proof.freeze=originalfreeze
    assert json.loads((view/'CERTIFICATE.json').read_text())==json.loads((P/'CERTIFICATE.json').read_text())
    shutil.copyfile(view/'CERTIFICATE.json',out/'EXACT_SAVED_FACTOR_CERTIFICATE.json')
    (view/'CERTIFICATE.json').unlink()
    # Hash corruption negative control: alter a copied alignment, keep old expected hash.
    import numpy as np
    af=json.loads((view/'ALIGNMENT_FREEZE.json').read_text());first=next(r for r in af['rows'] if 'alignment'in r);p=view/first['alignment']
    with np.load(p,allow_pickle=False) as z:X=z['alignment'].copy()
    p.unlink();X[0,0]+=1.;np.savez_compressed(p,alignment=X)
    try:
        proof.P=view;proof.freeze=replay_freeze;proof.certify()
    except AssertionError as exc:
        import traceback
        last=traceback.extract_tb(exc.__traceback__)[-1]
        assert last.name=='certify' and 'sha(P/row' in last.line
        rejection={'status':'ASSERTION_REJECTION','message':str(exc),'rejection_function':last.name,'rejection_line':last.line,'expected_alignment_sha256':first['sha256'],'mutated_alignment_sha256':sha(p)}
    else:raise AssertionError('stale alignment hash accepted')
    finally:proof.P=originalP;proof.freeze=originalfreeze
    for n,h in sf['files'].items():assert sha(P/n)==h,n
    freeze();receipt={'status':'PASS_ALL_FOUR_FULL_RAW_PROJECTION_AND_EXACT_SAVED_FACTOR_REPLAY','completed_utc':datetime.now(timezone.utc).isoformat(),'raw_rows':rawrows,'total_scalars_rechecked':4*18790154,'total_vector_norms_rechecked':4*303067,'total_projection_entries_recomputed':4*2629311,'saved_factor_certificate_exact_equal':True,'negative_hash_control':rejection,'new_estimator_runs':0,'new_SVD_runs':0,'persistent_raw_files':0,'replay_freeze_sha256':sha(P/'REPLAY_FREEZE.json'),'all_original_frozen_sources_unchanged':True,'scope':'Same-team replay and known-outcome engineering hash control. Reference source paths rebound only to identical verified arrays; all original frozen files unchanged. No fits, amplitude selection or threshold changes.','external_review':'PENDING','physical_promotion':0}
    (out/'REPLAY_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'status':receipt['status'],'new_fits':0}),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--baseline',required=True);p.add_argument('--out',required=True);a=p.parse_args();main(a.baseline,a.out)
