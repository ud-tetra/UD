"""Static ingestion only. No imported code, HTML scripts or archive builders run."""
from pathlib import Path
from collections import Counter,defaultdict
from xml.etree import ElementTree as ET
import json,hashlib,subprocess,zipfile,io,re
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).parent
def digest(b):return hashlib.sha256(b).hexdigest()
def write(n,v):(OUT/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
inventory=[];members=[];texts={};workbooks=[];expanded=0;hashchecks=[]
texttypes={'.md','.txt','.json','.py','.tex','.csv','.html','.svg','.jsx'}
def pdf(b):return subprocess.run(['pdftotext','-layout','-','-'],input=b,capture_output=True,check=True).stdout.decode('utf8',errors='replace')
def walk(b,label,depth=1):
 global expanded
 assert depth<=16
 with zipfile.ZipFile(io.BytesIO(b)) as z:
  for i in z.infolist():
   if i.is_dir():continue
   assert i.file_size<50000000
   v=z.read(i);expanded+=len(v);assert expanded<300000000
   key=label+'!'+i.filename;ext=Path(i.filename).suffix.lower()
   members.append({'container_member':key,'size_bytes':len(v),'sha256':digest(v),'depth':depth,'extension':ext})
   if i.filename.endswith('SHA256SUMS'):
    for line in v.decode().splitlines():
     m=re.match(r'^([0-9a-f]{64})\s+\*?(.+)$',line)
     if m:
      expected,fn=m.groups();full=str(Path(i.filename).parent/fn)
      ok=full in z.namelist() and digest(z.read(full))==expected
      hashchecks.append({'archive':label,'member':full,'status':'PASS' if ok else 'FAIL'})
   if ext=='.zip':walk(v,key,depth+1)
   elif ext in texttypes:texts[key]=v.decode('utf8',errors='replace')
   elif ext=='.pdf':texts[key]=pdf(v)
for p in sorted((ROOT/'docs').rglob('*')):
 if not p.is_file():continue
 b=p.read_bytes();name=str(p.relative_to(ROOT));ext=p.suffix.lower()
 d={'path':name,'size_bytes':len(b),'sha256':digest(b),'extension':ext}
 if ext=='.pdf':texts[name]=pdf(b);d['method']='pdftotext -layout; no OCR'
 elif ext=='.zip':walk(b,name);d['method']='recursive ZIP member bytes; no execution'
 elif ext=='.xlsx':
  with zipfile.ZipFile(io.BytesIO(b)) as z:
   w=ET.fromstring(z.read('xl/workbook.xml'));ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
   workbooks.append({'path':name,'sheets':[x.attrib.get('name') for x in w.findall('m:sheets/m:sheet',ns)],'scope':'OOXML inventory only; no cell/formula scientific audit'})
  d['method']='OOXML sheet inventory only'
 elif ext in texttypes:texts[name]=b.decode('utf8',errors='replace');d['method']='UTF8 static source'
 else:d['method']='hash only'
 d['text_chars']=len(texts.get(name,''));inventory.append(d)
patterns={'THM534':r'THM[\s-]*534','T2_6':r'\bT2\.6\b','pentagonal':r'pentagon','pentachoron':r'pentachor','hop_probability':r'hop.{0,30}probab','phase_injection':r'phase.{0,30}injection|injection.{0,30}phase|Π_phase','per_probe':r'per_probe_sigma2'}
hits={k:[] for k in patterns}
for name,s in texts.items():
 for line,v in enumerate(s.splitlines(),1):
  for k,pattern in patterns.items():
   if re.search(pattern,v,re.I):hits[k].append({'source':name,'line':line,'excerpt':v[:650]})
dups=defaultdict(list)
for x in inventory:dups[x['sha256']].append(x['path'])
write('SOURCE_INVENTORY.json',inventory);write('RECURSIVE_ARCHIVE_MEMBERS.json',members);write('SEARCH_HITS.json',hits)
write('ARCHIVE_HASH_CHECKS.json',{'checks':len(hashchecks),'passed':sum(x['status']=='PASS' for x in hashchecks),'failed':[x for x in hashchecks if x['status']!='PASS'],'scope':'SHA256SUMS entries inside recursively recovered ZIPs; payload integrity only; no mathematical proof or execution'})
write('INGEST_RECEIPT.json',{'source_commit':'82362e78ce0ca13185ba5c5ad5793c00fbf46ece','files':len(inventory),'bytes':sum(x['size_bytes'] for x in inventory),'types':dict(Counter(x['extension'] for x in inventory)),'recursive_zip_members':len(members),'recursive_zip_expanded_bytes':expanded,'max_zip_depth':max(x['depth'] for x in members),'zip_unique_payload_hashes':len({x['sha256'] for x in members}),'byte_duplicate_top_level_groups':[v for v in dups.values() if len(v)>1],'workbooks':workbooks,'search_hit_counts':{k:len(v) for k,v in hits.items()},'verification_scope':'all top-level hashes; static text/PDF extraction and recursive ZIP indexing; targeted scientific audit, not proof validation of every document; PDF image-only material and spreadsheet cells not semantically audited','archived_code_executed':False,'physical_promotion':0})
print(json.dumps({'files':len(inventory),'zip_members':len(members),'search_hits':{k:len(v) for k,v in hits.items()}}))
