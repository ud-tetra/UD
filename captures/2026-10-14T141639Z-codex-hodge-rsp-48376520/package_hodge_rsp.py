from pathlib import Path
import hashlib,json,zipfile
R=Path(__file__).parent;D=R/'dist';P=D/'sources/hodge-rsp-v0.1'
paths=['hodge_rsp.py','verify_hodge_rsp.py','rsp1.py','response_contract.py','verify_dependencies_v06.py','build_hodge_rsp.py','package_hodge_rsp.py','dist/assets/dependencies-v0.6.json','dist/assets/dependencies-v0.6.js','dist/assets/hodge-rsp-v0.1.js','dist/assets/style.css','dist/dependencies/index.html','dist/realization/index.html','dist/sources/UD_DEPENDENCY_VERIFICATION_v0.6.json']
paths+=sorted(str(p.relative_to(R)) for p in P.iterdir() if p.is_file())
g=json.loads((D/'assets/dependencies-v0.6.json').read_text());paths+=['dist'+s['path'] for s in g['sources']];paths=list(dict.fromkeys(paths))
readme='''# UD Hodge-to-RSP realization audit v0.1 / edition0.6

Public contract inspector: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/realization/

Exact conditional factor no-go proofs, explicit domain/decoder assumptions, source-typing limits and an exact K4 finite-window/wrap witness. The RSP recurrence is preserved. A finite trace encoding is not a global native factor or a source-selected predictor. Independent human review and broader source realization remain open. Physical promotion: 0.

Extract and run from the archive root:

    python hodge_rsp.py
    python verify_hodge_rsp.py
    python verify_dependencies_v06.py
    python dist/sources/hodge-rsp-v0.1/hodge-rsp-parallel-check.py . HODGE_RSP_PARALLEL_REPLAY.json

Python standard library only. Fraction arithmetic verifies the full15-chain K4 witness, boundary composition, skewness, A² and U⁴. Parallel checks enumerate finite factor candidates and preserve unbounded/discontinuous scope exceptions. These are constructor-team AI checks and separate AI reasoning/scope review, not a physical experiment or registry promotion. A new replay writes path/time metadata; compare source hashes and claims rather than expecting identical execution metadata.

UI files are review copies linked to the complete public atlas. Build scripts require the full Site checkout at preserved edition0.5. Prior graph/release bytes, scientific ledger and source records remain separate.
'''
manifest={'audit_version':'0.1','reading_edition':'0.6','physical_promotion':0,'files':[{'path':p,'size_bytes':(R/p).stat().st_size,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()} for p in paths]}
release=D/'releases/UD_HODGE_RSP_REALIZATION_v0.1.zip'
with zipfile.ZipFile(release,'w',zipfile.ZIP_DEFLATED) as z:
 for p in paths:z.write(R/p,p)
 z.writestr('README.md',readme);z.writestr('HASH_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(release) as z:
 assert z.testzip() is None
 for f in manifest['files']:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
print(json.dumps({'status':'PASS','files':len(paths)+2,'size_bytes':release.stat().st_size,'sha256':hashlib.sha256(release.read_bytes()).hexdigest()}))
