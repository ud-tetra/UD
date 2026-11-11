from pathlib import Path
import json,hashlib,zipfile
p=Path(__file__).resolve().parent;root=p.parent;files=[z for z in sorted(p.rglob('*')) if z.is_file() and '__pycache__' not in z.parts and z.name not in ['PACKAGE_RECEIPT.json','ZIP_MANIFEST.json','CAPTURE_ID.txt']];files += [root/fn for fn in json.loads((p/'FREEZE.json').read_text())['inputs']];files += [root/'graphite-safe-full/PACKAGE_RECEIPT.json'];files += [root/'graphite-safe-full/common.py',root/'graphite-branch-aware/geometry.py'];files=sorted(set(files));m={'files':[{'path':str(z.relative_to(root)),'size_bytes':z.stat().st_size,'sha256':hashlib.sha256(z.read_bytes()).hexdigest()} for z in files]};(p/'ZIP_MANIFEST.json').write_text(json.dumps(m,indent=2)+'\n');z=root/'UD_GRAPHITE_RELEASED_SLIDING_STATIONARITY_v0.1.zip'
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as a:
 for x in files+[p/'ZIP_MANIFEST.json']:a.write(x,x.relative_to(root))
with zipfile.ZipFile(z) as a:
 assert a.testzip() is None
 for x in m['files']:assert hashlib.sha256(a.read(x['path'])).hexdigest()==x['sha256']
r={'filename':z.name,'size_bytes':z.stat().st_size,'sha256':hashlib.sha256(z.read_bytes()).hexdigest(),'archive_integrity':'PASS','files':len(files)+1,'physical_promotion':0};(p/'PACKAGE_RECEIPT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
