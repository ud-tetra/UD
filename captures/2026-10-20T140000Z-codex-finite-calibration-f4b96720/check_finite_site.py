"""Static links, source hashes and invariant authority files; no browser claim."""
import hashlib,json,subprocess
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
R=Path('/workspace/scratch/1544cec576c6/ud-public');D=R/'dist'
class P(HTMLParser):
    def __init__(self):super().__init__();self.ids=[];self.links=[]
    def handle_starttag(self,t,a):
        a=dict(a)
        if 'id' in a:self.ids.append(a['id'])
        if t in ('a','script','link'):
            u=a.get('href') or a.get('src')
            if u:self.links.append(u)
links=0;pages=list(D.rglob('*.html'))
for f in pages:
    p=P();p.feed(f.read_text());assert len(p.ids)==len(set(p.ids)),f
    for u in p.links:
        x=urlsplit(u)
        if x.scheme or x.netloc or not x.path:continue
        v=D/unquote(x.path.lstrip('/')) if x.path.startswith('/') else f.parent/unquote(x.path)
        if v.is_dir():v=v/'index.html'
        assert v.is_file(),(f,u);links+=1
sources=json.loads((D/'assets/sources.json').read_text());assert len({x['id'] for x in sources})==len(sources)
x=next(x for x in sources if x['id']=='FCAL01');pdf=D/x['local'].lstrip('/')
assert x['sha256']==hashlib.sha256(pdf.read_bytes()).hexdigest()
assert x['size_bytes']==pdf.stat().st_size
for f in ['papers/index.html','updates/index.html','evidence/index.html']:assert 'id="finite-calibration-v01"' in (D/f).read_text()
assert len(json.loads((D/'assets/ledger.json').read_text())['rows'])==448
for f in ['dist/index.html','dist/assets/ledger.json','dist/assets/claims.json']:
    assert subprocess.check_output(['git','diff','--',f],cwd=R)==b'',f
result={'status':'PASS','html_pages':len(pages),'local_links_checked':links,'source_entries':len(sources),'source_ids_unique':True,'home_ledger_claims_unchanged':True,'pdf_hash_matches_register':True,'browser_QA':'not run: managed control-browser capability unavailable','physical_promotion':0}
(D/'sources/finite-calibration-v0.1/SITE_VALIDATION_v0.1.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
