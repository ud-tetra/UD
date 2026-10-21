"""Static source/output audit and independent finite graph witnesses. No imports of research code."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import ast,json,csv,hashlib,subprocess,re
C=Path(__file__).parent;ROOT=C.parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
def write(n,d):(C/n).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def read(name):return json.loads((ROOT/'docs'/name).read_text())
def scalars(node):
 if isinstance(node,ast.Constant):return node.value
 if isinstance(node,ast.Dict):return {scalars(k):scalars(v) for k,v in zip(node.keys,node.values)}
 if isinstance(node,(ast.List,ast.Tuple)):return [scalars(x) for x in node.elts]
 if isinstance(node,ast.BinOp) and isinstance(node.op,ast.Div):return scalars(node.left)/scalars(node.right)
 raise ValueError('Not a permitted static literal expression')
code=[]
for p in sorted((ROOT/'docs').glob('*.py')):
 s=p.read_text();tree=ast.parse(s);schemas=[];rng=[];solvers=[]
 for node in ast.walk(tree):
  if isinstance(node,ast.Dict):
   for k,v in zip(node.keys,node.values):
    if isinstance(k,ast.Constant) and k.value=='schema' and isinstance(v,ast.Constant):schemas.append(v.value)
  if isinstance(node,ast.Call):
   name=ast.unparse(node.func)
   if name.endswith(('default_rng','random.seed')):rng.append({'line':node.lineno,'call':ast.unparse(node)})
   if name.endswith(('eigsh','eigh')):solvers.append({'line':node.lineno,'call':ast.unparse(node),'v0_supplied':any(k.arg=='v0' for k in node.keywords)})
 code.append({'path':str(p.relative_to(ROOT)),'sha256':sha(p.read_bytes()),'docstring':ast.get_docstring(tree),'schemas':sorted(set(schemas)),'rng':rng,'eigensolvers':solvers,'functions':[{'name':n.name,'line':n.lineno} for n in tree.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))]})
write('CODE_STATIC_INDEX.json',code)
pairs=[
 ('shell1_sim.py','B_rho_raw.json','prescribed exponential shell profile; xi supplied; sigma2 length multiplied by8'),
 ('shell1_4x10.py','B_rho_raw_4x10.json','same profile family at level10; not eigenvector evidence'),
 ('shell1_eigensolve.py','B_rho_raw_eigensolve.json','single-channel sparse Hamiltonian and defect-overlap selection'),
 ('shell1_sector_resolved.py','B_rho_raw_sector.json','sector-selector repair; not interchangeable with prior selector'),
 ('shell1_hmulti_va.py','B_rho_raw_hmulti_va.json','3N clean operator; fallback chooses rho label even without rho-dominated candidate'),
 ('hmulti_version_a.py','Hmulti_A_raw.json','2N operator; two supplied mu ansatze; no burden'),
 ('hmulti_r6b.py','Hmulti_R6b.json','Theta potential removed, depth2/3 adjacency; graph remains disconnected'),
 ('r6b_version_b.py','R6b_VersionB.json','R6b plus supplied rho disorder; graph remains disconnected')]
records=[];site_checks=[]
for script,output,scope in pairs:
 p=ROOT/'docs'/output;d=read(output);rows=d if isinstance(d,list) else d['results']
 ss=(ROOT/'docs'/script).read_text();schemas=sorted({x.get('schema') for x in rows if x.get('schema')}) if isinstance(d,list) else [d.get('schema')]
 bindings=[]
 def find_bindings(x,path=''):
  if isinstance(x,dict):
   for k,v in x.items():
    if re.search(r'(?:code|script|operator|matrix|environment|command).*(?:sha|hash)|(?:sha|hash).*(?:code|script|operator|matrix)|^(?:seed|rng_state|eigensolver_residual)$',k,re.I):bindings.append({'path':path+'/'+k,'value':v})
    find_bindings(v,path+'/'+k)
  elif isinstance(x,list):
   for i,v in enumerate(x):find_bindings(v,path+'/'+str(i))
 find_bindings(d)
 for row in rows:
  N=row.get('N_sites',row.get('N'));level=row.get('ifs_level',row.get('level'));assert N==4**level
  site_checks.append({'output':output,'N':N,'level':level})
 records.append({'candidate_code':'docs/'+script,'code_sha256':sha((ROOT/'docs'/script).read_bytes()),'output':'docs/'+output,'output_sha256':sha(p.read_bytes()),'records':len(rows),'schemas':schemas,'matching_schema_declared_in_code':all(x in ss for x in schemas if x) if schemas else None,'association_status':'STATIC_CANDIDATE_MATCH__NOT_HASH_BOUND_EXECUTION','model_scope':scope,'structured_execution_binding_fields_found':bindings,'historical_timestamp':None if isinstance(d,list) else d.get('timestamp'),'fresh_simulation_replay':False})
assert len(site_checks)==39
# hmulti_repaired_v11 has a schema absent from every recovered JSON payload.
all_json={str(p.relative_to(ROOT)):p.read_text() for p in ROOT.rglob('*.json') if p.parts[len(ROOT.parts)] in ('docs','Docs')}
missing=[name for name,s in all_json.items() if 'Hmulti_A_repaired_v1.1' in s]
perprobe=[name for name,s in all_json.items() if 'per_probe_sigma2' in s]
assert not missing and not perprobe
# OCPF analysis is a literal transcribed dataset, not a generator execution receipt.
tree=ast.parse((ROOT/'docs/ocpf_v3_analyze.py').read_text());node=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='data' for t in n.targets))
literal=scalars(node.value);d=read('ocpf_v3_N567_data.json');csvrows=list(csv.DictReader((ROOT/'docs/ocpf_v3_N567_sweep.csv').open()))
assert len(csvrows)==39
for k,v in literal.items():
 assert v==d[str(k)]
 for lam,val in v['sweep']:
  rr=[r for r in csvrows if int(r['N'])==k and F(r['lambda_over_J'])==F(str(lam))]
  assert len(rr)==1 and F(rr[0]['f_close'])==F(str(val))
records.append({'candidate_code':['docs/ocpf_v3_sweep.py','docs/ocpf_v3_efficient.py'],'analysis':'docs/ocpf_v3_analyze.py','outputs':['docs/ocpf_v3_N567_data.json','docs/ocpf_v3_N567_sweep.csv'],'association_status':'EXACT_LITERAL_TRANSCRIPTION_MATCH_39_ROWS__GENERATOR_ORIGIN_UNVERIFIED','generator_difference':'canonical requests N5..13; efficient N5..10 and truncated eigenspaces at large dimensions; saved table only N5..7','runtime_execution_binding':'No source-hash/matrix/environment receipt establishing which generator produced the transcribed table','fresh_simulation_replay':False})
# New graph witness: for L>=3 every hopping preserves first L-3 base4 digits.
# Within each64 block, theta connects vertices in distinct groups of4 (weights differ by hierarchy).
def components(level):
 N=4**level;parent=list(range(N));edges=0
 def find(i):
  while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
  return i
 for start in range(0,N,64):
  for i in range(start,start+64):
   for j in range(i+1,start+64):
    if i//4!=j//4:
     parent[find(i)]=find(j);edges+=1
 sizes=Counter(find(i) for i in range(N));assert len(sizes)==4**(level-3) and set(sizes.values())=={64}
 return {'level':level,'N':N,'components':len(sizes),'component_size':64,'theta_edges':edges}
explicit=[components(l) for l in (3,4,5)]
for script in ('hmulti_r6b.py','r6b_version_b.py'):
 s=(ROOT/'docs'/script).read_text();assert '[:level-3]' in s and '[:level-2]' in s and '[:level-1]' in s
graph={'status':'EXACT_SOURCE_CODE_CONNECTIVITY_CLAIM_FALSIFIED','source_scripts':['docs/hmulti_r6b.py','docs/r6b_version_b.py'],'symbolic_statement':'For level L>=3 and N=4^L, theta graph has4^(L-3) connected components, each64 sites. Rho sibling edges and pointwise cross coupling also preserve that prefix. Full2N graph has the same number of128-coordinate components.','proof':'Every source edge is within a shared great-grandparent (prefix L-3); depth3 edges connect its four16-site groups, and depth2 edges connect distinct4-site groups. Hence each64-site group is connected and no edge leaves it. Diagonal potentials and on-site rho/theta coupling add no cross-prefix edge.','explicit_graph_checks':explicit,'theta_laplacian_zero_space':'dimension4^(L-3), because weights are positive and each block is connected','IPR_witness':'A unit vector constant on one64-site component has IPR=1/64 and F=N/64. A globally uniform unit vector has F=1. Both are theta Laplacian zero modes; rotations in this degenerate subspace change F. This statement is about H_theta, not an exact eigenvector assertion for coupled H_full.','versionB_comparison':[],'empirical_promotion':False}
for row in read('R6b_VersionB.json')['results']:
 target=F(row['N'],64);val=F(str(row['F_sigma2_Theta_mean']));assert abs(val-target)<F(1,10**6)
 graph['versionB_comparison'].append({'level':row['level'],'N':row['N'],'component_count':4**(row['level']-3),'component_uniform_F':str(target),'reported_F_theta':str(val),'absolute_difference':str(abs(val-target))})
write('GRAPH_CONNECTIVITY_CHECKS.json',graph)
write('SIMULATION_PROVENANCE_MAP.json',{'status':'AUDITED_STATIC_PROVENANCE_WITH_EXACT_COUNTERWITNESSES','families':records,'unmatched_code':['docs/hmulti_repaired_v11.py'],'unmatched_schema_search':missing,'per_probe_output_json_hits':perprobe,'shell_records_with_N_equals_4_power_level':len(site_checks),'output_execution_hash_bound_families':0,'provenance_limits':'Static schema/parameter agreement suggests a producer; does not prove execution or authenticate historical actor/timestamp. Eigenvector payloads, source-hash receipts and fresh solver residuals are not supplied by this audit. No imported scripts run.','physical_promotion':0})
# Inventory both case-distinct source folders, with targeted new-Docs relevance snippets.
inventory=[];relevance=[]
for folder in ('docs','Docs'):
 for p in sorted((ROOT/folder).rglob('*')):
  if not p.is_file():continue
  name=str(p.relative_to(ROOT));b=p.read_bytes();inventory.append({'path':name,'size_bytes':len(b),'sha256':sha(b)})
  if folder=='Docs':
   s=subprocess.run(['pdftotext','-layout',str(p),'-'],check=True,capture_output=True).stdout.decode('utf8',errors='replace') if p.suffix=='.pdf' else b.decode('utf8',errors='replace')
   lines=[{'line':i,'excerpt':v[:500]} for i,v in enumerate(s.splitlines(),1) if re.search(r'metric|action|support scale|not identified|same.carrier|independent|clock|THM.?534|pentagon|quark|lepton',v,re.I)]
   relevance.append({'path':name,'sha256':sha(b),'text_characters':len(s),'targeted_lines':lines[:14],'scope':'targeted static text review; historical claims not adopted as instructions or proof'})
write('SOURCE_INVENTORY.json',inventory);write('NEW_DOCS_RELEVANCE.json',relevance)
write('AUDIT_RESULTS.json',{'status':'PASS_SCOPED','source_files':len(inventory),'capital_Docs_files':len(relevance),'python_AST_files':len(code),'shell_records':len(site_checks),'OCPF_literal_CSV_JSON_matches':len(csvrows),'graph_claim':'FALSIFIED by new exact source-rule witness','frozen_operator_specification':'separate FREEZE_RECEIPT.json','imported_code_executed':False,'fresh_eigensolver_replay':False,'independent_review':'PENDING','physical_promotion':0})
print(json.dumps({'status':'PASS_SCOPED','source_files':len(inventory),'new_Docs':len(relevance),'static_simulation_families':len(records),'graph_components_L5_to_L8':[4**(l-3) for l in range(5,9)]}))
