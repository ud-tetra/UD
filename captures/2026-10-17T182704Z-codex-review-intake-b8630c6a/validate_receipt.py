#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
from fractions import Fraction as F
P=Path(__file__).resolve().parent;r=json.loads((P/'HASH_AUDIT.json').read_text())
assert len(r['targets'])==2
for target in r['targets']:
 assert target['counts']=={'MATCH':0,'MISMATCH':12,'INVALID_SHA256_FORMAT':0,'NOT_IN_FROZEN_TARGET':2}
 assert all(e['archive_matches_capture'] for e in target['entries'] if e['status']=='MISMATCH')
for e in json.loads((P/'EVIDENCE_MAP.json').read_text()):assert hashlib.sha256((P/e['path']).read_bytes()).hexdigest()==e['sha256']
x=json.loads((P/'RANK_COUNTEREXAMPLE.json').read_text());assert x['algebraic_rank_at_least']==2203>x['retained_count_above_threshold']==1893 and F(*x['sigma_2203_lower'])>0
c=json.loads((P/'evidence/noise_campaign/FROZEN_CONTRACT.json').read_text());assert F(*c['history_vector_error_ceiling'])==8*F(*c['sufficient_history_scalar_error_ceiling'])
d=json.loads((P/'REVIEW_DISPOSITION.json').read_text());assert not d['CRL_advancement'] and d['physical_promotion']==0
for name,h in json.loads((P/'PROVENANCE.json').read_text())['source_code_sha256'].items():assert hashlib.sha256((P/name).read_bytes()).hexdigest()==h
print(json.dumps({'status':'PASS_INTAKE_AUDIT_CONSISTENCY','review_gate':'HOLD','independent_review_performed_by_intake_auditor':False},indent=2))
