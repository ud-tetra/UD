#!/usr/bin/env python3
"""Evidence consistency, exact gates and source fingerprints; full replay is separate."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
P=Path(__file__).resolve().parent;N=P/'noise-campaign';spec=json.loads((N/'CAMPAIGN_FREEZE.json').read_text());freeze=json.loads((N/'IMPLEMENTATION_FREEZE.json').read_text());manifest=json.loads((N/'RECORD_MANIFEST.json').read_text());rows=json.loads((N/'FULL_CERTIFICATE_RESULTS.json').read_text())['rows'];prov=json.loads((P/'PROVENANCE.json').read_text())
assert hashlib.sha256((N/'CAMPAIGN_FREEZE.json').read_bytes()).hexdigest()==prov['campaign_sha256']==manifest['campaign_sha256']
assert hashlib.sha256((N/'inputs/FROZEN_CONTRACT.json').read_bytes()).hexdigest()==spec['frozen_contract_sha256']
for script,h in freeze['code_sha256'].items():assert hashlib.sha256((N/script).read_bytes()).hexdigest()==h
assert len(rows)==4
for row in rows:
 d=N/'results'/('certificate-'+row['case']);c=json.loads((d/'CERTIFICATE.json').read_text());b=json.loads((d/'BENCHMARK.json').read_text());assert c['status']=='CERTIFIED_NUMERIC_RECORD_SIGNATURE' and c['target_count']==1893
 lo,hi,tail=[F(*c[k]) for k in ['sigma_r_lower','sigma_1_upper','projection_tail_frobenius_upper']];T=F(*c['selection_threshold']);assert lo>T>tail and hi/lo<2029 and F(*c['condition_upper'])<F('752.797') and tail<F('7.320e-6')
 for script,h in b['executed_code_sha256'].items():assert h==freeze['code_sha256'][script]
 assert c['input_sha256']['record']==next(r['sha256'] for r in manifest['records'] if r['case']==row['case'])
 assert hashlib.sha256((N/'results'/('new-'+row['case'])/'PROPOSAL.npz').read_bytes()).hexdigest()==c['input_sha256']['proposal']
g=json.loads((N/'DISCOVERY_GAP_CERTIFICATE.json').read_text());eta2=F(*g['sketch_noise_squared_ceiling']);assert F(*g['sigma105_baseline_lower'])**2>9*eta2 and F(*g['sigma106_baseline_upper'])**2<eta2
assert json.loads((N/'TEST_RESULTS.json').read_text())['status']=='PASS'
assert json.loads((N/'REVIEW_TEMPLATE.json').read_text())['status']=='UNASSIGNED_NO_REVIEW'
assert not list(P.rglob('OPERATORS.npz')) and not list(P.rglob('REFINED_ROOT_INTERVALS.json'))
codec=P/'observer-work/codec';m=json.loads((codec/'CODEC_MANIFEST.json').read_text());assert m['raw_sha256']==spec['baseline_raw_sha256'];assert hashlib.sha256((codec/'LOSSLESS_RESIDUAL.npz').read_bytes()).hexdigest()==m['residual_sha256']
print(json.dumps({'status':'PASS','full_record_certificates':4,'scope':'Evidence/code consistency and exact rational gate checks; not independent review or a second full campaign replay.'},indent=2))
