"""Generate author-controlled fixtures; never independent review receipts."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import copy,json,hashlib,importlib.util
from admit_monitor import *
P=Path(__file__).resolve().parent;R=P.parents[1];prior=R/'captures/2026-10-22T133344Z-codex-sampled-monitor-93e0a217';old=R/'captures/2026-10-22T025145Z-codex-evidence-admission-7bf830a2'
def save(name,x):(P/name).write_text(json.dumps(x,indent=2)+'\n')
def filehash(p):return hashlib.sha256(p.read_bytes()).hexdigest()
profile=json.loads((old/'PROFILE.json').read_text());profile.update(dataset_doi='SYNTHETIC_ONLY_NO_MEASUREMENT',apparatus_run='SYNTHETIC_PROSPECTIVE_MONITOR_001',waveform_sha256=sha('synthetic acquisition identifier only'))
coverage={'start_s':'-1/100000000','end_s':'100000001/100000000'};acq={'start_s':profile['start_s'],'end_s':profile['end_s']}
binding={'apparatus_run':profile['apparatus_run'],'source_preparation':'SYNTHETIC_FIXED_PREPARATION_001','acquisition_profile_sha256':sha(canonical(profile)),'acquisition_channels':[1],'monitor_channels':['I','Q'],'monitor_epoch_s':'0','time_unit':'s','voltage_unit':'V','monitor_reference':'signed_complex_full_tail_residual','kernel_sha256':profile['kernel_sha256'],'source_contract_sha256':filehash(prior/'CONTRACT.json')}
hashes={'method_sha256':filehash(prior/'certify.py'),'contract_sha256':filehash(prior/'CONTRACT.json'),'theorem_sha256':filehash(prior/'THEOREM.md')}
cfg={'version':'UD_MONITOR_GRAPH_CONFIG_1','binding':binding,'coverage':coverage,'acquisition_interval':acq,'computation_hashes':hashes,'validator_sha256':filehash(P/'admit_monitor.py'),'policy':'external_review_authority_supplies_config_and_catalog; constructor_fixture_allowlist_is_not_independent_review'}
save('ACQUISITION_PROFILE_FIXTURE.json',profile);save('CONFIG.json',cfg)
packet={'format':'UD_MONITOR_GRAPH_1','synthetic_fixture':True,'binding':binding,'artifacts':{},'evidence':[]};catalog={'config_sha256':sha(canonical(cfg)),'purpose':'structure_review_only','synthetic_fixture':True,'approved_receipt_sha256':[]}
objects=packet['artifacts'];samplebody=(prior/'SYNTHETIC_SAMPLES.json').read_text();objects['witnesses/samples.json']=samplebody;objects['witnesses/timestamps.json']=canonical([str(F(j,1024)) for j in range(1024)]);objects['witnesses/method.json']=canonical({'synthetic_fixture':True,'warning':'Author-controlled software witness only; contains no calibration report, independent proof, authority or physical measurements.'})
e,rms=energy(strict(samplebody));tail=F(211,20)*(F(11,200000)+F(1,50000)+F(1,100000))+F(1,100000)
payloads={
'samples':{'path':'witnesses/samples.json','sha256':sha(samplebody),'indices':list(range(1024)),'unit':'V','reference':'signed_complex_full_tail_residual'},
'clock':{'path':'witnesses/timestamps.json','sha256':sha(objects['witnesses/timestamps.json']),'affine_error':'0','relative_affine_bound':'1/100000000','residual_bound_s':'1/100000000','epoch_s':'0'},
'iq_path':{'operator_error':'1/1000000','raw_vector_V':'5','output_error_V':'1/200000','response_scope':'entire_declared_path_frequency_voltage_loading_conditioning_extraction'},
'error_budget':{'shares_V':{'acquisition_quantization':'1/100000','quadrature_matrix':'1/200000','baseline':'3/1000000','numerical':'1/500000'},'meaning':'deterministic_complex_sample_RMS_triangle_budget'},
'source_class':{'modes':list(range(100,200)),'T0_s':'1','per_mode_error_Hz':'1/200','common_frequency_Hz':'0','coefficient_scope':'fixed_coefficients_and_frequencies_on_entire_coverage','completeness_basis':'independent_preparation_and_residual_bound'},
'outside_tv':{'value':'1/100000','unit':'V','direction':'upper','meaning':'complex_spectral_measure_total_variation','evidence_basis':'independent_of_acquisition_and_monitor_sample_output'},
'transfer':{'profile_sha256':binding['acquisition_profile_sha256'],'acquisition_interval':acq,'monitor_interval':coverage,'relation':'same_residual_complex_spectral_measure_on_entire_coverage','coverage_basis':'reviewed_simultaneous_same_preparation_same_epoch'},
'computation':{**hashes,'exact_energy_V2':str(e),'rms_ceiling_V':str(rms),'lambda_floor':'9/10','norm_factor':'211/20','tail_ceiling_V':str(tail)},
'tail_tv':{'value':str(tail),'unit':'V','direction':'upper','meaning':'deterministic_uniform'}}
for role,pay in payloads.items():
 refs={'witnesses/method.json':sha(objects['witnesses/method.json'])}
 if 'path' in pay:refs[pay['path']]=pay['sha256']
 pay['witnesses']=refs
 n={'id':role,'role':role,'binding_sha256':sha(canonical(binding)),'validity':coverage,'origin':ORIGINS[role],'inputs':DEPS[role],'constructor_id':'SYNTHETIC_CONSTRUCTOR','review_path':'reviews/'+role+'.json','synthetic_fixture':True,'payload':pay};body=canonical(n);pth='nodes/'+role+'.json';objects[pth]=body;packet['evidence'].append({'id':role,'path':pth,'sha256':sha(body)})
 r={'node_sha256':sha(body),'binding_sha256':n['binding_sha256'],'role':role,'verdict':'SCOPED_BOUND_SUPPORTED','reviewer_id':'SYNTHETIC_REVIEWER_LABEL_NOT_AN_INDEPENDENT_PERSON','review_basis':'inspected_method_and_witness_bytes','witness_sha256':refs,'synthetic_fixture':True};rb=canonical(r);objects[n['review_path']]=rb;catalog['approved_receipt_sha256'].append(sha(rb))
save('SYNTHETIC_PACKET.json',packet);save('SYNTHETIC_CATALOG.json',catalog)
results=[]
def case(name,p,c,expected,reason=None):
 r=evaluate(p,c,cfg);need(r['status']==expected,(name,r));need(not r['empirical_admission'] and r['physical_promotion']==0,'promotion leak')
 if reason:need(reason in r['reasons'],(name,'wrong gate',r))
 results.append({'case':name,'expected_gate':reason,**r});return r
positive=case('complete_author_controlled_fixture',packet,catalog,'STRUCTURALLY_READY_FIXTURE');save('TAIL_BOUND_PROPOSAL_FIXTURE.json',positive['tail_proposal'])
def change(p,c,role,fn):
 item=next(x for x in p['evidence'] if x['id']==role);n=strict(p['artifacts'][item['path']]);fn(n);body=canonical(n);p['artifacts'][item['path']]=body;item['sha256']=sha(body);r=strict(p['artifacts'][n['review_path']]);r.update(node_sha256=sha(body),binding_sha256=n['binding_sha256'],witness_sha256=n['payload']['witnesses']);rb=canonical(r);p['artifacts'][n['review_path']]=rb;c['approved_receipt_sha256'].append(sha(rb))
def mutate(name,role,fn,reason):
 p=copy.deepcopy(packet);c=copy.deepcopy(catalog);change(p,c,role,fn);case(name,p,c,'HOLD',reason)
for key,value in [('apparatus_run','OTHER_RUN'),('acquisition_channels',[2]),('monitor_channels',['Q','I']),('monitor_epoch_s','1'),('voltage_unit','mV'),('kernel_sha256','0'*64),('source_preparation','OTHER_PREPARATION'),('source_contract_sha256','0'*64)]:
 p=copy.deepcopy(packet);p['binding'][key]=value;case('binding_'+key,p,catalog,'HOLD','run/channel/epoch/units/kernel/source binding mismatch')
mutations=[
('stale_calibration','iq_path',lambda n:n['validity'].update(end_s='1/2'),'coverage gap'),
('clock_excess','clock',lambda n:n['payload'].update(residual_bound_s='1/10000'),'clock bounds'),
('clock_epoch','clock',lambda n:n['payload'].update(epoch_s='1'),'epoch mismatch'),
('IQ_wrong_product','iq_path',lambda n:n['payload'].update(output_error_V='1/1000000'),'IQ accounting'),
('IQ_incomplete_path','iq_path',lambda n:n['payload'].update(response_scope='matrix_only'),'IQ response scope'),
('IQ_undercharged','error_budget',lambda n:n['payload']['shares_V'].update(quadrature_matrix='1/1000000'),'IQ allocation undercharged'),
('negative_error','error_budget',lambda n:n['payload']['shares_V'].update(numerical='-1/1000000'),'allocation exceeded'),
('excess_error','error_budget',lambda n:n['payload']['shares_V'].update(numerical='1/1000'),'allocation exceeded'),
('float_bound','outside_tv',lambda n:n['payload'].update(value=.00001),'rational encoding'),
('statistical_outside','outside_tv',lambda n:n['payload'].update(meaning='RMS'),'outside TV type'),
('outside_wrong_unit','outside_tv',lambda n:n['payload'].update(unit='mV'),'outside TV type'),
('old_outside200uV','outside_tv',lambda n:n['payload'].update(value='1/5000'),'outside TV exceeded'),
('same_monitor_FFT','outside_tv',lambda n:n['payload'].update(evidence_basis='same_monitor_fft'),'circular outside evidence'),
('model_assumption_root','source_class',lambda n:n.update(origin='model_assumption'),'unsupported/circular origin'),
('nonstationary','source_class',lambda n:n['payload'].update(coefficient_scope='varying_coefficients'),'nonstationary source'),
('aliased_extra_mode','source_class',lambda n:n['payload']['modes'].append(1124),'mode family'),
('wrong_frequency_bound','source_class',lambda n:n['payload'].update(per_mode_error_Hz='1/100'),'frequency error'),
('unproven_transfer','transfer',lambda n:n['payload'].update(coverage_basis='same_device_later_day'),'unproven historical transfer'),
('transfer_profile','transfer',lambda n:n['payload'].update(profile_sha256='0'*64),'transfer profile mismatch'),
('transfer_interval','transfer',lambda n:n['payload']['acquisition_interval'].update(end_s='2'),'transfer interval mismatch'),
('wrong_source_code','computation',lambda n:n['payload'].update(method_sha256='0'*64),'computation source mismatch'),
('wrong_energy','computation',lambda n:n['payload'].update(exact_energy_V2='0'),'digital computation mismatch'),
('wrong_lambda','computation',lambda n:n['payload'].update(lambda_floor='1'),'Gram/tail computation mismatch'),
('forged_tail','tail_tv',lambda n:n['payload'].update(value='1/1000000'),'tail export mismatch'),
('unknown_dependency','tail_tv',lambda n:n.update(inputs=['absent']),'unknown dependency'),
('self_cycle','outside_tv',lambda n:n.update(inputs=['outside_tv']),'cyclic dependencies'),
('missing_required_dependency','computation',lambda n:n.update(inputs=['samples']),'required dependency set'),
('duplicate_dependency','computation',lambda n:n['inputs'].append('samples'),'dependency list'),
('sample_reference','samples',lambda n:n['payload'].update(reference='magnitude_only'),'sample unit/reference'),
('sample_indices','samples',lambda n:n['payload']['indices'].__setitem__(0,1),'sample indices')]
for name,role,fn,reason in mutations:mutate(name,role,fn,reason)
# Cycles and unsupported ancestors have valid fixture node/review hashes.
p=copy.deepcopy(packet);c=copy.deepcopy(catalog);change(p,c,'outside_tv',lambda n:n.update(inputs=['tail_tv']));case('transitive_cycle_via_computation',p,c,'HOLD','cyclic dependencies')
p=copy.deepcopy(packet);c=copy.deepcopy(catalog);change(p,c,'iq_path',lambda n:n.update(origin='same_output_fft'));case('circular_calibration_ancestor',p,c,'HOLD','unsupported/circular origin')
# Change witness bytes, then rebind their node and fixture receipt to reach semantic gates.
for name,role,wp,fn,reason in [
 ('timestamp_jitter','clock','witnesses/timestamps.json',lambda x:x.__setitem__(10,'1/2'),'sample timestamp residual'),
 ('repeated_timestamp','clock','witnesses/timestamps.json',lambda x:x.__setitem__(10,x[9]),'sample timestamp residual'),
 ('large_sample','samples','witnesses/samples.json',lambda x:x['samples'].__setitem__(0,[float(1).hex(),float(0).hex()]),'digital RMS exceeded'),
 ('nonfinite_sample','samples','witnesses/samples.json',lambda x:x['samples'][0].__setitem__(0,'inf'),'nonfinite sample'),
 ('short_sample','samples','witnesses/samples.json',lambda x:x['samples'].pop(),'sample count')]:
 p=copy.deepcopy(packet);c=copy.deepcopy(catalog);x=strict(p['artifacts'][wp]);fn(x);p['artifacts'][wp]=canonical(x);h=sha(p['artifacts'][wp]);change(p,c,role,lambda n:(n['payload'].update(sha256=h),n['payload']['witnesses'].update({wp:h})));case(name,p,c,'HOLD',reason)
p=copy.deepcopy(packet);p['artifacts']['witnesses/samples.json']+=' ';case('changed_bytes_unrebound',p,catalog,'HOLD','witness hash mismatch')
p=copy.deepcopy(packet);p['evidence'].pop();case('missing_role',p,catalog,'HOLD','missing monitor roles')
p=copy.deepcopy(packet);p['evidence'].append(p['evidence'][0]);case('duplicate_node',p,catalog,'HOLD','duplicate id')
p=copy.deepcopy(packet);p['evidence'][0]['path']='../private';case('unsafe_path',p,catalog,'HOLD','unsafe artifact path')
c=copy.deepcopy(catalog);c['approved_receipt_sha256']=[];case('unapproved_receipts',packet,c,'HOLD','unapproved review receipt')
p=copy.deepcopy(packet);c=copy.deepcopy(catalog);rp='reviews/source_class.json';r=strict(p['artifacts'][rp]);r['reviewer_id']='SYNTHETIC_CONSTRUCTOR';p['artifacts'][rp]=canonical(r);c['approved_receipt_sha256'].append(sha(p['artifacts'][rp]));case('constructor_review_label',p,c,'HOLD','constructor-only review')
# Fixture flag is propagated through sample and node/review objects; flipping only top-level fails.
p=copy.deepcopy(packet);p['synthetic_fixture']=False;case('fixture_laundering',p,catalog,'HOLD','fixture mismatch')
try:strict('{"x":1,"x":2}');raise AssertionError('duplicate parser')
except Hold:results.append({'case':'duplicate_JSON_key','status':'HOLD','reasons':['duplicate JSON key']})
# A changed decoded sample can remain under the RMS cap; the stored computation must still match.
p=copy.deepcopy(packet);c=copy.deepcopy(catalog);wp='witnesses/samples.json';x=strict(p['artifacts'][wp]);x['samples'][0]=[float(0).hex(),float(0).hex()];p['artifacts'][wp]=canonical(x);h=sha(p['artifacts'][wp]);change(p,c,'samples',lambda n:(n['payload'].update(sha256=h),n['payload']['witnesses'].update({wp:h})));case('low_RMS_changed_sample_stale_computation',p,c,'HOLD','digital computation mismatch')
p=copy.deepcopy(packet);p['artifacts'].pop('witnesses/method.json');case('missing_method_bytes',p,catalog,'HOLD','witness hash mismatch')
wrong=copy.deepcopy(cfg);wrong['validator_sha256']='0'*64
r=evaluate(packet,catalog,wrong);need(r['reasons']==['validator source mismatch'],'validator pin');results.append({'case':'validator_source_pin',**r})
# Preserve scoped historical disposition by running the original, unchanged checker.
spec=importlib.util.spec_from_file_location('old_admit',old/'admit.py');legacy=importlib.util.module_from_spec(spec);spec.loader.exec_module(legacy)
real=legacy.evaluate(json.loads((old/'CIRCUIT_PACKET.json').read_text()),json.loads((old/'EMPTY_TRUST_CATALOG.json').read_text()),json.loads((old/'PROFILE.json').read_text()));need(real['status']=='HOLD','historical admission changed')
save('CIRCUIT_DISPOSITION.json',{'scope':'Prior scoped candidate replay only; no new physical data or calibration supplied','historical_checker_sha256':filehash(old/'admit.py'),'missing_reviewed_acquisition_roles':sorted(legacy.REQUIREMENTS),'missing_reviewed_monitor_roles':sorted(DEPS),'transfer':'No reviewed same-run preparation/epoch binding to historical file6385',**real})
save('TEST_RESULTS.json',{'status':'PASS_CONSTRUCTOR_SOFTWARE_CHECKS','cases':len(results),'positive_fixture_count':1,'hold_controls':len(results)-1,'results':results,'historical_candidate':'HOLD','independent_review':'PENDING','empirical_admission':False,'physical_promotion':0})
print(json.dumps({'status':'PASS_CONSTRUCTOR_SOFTWARE_CHECKS','cases':len(results),'tail_fraction_V':str(tail),'historical_candidate':'HOLD'}))
