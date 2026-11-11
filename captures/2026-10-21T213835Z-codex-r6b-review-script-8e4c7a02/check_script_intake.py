#!/usr/bin/env python3
"""Inspect and reproduce the exact submitted review program; report observed defects."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,ast,json,subprocess,tempfile,sys
import numpy as np
C=Path(__file__).parent
CLAIMED='627cfd3b28693b2f8e7574dccc35ac231b0fd4b958c589a234a96cb29807f660'
ACTUAL='507fb13d83438a8462d74adff20f66b823397facf71115a1b31c41b9fb343e81'
PAYLOAD='fa6f6c4fa3dc9d1c13d0a9d0418cef93d1fd6d03cdfa0370055796164767fd3f'

def run(payload):
    p=C/'independent_audit_r6b.py';raw=p.read_bytes();actual=hashlib.sha256(raw).hexdigest()
    assert actual==ACTUAL and actual!=CLAIMED
    tree=ast.parse(raw)
    checks={n.name:sum(isinstance(x,ast.Assert) for x in ast.walk(n)) for n in tree.body if isinstance(n,ast.FunctionDef) and n.name.startswith('check_')}
    assert len(checks)==6 and checks['check_r06_r07_c08_residuals_and_perturbation']==1
    # Reviewed code contains imports, arithmetic/printing and no file/network/process operations.
    # Execute only these preserved bytes in a disposable cwd; never run recovered source programs.
    with tempfile.TemporaryDirectory(prefix='r6b-review-script-reproduction-') as td:
        proc=subprocess.run([sys.executable,str(p.resolve())],cwd=td,capture_output=True,timeout=30)
    (C/'RUN_STDOUT.txt').write_bytes(proc.stdout);(C/'RUN_STDERR.txt').write_bytes(proc.stderr)
    assert proc.returncode==0
    assert b'6.0186e-23 (< 1e-23) -> PASS' in proc.stdout
    assert b'ALL 8 VERIFICATION CHECKS' in proc.stdout
    sample=F('2e-13')**2/F('0.000664605')
    assert sample>F('1e-23')
    assert hashlib.sha256(payload.read_bytes()).hexdigest()==PAYLOAD
    with np.load(payload,allow_pickle=False) as z:
        A=z['full'];assert A.shape==(512,512)
        # Exact row sums of exact binary64 entries, not a floating norm approximation.
        true_inf=max(sum((F.from_float(float(q)) for q in abs(row)),F(0)) for row in A)
    assert true_inf>97 and true_inf<F(98) and true_inf>F('52.20296')
    outcome={'status':'PASS_INTAKE_DEFECT_CONTROLS','review_script_verification_status':'INSUFFICIENT_FOR_FULL_C01_C08_CERTIFICATE',
             'physical_promotion':0,'reviewer':'Devin Ramos; user-attested non-constructor, AI-assisted',
             'script_binding':{'claimed_sha256':CLAIMED,'actual_sha256':actual,'match':False,'bytes':len(raw)},
             'fresh_execution':{'returncode':proc.returncode,'runtime_python_version':list(sys.version_info[:3]),
                                'stdout_sha256':hashlib.sha256(proc.stdout).hexdigest(),'stderr_bytes':len(proc.stderr),
                                'meaning':'constructor reproduction now; not proof of a prior external execution'},
             'assertions_by_check_function':checks,
             'exact_controls':{'sample_Temple_bound':str(sample),'sample_bound_exceeds_1e_minus23':True,
                               'sample_bound_decimal':float(sample),'reported_infinity_norm_sample':'52.20296',
                               'pinned_full_infinity_norm_exact':str(true_inf),'pinned_full_infinity_norm_display':float(true_inf)},
             'payload_sha256':PAYLOAD,
             'coverage_limits':['topology function computes the expected count without constructing edges or components',
                                'spectrum formulas and ranks are stipulated; no independent Laplacian or projectors assembled',
                                'rho trial norm and orthogonality printed but not computed',
                                'no32/6-coordinate embeddings, source eigenvalue intervals or channel weights checked',
                                'no pinned files, commits, payload hashes or eigenpair residuals read by submitted program',
                                'shift-invert uses example values; no serialized probe coverage or ARPACK execution',
                                'sample Temple assertion absent; footer prints all8 passed unconditionally'],
             'scope':'attribution retained; file received and run; binding and full independent-audit coverage remain open'}
    (C/'CHECKS.json').write_text(json.dumps(outcome,indent=2)+'\n')
    return outcome
if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--payload',type=Path,required=True)
    out=run(parser.parse_args().payload)
    print(json.dumps({'status':out['status'],'binding':out['script_binding'],'exact_controls':out['exact_controls']},indent=2))
