"""Inventory and package the versioned three-condition evidence."""
from pathlib import Path
import json,hashlib,zipfile
R=Path(__file__).parent;D=R/'dist';P=D/'sources/subdivision-v0.1'
paths=['subdivision_metric.py','verify_subdivision_ui.mjs','verify_dependencies_v011.py','check_site_v011.py','build_subdivision.py','package_subdivision.py','dist/assets/subdivision-v0.1.js','dist/assets/dependencies-v0.11.json','dist/assets/dependencies-v0.11.js','dist/assets/app.js','dist/assets/style.css','dist/subdivision/index.html','dist/dependencies/index.html','dist/sources/UD_DEPENDENCY_VERIFICATION_v0.11.json']
if (D/'sources/UD_ATLAS_SITE_VALIDATION_v0.11.json').exists():paths.append('dist/sources/UD_ATLAS_SITE_VALIDATION_v0.11.json')
paths+=sorted(str(f.relative_to(R)) for f in P.iterdir() if f.is_file());g=json.loads((D/'assets/dependencies-v0.11.json').read_text());paths+=['dist'+s['path'] for s in g['sources']];paths=list(dict.fromkeys(paths))
manifest={'version':'0.1','reading_edition':'0.11','physical_promotion':0,'files':[{'path':f,'size_bytes':(R/f).stat().st_size,'sha256':hashlib.sha256((R/f).read_bytes()).hexdigest()} for f in paths]}
readme='''# Subdivision three-condition gate v0.1 / public reading edition0.11

Public inspector: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/subdivision/

Recovered ordinary barycentric subdivision with15→149 dimensions and factorial norm factors1,2,6,24. Separate exact norm/boundary/generator gates and negative controls. New conditional affine retraction/complement metric satisfies all three equations on the embedded coarse image, retaining134 direct-sum complement directions. It changes the pairing/operator and does not refute earlier Euclidean no-go results. No universal sqrt2 law, native selection, physical bridge, free reset or indefinite funded refinement. Physical promotion0.

Run from release root:

    python subdivision_metric.py
    python dist/sources/subdivision-v0.1/subdivision-metric-parallel-check.py
    python verify_dependencies_v011.py
    node verify_subdivision_ui.mjs

Scientific replay uses Python standard library and exact Fraction arithmetic. Imported archival scripts are not executed. The weighted-adjoint identity is checked without a149x149 inverse: B′ᵀHS=HSBᵀ together with the exact positive split-norm proof. Both maps, RS=I, Gram factors and negative controls are regenerated. Parallel checker also verifies all24 signed S4 actions. These are constructor-team AI checks; independent human review pending.

Exact source snapshots preserve existing catalog UTF-8 content fields, not original release/PDF bytes; provenance JSON accompanies them. The graph includes source snapshots for citation hashes, explicit premises, acyclicity and30 change scenarios. This is a scoped evidence bundle, not the full Site: check_site_v011.py/build_subdivision.py require its retained previous editions. Replays overwrite only their local receipts; immutable original ZIP/capture bytes remain preserved. Browser visual QA unavailable. HASH_MANIFEST identifies every packaged byte.

The134 extra directions are chain-coordinate dimensions, not qubits or tensor donor banks. The complete direct-sum identification retains arbitrary complement information. Local simplex stocks/readout, complement preparation, event clock, outgoing records and reset acquisition remain separate open obligations. H is generally nondiagonal. The completed metric is an authored compatibility witness, not a source-selected UD law or full unequal-dimensional operator equivalence.
'''
release=D/'releases/UD_SUBDIVISION_THREE_CONDITION_GATE_v0.1.zip'
with zipfile.ZipFile(release,'w',zipfile.ZIP_DEFLATED) as z:
    for f in paths:z.write(R/f,f)
    z.writestr('README.md',readme);z.writestr('HASH_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(release) as z:
    assert z.testzip() is None
    for f in manifest['files']:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
print(json.dumps({'status':'PASS','files':len(paths)+2,'size_bytes':release.stat().st_size,'sha256':hashlib.sha256(release.read_bytes()).hexdigest()}))
