"""Static checks for the dataset audit; no browser-verification claim."""
import hashlib, json, subprocess
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote,urlsplit
root=Path('/workspace/scratch/1544cec576c6/ud-public');d=root/'dist'
class P(HTMLParser):
    def __init__(self):super().__init__();self.ids=[];self.links=[]
    def handle_starttag(self,t,a):
        a=dict(a)
        if 'id' in a:self.ids.append(a['id'])
        if t in ('a','script','link'):
            u=a.get('href') or a.get('src')
            if u:self.links.append(u)
count=0
for f in d.rglob('*.html'):
    p=P();p.feed(f.read_text());assert len(p.ids)==len(set(p.ids)),f
    for u in p.links:
        x=urlsplit(u)
        if x.scheme or x.netloc or not x.path:continue
        v=d/unquote(x.path.lstrip('/')) if x.path.startswith('/') else f.parent/unquote(x.path)
        if v.is_dir():v=v/'index.html'
        assert v.exists(),(f,u);count+=1
s=json.loads((d/'assets/sources.json').read_text());assert len({v['id'] for v in s})==len(s)
v=next(x for x in s if x['id']=='MRA01');f=d/v['local'].lstrip('/')
assert hashlib.sha256(f.read_bytes()).hexdigest()==v['sha256']
assert 'PHYSICAL PROMOTION 0' in v['status']
assert len(json.loads((d/'assets/ledger.json').read_text())['rows'])==448
assert subprocess.check_output(['git','diff','--','dist/index.html'],cwd=root)==b''
assert all('id="measurable-audit-v01"' in (d/p).read_text() for p in ['updates/index.html','evidence/index.html'])
receipt={'status':'PASS','local_links':count,'sources':len(s),'ledger_rows':448,'home_unchanged':True,'pdf_sha_matches_source_register':True,'browser_QA':'not run; managed control-browser capability unavailable','physical_promotion':0}
(d/'sources/measurable-audit-v0.1/SITE_VALIDATION_v0.1.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
