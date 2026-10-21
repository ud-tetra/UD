"""Recover source data and search text from hash-verified historical bundles."""
import gzip,hashlib,json,re,tarfile,tempfile,sys
from pathlib import Path

root=Path(__file__).resolve().parents[2]
assert len(sys.argv)==2, 'usage: recover_archives.py NEW_OUTPUT_DIRECTORY'
capture=Path(sys.argv[1]).resolve()
capture.mkdir(exist_ok=False)
old=root/'captures/2026-10-07T191951Z-codex-ud-bootstrap-5170f8b8'
m=json.loads((old/'MANIFEST.json').read_text()); inventory={x['path']:x for x in m['files']}
sources=json.loads(gzip.decompress((old/'SOURCE_INDEX.json.gz').read_bytes()))['sources']
index={x['archive_path']:x for x in sources}
receipts=[];matches=[];recovered=[]
for bundle in m['bundles']:
 if bundle['origin'] not in ['library','portal']:continue
 with tempfile.TemporaryFile() as stream:
  for part in bundle['parts']:
   p=root/part; h=hashlib.sha256();size=0
   with p.open('rb') as f:
    for block in iter(lambda:f.read(1048576),b''):
     stream.write(block);h.update(block);size+=len(block)
   assert h.hexdigest()==inventory[part]['sha256'] and size==inventory[part]['size_bytes']
  stream.seek(0);scanned=0
  with tarfile.open(fileobj=stream,mode='r|gz') as tar:
   for member in tar:
    if not member.isfile():continue
    name=member.name
    if not name.lower().endswith(('.json','.md','.txt','.html','.tex','.csv')):continue
    if member.size>5000000:continue
    data=tar.extractfile(member).read();scanned+=1
    if name.endswith('UD_COEFFICIENT_PROVENANCE_LEDGER_v0.85_OPTICAL_NOISE_RECONCILIATION.json'):
     source=index[name];assert len(data)==source['size_bytes'] and hashlib.sha256(data).hexdigest()==source['sha256']
     filename=bundle['origin']+'_LEDGER_v0.85.json';(capture/filename).write_bytes(data)
     recovered.append(dict(source,output=filename))
    text=data.decode('utf-8',errors='replace')
    for mt in re.finditer(r'EXIT[-_ ]03|Dimensional Normalization Verification|GLOS-2C\.3',text,re.I):
     matches.append({'archive_path':name,'sha256':hashlib.sha256(data).hexdigest(),'offset':mt.start(),'excerpt':text[max(0,mt.start()-180):mt.end()+450]})
  receipts.append({'bundle':bundle['origin'],'verified_parts':len(bundle['parts']),'text_files_scanned':scanned,'text_extensions':['json','md','txt','html','tex','csv'],'maximum_member_bytes':5000000})
out={'source_capture':old.name,'recovered':recovered,'bundle_checks':receipts,'gate_search_matches':matches,'physical_promotion':0}
(capture/'RECOVERY_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'recovered':len(recovered),'matches':len(matches),'checks':receipts}))
