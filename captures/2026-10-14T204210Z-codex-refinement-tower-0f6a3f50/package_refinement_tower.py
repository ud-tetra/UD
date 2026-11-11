"""Hash/package scoped multilevel calibration proof and sparse replay."""
from pathlib import Path
import json,hashlib,zipfile
R=Path(__file__).parent;D=R/'dist';P=D/'sources/refinement-tower-v0.1'
paths=['refinement_tower.py','subdivision_metric.py','verify_refinement_tower_ui.mjs','verify_dependencies_v013.py','check_site_v013.py','build_refinement_tower.py','package_refinement_tower.py','dist/assets/refinement-tower-v0.1.js','dist/assets/dependencies-v0.13.json','dist/assets/dependencies-v0.13.js','dist/assets/app.js','dist/assets/style.css','dist/refinement-tower/index.html','dist/dependencies/index.html','dist/sources/UD_DEPENDENCY_VERIFICATION_v0.13.json']
if (D/'sources/UD_ATLAS_SITE_VALIDATION_v0.13.json').exists():paths.append('dist/sources/UD_ATLAS_SITE_VALIDATION_v0.13.json')
paths+=sorted(str(f.relative_to(R)) for f in P.iterdir() if f.is_file());g=json.loads((D/'assets/dependencies-v0.13.json').read_text());paths+=['dist'+s['path'] for s in g['sources']];paths=list(dict.fromkeys(paths))
manifest={'version':'0.1','reading_edition':'0.13','physical_promotion':0,'files':[{'path':f,'size_bytes':(R/f).stat().st_size,'sha256':hashlib.sha256((R/f).read_bytes()).hexdigest()} for f in paths]}
readme='''# Refinement tower coherence v0.1 / reading edition0.13

Public inspector: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/refinement-tower/

Exact sparse15→149→2745 barycentric tower, sequential/fresh unit detail-calibration mismatch, complete hierarchical decomposition, transported composite complement pairing, associative coarse observable and17 complete positive support effects. The new grouping requirement is additional: prior one-step uniqueness and coarse generator preservation remain intact. No native history/metric/event selection or physical promotion.

Run from release root:

    python refinement_tower.py
    python dist/sources/refinement-tower-v0.1/tower-parallel-check.py
    python verify_dependencies_v013.py
    node verify_refinement_tower_ui.mjs

The root scientific replay uses Python standard library Fraction arithmetic and independently regenerates all step/composite maps and boundaries. The parallel replay uses the retained freshly generated subdivision_metric.py for its first-step basis/maps and independently generates the sparse second step. Its dependency is included next to the checker for portable replay. It verifies2748 exact norm/effect probes and may take longer because it retains sparse projector data. Neither materializes a dense2745-square metric or inverse. Composite projector idempotence is exact from replayed left-inverse identities. Imported archived scientific scripts are not executed.

Source bindings remain prior versioned SG01/MS01, R33/R34 and observable-ordering records, with exact public catalog text snapshots in the graph. Those text hashes do not establish original manuscript/release-byte recovery. The graph includes44 snapshots and36 change scenarios. This is a scoped evidence bundle: full Site check/build scripts require its retained earlier editions. Replays write only local receipts; original release/capture bytes remain unchanged. Browser visual QA unavailable. Constructor-team checks are not independent human/CRL review.

The induced composite detail matrix is ambient-semidefinite and positive on its complement restriction. Regrouping the same retained sequence is not covariance across different refinement histories. All2730 details remain direct-sum chain coordinates, not qubits or tensor donor banks. Pure coarse embeddings do not create detail excitations, events or growth preferences. Local/physical observation, fresh coordinate preparation, clocks, protected outgoing records and reset resources remain separate open obligations. Physical promotion0; no free reset, universal sqrt2 law or indefinite funded growth.

HASH_MANIFEST inventories packaged bytes. Exact later-level count rows follow the flag recurrence; their matrices are not generated or claimed.
'''
release=D/'releases/UD_REFINEMENT_TOWER_COHERENCE_v0.1.zip'
with zipfile.ZipFile(release,'w',zipfile.ZIP_DEFLATED) as z:
    for f in paths:z.write(R/f,f)
    z.writestr('README.md',readme);z.writestr('HASH_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(release) as z:
    assert z.testzip() is None
    for f in manifest['files']:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
print(json.dumps({'status':'PASS','files':len(paths)+2,'size_bytes':release.stat().st_size,'sha256':hashlib.sha256(release.read_bytes()).hexdigest()}))
