"""Independent AST/protocol comparison of preserved v1 and active v1.1."""
from pathlib import Path
import ast,hashlib,json
P=Path(__file__).resolve().parent;W=P.parent;old=W/'c20_verifier_v1';new=W/'c20_verifier'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def dump(n):return ast.dump(n,include_attributes=False)
a=ast.parse((old/'verifier.py').read_text());b=ast.parse((new/'verifier.py').read_text());fa={x.name:x for x in a.body if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef))};fb={x.name:x for x in b.body if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef))};assert set(fa)==set(fb)
changed=[n for n in fa if dump(fa[n])!=dump(fb[n])];assert changed==['main']
assert dump(ast.Module(body=[x for x in a.body if x is not fa['main']],type_ignores=[]))==dump(ast.Module(body=[x for x in b.body if x is not fb['main']],type_ignores=[]))
mainb=ast.parse(ast.unparse(fb['main'])).body[0];handlers=[h for n in ast.walk(mainb)if isinstance(n,ast.Try)for h in n.handlers];removed=0
for h in handlers:
 if isinstance(h.type,ast.Tuple):
  keep=[]
  for t in h.type.elts:
   if isinstance(t,ast.Attribute)and isinstance(t.value,ast.Name)and t.value.id=='zipfile'and t.attr=='BadZipFile':removed+=1
   else:keep.append(t)
  h.type.elts=keep
assert removed==1 and dump(mainb)==dump(fa['main'])
oldprotocol=read(old/'PROTOCOL.json');newprotocol=read(new/'PROTOCOL.json');expected=dict(oldprotocol);expected['version']='1.1';assert expected==newprotocol
for d in [old,new]:
 for n,h in read(d/'SEAL.json')['files'].items():assert sha(d/n)==h
v1=read(P/'FIXTURE_RESULTS_v1.json');assert all(sha(old/n)==h for n,h in v1['root_package_sha256'].items())
result={'status':'PASS_INDEPENDENT_AST_AND_PROTOCOL_DIAGNOSTIC_CORRECTION_REVIEW','changed_functions':changed,'only_main_catch_changed':True,'exact_change':'Add zipfile.BadZipFile to the structured intake/input-IO exception tuple','all_other_AST_nodes_identical':True,'protocol_change':'version1.0 to1.1 only; thresholds/resource caps/math unchanged','sealed_v1_history_preserved':True,'v1_crc_finding_sha256':sha(P/'CRC_PROBE.json'),'mathematical_retractions':0,'diagnostic_corrections':1,'source_sha256':{str(p.relative_to(W)):sha(p)for p in [old/'verifier.py',old/'PROTOCOL.json',old/'SEAL.json',new/'verifier.py',new/'PROTOCOL.json',new/'SEAL.json',W/'c20_root/DIAGNOSTIC_CORRECTION.json']},'v1_receipt_historical_path_mapping':{'c20_verifier/':'c20_verifier_v1/','c20_primary/':'c20_v1_primary/'},'new_fits':0,'physical_promotion':0}
with(P/'DIAGNOSTIC_CORRECTION_REVIEW.json').open('x')as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'status':result['status'],'changed_functions':changed,'mathematical_retractions':0}))
