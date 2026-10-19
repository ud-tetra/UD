"""Read retained DIRECT public policy JSON against immutable member hashes."""
from pathlib import Path
import json,hashlib
R=Path('/workspace/scratch/f3d1c2f040c9');P=Path(__file__).resolve().parent;source=R/'real-intake-work-20261019';d=json.loads((source/'KNOWN_SYNTHETIC_AUTHORITY.json').read_text());dfp=R/'ud-repo/captures/2026-10-19T201524Z-codex-strict-auth-9a2523f6/auth_data/DATA_FREEZE.json';raw=dfp.read_bytes();assert hashlib.sha256(raw).hexdigest()==d['source_direct_DATA_FREEZE_sha256'];df=json.loads(raw);members={e['path']:e for e in df['members']};pub=set();rows=[]
def is_public_hex(s):return isinstance(s,str) and len(s)==64 and set(s)<=set('0123456789abcdef')
for row in d['retained_direct_policy_json_inspected']:
 q=Path(row['retained_direct_json']);m=members[row['published_member']];b=q.read_bytes();assert hashlib.sha256(b).hexdigest()==row['sha256']==m['sha256'] and len(b)==m['size_bytes'];pol=json.loads(b)
 if 'keys' in pol:
  for key in pol['keys'].values():
   if is_public_hex(key['public_key_hex']):pub.add(key['public_key_hex'])
 else:assert row['published_member']=='bundles/bundle_replacement_policy_ignored/POLICY.json' and is_public_hex(pol['untrusted_bundle_key']);pub.add(pol['untrusted_bundle_key'])
 rows.append({'published_member':row['published_member'],'sha256':row['sha256']})
assert sorted(pub)==d['public_key_hex'];policies=sorted(set(m['sha256'] for m in df['members'] if m['path'].startswith('trust/') and m['path'].endswith('.json')));adm=sorted(set(m['sha256'] for m in df['members'] if m['path'].startswith('bundles/') and m['path'].endswith('/ADMISSION.json')));assert policies==d['policy_sha256'] and adm==d['admission_sha256']
x={'status':'PASS_DIRECT_PUBLIC_AUTHORITY_PROVENANCE_CHECK','direct_public_policy_members_read':len(rows),'unique_valid_published_publickeys':len(pub),'unique_trust_policy_hashes':len(policies),'admission_hashes':len(adm),'source_direct_DATA_FREEZE_sha256':hashlib.sha256(raw).hexdigest(),'members':rows,'archive_contents_opened':0,'old52_controls_executed':0,'signatures_or_private_keys_created':0,'actual_real_records':0,'external_review':'PENDING','physical_promotion':0};(P/'PUBLIC_AUTHORITY_PROVENANCE_REVIEW.json').write_text(json.dumps(x,indent=2));print(json.dumps({k:v for k,v in x.items() if k!='members'}))
