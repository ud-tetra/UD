from pathlib import Path
import json,hashlib,zipfile
R=Path(__file__).parent;D=R/'dist';P=D/'sources/rsp1-v0.1'
paths=['rsp1.py','response_contract.py','verify_rsp1.py','verify_dependencies_v05.py','build_rsp1.py','package_rsp1.py','dist/assets/dependencies-v0.5.json','dist/assets/dependencies-v0.5.js','dist/assets/rsp1-v0.1.js','dist/assets/style.css','dist/dependencies/index.html','dist/source-programme/index.html','dist/sources/UD_DEPENDENCY_VERIFICATION_v0.5.json']
paths+=sorted(str(p.relative_to(R)) for p in P.iterdir() if p.is_file())
# Include precisely the prior source snapshots needed by the additive dependency register.
g=json.loads((D/'assets/dependencies-v0.5.json').read_text())
paths+=['dist'+s['path'] for s in g['sources']];paths=list(dict.fromkeys(paths))
readme='''# UD RSP-1 source programme v0.1 / reading edition 0.5

Public workbench: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/source-programme/

This is a complete prepared-register candidate source-interface recurrence, not a native physical law. Both close and hold branches are preserved. Counters, fixed integrity/frame, feedback and finite bank renewal are supplied choices. Independent human review and HD-to-source realization remain open. Physical promotion: 0.

Extract and run from the archive root:

    python verify_rsp1.py
    python verify_dependencies_v05.py
    python dist/sources/rsp1-v0.1/rsp1-parallel-check.py . RSP1_PARALLEL_REPLAY.json
    python rsp1.py dist/sources/rsp1-v0.1/RSP1_EXAMPLE_PRE_STATE_v0.1.json

Only Python's standard library is needed. The root verification binds the captured parallel receipt and AI scope report to the exact implementation. A parallel replay writes a fresh receipt with its execution path; compare claims/hashes/counts rather than treating path metadata as a scientific change. Traces and review are AI constructor/scope checks, not independent empirical data or CRL promotion.

UI files are review copies with links to the complete public atlas; this is not an offline copy of every atlas source. build_rsp1.py requires the full preserved Site source checkout at reading edition 0.4. Original sources and earlier graph/release versions remain separate. A cached prior L is an admitted receipt, not reconstructed from current stock. Model HALT excludes the final unchanged inspection from committed duration and is not a physical no-event verdict.
'''
manifest={'program_version':'0.1','reading_edition':'0.5','physical_promotion':0,'files':[{'path':p,'size_bytes':(R/p).stat().st_size,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()} for p in paths]}
release=D/'releases/UD_RSP1_SOURCE_PROGRAMME_v0.1.zip'
with zipfile.ZipFile(release,'w',zipfile.ZIP_DEFLATED) as z:
 for p in paths:z.write(R/p,p)
 z.writestr('README.md',readme);z.writestr('HASH_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(release) as z:
 assert z.testzip() is None
 for f in manifest['files']:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
print(json.dumps({'status':'PASS','files':len(paths)+2,'size_bytes':release.stat().st_size,'sha256':hashlib.sha256(release.read_bytes()).hexdigest()}))
