"""Hash and package selection proofs, source snapshots and exact replay."""
from pathlib import Path
import json,hashlib,zipfile
R=Path(__file__).parent;D=R/'dist';P=D/'sources/metric-selection-v0.1'
paths=['metric_selection.py','subdivision_metric.py','verify_metric_selection_ui.mjs','verify_dependencies_v012.py','check_site_v012.py','build_metric_selection.py','package_metric_selection.py','dist/assets/metric-selection-v0.1.js','dist/assets/dependencies-v0.12.json','dist/assets/dependencies-v0.12.js','dist/assets/app.js','dist/assets/style.css','dist/metric-selection/index.html','dist/dependencies/index.html','dist/sources/UD_DEPENDENCY_VERIFICATION_v0.12.json']
if (D/'sources/UD_ATLAS_SITE_VALIDATION_v0.12.json').exists():paths.append('dist/sources/UD_ATLAS_SITE_VALIDATION_v0.12.json')
paths+=sorted(str(f.relative_to(R)) for f in P.iterdir() if f.is_file());g=json.loads((D/'assets/dependencies-v0.12.json').read_text());paths+=['dist'+s['path'] for s in g['sources']];paths=list(dict.fromkeys(paths))
manifest={'version':'0.1','reading_edition':'0.12','physical_promotion':0,'files':[{'path':f,'size_bytes':(R/f).stat().st_size,'sha256':hashlib.sha256((R/f).read_bytes()).hexdigest()} for f in paths]}
readme='''# Metric and observable selection gate v0.1 / reading edition0.12

Public inspector: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/metric-selection/

Exact native fixed-carrier source fidelity, full compatible metric classification, metric/observer nonselection witnesses, any-diagonal-metric generator obstruction and unique conditional selector after explicit extra premises. Current source does not adopt affine exterior readout, residual unit calibration, orthogonal split or complement-blind observation. These premises are candidates; physical promotion0 and human review pending.

Run from release root:

    python metric_selection.py
    python dist/sources/metric-selection-v0.1/selection-parallel-check.py
    python verify_dependencies_v012.py
    node verify_metric_selection_ui.mjs

The scientific checkers use standard-library exact Fraction arithmetic and the retained freshly generated subdivision_metric.py. They do not execute imported archival programmes. The parallel checker has an adjacent copy of that generated dependency for portable replay. The root is not a new independent reconstruction of every subdivision map; those exact source-map checks remain in the previous versioned subdivision release.

Metric witnesses keep allthree compatibility equations and24 signed S4 symmetries. Positive code-calibrated observables still differ on the complement. The16 complete support receipts retain a separate residual outcome: the example fractions are1/8,1/8,3/4. These are mathematical quadratic support fractions, not a physical measurement instrument or derived Born law. Decoded coarse currents do not become local fine-simplex additive stocks.

Catalog text snapshots with exact hashes identify extracted public content, not original manuscript/PDF/release bytes. Graph replay includes43 snapshots, explicit premises, acyclicity and33 change scenarios. This is a scoped evidence bundle, not the full Site: check_site_v012.py/build_metric_selection.py require the retained previous Site editions. Replays write local receipts without changing original ZIP/capture bytes. Browser visual QA unavailable. HASH_MANIFEST inventories packaged bytes.

The134 complement directions remain direct-sum chain coordinates, not qubits or tensor donor banks. Metric/locality, readout, initialization, clocks, outgoing records and reset resources remain open. No source-selected dense metric, universal sqrt2 law or physical/registry promotion follows from conditional uniqueness.
'''
release=D/'releases/UD_METRIC_OBSERVABLE_SELECTION_GATE_v0.1.zip'
with zipfile.ZipFile(release,'w',zipfile.ZIP_DEFLATED) as z:
    for f in paths:z.write(R/f,f)
    z.writestr('README.md',readme);z.writestr('HASH_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(release) as z:
    assert z.testzip() is None
    for f in manifest['files']:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
print(json.dumps({'status':'PASS','files':len(paths)+2,'size_bytes':release.stat().st_size,'sha256':hashlib.sha256(release.read_bytes()).hexdigest()}))
