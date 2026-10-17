"""Static publication checks. Does not claim rendered browser QA."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re
ROOT=Path(__file__).parent;D=ROOT/'dist';errors=[];links=0
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.main=False;self.title=False
 def handle_starttag(self,t,a):
  a=dict(a)
  if 'id' in a:self.ids.append(a['id'])
  if t=='main':self.main=True
  if t=='title':self.title=True
  if t in ['a','script','link']:
   u=a.get('href') or a.get('src')
   if u:self.links.append(u)
for p in D.rglob('*.html'):
 parser=Parser();parser.feed(p.read_text());assert parser.main and parser.title,p
 assert len(parser.ids)==len(set(parser.ids)),p
 for u in parser.links:
  x=urlsplit(u)
  if x.scheme or x.netloc or not x.path:continue
  links+=1;target=D/unquote(x.path.lstrip('/')) if x.path.startswith('/') else p.parent/unquote(x.path)
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append((str(p.relative_to(D)),u))
sources=json.loads((D/'assets/sources.json').read_text());assert len({x['id'] for x in sources})==len(sources)
for x in sources:
 if x['local']:assert (D/x['local'].lstrip('/')).is_file(),x['id']
for p in json.loads((D/'assets/claims.json').read_text()):assert p['source_id'] in {s['id'] for s in sources}
assert len(json.loads((D/'assets/ledger.json').read_text())['rows'])==448
for name in ['Gap2_FINAL_Finite_Genesis.png','Notes-Backup-17-04-2026-07-13.txt','QT1.txt']:
 assert not any(p.name==name or p.name.endswith(name) for p in D.rglob('*') if p.is_file())
assert not errors,errors
receipt={'status':'PASS','html_pages':len(list(D.rglob('*.html'))),'local_links_checked':links,'source_entries':len(sources),'source_ids_unique':True,'claim_source_ids_valid':True,'ledger_rows':448,'javascript_check':'app.js, dependencies-v0.10.js, response-contract-v0.1.js, rsp1-v0.1.js, hodge-rsp-v0.1.js, joint-carrier-v0.1.js, programmed-clock-v0.1.js and native-admission-v0.1.js and metric-admission-v0.1.js syntax checked separately','browser_visual_qa':'not run: control-browser capability unavailable in managed runtime','physical_promotion':0}
(D/'sources/UD_ATLAS_SITE_VALIDATION_v0.10.json').write_text(json.dumps(receipt,indent=2))
print(json.dumps(receipt))
