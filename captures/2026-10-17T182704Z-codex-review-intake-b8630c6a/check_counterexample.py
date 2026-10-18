#!/usr/bin/env python3
"""Threshold count is not algebraic rank: exact rank-perturbation consequence."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
P=Path(__file__).resolve().parent;base=P/'evidence/record_only';camp=P/'evidence/noise_campaign'
c=json.loads((base/'CERTIFICATE.json').read_text());control=json.loads((base/'CONTROL_CERTIFICATES.json').read_text())['controls'][0];fresh=json.loads((camp/'SINGLE_VECTOR_CERTIFICATE.json').read_text())
r=c['target_count'];M=4096;tau=F(*c['projection_tail_frobenius_upper']);u=F(1,2**20);a=u/M;lower=a-tau
assert control['numeric_signature_certified'] and fresh['status']=='CERTIFIED_NUMERIC_RECORD_SIGNATURE'
assert control['modified_record_sha256']==fresh['input_sha256']['record']
assert lower>0 and M-r>r and fresh['target_count']==r==1893
report={'status':'DERIVED_CONSTRUCTOR_COUNTEREXAMPLE_TO_RANK_EQUALS_THRESHOLD_COUNT','physical_promotion':0,'independent_review':'pending','record_sha256':fresh['input_sha256']['record'],'retained_count_above_threshold':r,'algebraic_rank_at_least':M-r,'sigma_2203_lower':[lower.numerator,lower.denominator],'impulse_amplitude':[u.numerator,u.denominator],'impulse_hankel_rank':M,'impulse_nonzero_singular_value':[a.numerator,a.denominator],'baseline_rank_r_approximation_error_upper':[tau.numerator,tau.denominator],'argument':'The central impulse has M singular values u/M. Adding the rank-r approximant can remove at most r such directions. The baseline approximation error shifts each singular value by at most tau. Thus sigma_(M-r)>=u/M-tau>0, while the retained count above the fixed threshold is certified asr.','scope':'Does not assert that the baseline exact rank was1893, or that algebraic rank changed between the two encoded records.'}
(P/'RANK_COUNTEREXAMPLE.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
