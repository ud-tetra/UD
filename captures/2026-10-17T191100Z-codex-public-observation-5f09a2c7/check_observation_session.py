"""Publication structure, byte provenance and scope checks; no scientific replay or browser QA."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,hashlib
R=Path(__file__).parent;D=R/'dist'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.main=0;self.title=0;self.h1=0;self.nav=False
 def handle_starttag(self,t,a):
  a=dict(a)
  if 'id' in a:self.ids.append(a['id'])
  if t=='main':self.main+=1
  if t=='title':self.title+=1
  if t=='h1':self.h1+=1
  if t=='nav' and a.get('id')=='navigation':self.nav=True
  if t in ['a','link','script','img']:
   u=a.get('href') or a.get('src')
   if u:self.links.append(u)
pages={}
for p in D.rglob('*.html'):
 q=Page();q.feed(p.read_text());assert q.main==1 and q.title>=1,p;assert len(q.ids)==len(set(q.ids)),p
 pages[p.resolve()]=q
links=0
for p,q in pages.items():
 for u in q.links:
  s=urlsplit(u)
  if s.scheme or s.netloc:continue
  target=D/unquote(s.path.lstrip('/')) if s.path.startswith('/') else p.parent/unquote(s.path) if s.path else p
  if target.is_dir():target=target/'index.html'
  assert target.exists(),(p,u)
  if s.fragment and target.suffix=='.html' and target.resolve() in pages:assert unquote(s.fragment) in pages[target.resolve()].ids,(p,u,'missing fragment')
  links+=1
 for_nav=q.nav
 if for_nav:assert '/observation/' in q.links,p
sources=json.loads((D/'assets/sources.json').read_text());assert len({x['id'] for x in sources})==len(sources)
ids={x['id'] for x in sources}
for x in json.loads((D/'assets/claims.json').read_text()):assert x['source_id'] in ids
for x in sources:
 if x.get('local'):assert (D/x['local'].lstrip('/')).is_file(),x['id']
items=json.loads((R/'observation_session_input.json').read_text())['items'];assert len(items)==26
for i,x in enumerate(items,1):
 p=D/x['local'].lstrip('/');b=p.read_bytes();assert len(b)==x['size_bytes'] and hashlib.sha256(b).hexdigest()==x['sha256']
 y=next(y for y in sources if y['id']==f'OBSSESSION{i:02}');assert y['sha256']==x['sha256'] and y['content']==b.decode()
assert sum(x['phase']=='Recovered earlier package' for x in items)==17
assert sum(x['phase']=='Later research capture' for x in items)==9
assert json.loads((D/'assets/ledger.json').read_text())['rows'].__len__()==448
t=(D/'observation/index.html').read_text()
for token in ['1893','747','2498','142','2640','605','286.75','18,790,154','2203','HOLD','Physical promotion 0','2<sup>−39</sup>','105','37','1877','763']:assert token in t,token
assert all('/observation/' in (D/p).read_text() for p in ['index.html','updates/index.html','contribution/index.html','papers/index.html','evidence/index.html'])
assert 'https://unified-dynamics-public.ben-w-mayes.chatgpt.site/observation/' in (D/'sitemap.xml').read_text()
assert (D/'sources/observation-v0.1/SESSION_SOURCE_MAP.json').read_bytes()==(R/'observation_session_input.json').read_bytes()
receipt=dict(status='PASS',html_pages=len(pages),local_links_checked=links,research_sources=26,copied_report_hashes_verified=26,recovered_archives_indexed=17,later_captures_indexed=9,scientific_replay='not performed; original certificates retain their scope',browser_visual_qa='not run: control-browser capability unavailable in managed runtime',physical_promotion=0,independent_review='HOLD / not established')
(D/'sources/observation-v0.1/SITE_VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
