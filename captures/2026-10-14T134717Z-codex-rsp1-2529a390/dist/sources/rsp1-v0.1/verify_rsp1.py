"""Root constructor checks extending counter range and binding parallel evidence."""
from pathlib import Path
from itertools import product
from dataclasses import replace,asdict
import hashlib,json
from rsp1 import State,transition,run,available_stock,close_duration,potential

R=Path(__file__).parent;P=R/'dist/sources/rsp1-v0.1'
seats=[(t,l,q) for t,l,q in product((0,1),repeat=3) if t*l<=q<=t]
cases=0
for triple in product(seats,repeat=3):
 T,L,q=zip(*triple)
 for r in product(range(4),repeat=3):
  if any(v and not t for v,t in zip(r,T)):continue
  for branch in ['C','H']:
   s=State(T,L,q,r,branch=branch);out=run(s)
   assert out['committed_updates']<=potential(s)
   assert all(row['pre_state']!=row['post_state'] for row in out['trace'])
   assert out['terminal']['pre_state']==out['terminal']['post_state']
   if branch=='C':
    # Per-address pulse schedule, including a possible one-tick broken-cache normalization.
    expected=max([2*n+old for n,old in zip(r,q)]+[int(any(ll and not tt for ll,tt in zip(L,T)))])
    assert out['committed_updates']==expected==close_duration(s)
    assert out['opening_toggles']==sum(r) and out['closure_toggles']==sum(r)+sum(q)
    assert out['remaining_stock']==0 and out['terminal']['halt_reason']=='EXHAUSTED_QUIESCENT'
   else:
    assert out['committed_updates']<=2+int(any(ll and not tt for ll,tt in zip(L,T)))
    assert out['closure_toggles']==0
   for row in out['trace']:
    e=row['event'];assert e['mu_theta']==e['viable_index']+sum(e['h_prior_aligned'])-sum(e['h_output'])
    assert row['available_stock_before']-row['available_stock_after']==row['consumed_tokens']
    assert row['potential_after']<row['potential_before']
   cases+=1
assert cases==5488
# Larger counters, serial refills, a preconsumed cursor and zero refill rows.
large=State((1,1,1),(1,0,0),(1,0,1),(17,0,4),((0,0,0),(0,0,0),(2,9,1)),cursor=1)
out=run(large);assert out['committed_updates']==close_duration(large)==55
assert out['opening_toggles']==available_stock(large) and out['remaining_stock']==0
# Visible-null and balanced-gross events must remain distinct.
h=transition(State((1,0,0),(1,0,0),(1,0,0),(0,0,0),branch='H'))
assert h['changed'] and h['response_tag']=='RESPONSE_NULL' and h['event']['viable_index']==1 and h['event']['mu_theta']==0
c=transition(State((1,1,0),(1,0,0),(1,0,0),(0,1,0)))
assert c['response_tag']=='BIT_EVENT' and c['event']['mu_theta']==0 and c['event']['gross_pair_toggles']==2 and c['consumed_tokens']==1
z=transition(State((0,0,0),(0,0,0),(0,0,0),(0,0,0),((0,0,0),)))
assert z['transition_kind']=='RENEWAL_ONLY' and z['changed'] and z['state'].cursor==1
# A Theta-only source projection is not single-valued even for this complete candidate.
s=State((1,1,1),(0,0,0),(0,0,0),(0,0,0))
assert transition(s)['state'].q!=transition(replace(s,r=(1,0,0)))['state'].q
invalid=[]
for name,patch in [('negative_stock',{'r':(-1,0,0)}),('boolean_counter',{'r':(True,0,0)}),('bad_mask',{'T':(2,1,1)}),('viability_exceeds_response',{'L':(1,0,0)}),('wrong_branch',{'branch':'native'}),('bad_cursor',{'cursor':1}),('bank_not_finite_queue',{'bank':None}),('broken_integrity_stock',{'T':(0,1,1),'r':(1,0,0)})]:
 try:replace(s,**patch)
 except ValueError:invalid.append(name)
 else:raise AssertionError(name)
parallel=json.loads((P/'RSP1_PARALLEL_VERIFICATION_v0.1.json').read_text())
impl=hashlib.sha256((R/'rsp1.py').read_bytes()).hexdigest()
assert parallel['status']=='PASS' and parallel['implementation']['sha256']==impl
assert parallel['response_contract_sha256']==hashlib.sha256((R/'response_contract.py').read_bytes()).hexdigest()
assert parallel['checker_sha256']==hashlib.sha256((P/'rsp1-parallel-check.py').read_bytes()).hexdigest()
review=(P/'RSP1_SOURCE_SCOPE_REVIEW_v0.1.md').read_text();assert impl in review and 'separate AI' in review
# Original ledger and prior release hashes are preserved by the extension (recorded separately in source basis).
record={'status':'PASS','physical_promotion':0,'root_no_bank_states_stock_0_to_3':cases,'large_cursor_bank_example_committed_updates':out['committed_updates'],
 'invalid_initial_states_rejected':invalid,'parallel_initial_states':parallel['exhaustive_initial_states'],
 'parallel_targeted_states':parallel['targeted_adversarial_states'],'parallel_relabel_comparisons':parallel['relabel_covariance_comparisons'],
 'implementation_sha256':impl,'theorem_sha256':hashlib.sha256((P/'UD_RSP1_FINITE_PRE_EVENT_SOURCE_PROGRAMME_v0.1.md').read_bytes()).hexdigest(),'parallel_receipt_sha256':hashlib.sha256((P/'RSP1_PARALLEL_VERIFICATION_v0.1.json').read_bytes()).hexdigest(),
 'source_scope_review_sha256':hashlib.sha256((P/'RSP1_SOURCE_SCOPE_REVIEW_v0.1.md').read_bytes()).hexdigest(),
 'checks':['finite admitted recurrence','strict global potential','exact C pulse duration and token/toggle balance','H finite latch bound','source-null and zero-budget bit events','zero refill pointer progress','complete-state stopping','visible projection counterexample','input rejection','parallel evidence hash binding'],
 'scope':'Constructor-team mathematics and separate AI scope audit; no native realization, independent human proof review, registry promotion or empirical score.'}
(P/'RSP1_ROOT_VERIFICATION_v0.1.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))
