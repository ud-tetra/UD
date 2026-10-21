from pathlib import Path
import json,hashlib,subprocess,tempfile,shutil,re
c=Path(__file__).parent
with tempfile.TemporaryDirectory() as tmp:
 t=Path(tmp);shutil.copytree(c/'sources',t/'sources');shutil.copyfile(c/'extract_sources.py',t/'extract_sources.py')
 subprocess.run(['python3',str(t/'extract_sources.py')],check=True,capture_output=True)
 for name in ('UD_v1.5.html','UD-Public_v1.5.html'):
  got=json.loads((t/(name+'.extracted.json')).read_text());want=json.loads((c/(name+'.extracted.json')).read_text())
  got.pop('source_path');want.pop('source_path');assert got==want
  assert got['sha256']==hashlib.sha256((c/'sources'/name).read_bytes()).hexdigest()
  assert not any(got['literal_scans'].values())
 graph=json.loads((t/'UD_v1.5.html.graph.json').read_text())
 assert graph==json.loads((c/'UD_v1.5.html.graph.json').read_text())
 assert len(graph['nodes'])==54 and len(graph['edges'])==107
 assert len({x['id'] for x in graph['nodes']})==54
 d=json.loads((t/'UD_v1.5.html.extracted.json').read_text());assert not d['dangling_dependencies']
 ids=[re.search(r'\bT[23]\.\d+',x['text']).group() for x in d['audit_rows']]
 assert len(ids)==19 and 'T2.6' not in ids and 'T3.0' in ids
 s=(c/'sources/UD_v1.5.html').read_text()
 assert 'not yet internally forced' in s and 'not direct discrete simulations' in s
 assert 'frontier bridge, not a completed derivation' in s
 assert 'All 5 field equations derived' in (c/'sources/UD-Public_v1.5.html').read_text()
 print(json.dumps({'status':'PASS','scope':'byte hashes, deterministic static-extraction replay, dependency resolution, audit gap and source-status declarations','nodes':54,'edges':107,'audit_rows':19,'missing_audit_row':'T2.6','independent_review':False,'physical_promotion':0},indent=2))
