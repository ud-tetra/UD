"""Pure rejection/schema controls; no historical bundle reduction."""
import argparse,json,tempfile
from pathlib import Path
import reduce as r

def run():
 r.frozen();rows=[]
 def rejects(name,fn):
  try:fn();got=False
  except(Exception):got=True
  r.need(got,'control failed '+name);rows.append({'id':name,'pass':True})
 for name,x in [('zero_denominator',[1,0]),('negative_denominator',[1,-2]),('float_rational',[1.0,2]),('bool_rational',[True,2]),('scalar_rational',1)]:rejects(name,lambda x=x:r.rational(x))
 r.need(not r.cap([2,1],[1,1])and not r.cap([-1,1],[1,1]),'cap checks');rows.append({'id':'over_cap_and_negative_refused','pass':True})
 rejects('wrong_case_order',lambda:r.rows({'rows':[{'case':r.CASES[1]},{'case':r.CASES[0]}]}));rejects('duplicate_case',lambda:r.rows({'rows':[{'case':r.CASES[0]},{'case':r.CASES[0]}]}))
 rejects('missing_proof_pin',lambda:r.source_pin({'pins':[]},'x'));rejects('ambiguous_proof_pin',lambda:r.source_pin({'pins':[{'path':'x','sha256':'0'*64}]*2},'x'))
 rejects('metadata_flags_cannot_form_proof_bundle',lambda:r.identity({'pass':True,'physical_promotion':0},{'inputs':{}}))
 for name,p in [('self',r.P),('descendant',r.P/'bad'),('ancestor',r.P.parent)]:rejects('guard_'+name,lambda p=p:r.guard(p))
 with tempfile.TemporaryDirectory(prefix='ud-admission-guard-')as td:
  p=Path(td)/'alias';p.symlink_to(r.P,target_is_directory=True);rejects('guard_symlink',lambda:r.guard(p/'bad'))
  out=Path(td)/'fresh';r.run(Path('/does-not-exist'),out,'fresh');receipt=json.loads((out/'CERTIFICATE.json').read_text());r.need(receipt['status']=='HOLD_FOREIGN_OR_UNVERIFIED_FRESH_BUNDLE'and 'rows'not in receipt,'fresh mode cannot admit metadata');rows.append({'id':'fresh_bundle_always_HOLD_without_any_repository_read','pass':True})
 good={'eigenvalue_radius_upper':[1,4],'source_half_chord_lower':[1,2],'phase_error_upper':[1,4],'phase_matching_margin_lower':[1,4]}
 for name,update in [('radius_negative',{'eigenvalue_radius_upper':[-1,4]}),('radius_one',{'eigenvalue_radius_upper':[1,1]}),('touching_disks',{'eigenvalue_radius_upper':[1,2]}),('angle_at_half',{'phase_error_upper':[1,2]}),('zero_margin',{'phase_matching_margin_lower':[0,1]})]:
  r.need(not r.strict_disks(good|update),'strict disk control '+name);rows.append({'id':name,'pass':True})
 for name,keys in [('phase',r.PHASE_GATES),('route',r.ROUTE_GATES)]:
  full={k:True for k in keys}
  for tag,values in [('empty',{}),('missing',{k:v for k,v in full.items()if k!=sorted(keys)[0]}),('extra',full|{'unknown':True}),('false',full|{sorted(keys)[0]:False})]:
   r.need(not r.exact_gates(values,keys),'exact gate control '+name+tag);rows.append({'id':name+'_'+tag+'_gates_refused','pass':True})
 r.frozen();return {'status':'PASS_PURE_REJECTION_CONTROLS','rows':rows,'historical_reductions':0,'new_estimator_calls':0,'physical_promotion':0}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True);a=p.parse_args();out=r.guard(a.out);out.mkdir(parents=True,exist_ok=False)
 with(out/'CONTROLS.json').open('x')as f:json.dump(run(),f,indent=2);f.write('\n')
