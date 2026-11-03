"""Inventory and package this edition's additive scientific evidence."""
from pathlib import Path
import hashlib,json,zipfile
R=Path(__file__).parent;D=R/'dist';P=D/'sources/metric-admission-v0.1'
paths=['metric_admission.py','verify_metric_admission_ui.mjs','verify_dependencies_v010.py','check_site_v010.py','build_metric_admission.py','package_metric_admission.py','dist/assets/metric-admission-v0.1.js','dist/assets/dependencies-v0.10.json','dist/assets/dependencies-v0.10.js','dist/assets/app.js','dist/assets/style.css','dist/metric-admission/index.html','dist/dependencies/index.html','dist/sources/UD_DEPENDENCY_VERIFICATION_v0.10.json']
if (D/'sources/UD_ATLAS_SITE_VALIDATION_v0.10.json').exists():paths.append('dist/sources/UD_ATLAS_SITE_VALIDATION_v0.10.json')
paths+=sorted(str(f.relative_to(R)) for f in P.iterdir() if f.is_file())
g=json.loads((D/'assets/dependencies-v0.10.json').read_text());paths+=['dist'+s['path'] for s in g['sources']];paths=list(dict.fromkeys(paths))
manifest={'version':'0.1','reading_edition':'0.10','physical_promotion':0,'files':[{'path':f,'size_bytes':(R/f).stat().st_size,'sha256':hashlib.sha256((R/f).read_bytes()).hexdigest()} for f in paths]}
readme='''# Source metric admission v0.1 / public reading edition0.10

Public page: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/metric-admission/

Exact source metric-convention crosswalk, invariant S4 three-band family, all-shape Gram default-clock obstruction and degree-weighted glued commensurability obstruction. All no-go statements concern full generators in identical same-parameter uncoupled copies with a common rate. Heterogeneous/coupled carriers, different complexes and explicitly weaker contracts remain outside. Source selection and human review OPEN. Physical promotion0.

Run from release root:

    python metric_admission.py
    python dist/sources/metric-admission-v0.1/s4-metric-parallel-check.py
    python dist/sources/metric-admission-v0.1/gram-five-band-parallel-check.py
    python verify_dependencies_v010.py
    node verify_metric_admission_ui.mjs

All scientific replays above use the Python standard library and exact Fraction arithmetic. Imported archival scripts are not executed. Source snapshots are exact existing catalog content fields, with provenance JSON; they are not original manuscript/PDF bytes. Constructor-team AI source review and exact replays do not constitute independent human/CRL review.

The graph includes retained source snapshots to replay citation hashes, explicit premises, acyclicity, forbidden inference edges and27 change scenarios. The release is a scoped evidence bundle rather than the full website: check_site_v010.py and build_metric_admission.py require the retained Site checkout and its previous editions. The HTML inspector and shared assets are review copies. No browser visual QA was available. HASH_MANIFEST inventories packaged bytes. Replays overwrite only their local receipt files; original release/capture bytes remain immutable.

The three-center radius1 and Gram ratio gap1/144 are different quantities. The latter proves exact inequality but is not an operator residual. Neither gives an endpoint-error lower bound. No target-fitted geometry, adopted native coupling, empirical data or calibrated physical bridge is supplied.
'''
release=D/'releases/UD_SOURCE_METRIC_ADMISSION_v0.1.zip'
with zipfile.ZipFile(release,'w',zipfile.ZIP_DEFLATED) as z:
    for f in paths:z.write(R/f,f)
    z.writestr('README.md',readme);z.writestr('HASH_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(release) as z:
    assert z.testzip() is None
    for f in manifest['files']:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
print(json.dumps({'status':'PASS','files':len(paths)+2,'size_bytes':release.stat().st_size,'sha256':hashlib.sha256(release.read_bytes()).hexdigest()}))
