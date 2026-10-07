import hashlib,json,subprocess,zipfile,shutil,re
from pathlib import Path
from lxml import html
R=Path(__file__).resolve().parent;S=R.parent/'ud-site';D=S/'dist'
for src,name in [('transport/UD_CONSTITUTIVE_CURRENT_IDENTIFIABILITY_v0.1.md','CONSTITUTIVE_CURRENT_IDENTIFIABILITY_v0.1.md'),('transport/sources/HASSE_CURRENT_CURL_AUDIT.md','HASSE_CURRENT_CURL_AUDIT_v0.1.md'),('transport/sources/GOVERNANCE.md','GOVERNANCE_CRL2_SUBDIVISION_v1.0.md'),('transport/sources/LEDGER_v0.39.md','LEDGER_v0.39.md')]:
 shutil.copy2(R.parent/src,R/'sources'/name)
receipt=json.loads((R/'REPLAY_RECEIPT.json').read_text());assert receipt['status']=='PASS' and receipt['exact_checks']==15
name='UD_TRANSPORT_NOISE_MARGIN_v0.1'
body=subprocess.run(['pandoc',str(R/(name+'.md')),'-f','markdown+tex_math_single_backslash','-t','html5','--mathml','--wrap=none'],check=True,text=True,capture_output=True).stdout
standalone='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>UD transport noise margin</title><style>body{max-width:980px;margin:2rem auto;padding:0 1rem;font:18px/1.6 system-ui;color:#182230}h1,h2{line-height:1.25}math[display=block],table{display:block;overflow-x:auto}td,th{padding:.5rem;border:1px solid #b6c3d2}table{border-collapse:collapse;font-size:16px}code{overflow-wrap:anywhere}</style></head><body>'+body+'</body></html>'
(R/(name+'.html')).write_text(standalone)
doc=html.fromstring(standalone);assert len(doc.xpath('//h2'))==6 and len(doc.xpath('//math'))==7
assert '\\[' not in doc.text_content()
files=sorted(p for p in R.rglob('*') if p.is_file() and p.name!='SHA256SUMS.json' and '__pycache__' not in p.parts)
(R/'SHA256SUMS.json').write_text(json.dumps({str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},indent=2)+'\n')
z=R.parent/(name+'_RELEASE.zip')
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as f:
 for p in files+[R/'SHA256SUMS.json']:f.write(p,name+'/'+str(p.relative_to(R)))
shutil.copytree(R,D/'source/transport-noise-margin-v0.1',dirs_exist_ok=True);shutil.copy2(z,D/'releases'/z.name)
page=body+'<p><a href="./releases/'+z.name+'" download>Complete source, replay and hash release</a> · <a href="#/doc/constitutiveCurrent">Previous constitutive inference audit</a></p>'
(D/'content/transport-noise-margin.html').write_text(page)
p=D/'app.js';s=p.read_text();key='transportNoiseMargin';assert key+':' not in s
item={'title':'Development — Transport reconstruction noise margin','label':'Development addendum 0.1 · 5 October 2026','note':'Four-class 4:1 stock profile; exact derivative separation 2/25; combined stock/readout certificate and tree-probe comparison. 15 grouped exact checks. Finite family optimum only; independent review pending; physical promotion 0.','kind':'html','file':'./content/transport-noise-margin.html','source':'./releases/'+z.name}
s=s.replace('const docs = {','const docs = {\n  '+key+':'+json.dumps(item)+',',1).replace('items:["manuscriptIntegration","constitutiveCurrent"','items:["manuscriptIntegration","transportNoiseMargin","constitutiveCurrent"',1);p.write_text(s)
p=D/'content/updates.html';old=p.read_text();assert 'id="transport-noise-margin-current"' not in old
p.write_text('<aside class="reading-rule" id="transport-noise-margin-current"><h2>5 October: bounded stock range and robust current inference</h2><p>A four-class profile with 4:1 stock range separates all 16,384 real sign rays. Exact derivative separation is 2/25; the worst-case certificate permits 1% relative stock error plus 1/50 absolute derivative error under the exact supplied generator. A finite integer-family search optimizes a sufficient local bound. Equal stocks remain preferable for signed tree-current probes. No physical readout or native preparation is supplied. Fifteen grouped exact checks pass; independent review pending; physical promotion 0.</p><p><a href="#/doc/transportNoiseMargin">Profile, exhaustive gap, uncertainty contract and observation tradeoff</a></p></aside>'+old)
p=S/'scripts/build-reading-search.py';s=p.read_text().replace("[('doc/constitutiveCurrent'","[('doc/transportNoiseMargin','content/transport-noise-margin.html','Transport uncertainty',True),('doc/constitutiveCurrent'",1);p.write_text(s)
print(json.dumps({'status':'PASS','report':str(R/(name+'.html')),'release':str(z),'sha256':hashlib.sha256(z.read_bytes()).hexdigest(),'math_elements':len(doc.xpath('//math'))}))
