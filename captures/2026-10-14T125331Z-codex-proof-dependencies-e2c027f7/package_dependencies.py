"""Package the scoped graph, public UI and reproducible constructor checks."""
from pathlib import Path
import zipfile,json,hashlib
R=Path(__file__).parent;D=R/'dist'
paths=['build_dependencies.py','verify_dependencies.py','package_dependencies.py',
 'dist/assets/dependencies-v0.3.json','dist/assets/dependencies-v0.3.js',
 'dist/dependencies/index.html','dist/assets/style.css',
 'dist/sources/UD_SCOPED_PROOF_DEPENDENCIES_v0.3.md','dist/sources/UD_DEPENDENCY_VERIFICATION_v0.3.json']
paths+=sorted(str(p.relative_to(R)) for p in (D/'sources/dependency-snapshots-v0.3').glob('*.txt'))
readme='''# UD scoped dependencies v0.3

Public explorer: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/dependencies/

Extract this archive and run `python verify_dependencies.py` to replay the constructor checks using only the Python standard library. Node can syntax-check the supplied JavaScript. UI files are review copies with links to the complete public atlas; this archive is not a standalone copy of the entire atlas.

The build script requires the full Site source checkout at its preserved reading edition 0.2 baseline. Source-text snapshots are extracted atlas content; original portal package byte recovery is not claimed. All declared source limitations are retained in the graph and report.

Graph completeness applies only to its declared finite targets. The full research proof DAG and independent human review remain open. Hypothetical change drills do not alter scientific registry statuses. Physical promotion: 0.
'''
manifest={'edition':'0.3','physical_promotion':0,'files':[{'path':p,'size_bytes':(R/p).stat().st_size,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()} for p in paths]}
out=D/'releases/UD_SCOPED_DEPENDENCIES_v0.3.zip'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for p in paths:z.write(R/p,p)
 z.writestr('README.md',readme);z.writestr('HASH_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(out) as z:
 assert z.testzip() is None
 for f in manifest['files']:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
print(json.dumps({'release':str(out),'files':len(paths)+2,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'status':'PASS'}))
