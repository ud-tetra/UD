from pathlib import Path
import hashlib,json,zipfile
R=Path(__file__).parent;D=R/'dist';P=D/'sources/native-admission-v0.1'
paths=['native_admission.py','verify_native_admission.py','verify_native_admission_ui.mjs','programmed_clock.py','joint_carrier.py','rsp1.py','response_contract.py','verify_dependencies_v09.py','build_native_admission.py','package_native_admission.py','dist/assets/native-admission-v0.1.js','dist/assets/dependencies-v0.9.js','dist/assets/dependencies-v0.9.json','dist/assets/style.css','dist/native-admission/index.html','dist/dependencies/index.html','dist/sources/UD_DEPENDENCY_VERIFICATION_v0.9.json']
paths+=sorted(str(f.relative_to(R)) for f in P.iterdir() if f.is_file());g=json.loads((D/'assets/dependencies-v0.9.json').read_text());paths+=['dist'+s['path'] for s in g['sources']];paths=list(dict.fromkeys(paths))
readme='''# Native spectral admission v0.1 / atlas reading edition0.9

Public inspector: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/native-admission/

Frozen unitmetric native classes, exact radical residual-floor optimization, complete dimension/multiplicity gates, sharpness with sufficient identical copies and unconstrained eigenbasis encoding, and an explicit complete endpoint alias. A generator residual floor is not an endpoint-error lower bound. Comparison scales select no native metric, rate or physical clock.

Run from release root:

    python native_admission.py
    python verify_native_admission.py
    python verify_dependencies_v09.py
    node verify_native_admission_ui.mjs
    python dist/sources/native-admission-v0.1/native-spectral-parallel-check.py

Exact optimization/field/matrix certificates use Python standard library. Root dense alias diagnostics use numpy/scipy. The independent generated checker uses numpy/scipy/sympy. It reconstructs source simplicial operators from deletion rules, not execution of imported archived programmes. Its receipt writes next to its checker. Exact and numerical diagnostics remain separate. Numerical residual/endpoint values have tolerances and may vary in last digits across platforms.

The default full programme is not densely materialized. The11→75 alias is a compressed prefix-frame block; the complete-Q statement has an explicit proof. Root optimum unions retain disconnected short-clock solutions; the all-zero nonwinning partition retains an unbounded high-centre interval. Source basis, copy/encoding/rate constraints and protected output remain OPEN. No empirical data, source-acquired encoding, calibrated physical identification, independent human review or registry promotion is supplied. Physical promotion0.

UI assets are linked review copies; the public atlas supplies shared app.js. Cross-language calculator/markup checks do not certify rendered browser behavior. Full build script requires the previous retained Site source. HASH_MANIFEST inventories packaged bytes; numerical reruns on another platform should compare scopes/tolerances rather than demand bit-identical floats.
'''
manifest={'version':'0.1','reading_edition':'0.9','physical_promotion':0,'files':[{'path':f,'size_bytes':(R/f).stat().st_size,'sha256':hashlib.sha256((R/f).read_bytes()).hexdigest()} for f in paths]}
release=D/'releases/UD_NATIVE_SPECTRAL_ADMISSION_v0.1.zip'
with zipfile.ZipFile(release,'w',zipfile.ZIP_DEFLATED) as z:
    for f in paths:z.write(R/f,f)
    z.writestr('README.md',readme);z.writestr('HASH_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(release) as z:
    assert z.testzip() is None
    for f in manifest['files']:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
print(json.dumps({'status':'PASS','files':len(paths)+2,'size_bytes':release.stat().st_size,'sha256':hashlib.sha256(release.read_bytes()).hexdigest()}))
