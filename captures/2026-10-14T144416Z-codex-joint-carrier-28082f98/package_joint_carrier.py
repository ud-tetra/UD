"""Create the reviewable additive release with source snapshots and exact hash inventory."""
from pathlib import Path
import json,hashlib,zipfile
R=Path(__file__).parent;D=R/'dist';P=D/'sources/joint-carrier-v0.1'
paths=['joint_carrier.py','verify_joint_carrier.py','verify_joint_carrier_ui.mjs','rsp1.py','response_contract.py','verify_dependencies_v07.py','build_joint_carrier.py','package_joint_carrier.py','dist/assets/dependencies-v0.7.json','dist/assets/dependencies-v0.7.js','dist/assets/joint-carrier-v0.1.js','dist/assets/style.css','dist/joint-carrier/index.html','dist/dependencies/index.html','dist/sources/UD_DEPENDENCY_VERIFICATION_v0.7.json']
paths+=sorted(str(p.relative_to(R)) for p in P.iterdir() if p.is_file())
g=json.loads((D/'assets/dependencies-v0.7.json').read_text());paths+=['dist'+s['path'] for s in g['sources']];paths=list(dict.fromkeys(paths))
readme='''# UD finite-window joint carrier v0.1 / reading edition0.7

Public inspector: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/joint-carrier/

Supplied finite label permutation/unitary with explicit master clock, retained old-state history, per-tick receipts, outgoing complete payloads and finite independent reset donors. Algebraic inverse and prepared-window proof include arbitrary spectator correlations. No native Hodge, SI timing, physical energy/detection, permanent absorbing state, unlimited donor supply or complete autonomous restart is established. Human review pending; physical promotion0.

Extract and run from this release root:

    python joint_carrier.py
    python verify_joint_carrier.py
    python verify_dependencies_v07.py
    node verify_joint_carrier_ui.mjs
    python dist/sources/joint-carrier-v0.1/joint-carrier-parallel-check.py . JOINT_CARRIER_PARALLEL_REPLAY.json

Python standard library, with Node standard modules for the cross-language inspector check. Exact root receipts and witness reproduce deterministically; the separate parallel replay includes location/time metadata, so compare checked claims, source/checker hashes and counts, rather than expecting the same complete JSON hash. No archived source program is executed for ingestion.

Allocated register capacity is not an entropy/heat or optimal memory claim. Modular receipt labels name a complete per-cell dictionary with0 blank. Both C and H are supplied response choices. Master clock advances across payload resets; after the declared K=L−1 transitions, its next step wraps but supplies no fresh resource. Dirty-reuse and used-donor failure controls are included, without claiming every trivial preparation must fail immediately.

UI files are linked review copies; the full atlas supplies shared app.js and styles/navigation. The UI verifier checks exact calculator traces/parameters/IDs, not rendered browser behavior. Full build script requires the previous preserved Site edition. Source snapshots, prior graphs and scientific ledger keep their existing bytes and types.
'''
manifest={'carrier_version':'0.1','reading_edition':'0.7','physical_promotion':0,'files':[{'path':p,'size_bytes':(R/p).stat().st_size,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()} for p in paths]}
release=D/'releases/UD_FINITE_WINDOW_JOINT_CARRIER_v0.1.zip'
with zipfile.ZipFile(release,'w',zipfile.ZIP_DEFLATED) as z:
    for p in paths:z.write(R/p,p)
    z.writestr('README.md',readme);z.writestr('HASH_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(release) as z:
    assert z.testzip() is None
    for f in manifest['files']:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
print(json.dumps({'status':'PASS','files':len(paths)+2,'size_bytes':release.stat().st_size,'sha256':hashlib.sha256(release.read_bytes()).hexdigest()}))
