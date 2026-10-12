"""Read-only literal recovery over provided sources; never derive from target."""
import argparse,hashlib,json,re,subprocess,zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

PATTERNS={'decimal_target':r'238\s*[.,]\s*14','exact_decimal_rewrite':r'11907\s*/\s*50','toroidal':r'toroid','cascade':r'cascade','coarse_graining':r'coarse.grain'}
def text(p):
 if p.suffix.lower()=='.pdf':return subprocess.run(['pdftotext','-layout',str(p),'-'],check=True,capture_output=True,text=True).stdout
 if p.suffix.lower()=='.docx':
  with zipfile.ZipFile(p) as z:return '\n'.join(t.text or '' for t in ET.fromstring(z.read('word/document.xml')).iter() if t.tag.endswith('}t'))
 return p.read_text(errors='replace')
def scan(label,s):
 lines=s.splitlines();return {'source':label,'characters':len(s),'matches':{key:[{'line':i+1,'text':line[:400]} for i,line in enumerate(lines) if re.search(pattern,line,re.I)] for key,pattern in PATTERNS.items()}}
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--sources',type=Path,required=True);args=a.parse_args();files=[];scans=[];members=[]
 for p in sorted(args.sources.iterdir()):
  if not p.is_file():continue
  b=p.read_bytes();files.append({'name':p.name,'size_bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
  if p.suffix.lower()=='.zip':
   with zipfile.ZipFile(p) as z:
    members.extend(z.namelist())
    for n in z.namelist():
     if Path(n).suffix.lower() in {'.md','.txt','.json','.py','.html','.csv'}:scans.append(scan(p.name+'!'+n,z.read(n).decode('utf-8',errors='replace')))
  elif p.suffix.lower() in {'.md','.txt','.pdf','.docx'}:scans.append(scan(p.name,text(p)))
 direct=[{'source':s['source'],'pattern':key,'matches':s['matches'][key]} for s in scans for key in ('decimal_target','exact_decimal_rewrite','toroidal') if s['matches'][key]]
 out={'execution_status':'PASS','recovery_status':'SOURCE_EQUATION_NOT_RECOVERED' if not direct else 'MATCHES_REQUIRE_SOURCE_REVIEW','physical_promotion':0,'files':files,'archive_member_count':len(members),'text_units_scanned':len(scans),'direct_matches':direct,'context_matches':[s for s in scans if any(s['matches'].values())],'limitations':['literal machine-readable text only','archive PDF/image members were not rendered','unavailable Genesis PNG excluded','not a proof of absence outside supplied sources','no source equation backsolved from 238.14']}
 print(json.dumps(out,indent=2))
