"""Constructor checks against direct enumeration and hostile receipt mutations."""
from pathlib import Path
from itertools import product,permutations
from collections import Counter
from fractions import Fraction
from copy import deepcopy
import json,hashlib,math
from response_contract import response_fiber,readout,transport,validate_receipt
R=Path(__file__).parent;P=R/'dist/sources/response-contract-v0.1'
bitmasks=list(product((0,1),repeat=3));perms=list(permutations(range(3)))
hist=Counter();admitted=[];symmetry_cases=0;count_classes=0
for T,L in product(bitmasks,repeat=2):
 f=response_fiber(T,L);i=f['i'];hist[i]+=1
 direct={q for q in bitmasks if all(t*l<=qv<=t for t,l,qv in zip(T,L,q))}
 assert {r['q'] for r in f['responses']}==direct and len(direct)==2**i
 for j in range(i+1):
  assert sum(r['idle_count']==j for r in f['responses'])==math.comb(i,j);count_classes+=1
 stabilizer=[p for p in perms if transport(T,p)==T and transport(L,p)==L]
 fixed={r['h'] for r in f['responses'] if all(transport(r['h'],p)==r['h'] for p in stabilizer)}
 assert fixed=={(0,0,0),f['I']};symmetry_cases+=1
 # Nonuniform orbit weights demonstrate symmetry does not fix cardinality probabilities.
 weights=[Fraction(j+1,(i+1)*(i+2)//2) for j in range(i+1)]
 probabilities={r['h']:weights[r['idle_count']]/math.comb(i,r['idle_count']) for r in f['responses']}
 assert sum(probabilities.values())==1
 for p in stabilizer:
  assert all(probabilities[h]==probabilities[transport(h,p)] for h in probabilities)
 for r in f['responses']:admitted.append((T,L,r['q'],f['omega'],r['h']))
assert [hist[i] for i in range(4)]==[27,27,9,1] and len(admitted)==125
frame_checks=0
for old,new in product(admitted,repeat=2):
 theta=tuple(1-v for v in old[2]);f=response_fiber(new[0],new[1]);budgets=[]
 for h in [r['h'] for r in f['responses']]:
  out=readout(theta,old[3],new[0],new[1],h);mu=out['mu_theta'];budgets.append(mu)
  assert mu==sum(old[2])-sum(f['omega'])-sum(h)
  assert sum(out['close_mask'])-sum(out['reopen_mask'])==mu
 assert set(budgets)==set(range(sum(old[2])-sum(f['omega'])-f['i'],sum(old[2])-sum(f['omega'])+1))
 # Transport both prior masks; simultaneously relabel the new masks to compare equivalent frames.
 for p in perms:
  out=readout(theta,old[3],transport(new[0],p),transport(new[1],p),transport(new[4],p),p)
  base=readout(theta,old[3],new[0],new[1],new[4])
  assert out['mu_theta']==base['mu_theta']
  assert out['close_mask']==transport(base['close_mask'],p) and out['reopen_mask']==transport(base['reopen_mask'],p)
  frame_checks+=1
packet=json.loads((P/'synthetic_receipt.json').read_text());valid=validate_receipt(packet,P)
assert valid['status']=='STRUCTURE_PASS__SYNTHETIC_ONLY' and valid['conditional_readout']['mu_theta']==0
mutations={
 'endpoint_exposed':('target_exposed',True),
 'release_before_freeze':('endpoint_release_at','2026-10-13T23:59:00Z'),
 'timezone_missing':('input_sealed_at','2026-10-14T00:00:00'),
 'idle_outside_I':('idle_h',[1,0,0]),
 'source_values_rebound':('prospective_L',[0,0,0]),
 'frame_not_permutation':('frame_old_to_current',[0,0,2]),
 'bits_not_integer':('prior_theta',[False,1,1]),
 'invalid_prior_domain':('prior_T',[0,0,0]),
 'native_program_missing':('source_class','native_candidate'),
 'physical_clock_inserted':('time_semantics','seconds'),
 'event_null_undefined':('null_event_policy',None),
 'tie_undefined':('tie_policy',None)}
rejected=[]
for name,(key,val) in mutations.items():
 p=deepcopy(packet);p[key]=val;r=validate_receipt(p,P)
 assert r['failures'] and r['status']=='SOURCE_INVALID__NO_SCORE',name
 rejected.append(name)
for name,path,sha in [('bad_hash','synthetic_pre_event_construction.json','0'*64),('missing_bytes','missing.json','0'*64),('unsafe_path','../synthetic_pre_event_construction.json','0'*64)]:
 p=deepcopy(packet);p['artifacts'][0].update(path=path,sha256=sha);assert validate_receipt(p,P)['failures'];rejected.append(name)
p=deepcopy(packet);p['artifacts'].append(deepcopy(p['artifacts'][0]));assert validate_receipt(p,P)['failures'];rejected.append('duplicate_construction')
# A structurally complete native-candidate specimen must still never get native/empirical authority.
import tempfile
with tempfile.TemporaryDirectory() as tmp:
 t=Path(tmp);binding=json.loads((P/'synthetic_pre_event_construction.json').read_text());binding['source_class']='native_candidate'
 b=t/'construction.json';b.write_text(json.dumps(binding));p=deepcopy(packet);p['source_class']='native_candidate';p['artifacts'][0].update(path=b.name,sha256=hashlib.sha256(b.read_bytes()).hexdigest())
 p['source_program']={k:'Declared candidate rule; not independently validated.' for k in ['complete_state','viability_update','idle_response','event_and_null_rule','frame_rule','state_feedback','renewal_rule','collision_ties']}
 assert validate_receipt(p,t)['status']=='STRUCTURE_PASS__NATIVE_VALIDATION_PENDING__NO_SCORE'
# Counts do not determine an intermediate idle address.
f=response_fiber((1,1,1),(1,0,0));j1=[r for r in f['responses'] if r['idle_count']==1]
assert len(j1)==2 and len({r['theta'] for r in j1})==2
result={'status':'PASS','physical_promotion':0,'source_pairs':64,'response_states':125,'idle_potential_histogram':[hist[i] for i in range(4)],
 'cardinality_orbits_checked':count_classes,'reduced_deterministic_symmetry_cases':symmetry_cases,
 'ordered_response_pairs':15625,'frame_covariance_cases':frame_checks,'hostile_receipts_rejected':rejected,
 'synthetic_example_verdict':valid['status'],'native_candidate_authority':'STRUCTURE_PASS never establishes native validation or score eligibility',
 'review':'Constructor verification; independent adversarial proof review pending',
 'theorem_sha256':hashlib.sha256((P/'UD_MINIMAL_PRE_EVENT_RESPONSE_SOURCE_THEOREM_v0.1.md').read_bytes()).hexdigest()}
(P/'UD_RESPONSE_CONTRACT_VERIFICATION_v0.1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
