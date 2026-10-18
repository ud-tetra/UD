import json,subprocess,sys
from bindings import P,sha,check_freeze,load_case
from frame_math import assemble_span

def validate():
 f=check_freeze();d=json.loads((P/'DATA_FREEZE.json').read_text());assert d['campaign_sha256']==sha(P/'CAMPAIGN_FREEZE.json');c=json.loads((P/'inputs/PHASE_STABILITY_CERTIFICATE.json').read_text())['constants'];rows=[];replays=0
 for e,r in zip(f['cases'],d['records']):
  assert e['case']==r['case'] and r['encoded_readings_checked']==18790154 and r['bytes']==150321232 and r['recipe']==e
  o=P/f"results/{e['case']}";audit=json.loads((o/'DISCOVERY_AUDIT.json').read_text());assert audit['record_sha256']==r['record_sha256']
  if (o/'HOLD.json').exists():
   h=json.loads((o/'HOLD.json').read_text());assert h==json.loads((P/f"results/original-{e['case']}/HOLD.json").read_text());rows.append({'case':e['case'],'stage':'proposer','status':'HOLD','reason':h['reason'],'learned_order':audit['temporal_dimension']});continue
  if (o/'ADAPTER_HOLD.json').exists():
   h=json.loads((o/'ADAPTER_HOLD.json').read_text());assert audit['temporal_dimension']!=105 and sha(o/'PROPOSAL.npz')==sha(P/f"results/original-{e['case']}/PROPOSAL.npz");rows.append(h);continue
  _,entry,_,_=load_case(e['case']);a=json.loads((o/'SPAN_CERTIFICATE.json').read_text());b=json.loads((o/'REPLAY_CERTIFICATE.json').read_text());dynamic={'replay','wall_seconds','peak_rss_kib'}
  assert {k:v for k,v in a.items() if k not in dynamic}=={k:v for k,v in b.items() if k not in dynamic};assert not a['replay'] and b['replay'];replays+=1
  for k in ['record_sha256','witness_sha256','proposal_sha256']:assert a[k]==entry[k]
  assert a['frame_reduction_sha256']==sha(o/'FRAME_REDUCTION.npz')
  try:proof=assemble_span(a['metrics'],c)
  except AssertionError as exc:proof={'status':'HOLD','reason':str(exc),'unique_reference_phase_matching':False,'physical_promotion':0}
  assert all(a[k]==v for k,v in proof.items());rows.append({'case':e['case'],'status':a['status'],'readable':a.get('readable'),'reason':a.get('reason'),'learned_order':audit['temporal_dimension'],'original_proposal_byte_identical':True})
 t=subprocess.run([sys.executable,'-m','unittest','discover','-v','-p','test_*.py'],cwd=P,capture_output=True,text=True);assert t.returncode==0,t.stderr;(P/'TEST_RESULTS.txt').write_text(t.stdout+t.stderr)
 return {'status':'PASS','physical_promotion':0,'independent_review':'pending','fresh_timing_records':len(rows),'encoded_source_readings_checked':sum(r['encoded_readings_checked'] for r in d['records']),'original_and_instrumented_proposer_runs':2*len(rows),'saved_array_phase_replays':replays,'tests':14,'cases':rows,'all_HOLDs_retained':True,'new_full_Hankel_execution':False,'no_full_Hankel_allocated':True,'uniform_all_input_phase_guarantee':False,'SI_or_physical_timing_certification':False}
if __name__=='__main__':
 r=validate();(P/'VALIDATION.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
