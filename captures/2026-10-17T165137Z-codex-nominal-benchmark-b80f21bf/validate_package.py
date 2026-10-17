#!/usr/bin/env python3
"""Lightweight evidence/threshold validation; full independent computation is replay.py."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
P=Path(__file__).resolve().parent;n=P/'nominal-work';o=n/'output';r=json.loads((P/'BENCHMARK_RESULT.json').read_text());c=json.loads((n/'sources/FROZEN_CONTRACT.json').read_text());b=json.loads((o/'PIPELINE_BENCHMARK.json').read_text())
assert r['status']=='PASS_CONSTRUCTOR_NOMINAL_ONLY' and b['status']=='PASS'
assert r['frozen_contract_sha256']==hashlib.sha256((n/'sources/FROZEN_CONTRACT.json').read_bytes()).hexdigest()
t=F(*r['selection_threshold']);assert r['selection_threshold']==c['spectral_rule']['selection_threshold']
assert F(*r['sigma_1893_lower_dyadic'])>t>F(*r['tail_upper_dyadic'])
assert F(*r['sigma_1_upper_dyadic'])/F(*r['sigma_1893_lower_dyadic'])<F('706.570')<2029
assert F(*r['tail_upper_dyadic'])<F('9.615e-14')
for script,expected in b['executed_code_sha256'].items():assert hashlib.sha256((n/script).read_bytes()).hexdigest()==expected
for name,h in json.loads((o/'PROGRESS.json').read_text())['inputs']['source_hashes'].items():assert hashlib.sha256((n/'sources'/name).read_bytes()).hexdigest()==h
assert json.loads((o/'UNIFORM_BOUNDS.json').read_text())['status']=='PASS'
assert json.loads((o/'METHOD_TESTS.json').read_text())['status']=='PASS'
assert json.loads((o/'ACTIONS_CERTIFICATE.json').read_text())['exact_checks']['adjoint_identity']
assert r['dense_H_bytes_not_allocated']==253952*151552*8
print(json.dumps({'status':'PASS','scope':'Evidence consistency, code/source fingerprints and exact rational threshold arithmetic; not an independent computational replay.'},indent=2))
