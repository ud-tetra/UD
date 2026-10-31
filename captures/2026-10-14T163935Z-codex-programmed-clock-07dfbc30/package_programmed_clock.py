from pathlib import Path
import hashlib,json,zipfile
R=Path(__file__).parent;D=R/'dist';P=D/'sources/programmed-clock-v0.1'
paths=['programmed_clock.py','verify_programmed_clock.py','verify_programmed_clock_ui.mjs','joint_carrier.py','rsp1.py','response_contract.py','verify_dependencies_v08.py','build_programmed_clock.py','package_programmed_clock.py','dist/assets/programmed-clock-v0.1.js','dist/assets/joint-carrier-v0.1.js','dist/assets/dependencies-v0.8.js','dist/assets/dependencies-v0.8.json','dist/assets/style.css','dist/programmed-clock/index.html','dist/dependencies/index.html','dist/sources/UD_DEPENDENCY_VERIFICATION_v0.8.json']
paths+=sorted(str(f.relative_to(R)) for f in P.iterdir() if f.is_file());g=json.loads((D/'assets/dependencies-v0.8.json').read_text());paths+=['dist'+s['path'] for s in g['sources']];paths=list(dict.fromkeys(paths))
readme='''# Programmed weighted-path clock v0.1 / atlas edition0.8

Public inspector: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/programmed-clock/

Supplied constant history Hamiltonian implements the complete finite carrier word. Rational path metrics give an exact engineered graph-Hodge form for even word length. Identity padding resolves the odd full-carrier harmonic mismatch while charging one address. Complete mixed-state terminal distance, projective recurrence, resource/error ledger and source-defined native-isometry residual gate are explicit.

This is an engineered conditional construction, not native tetrahedral source selection, locality, calibrated time/energy, detector behavior or protected permanent export. The full operator cannot embed in the unit-metric single-tetrahedron class for even n>=4. Full research DAG and human review remain open. Development—no registry entry; physical promotion0.

Run from release root:

    python programmed_clock.py
    python verify_programmed_clock.py
    python verify_dependencies_v08.py
    node verify_programmed_clock_ui.mjs
    python dist/sources/programmed-clock-v0.1/continuous-lift-parallel-check.py

Root math replay uses Python standard library; UI check also uses Node standard modules. The independent generated checker requires numpy, scipy and sympy. It reimplements the declared small gate map and does not execute archived source programs. Its result file is written next to its checker. Small floating matrix diagnostics have tolerances; general theorems are not proved by numerical enumeration. Exact and numerical checks are separately labeled.

The default full matrix is not built: its dimension is42,568,187,904. The witness stores exact metrics, encoded states and prefix word, with numerical phase samples. Release UI files are linked review copies; shared app.js and the complete atlas navigation belong to the public Site. Static/cross-language QA is not rendered browser QA. The build script requires the prior full Site source checkout.

Prior science, ledger and graphs remain unchanged. HASH_MANIFEST inventories exact packaged source bytes. The governance CRL2 file is a proposal, and all AI checks are constructor-team work rather than non-constructor human promotion.
'''
manifest={'version':'0.1','reading_edition':'0.8','physical_promotion':0,'files':[{'path':p,'size_bytes':(R/p).stat().st_size,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()} for p in paths]}
release=D/'releases/UD_PROGRAMMED_WEIGHTED_PATH_CLOCK_v0.1.zip'
with zipfile.ZipFile(release,'w',zipfile.ZIP_DEFLATED) as z:
    for p in paths:z.write(R/p,p)
    z.writestr('README.md',readme);z.writestr('HASH_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(release) as z:
    assert z.testzip() is None
    for f in manifest['files']:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
print(json.dumps({'status':'PASS','files':len(paths)+2,'size_bytes':release.stat().st_size,'sha256':hashlib.sha256(release.read_bytes()).hexdigest()}))
