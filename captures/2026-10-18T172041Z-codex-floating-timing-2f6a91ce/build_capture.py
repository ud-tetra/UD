from pathlib import Path
import json,hashlib,zipfile,datetime,shutil
P=Path(__file__).resolve().parent;repo=P.parent/'ud-repo';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ID=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H%M%SZ')+'-codex-floating-timing-2f6a91ce';out=repo/'captures'/ID;out.mkdir(parents=True,exist_ok=False)
f=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());arrays=[];archives=[];large=set()
for e in f['cases']:
 n=e['case'];o=P/f'results/{n}'
 if (o/'HOLD.json').exists():continue
 a=out/f'WITNESS_{n}.zip'
 with zipfile.ZipFile(a,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p in [o/'FLOAT_WITNESS.npz',P/f'results/original-{n}/PROPOSAL.npz']:
   large.add(p);z.write(p,p.relative_to(P).as_posix());arrays.append({'path':p.relative_to(P).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p),'archive':a.name})
 assert a.stat().st_size<12000000
 archives.append({'filename':a.name,'size_bytes':a.stat().st_size,'sha256':sha(a)})
(P/'WITNESS_INDEX.json').write_text(json.dumps({'status':'ALL_AVAILABLE_FLOAT_ARRAYS_AND_ORIGINAL_PROPOSALS_RETAINED','physical_promotion':0,'arrays':arrays,'archives':archives,'instructions':'Extract core and every witness ZIP into one folder, then run replay_package.py; raw regeneration is separate'},indent=2))
files=[p for p in P.rglob('*') if p.is_file() and not any(x in p.relative_to(P).parts for x in ['__pycache__','records','codec']) and p not in large and p.name!='PACKAGE_MANIFEST.json']
(P/'PACKAGE_MANIFEST.json').write_text(json.dumps({'artifact':'UD_FLOATING_TIMING_CAMPAIGN_v0.1','physical_promotion':0,'independent_review':'pending','files':[{'path':p.relative_to(P).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)]},indent=2));files.append(P/'PACKAGE_MANIFEST.json')
core=out/'UD_FLOATING_TIMING_CAMPAIGN_v0.1_CORE.zip'
with zipfile.ZipFile(core,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(files):z.write(p,p.relative_to(P).as_posix())
assert core.stat().st_size<12000000
for p in P.iterdir():
 if p.is_file() and p.suffix in ['.py','.md','.json','.txt','.patch']:shutil.copyfile(p,out/p.name)
entries=[{'path':p.relative_to(repo).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p),'status':'Validated timing-source evaluation / actual floating phase certificates, HOLD and replays, as typed in CLAIM_LEDGER.json','provenance':'Frozen timing recipes before generation, all raw hashes frozen before fitting, unchanged PR189 mathematical proof and actual floating proposer, independent review pending'} for p in sorted(out.iterdir())]
(out/'MANIFEST.json').write_text(json.dumps({'capture_id':ID,'physical_promotion':0,'status':'CONSTRUCTOR_PREPARATION_TIMING_FLOAT_VALIDATION','supersedes':[],'extends':['2026-10-18T020014Z-codex-frame-span-7b29c641','2026-10-18T163005Z-codex-preparation-clocks-b74f20d9'],'verification_scope':'Four fresh direct modal timing records; 75,160,616 encoded readings and 45,880 direct Arb spot checks; actual floating output certificates and all HOLDs retained;14 tests; deterministic raw regeneration. No new full-Hankel proof, uniform phase guarantee, SI calibration, independent review or physical promotion.','files':entries},indent=2))
(repo/'events'/f'{ID}.json').write_text(json.dumps({'capture_id':ID,'event':'frozen_preparation_specific_timing_float_validation','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'physical_promotion':0,'summary':'Four frozen direct modal records exercise zero clocks, alternating preparation origins, ramp origins with small clocks and larger clock errors. Original/instrumented floating outputs compared; all certificates and HOLDs retained. 75,160,616 encoded readings, 45,880 direct Arb source spot checks,14 tests and deterministic raw regeneration. Exact waveform generation bound and a posteriori actual output proof remain distinct. No SI, uniform convergence, independent-review, full-Hankel or physical promotion claim.'},indent=2))
print(json.dumps({'capture':str(out),'core_sha256':sha(core),'core_bytes':core.stat().st_size,'total_payload_bytes':sum(p.stat().st_size for p in out.glob('*.zip')),'archives':len(archives)+1,'core_files':len(files)}))
