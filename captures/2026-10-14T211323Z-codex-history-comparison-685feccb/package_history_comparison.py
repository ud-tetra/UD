"""Package immutable edition0.14 proof and exact replay payload."""
from pathlib import Path
import json,hashlib,zipfile
R=Path(__file__).parent;D=R/'dist';P=D/'sources/history-comparison-v0.1'
paths=['history_comparison.py','subdivision_metric.py','verify_dependencies_v014.py','check_site_v014.py','build_history_comparison.py','package_history_comparison.py','dist/assets/dependencies-v0.14.json','dist/assets/dependencies-v0.14.js','dist/assets/app.js','dist/assets/style.css','dist/history-comparison/index.html','dist/dependencies/index.html','dist/sources/UD_DEPENDENCY_VERIFICATION_v0.14.json']
paths+=sorted(str(f.relative_to(R)) for f in P.iterdir() if f.is_file())
if (D/'sources/UD_ATLAS_SITE_VALIDATION_v0.14.json').exists():paths.append('dist/sources/UD_ATLAS_SITE_VALIDATION_v0.14.json')
g=json.loads((D/'assets/dependencies-v0.14.json').read_text());paths+=['dist'+s['path'] for s in g['sources']];paths=list(dict.fromkeys(paths))
manifest={'version':'0.1','reading_edition':'0.14','physical_promotion':0,'files':[{'path':f,'size_bytes':(R/f).stat().st_size,'sha256':hashlib.sha256((R/f).read_bytes()).hexdigest()} for f in paths]}
readme='''# Refinement histories and detail-source gate v0.1

Public page: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/history-comparison/

Development lane, no registry entry; physical promotion0. Exact conditional star29/bary149 history comparison, non-equivariant spectral capacity, S4-equivariant obstruction, lossy coarse map,163-direction retained-record transfer and universal inherited-skew no-seed theorem. Native selection OPEN; independent human review PENDING.

Replay from release root: python history_comparison.py
Requires Python, SymPy and NumPy. It constructs star maps and exact projectors and uses included authored subdivision_metric.py for barycentric maps. Exact DomainMatrix rank and S4-projector intersections establish conclusions; numerical samples are diagnostic only. No archival executable is imported. A replay writes its own local receipt; the bundled original receipt remains evidence of the constructor run.

Graph replay: python verify_dependencies_v014.py
The Site static checker requires the complete retained Site editions, not just this scoped release. Browser visual QA was unavailable; no rendered QA is claimed. Source snapshot hashes bind public source text, not inaccessible original archive bytes. AI parallel checks are constructor-team checks, not independent human review. Older graphs/releases remain immutable.

All spectra use conditional H=R.T R+Q.T Q, fixed internal rates and full graded carriers. The163-direction transfer preserves retained records but does not assert complete native-generator equivalence or a physical resource minimum. The historical C4 launch stock is not identified with metric detail norm, forcing or physical energy. No native excitation, physical correspondence or universal sqrt2 saturation law is acquired.

HASH_MANIFEST.json inventories exact packaged bytes.
'''
release=D/'releases/UD_REFINEMENT_HISTORY_AND_DETAIL_SOURCE_v0.1.zip'
with zipfile.ZipFile(release,'w',zipfile.ZIP_DEFLATED) as z:
    for f in paths:z.write(R/f,f)
    z.writestr('README.md',readme);z.writestr('HASH_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(release) as z:
    assert z.testzip() is None
    for f in manifest['files']:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
print(json.dumps({'status':'PASS','files':len(paths)+2,'size_bytes':release.stat().st_size,'sha256':hashlib.sha256(release.read_bytes()).hexdigest()}))
