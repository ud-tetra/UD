"""Exact JSON/Fraction-endpoint comparison; no scientific calculations."""
import json,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent;R=P.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
f=json.loads((P/'PORTABLE_COMPARISON_FREEZE.json').read_text())
for n,h in f['files'].items():assert sha(R/n)==h,n
old=json.loads((P/'BOUNDS.json').read_text());new=json.loads((R/'frame-apparatus-work-20261019/results/FAMILY_PHASE_CERTIFICATE.json').read_text())
keys=['status','ideal_rows','conditional_floating_rows','source_reference_offset','source_minimum_target_chord_lower','raw_frame_cap','published_shift_allowance','source_error_is_Frobenius_by_explicit_PR233_model_bound_not_by_sigma210_alone','no_narrower_PASS_from_this_coarse_zero_floor','new_records_fits_or_phase_output_evaluations','scope','external_review','physical_promotion']
checks={k:old[k]==new[k] for k in keys}
assert all(checks.values()),checks
receipt={'status':'PASS_EXACT_ALL_ENDPOINT_AND_MATH_ROW_EQUALITY','keys':checks,'additive_tolerance':0,'numeric_recomputation_performed':False,'independent_scalar_sha256':sha(P/'BOUNDS.json'),'portable_scalar_sha256':sha(R/'frame-apparatus-work-20261019/results/FAMILY_PHASE_CERTIFICATE.json'),'same_team_only':True,'new_fits':0,'physical_promotion':0}
p=P/'PORTABLE_EXACT_COMPARISON.json';assert not p.exists();p.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'status':receipt['status'],'sha256':sha(p),'keys_compared':len(keys)}))
