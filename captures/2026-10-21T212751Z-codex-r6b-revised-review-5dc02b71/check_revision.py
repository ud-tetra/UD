#!/usr/bin/env python3
"""Constructor intake checks; no submitted code is executed."""
from pathlib import Path
from fractions import Fraction as F
import json,subprocess,hashlib,re
C=Path(__file__).parent;R=C.parents[1]
def main():
    b=(C/'SUBMITTED_AMENDMENT.txt').read_bytes();raw=(C/'SUBMITTED_RECEIPT.json').read_bytes()
    assert raw==re.search(rb'```json\r?\n(.*?)\r?\n```',b,re.S).group(1)
    receipt=json.loads(raw);attr=json.loads((C/'ATTRIBUTION.json').read_text())
    assert attr['reviewer_name']=='Devin Ramos' and attr['non_constructor_status']=='user-attested'
    assert set(receipt['remediation_ledger'])=={'R0'+str(i) for i in range(1,9)}
    assert receipt['disposition']['physical_promotion']==0 and not receipt['disposition']['registry_promotion_requested']
    assert re.fullmatch('[0-9a-f]{64}',receipt['execution_environment']['script_sha256'])
    n=[1,3,12];x=list(map(F,[0,1,2]));N=sum(n);mean=sum(ni*xi for ni,xi in zip(n,x))/N
    pair=sum(n[i]*n[j]*(x[i]-x[j])**2 for i in range(3) for j in range(i+1,3))
    var=sum(ni*(xi-mean)**2 for ni,xi in zip(n,x))
    assert (mean,pair,var)==(F(27,16),87,F(87,16)) and pair==N*var
    commit='98d084191b2c6471b1e73aae2985abefc8bc80ff'
    path='captures/2026-10-21T204744Z-codex-r6b-error-budget-bc7134a9/AUDIT.json'
    ab=subprocess.check_output(['git','show',commit+':'+path],cwd=R);audit=json.loads(ab)
    controls=[]
    for row in audit['module_certificates']:
        beta=F(row['stored_second_eigenvalue_lower']);mu=F(row['trial_Rayleigh']['lower'])
        s2=F(row['trial_residual_variance']['upper'])
        # Certified trial variance, not the generic returned-eigenpair scaled tolerance, supplies precision.
        assert s2/(beta-mu)<F('1e-23')
        assert F('5e-12')**2/(beta-mu)>F('1e-23')
        controls.append({'module':row['module_first_digit'],'certified_trial_variance_suffices':True,
                         'acceptance_threshold_alone_insufficient_for_1e_minus23_width':True})
    return {'status':'PASS_CONSTRUCTOR_REVISION_INTAKE','reviewer_attribution':'Devin Ramos, user-attested non-constructor; AI-assisted',
            'physical_promotion':0,'submitted_receipt_id':receipt['receipt_id'],
            'submitted_receipt_sha256':hashlib.sha256(raw).hexdigest(),'submitted_amendment_sha256':hashlib.sha256(b).hexdigest(),
            'PR358_AUDIT_sha256':hashlib.sha256(ab).hexdigest(),'remediation_statements_present':8,
            'weighted_variance_control':{'mean':str(mean),'pair_sum':str(pair),'variance_sum':str(var)},
            'precision_controls':controls,'independent_audit_execution':'REPORTED_NOT_VERIFIED; script and full outputs absent',
            'authentication_claim':'not inferred from a role, schema URI or hash string',
            'promotion':'NONE; no registry promotion requested'}
if __name__=='__main__':
    out=main();(C/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
