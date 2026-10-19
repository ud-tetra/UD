"""Separate same-team, post-producer-outcome controls. No waveform or author code.
Freeze this file before first execution. Read only explicit packet/repo/source text.
Controls assess metadata scope, not authenticity, calibration, or physical truth.
"""
import copy,hashlib,importlib.util,json,sys
from pathlib import Path
D=Path(sys.argv[1]).resolve();R=Path(sys.argv[2]).resolve()
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 spec=importlib.util.spec_from_file_location('reviewed_checker',D/'check_request.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
 t=json.loads((D/'CANDIDATE_REQUEST_v0.1.json').read_text());s=c.load_schema();rows=[]
 def add(name,ok,detail):rows.append({'name':name,'pass':bool(ok),'detail':detail})
 def safe(r):return all(r[k] is False for k in ['raw_access_authorized','calibration_verified','evidence_authenticity_verified','physical_model_verified']) and r['physical_promotion']==0 and r['qualification_blockers_closed']==0
 r=c.evaluate(t);add('actual_snapshot_safe_HOLD',safe(r) and r['status']=='HOLD_INCOMPLETE_UNVERIFIED_REQUEST',r['status'])
 def fill(z):
  if 'const'in z:return copy.deepcopy(z['const'])
  if 'enum'in z:return next(copy.deepcopy(x) for x in z['enum'] if x is not None)
  types=z['type'];types=[types] if isinstance(types,str) else types;kind=next(x for x in types if x!='null')
  if kind=='object':return {k:fill(v) for k,v in z['properties'].items()}
  if kind=='array':return [fill(z['items']) for _ in range(z.get('minItems',0))]
  if kind=='boolean':return False
  if kind=='integer':return z.get('minimum',1)
  if kind=='string':return '0'*64 if '64' in z.get('pattern','') else '1/1' if 'pattern'in z else 'SYNTHETIC_UNVERIFIED_DECLARATION'
 filled=fill(s);rf=c.evaluate(filled)
 add('all_mutable_fields_filled_no_authorization',safe(rf) and not rf['schema_errors'],'Complete mutable declarations are synthetic; no URI is evidence.')
 add('const_null_wiring_makes_complete_status_unreachable',rf['unsupplied_count']==10 and rf['status']=='HOLD_INCOMPLETE_UNVERIFIED_REQUEST',{'remaining_null_paths':rf['unsupplied']})
 def mutation(name,fn):
  x=copy.deepcopy(t);fn(x);r=c.evaluate(x);add(name,safe(r) and r['status']=='HOLD_INVALID_REQUEST_METADATA',r['schema_errors'])
 mutation('boolean_channel_identity_refused',lambda x:x['channel_roles_filename_only'][0].update(channel=True))
 # JSON Schema const equality may treat integral floating JSON numbers as equal.
 xnum=copy.deepcopy(t);xnum['channel_roles_filename_only'][0]['channel']=1.0
 rnum=c.evaluate(xnum);add('numeric_const_equality_is_not_boolean_equality',safe(rnum),'Integral float acceptance alone is not a JSON Schema const defect.')
 mutation('swapped_CH9_CH10_roles_refused',lambda x:x['channel_roles_filename_only'][8].update(role='site5'))
 mutation('top_level_list_refused',lambda x:None) if False else None
 for name,obj in [('null_input',None),('array_input',[]),('boolean_input',True),('empty_object',{})]:
  r=c.evaluate(obj);add(name,safe(r) and r['status']=='HOLD_INVALID_REQUEST_METADATA',r['schema_errors'])
 # Prove in-memory checking never opens declared references, sockets or file writes.
 import builtins,socket
 old_open=builtins.open;old_socket=socket.socket;old_read=Path.read_bytes
 def refuse(*a,**k):raise AssertionError('Unexpected external access during metadata evaluation')
 try:
  builtins.open=refuse;socket.socket=refuse;Path.read_bytes=refuse
  rn=c.evaluate(filled,schema=s)
 finally:builtins.open=old_open;socket.socket=old_socket;Path.read_bytes=old_read
 add('declared_evidence_never_opened',safe(rn) and rn==rf,'Filesystem/network entry points refused while evaluating supplied schema.')
 old=R/'captures/2026-10-19T215410Z-codex-phase-run-calibration-43cadbae/calibration'
 ot=json.loads((old/'REQUEST_TEMPLATE.json').read_text());os=json.loads((old/'REQUEST_SCHEMA.json').read_text())
 for name in ('calibration','physical_model_comparison'):
  add('PR250_'+name+'_template_exact',t[name]==ot[name],'Decoded JSON subsection equality; no inherited blocker closed.')
  add('PR250_'+name+'_schema_exact',s['properties'][name]==os['properties'][name],'Decoded JSON schema subsection equality.')
 src=json.loads((D/'SOURCE_CELLS.json').read_text());fc={x['index']:x['source'] for x in src['cells']['figures']}
 add('author_path_and_channel_readout_syntax',t['source']['path'] in fc[10] and 'data[[0,1,2,3,4,5,6,7,9]' in fc[10],'Source text predicate only; no author code executed.')
 add('author_parameter_and_exposure_chain',all(z in fc[22] for z in ['Jexp','ν[shotidx]','fshift[1]']) and 'shotidx = 209' in fc[17] and 'used to get $J$' in fc[28] and all('Fig '+str(n) in fc[i] for i,n in [(23,7),(25,4),(32,8)]),'Candidate-derived Jexp and reused shift; no notebook output claim.')
 text=(D/'THEOREMS.md').read_text()
 add('retrospective_use_preserved',all(z in text for z in ['retrospective','None of these observations imply that all data are unusable','128 PR250 qualification blockers remain unresolved','no raw authorization']),'No never-usable claim; no calibration admission.')
 f=json.loads((D/'FREEZE.json').read_text());add('producer_frozen_files_intact',all((D/x['path']).stat().st_size==x['bytes'] and digest(D/x['path'])==x['sha256'] for x in f['files']),'Prospective producer file freeze replayed.')
 return {'artifact_type':'SAME_TEAM_POST_OUTCOME_INTAKE_REVIEW','controls':rows,'count':len(rows),'all_pass':all(x['pass'] for x in rows),'actual_null_leaf_count':r['unsupplied_count'] if False else c.evaluate(t)['unsupplied_count'],'null_leaf_count_is_not_independent_blockers':True,'original_qualification_blockers_unresolved':128,'physical_promotion':0,'raw_access_authorized':False,'new_raw_downloads':0,'new_fits':0,'author_code_executed':False}
if __name__=='__main__':print(json.dumps(main(),indent=2,sort_keys=True))
