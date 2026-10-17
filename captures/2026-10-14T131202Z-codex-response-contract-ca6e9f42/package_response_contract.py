from pathlib import Path
import hashlib,json,zipfile
R=Path(__file__).parent;D=R/'dist';P=D/'sources/response-contract-v0.1'
paths=['response_contract.py','verify_response_contract.py','verify_dependencies_v04.py','build_response_contract.py','package_response_contract.py','dist/assets/dependencies-v0.4.json','dist/assets/dependencies-v0.4.js','dist/assets/response-contract-v0.1.js','dist/assets/style.css','dist/dependencies/index.html','dist/source-contract/index.html','dist/sources/UD_DEPENDENCY_VERIFICATION_v0.4.json']
paths+=sorted(str(p.relative_to(R)) for p in P.iterdir() if p.is_file())
paths+=sorted(str(p.relative_to(R)) for p in (D/'sources/dependency-snapshots-v0.3').glob('*.txt'))
readme='''# UD response source contract v0.1 / reading edition 0.4

Public contract: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/source-contract/

Extract and run `python verify_response_contract.py` and `python verify_dependencies_v04.py` from the archive root. Python standard library only. The synthetic fixture is not native data or a blinded experiment. Validate it with `python response_contract.py dist/sources/response-contract-v0.1/synthetic_receipt.json --artifact-root dist/sources/response-contract-v0.1`.

Structural admission never establishes native source truth or scorer eligibility. Passing native-candidate packets still return NATIVE_VALIDATION_PENDING__NO_SCORE. The new finite theorem is development — no registry entry; independent adversarial review pending; physical promotion 0.

UI files are review copies linked to the full public atlas. Build scripts require the complete Site source checkout; this is a focused source/check release, not an offline copy of every atlas source. Prior graph and source bytes remain preserved in earlier releases and the Site Git history.
'''
manifest={'version':'0.1','reading_edition':'0.4','physical_promotion':0,'files':[{'path':p,'size_bytes':(R/p).stat().st_size,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()} for p in paths]}
zipout=D/'releases/UD_RESPONSE_SOURCE_CONTRACT_v0.1.zip'
with zipfile.ZipFile(zipout,'w',zipfile.ZIP_DEFLATED) as z:
 for p in paths:z.write(R/p,p)
 z.writestr('README.md',readme);z.writestr('HASH_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(zipout) as z:
 assert z.testzip() is None
 for f in manifest['files']:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
print(json.dumps({'status':'PASS','files':len(paths)+2,'sha256':hashlib.sha256(zipout.read_bytes()).hexdigest(),'size_bytes':zipout.stat().st_size}))
