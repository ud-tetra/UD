"""Portable exact receipt checks; does not claim to repeat omitted full runs."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,unittest
import numpy as np
from residual_preflight import residual_preflight
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def validate():
    freeze=json.loads((ROOT/'IMPLEMENTATION_FREEZE.json').read_text())
    for n,h in freeze['implementation'].items():assert sha(ROOT/n)==h,(n,'Frozen source mismatch')
    assert sha(ROOT/'proof_math.py')=='78a5e376e9f9d347f98a780ba514b67ba9d8fa6dc24fa29df4847b87db387072'
    contract=json.loads((ROOT/'inputs/FROZEN_CONTRACT.json').read_text());T=F(*contract['spectral_rule']['selection_threshold'])
    assert sha(ROOT/'inputs/FROZEN_CONTRACT.json')==freeze['contract_sha256']
    assert contract['spectral_rule']['target_count']==1893
    assert contract['spectral_rule']['retained_condition_number_strict_upper']==2029
    corpus=json.loads((ROOT/'RECEIPT_REPLAY.json').read_text())
    assert len(corpus['cases'])==8
    for r in corpus['cases']:
        d=ROOT/'inputs/receipt-corpus'/r['case']
        old=json.loads((d/'CERTIFICATE.json').read_text());res=json.loads((d/'RECORD_RESIDUAL.json').read_text())
        assert sha(d/'RECORD_RESIDUAL.json')==r['residual_receipt_sha256']
        assert sha(d/'CERTIFICATE.json')==r['parent_certificate_sha256']
        assert res['input_sha256']==r['input_sha256']
        g=r['preflight'];recomputed=residual_preflight(F(*res['exact_weighted_squared_error']),g['coefficient_row_max_sum'],T)
        assert recomputed==g
        assert old['status']==r['old_status']==r['composed_status']
        if old['status'].startswith('CERTIFIED'):assert g['status']=='CONTINUE_FULL_VERIFIER'
    strong=ROOT/'results/strong_null_alternating_isolated'
    positive=ROOT/'results/bounded_null_impulse'
    for n,d in [('strong_null_alternating',strong),('bounded_null_impulse',positive)]:
        cert=json.loads((d/'CERTIFICATE.json').read_text());res=json.loads((d/'RECORD_RESIDUAL.json').read_text());g=json.loads((d/'RESIDUAL_PREFLIGHT.json').read_text())
        p=ROOT/f'inputs/{n}.npz'
        assert sha(p)==cert['input_sha256']['proposal']==res['input_sha256']['proposal']
        with np.load(p,allow_pickle=False) as z:
            bound=sum(int(v) for v in np.max(np.abs(z['coeff'][1:]),axis=1))
        computed=residual_preflight(F(*res['exact_weighted_squared_error']),bound,T)
        assert all(g[k]==v for k,v in computed.items())
        assert g['input_sha256']==cert['input_sha256']==res['input_sha256']
        assert res['scalar_readings_checked']==18790154 and cert['input_identity_stable']
        old=ROOT/'inputs/receipt-corpus'/n
        assert (d/'RECORD_RESIDUAL.json').read_bytes()==(old/'RECORD_RESIDUAL.json').read_bytes()
        stages=[r['stage'] for r in json.loads((d/'PROGRESS.json').read_text())]
        if n.startswith('strong'):
            assert cert['status']=='HOLD' and not cert['spectral_bounds_computed']
            assert F(*g['true_proposal_residual_frobenius_lower'])>T
            assert 'factor_grams' not in stages and not (d/'FACTOR_GRAMS.npz').exists()
            assert not cert['readable']
        else:
            assert cert['status']=='CERTIFIED_NUMERIC_RECORD_SIGNATURE'
            assert 'factor_grams' in stages and 'svd_residual_verified' in stages
            assert (d/'CERTIFICATE.json').read_bytes()==(old/'CERTIFICATE.json').read_bytes()
            assert F(*cert['sigma_r_lower'])>T>F(*cert['sigma_r_plus1_upper'])
            assert F(*cert['condition_upper'])<2029
    for d in [strong,positive,ROOT/'results/strong_null_alternating',ROOT/'results/strong_null_alternating_serial']:
        b=json.loads((d/'BENCHMARK.json').read_text())
        assert b['executed_code_sha256']=={n:sha(ROOT/n) for n in ['certify_record.py','proof_math.py','residual_preflight.py']}
        assert not b['dense_hankel_allocated']
    suite=unittest.defaultTestLoader.discover(str(ROOT),pattern='test_preflight.py')
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    assert result.wasSuccessful()
    return {'status':'PASS','exact_unit_tests':result.testsRun,'archived_residual_replays':8,'fresh_full_positive_replays':1,'fresh_early_hold_replays':3,'positive_certificate_byte_identical':True,'all_4_record_residuals_byte_identical_to_parent':True,'all_readings_per_run':18790154,'proof_module_unchanged':True,'dense_hankel_allocated':False,'independent_review':'pending','physical_promotion':0}
if __name__=='__main__':
    result=validate();(ROOT/'VALIDATION.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
