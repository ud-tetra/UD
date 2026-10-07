import hashlib,json,subprocess,zipfile,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;S=R.parent/'ud-site';D=S/'dist'
subprocess.run(['python3',str(R/'replay.py')],check=True,capture_output=True)
body=subprocess.run(['pandoc',str(R/'UD_CONSTITUTIVE_CURRENT_IDENTIFIABILITY_v0.1.md'),'-f','markdown+tex_math_single_backslash','-t','html5','--mathml','--wrap=none'],check=True,text=True,capture_output=True).stdout
report='UD_CONSTITUTIVE_CURRENT_IDENTIFIABILITY_v0.1.html'
(R/report).write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>UD constitutive current identifiability</title><style>body{max-width:980px;margin:2rem auto;padding:0 1rem;font:18px/1.6 system-ui;color:#182230}h1,h2{line-height:1.25}math[display=block]{display:block;overflow-x:auto}code{overflow-wrap:anywhere}</style></head><body>'+body+'</body></html>')
files=sorted(p for p in R.rglob('*') if p.is_file() and p.name!='SHA256SUMS.json' and '__pycache__' not in p.parts)
(R/'SHA256SUMS.json').write_text(json.dumps({str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},indent=2)+'\n')
z=R.parent/'UD_CONSTITUTIVE_CURRENT_IDENTIFIABILITY_v0.1_RELEASE.zip'
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as f:
    for p in files+[R/'SHA256SUMS.json']:f.write(p,'UD_CONSTITUTIVE_CURRENT_IDENTIFIABILITY_v0.1/'+str(p.relative_to(R)))
shutil.copytree(R,D/'source/constitutive-current-v0.1',dirs_exist_ok=True);shutil.copy2(z,D/'releases'/z.name)
(D/'content/constitutive-current.html').write_text(body+'<p><a href="./releases/'+z.name+'" download>Complete replay and source release</a> · <a href="#/doc/hasseCurrentCurl">Previous unrestricted-current audit</a></p>')
p=D/'app.js';s=p.read_text();key='constitutiveCurrent';assert key+':' not in s
item={'title':'Development — Constitutive current identifiability','label':'Development addendum 0.1 · 5 October 2026','note':'Real-state known stocks: generic derivative identifiability, explicit circulation degeneracy, and signed spanning-tree probe repair. Eight grouped exact checks and exhaustive 16384-ray profiles. Physical promotion 0; independent review pending.','kind':'html','file':'./content/constitutive-current.html','source':'./releases/'+z.name}
s=s.replace('const docs = {','const docs = {\n  '+key+':'+json.dumps(item)+',',1).replace('items:["manuscriptIntegration","hasseCurrentCurl"','items:["manuscriptIntegration","constitutiveCurrent","hasseCurrentCurl"',1);p.write_text(s)
p=D/'content/updates.html';old=p.read_text();assert 'id="constitutive-current-current"' not in old
p.write_text('<aside class="reading-rule" id="constitutive-current-current"><h2>5 October: current-law constraints narrow transport ambiguity</h2><p>Known stocks and the retained real-amplitude current law generically determine all currents from stock derivatives. Equal stocks still admit explicit circulation degeneracy: 128 repeated signatures in 16,384 sign rays. Signed spanning-tree currents provide a sufficient repair; readout margins and full complex-phase reconstruction remain open. Eight grouped exact checks passed. Development; independent review pending; physical promotion 0.</p><p><a href="#/doc/constitutiveCurrent">Proofs, degeneracy witness, reconstruction and replay</a></p></aside>'+old)
p=S/'scripts/build-reading-search.py';s=p.read_text().replace("[('doc/hasseCurrentCurl'","[('doc/constitutiveCurrent','content/constitutive-current.html','Constitutive current inference',True),('doc/hasseCurrentCurl'",1);p.write_text(s)
print(json.dumps({'report':str(R/report),'release':str(z),'release_sha256':hashlib.sha256(z.read_bytes()).hexdigest()}))
