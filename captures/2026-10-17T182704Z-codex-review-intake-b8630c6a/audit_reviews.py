#!/usr/bin/env python3
"""Compare pasted review manifests with immutable archives; never execute supplied artifacts."""
import hashlib,json,re,zipfile,argparse
from pathlib import Path
P=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--noise-archive',required=True);parser.add_argument('--record-archive',required=True);parser.add_argument('--output',required=True);parser.add_argument('--capture-root');args=parser.parse_args();O=Path(args.output).resolve();O.mkdir(exist_ok=False,parents=True)
ARCHIVES={'noise_campaign':Path(args.noise_archive).resolve(),'record_only':Path(args.record_archive).resolve()}
EXPECTED={'noise_campaign':'0c9d1129e9e931a4e2bd0bbaaa7f9f36398fd79b55b25689b9912e02024c2af8','record_only':'11294d1f5ec059b2de54667de1e50cc69d2f103255c14d8b7b9e37e0a1a46af4'}
TARGETS={
 'noise_campaign':{'archive':'noise-campaign/UD_NOISY_RECORD_PROPOSAL_CAMPAIGN_v0.1.zip','capture':'ud-repo/captures/2026-10-17T181003Z-codex-noisy-proposal-6371dfe9','commit':'15fd28a8bdd369d4b9f8c6ea693138b64a651f64'},
 'record_only':{'archive':'observer-work/UD_RECORD_ONLY_SPECTRAL_CERTIFICATE_v0.2.zip','capture':'ud-repo/captures/2026-10-17T173305Z-codex-record-only-spectrum-fc6e3b97','commit':'9672289035365f7af477ff63aaf649fee8ed530d'}}
def sha(data):return hashlib.sha256(data).hexdigest()
reports=[];bindings=[]
for key,target in TARGETS.items():
 archive=ARCHIVES[key];assert sha(archive.read_bytes())==EXPECTED[key],'Unexpected package revision';cap=Path(args.capture_root)/target['capture'].split('captures/',1)[1] if args.capture_root else None;ref=O/'reference'/key;ref.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(archive) as z:
  entries={}
  for name in z.namelist():
   if not name.endswith('/'):
    rel=name.split('/',1)[1];entries[rel]=sha(z.read(name))
  rows=[]
  for number,line in enumerate((P/'submitted'/key/'VERIFICATION_HASH_MANIFEST.sha256').read_text().splitlines(),1):
   h,rel=line.split(None,1);rel=rel.strip();valid=bool(re.fullmatch('[0-9a-fA-F]{64}',h));expected=entries.get(rel)
   capture_matches=None
   if cap is not None and (cap/rel).is_file():capture_matches=sha((cap/rel).read_bytes())==expected;assert capture_matches,'Frozen archive/capture disagreement'
   status='NOT_IN_FROZEN_TARGET' if expected is None else('INVALID_SHA256_FORMAT' if not valid else('MATCH' if h.lower()==expected else'MISMATCH'))
   rows.append({'line':number,'path':rel,'submitted_sha256':h,'submitted_length':len(h),'valid_sha256_format':valid,'actual_archive_sha256':expected,'archive_matches_capture':capture_matches,'status':status})
 (ref/'REFERENCE_PACKAGE_FILES.sha256').write_text(''.join(f'{h}  {name}\n' for name,h in sorted(entries.items())))
 binding={'package':archive.stem,'archive_sha256':sha(archive.read_bytes()),'archive_bytes':archive.stat().st_size,'frozen_capture':target['capture'].split('captures/',1)[1],'local_commit':target['commit'],'reference_inventory_files':len(entries),'reference_manifest_status':'CONSTRUCTOR_COMPUTED_REFERENCE_NOT_INDEPENDENT_REVIEW'}
 (ref/'ARCHIVE_BINDING.json').write_text(json.dumps(binding,indent=2));bindings.append(binding)
 counts={s:sum(r['status']==s for r in rows) for s in ['MATCH','MISMATCH','INVALID_SHA256_FORMAT','NOT_IN_FROZEN_TARGET']}
 reports.append({'target':key,'archive_binding':binding,'entries':rows,'counts':counts})
result={'status':'HOLD_REVIEW_HASH_BINDING_FAILED','scope':'Authenticates neither reviewer identity nor reproduction; compares the provided strings to actual frozen target bytes.','targets':reports}
(O/'HASH_AUDIT.json').write_text(json.dumps(result,indent=2));print(json.dumps({'status':result['status'],'counts':{r['target']:r['counts'] for r in reports}},indent=2))
