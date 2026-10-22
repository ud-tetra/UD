from pathlib import Path
import copy,json,hashlib
from admit import *
P=Path(__file__).resolve().parent
profile={'dataset_doi':'10.11588/DATA/6MEKHI','waveform_sha256':'7966700a6208e2bd2b5829a32b38cce7016f0c3460ace2708c85bac8577c282c','kernel_sha256':'5beebe40fa2bfe744a0a64ee57401e77334b925bf0a23c0d2f24cafcd60ff254','apparatus_run':'UNRESOLVED_RIECHERT_FILE6385','channels':[1],'start_s':'0','end_s':'16183/1953125','sample_rate_nominal_Hz':'1953125','carrier_Hz':'4015625/129472','target':'full_complex_envelope_including_tail','spectral_measure':'complex_measure_total_variation_V','sample_window':2049,'timing_scope':'all_displaced_sample_intervals; common epoch required for cross-channel extension','implementation':'declared_serial_binary64_dot_products_only'}
# Correct carrier binding from the frozen rational definition, with no target fitting.
profile['carrier_Hz']=str(Fraction(257*1953125,16184));ph=digest(canonical(profile));(P/'PROFILE.json').write_text(json.dumps(profile,indent=2)+'\n')
packet={'format':'UD_QUADRATURE_EVIDENCE_1','profile':profile,'synthetic_fixture':True,'artifacts':{},'evidence':[]};catalog={'profile_sha256':ph,'purpose':'structure_review_only','synthetic_fixture':True,'approved_receipt_sha256':[]}
for role,(unit,direction,value) in REQUIREMENTS.items():
 identity=role;node={'id':identity,'role':role,'profile_sha256':ph,'bound':{'value':value,'unit':unit,'direction':direction,'meaning':'deterministic_uniform'},'validity':{'start_s':'0','end_s':profile['end_s']},'origin':'independent_source_bound' if role in ['inband_tv','envelope_band','tail_tv','full_amplitude','tail_absolute_frequency'] else 'external_calibration','inputs':[],'constructor_id':'SYNTHETIC_CONSTRUCTOR','review_path':'reviews/'+identity+'.json','synthetic_fixture':True};body=canonical(node);path='bounds/'+identity+'.json';packet['artifacts'][path]=body;packet['evidence'].append({'id':identity,'path':path,'sha256':digest(body)})
 receipt={'evidence_sha256':digest(body),'profile_sha256':ph,'role':role,'verdict':'SCOPED_BOUND_SUPPORTED','reviewer_id':'SYNTHETIC_REVIEWER','review_basis':'inspected_method_and_witness_bytes','synthetic_fixture':True};rb=canonical(receipt);packet['artifacts'][node['review_path']]=rb;catalog['approved_receipt_sha256'].append(digest(rb))
(P/'SYNTHETIC_PACKET.json').write_text(json.dumps(packet,indent=2)+'\n');(P/'SYNTHETIC_CATALOG.json').write_text(json.dumps(catalog,indent=2)+'\n')
# Author-controlled fixture receipts exercise software only; they are not nonconstructor reviews.
results=[]
def check_case(name,p,c,expected):
 r=evaluate(p,c,profile);assert r['status']==expected,(name,r);assert not r['empirical_admission'] and r['physical_promotion']==0;results.append({'case':name,**r})
check_case('complete_synthetic_fixture',packet,catalog,'STRUCTURALLY_READY_FIXTURE')
def changed(role,fn):
 p=copy.deepcopy(packet);c=copy.deepcopy(catalog);item=next(x for x in p['evidence'] if x['id']==role);node=json.loads(p['artifacts'][item['path']]);fn(node);body=canonical(node);p['artifacts'][item['path']]=body;item['sha256']=digest(body)
 # Rebind fixture receipt so semantic mutations are checked beyond the hash gate.
 rb=json.loads(p['artifacts'][node['review_path']]);rb['evidence_sha256']=item['sha256'];text=canonical(rb);p['artifacts'][node['review_path']]=text;c['approved_receipt_sha256'].append(digest(text));return p,c
mutations=[('wrong_units','time_error',lambda n:n['bound'].update(unit='ms')),('wrong_direction','full_amplitude',lambda n:n['bound'].update(direction='upper')),('negative','tail_tv',lambda n:n['bound'].update(value='-1')),('float_value','tail_tv',lambda n:n['bound'].update(value=.001)),('nonfinite_string','tail_tv',lambda n:n['bound'].update(value='NaN')),('excess_tail','tail_tv',lambda n:n['bound'].update(value='1/500')),('low_amplitude','full_amplitude',lambda n:n['bound'].update(value='1/4')),('time_gap','time_error',lambda n:n['validity'].update(start_s='1')),('bound_profile','relative_gain',lambda n:n.update(profile_sha256='0'*64)),('same_output_circular','tail_tv',lambda n:n.update(origin='same_output_fft')),('model_only','tail_tv',lambda n:n.update(origin='model_assumption')),('unknown_dependency','clean_slope',lambda n:n.update(inputs=['absent'])),('self_cycle','clean_slope',lambda n:n.update(origin='derived_bound',inputs=['clean_slope'])),('statistical_only','noise_quantization',lambda n:n['bound'].update(meaning='standard_deviation')),('unanchored_derivation','clean_slope',lambda n:n.update(origin='derived_bound'))]
for name,role,fn in mutations:
 p,c=changed(role,fn);check_case(name,p,c,'HOLD')
p=copy.deepcopy(packet);p['evidence']=p['evidence'][1:];check_case('missing_role',p,catalog,'HOLD')
p=copy.deepcopy(packet);p['evidence'].append(p['evidence'][0]);check_case('duplicate_id',p,catalog,'HOLD')
p=copy.deepcopy(packet);p['profile']['channels']=[2];check_case('wrong_channels',p,catalog,'HOLD')
p=copy.deepcopy(packet);p['artifacts'][p['evidence'][0]['path']]+=' ';check_case('tampered_bytes',p,catalog,'HOLD')
c=copy.deepcopy(catalog);c['approved_receipt_sha256']=[];check_case('unapproved_receipt',packet,c,'HOLD')
p=copy.deepcopy(packet);key='reviews/inband_tv.json';r=json.loads(p['artifacts'][key]);r['reviewer_id']='SYNTHETIC_CONSTRUCTOR';p['artifacts'][key]=canonical(r);c=copy.deepcopy(catalog);c['approved_receipt_sha256'].append(digest(p['artifacts'][key]));check_case('constructor_only',p,c,'HOLD')
p=copy.deepcopy(packet);p['evidence'][0]['path']='../outside';check_case('path_traversal',p,catalog,'HOLD')
p=copy.deepcopy(packet);key=p['evidence'][0]['path'];p['artifacts'][key]='{"id":"x","id":"y"}';p['evidence'][0]['sha256']=digest(p['artifacts'][key]);check_case('duplicate_json_key',p,catalog,'HOLD')
# Two-node cycle and transitive same-output root controls.
p,c=changed('clean_slope',lambda n:n.update(origin='derived_bound',inputs=['tail_tv']))
item=next(x for x in p['evidence'] if x['id']=='tail_tv');node=json.loads(p['artifacts'][item['path']]);node.update(origin='derived_bound',inputs=['clean_slope']);body=canonical(node);p['artifacts'][item['path']]=body;item['sha256']=digest(body);r=json.loads(p['artifacts'][node['review_path']]);r['evidence_sha256']=item['sha256'];rb=canonical(r);p['artifacts'][node['review_path']]=rb;c['approved_receipt_sha256'].append(digest(rb));check_case('two_node_cycle',p,c,'HOLD')
p,c=changed('clean_slope',lambda n:n.update(origin='derived_bound',inputs=['tail_tv']))
item=next(x for x in p['evidence'] if x['id']=='tail_tv');node=json.loads(p['artifacts'][item['path']]);node['origin']='same_output_fft';body=canonical(node);p['artifacts'][item['path']]=body;item['sha256']=digest(body);check_case('circular_source_ancestor',p,c,'HOLD')
p=copy.deepcopy(packet);p['profile']['kernel_sha256']='0'*64;check_case('wrong_kernel',p,catalog,'HOLD')
# Actual scoped candidate: source artifacts support signed voltage, but none of the twelve reviewed bound records has been supplied.
real={'format':'UD_QUADRATURE_EVIDENCE_1','profile':profile,'synthetic_fixture':False,'artifacts':{},'evidence':[]};trust={'profile_sha256':ph,'purpose':'structure_review_only','synthetic_fixture':False,'approved_receipt_sha256':[]}
(P/'CIRCUIT_PACKET.json').write_text(json.dumps(real,indent=2)+'\n');(P/'EMPTY_TRUST_CATALOG.json').write_text(json.dumps(trust,indent=2)+'\n');actual=evaluate(real,trust,profile);assert actual['status']=='HOLD'
(P/'CIRCUIT_DISPOSITION.json').write_text(json.dumps({'scope':'Mapping of prior scoped audit; no new dataset download or author contact','missing_reviewed_roles':sorted(REQUIREMENTS),'signed_trace':'Previously supported component; insufficient to satisfy bounds','apparatus_run_binding':'UNRESOLVED; no physical-ready profile claimed',**actual},indent=2)+'\n')
(P/'TEST_RESULTS.json').write_text(json.dumps({'status':'PASS_SOFTWARE_CONTROLS','cases':len(results),'results':results,'independent_review':'PENDING','empirical_admission':False,'physical_promotion':0},indent=2)+'\n');print(json.dumps({'status':'PASS','controls':len(results),'circuit':actual['status'],'missing_roles':len(REQUIREMENTS)}))
