"""Portable METADATA-only revalidation; deliberately no raw/profile/solver calls."""
import sys
sys.dont_write_bytecode=True
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from recipes import DEN,cayley_numerator,matmul,seeded_spatial,round_ratio
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main(repo,out):
    repo=Path(repo).resolve();out=Path(out).resolve();capture=P.resolve()
    assert out!=capture and capture not in out.parents and out not in capture.parents,'Output must be NEW and external to this capture and its ancestors'
    capture_root=next((a for a in [capture,*capture.parents] if (a/'MANIFEST.json').is_file()),capture)
    assert out!=capture_root and capture_root not in out.parents and out not in capture_root.parents,'Output must be external to the entire manifested capture'
    out.mkdir(parents=True,exist_ok=False)
    f=json.loads((P/'PROTOCOL_FREEZE.json').read_text())
    for n,h in f['files'].items():assert sha(P/n)==h,n
    index=json.loads((P/'SOURCE_INDEX.json').read_text())
    for row in index['sources']:
        src=repo/row['repository_source'];manifest=repo/Path(*Path(row['repository_source']).parts[:2])/'MANIFEST.json'
        assert sha(src)==row['sha256'] and sha(manifest)==row['capture_manifest_sha256']
    provenance=json.loads((P/'INPUT_PROVENANCE.json').read_text())
    for row in provenance['copied_inputs']:
        assert sha(P/row['destination'])==sha(repo/row['repository_source'])==row['sha256']
    rows={r['role']:r for r in index['sources']};anchors=json.loads((repo/rows['anchor_data']['repository_source']).read_text())['records'];oldsp=json.loads((repo/rows['old_spatial_selection']['repository_source']).read_text());c=json.loads((P/'CONTRACT.json').read_text())
    assert c['fixed_case_order']==['new_A_control','new_A_ramped_low','new_B_control','new_B_chirped_high'] and c['planned_future_estimator_runs']==4
    for prep in c['preparations']:
        parent=next(r for r in anchors if r['case']==prep['existing_family_reference_anchor']);assert parent['transform_denominator']==1
        M=matmul(cayley_numerator(prep['pairing_cyclic_offset_within_parity']),parent['transform_integer_matrix']);assert M==prep['matrix_numerator'] and prep['denominator']==DEN
        assert all(sum(M[i][k]*M[j][k] for k in range(37))==DEN*DEN*int(i==j) for i in range(37) for j in range(37));assert all(not M[i][j] or i%2==j%2 for i in range(37) for j in range(37));assert F(4,DEN)<F(1,1<<40)
    A=[{'preparation':a,'channel':int(oldsp['channels'][a]),'sign':int(oldsp['signs'][a])} for a in range(37)];B=seeded_spatial();targets=json.loads((P/'inputs/SOURCE_PHASE.json').read_text());bylabel={r['label']:r for r in targets['target_matches']}
    for case in c['cases']:assert case['spatial']==(A if case['preparation_id']=='A' else B) and case['carrier_omega']==bylabel[case['carrier_target_label']]['omega']
    sep=F(*targets['metrics']['minimum_target_chord_lower']);assert F(*c['strict_finite_emission_circular_error_cap'])==sep/2
    caps=json.loads((P/'inputs/OLD_POLICY.json').read_text())['gates'];assert all(v==caps[k] for k,v in c['unchanged_phase_quality_caps'].items())
    assert sha(repo/rows['actual_estimator']['repository_source'])==c['unchanged_actual_estimator_source_sha256']
    assert [round_ratio(n,2) for n in [-3,-1,1,3]]==[-2,0,0,2]
    for n,h in f['files'].items():assert sha(P/n)==h,n
    receipt={'status':'PASS_PORTABLE_METADATA_ONLY_PROTOCOL_REVALIDATION','protocol_sha256':sha(P/'PROTOCOL_FREEZE.json'),'contract_sha256':sha(P/'CONTRACT.json'),'source_dependencies_checked':len(index['sources']),'preparation_integer_orthogonality_equalities_checked':2*37*37,'source_separation_cap_and_estimator_hash_unchanged':True,'time_indexed_carrier_or_profile_tables_generated':0,'raw_records_generated':0,'estimator_SVD_eigenvalue_inverse_alignment_calls':0,'scope':'Static future contract only, not a future phase/frame/cutoff outcome or calibration2^-39 guarantee.','completed_utc':datetime.now(timezone.utc).isoformat(),'external_review':'PENDING','physical_promotion':0};(out/'STATIC_REPLAY.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--out',required=True);a=p.parse_args();main(a.repo,a.out)
