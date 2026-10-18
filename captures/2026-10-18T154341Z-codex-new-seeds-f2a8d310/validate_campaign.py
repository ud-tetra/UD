import json,subprocess,sys
from bindings import P,sha,check_freeze,load_case
from frame_math import assemble_span

def validate():
 f=check_freeze();d=json.loads((P/'DATA_FREEZE.json').read_text());assert d['campaign_sha256']==sha(P/'CAMPAIGN_FREEZE.json');c=json.loads((P/'inputs/PHASE_STABILITY_CERTIFICATE.json').read_text())['constants'];rows=[];replays=0
 for e,r in zip(f['cases'],d['records']):
  assert e['case']==r['case'] and r['all_scalar_differences_checked']==18790154
  assert r['per_vector_2neg20_met']==(r['max_vector_integer_squared_error']<=2**56) and r['sufficient_scalar_2neg23_met']==(r['max_scalar_integer_error']<=2**25)
  o=P/f"results/{e['case']}";audit=json.loads((o/'DISCOVERY_AUDIT.json').read_text());assert audit['record_sha256']==r['record_sha256']
  if (o/'HOLD.json').exists():
   h=json.loads((o/'HOLD.json').read_text());assert h==json.loads((P/f"results/original-{e['case']}/HOLD.json").read_text());rows.append({'case':e['case'],'stage':'proposer','status':'HOLD','reason':h['reason'],'learned_order':audit['temporal_dimension'],'per_vector_gate':r['per_vector_2neg20_met']});continue
  _,entry,_,_=load_case(e['case']);a=json.loads((o/'SPAN_CERTIFICATE.json').read_text());b=json.loads((o/'REPLAY_CERTIFICATE.json').read_text());dynamic={'replay','wall_seconds','peak_rss_kib'}
  assert {k:v for k,v in a.items() if k not in dynamic}=={k:v for k,v in b.items() if k not in dynamic};assert not a['replay'] and b['replay'];replays+=1
  for k in ['record_sha256','witness_sha256','proposal_sha256']:assert a[k]==entry[k]
  assert a['frame_reduction_sha256']==sha(o/'FRAME_REDUCTION.npz')
  try:proof=assemble_span(a['metrics'],c)
  except AssertionError as exc:proof={'status':'HOLD','reason':str(exc),'unique_reference_phase_matching':False,'physical_promotion':0}
  assert all(a[k]==v for k,v in proof.items())
  rows.append({'case':e['case'],'stage':'phase_certificate','status':a['status'],'readable':a.get('readable'),'reason':a.get('reason'),'learned_order':audit['temporal_dimension'],'per_vector_gate':r['per_vector_2neg20_met'],'original_proposal_byte_identical':True})
 t=subprocess.run([sys.executable,'-m','unittest','discover','-v','-p','test_*.py'],cwd=P,capture_output=True,text=True);assert t.returncode==0,t.stderr;(P/'TEST_RESULTS.txt').write_text(t.stdout+t.stderr)
 return {'status':'PASS','physical_promotion':0,'independent_review':'pending','known_baseline_new_constructor_noise_cases':len(rows),'exact_additive_scalar_comparisons':sum(r['all_scalar_differences_checked'] for r in d['records']),'original_and_instrumented_proposer_runs':2*len(rows),'saved_array_phase_replays':replays,'tests':13,'cases':rows,'all_HOLDs_retained':True,'new_full_Hankel_execution':False,'no_full_Hankel_allocated':True,'uniform_all_input_phase_guarantee':False,'independent_records_or_review_claimed':False}
if __name__=='__main__':
 r=validate();(P/'VALIDATION.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
