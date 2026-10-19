"""Freeze operational code/source metadata; no recipes, raw data or solver calls."""
import json,hashlib,ast
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
P=Path(__file__).resolve().parent
sha=lambda x:hashlib.sha256(Path(x).read_bytes()).hexdigest()

def run():
    assert not(P/'PROTOCOL_FREEZE.json').exists() and not(P/'DATA_FREEZE.json').exists() and not(P/'results').exists()
    C=json.loads((P/'CONTRACT.json').read_text());idx=json.loads((P/'SOURCE_INDEX.json').read_text());repo=P.parent/'ud-repo'
    assert sha(P/'CONTRACT.json')=='f58b24fe11234df38f9870319a208580937c0428af5bdce67c0188f81d6c81b4'
    assert sha(P/'recipes.py')=='909392cc1a6566f6d821deac5da140fb76e3fbc92c3612bf057871d48cb4e521'
    assert sha(P/'estimator.py')==C['unchanged_actual_estimator_source_sha256']=='5fa15ca0f3830f168fe9e1483db7f21cb6e462780209b4d8b4e8ad43d64cfe86'
    assert C['fixed_case_order']==['new_A_control','new_A_ramped_low','new_B_control','new_B_chirped_high']
    g=json.loads((P/'inputs/OLD_POLICY.json').read_text())['gates'];assert set(C['unchanged_phase_quality_caps'])=={'inverse_residual','proposed_inverse_norm','eigenpair_residual','emitted_argument_error'}
    assert {k:g[k] for k in C['unchanged_phase_quality_caps']}==C['unchanged_phase_quality_caps']
    b=json.loads((P/'inputs/FIXED_BUDGET.json').read_text())['source_budget'];caps=C['unchanged_frame_caps']
    assert F(*b['allowed_raw_frame_residual_lower'])==F(*caps['strict_raw_alignment']) and F(*b['retained_Gram_cap'])==F(*caps['nonstrict_retained_Gram']) and F(*b['normal_cap'])==F(*caps['nonstrict_normal'])
    phase=json.loads((P/'inputs/SOURCE_PHASE.json').read_text());assert len(phase['target_matches'])==209 and F(*phase['metrics']['minimum_target_chord_lower'])==F(*C['fixed_source_minimum_chord_lower'])
    for n,h in idx['repository_sources'].items():assert sha(repo/n)==h,n
    for n in P.glob('*.py'):ast.parse(n.read_text())
    files={str(n.relative_to(P)):sha(n) for n in sorted(P.rglob('*')) if n.is_file() and '__pycache__' not in n.parts and n.name!='PROTOCOL_FREEZE.json'}
    out={'status':'OPERATIONAL_RUNNER_FROZEN_BEFORE_ANY_CARRIER_RAW_OR_FIT','frozen_utc':datetime.now(timezone.utc).isoformat(),'case_order':C['fixed_case_order'],'files':files,'repository_sources':idx['repository_sources'],'reference_basis_archives':idx['reference_basis_archives'],'baseline_sha256':C['expected_synthetic_baseline_sha256'],'planned_estimator_calls':4,'case_policy':'All four complete data/projection hashes before firstfit; GLOBAL_DATA_HOLD=zero fits, then once per case, no retries or order forcing, all outcomes retained','known_before_freeze':'PR237/240/244 outcomes known. PR246 four future records/carriers and all resulting estimator/phase/frame outcomes NOT evaluated before this operational freeze. Same-team adversarial static review, not blinded or external registration.','raw_storage':'Anonymous memfd, sequential, no persistent raw150MB copies.','scope':'Four finite synthetic preparations/noise recipes. Phaseidentity half-sourcechord gate is not2^-39 calibration gate. Strict frame/Gram/normal and exact-T optional secondary separate.','external_review':'PENDING','physical_promotion':0}
    (P/'PROTOCOL_FREEZE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'protocol_sha256':sha(P/'PROTOCOL_FREEZE.json'),'frozen_files':len(files)}))
if __name__=='__main__':run()
