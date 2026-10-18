from pathlib import Path
import json,hashlib,zipfile,datetime,shutil
P=Path(__file__).resolve().parent;repo=P.parent/'ud-repo';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ID=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H%M%SZ')+'-codex-wide-timing-81a7d5c2';out=repo/'captures'/ID;out.mkdir(parents=True,exist_ok=False)
files=[p for p in P.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='PACKAGE_MANIFEST.json']
(P/'PACKAGE_MANIFEST.json').write_text(json.dumps({'artifact':'UD_WIDE_TIMING_SKETCH_DIAGNOSTIC_v0.1','physical_promotion':0,'independent_review':'pending','files':[{'path':p.relative_to(P).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)]},indent=2));files.append(P/'PACKAGE_MANIFEST.json')
core=out/'UD_WIDE_TIMING_SKETCH_DIAGNOSTIC_v0.1.zip'
with zipfile.ZipFile(core,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(files):z.write(p,p.relative_to(P).as_posix())
assert core.stat().st_size<12000000
for p in P.iterdir():
 if p.is_file() and p.suffix in ['.py','.md','.json','.txt']:shutil.copyfile(p,out/p.name)
entries=[{'path':p.relative_to(repo).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p),'status':'Validated exact encoded-sketch count / source-aware comparison-rank theorem; constructor replay only','provenance':'Known PR195 records; frozen nested sketches and two cutoff rules; exact integer Grams and residual-enclosed eigenproposals; independent review pending'} for p in sorted(out.iterdir())]
(out/'MANIFEST.json').write_text(json.dumps({'capture_id':ID,'physical_promotion':0,'status':'WIDE_TIMING_SKETCH_SATURATION_DIAGNOSED','supersedes':[],'extends':['2026-10-18T172041Z-codex-floating-timing-2f6a91ce'],'verification_scope':'Two known records, six case/width Grams and two frozen cutoff rules; exact counts and conditions, raw projection replay, five tests. Waveform-span bound209 versus shift-closure bound417; comparison rank[205,209]. No new phase output, BLAS rounding bridge, full-Hankel, SI or independent-review certificate.','files':entries},indent=2))
(repo/'events'/f'{ID}.json').write_text(json.dumps({'capture_id':ID,'event':'wider_timing_sketch_saturation_diagnostic','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'physical_promotion':0,'summary':'Stress encoded-sketch counts161/202/205 at widths161/257/321 under common cutoff,161/200/204 under scaled cutoff; small-clock control remains105. Exact integer Grams and both raw projection replays pass; five tests. Waveform rank upper209 and one-step closure upper417 distinct; comparison rank in[205,209], encoded sigma210<1.034e-10 at width321. PR195 phase/HOLD scope unchanged; no physical or independent-review promotion.'},indent=2))
print(json.dumps({'capture':str(out),'archive_sha256':sha(core),'archive_bytes':core.stat().st_size,'core_files':len(files)}))
