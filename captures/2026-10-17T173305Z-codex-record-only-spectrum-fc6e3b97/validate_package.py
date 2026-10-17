#!/usr/bin/env python3
"""Validate fingerprints and rational acceptance arithmetic; replay performs full computation."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
P=Path(__file__).resolve().parent
r=json.loads((P/'RESULT.json').read_text());c=json.loads((P/'certified/CERTIFICATE.json').read_text());b=json.loads((P/'certified/BENCHMARK.json').read_text());p=json.loads((P/'PROVENANCE.json').read_text());q=json.loads((P/'codec/CODEC_MANIFEST.json').read_text());ctrl=json.loads((P/'controls/CONTROL_CERTIFICATES.json').read_text())
assert c['status']=='CERTIFIED_NUMERIC_RECORD_SIGNATURE' and r['status']==c['status']
lo,hi,tail=[F(*c[k]) for k in ['sigma_r_lower','sigma_1_upper','projection_tail_frobenius_upper']];T=F(*c['selection_threshold']);assert lo>T>tail and hi/lo<F('706.570')<2029
assert tail<F('1.132e-12')
for name,h in b['executed_code_sha256'].items():assert hashlib.sha256((P/name).read_bytes()).hexdigest()==h
for name,h in p['source_code_sha256'].items():assert hashlib.sha256((P/name).read_bytes()).hexdigest()==h
assert hashlib.sha256((P/'inputs/FROZEN_CONTRACT.json').read_bytes()).hexdigest()==c['input_sha256']['contract']
assert hashlib.sha256((P/'output/PROPOSAL.npz').read_bytes()).hexdigest()==c['input_sha256']['proposal']
assert q['raw_sha256']==c['input_sha256']['record']
assert hashlib.sha256((P/'codec/LOSSLESS_RESIDUAL.npz').read_bytes()).hexdigest()==q['residual_sha256']
assert hashlib.sha256((P/'codec/CODEC_DICTIONARY.npz').read_bytes()).hexdigest()==q['dictionary_sha256']
assert ctrl['status']=='PASS' and ctrl['controls'][0]['numeric_signature_certified'] and ctrl['controls'][1]['actual_signature_breach_proved']
assert ctrl['controls'][1]['guaranteed_count_above_threshold_at_least']>1893
assert json.loads((P/'TEST_RESULTS.json').read_text())['status']=='PASS'
assert not list(P.rglob('OPERATORS.npz')) and not list(P.rglob('REFINED_ROOT_INTERVALS.json'))
print(json.dumps({'status':'PASS','scope':'Hashes, gates and evidence consistency. Independent full computational replay remains pending.'},indent=2))
