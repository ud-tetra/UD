"""Exact four-state source audit of Q156 product-gated UD expressions."""
from fractions import Fraction as F
from pathlib import Path
import json

states = [(c, t) for c in (0, 1) for t in (0, 1)]
def h(state): return state[0] * state[1]
def q156(state): return h(state)  # one addressed boundary edge
def q162(state): return -F(1, 4) * h(state)  # declared unit gradient
def q164(state): return F(1, 4) * h(state)  # declared unit normalized difference
def q167(state): return 2 * h(state)  # declared unit oriented amplitude product
def source_signature(state): return (q156(state), q162(state), q164(state), q167(state))
def set_closure(state): return (1, state[1])
def set_transport(state): return (state[0], 1)

checks = {}
def check(name, condition):
    checks[name] = bool(condition)
    assert condition, name

check('four_boolean_factor_states', len(states) == 4)
check('hard_mask_one_iff_both_factors_one', [h(s) for s in states] == [0, 0, 0, 1])
check('three_closed_states_same_product_gated_signature',
      len({source_signature(s) for s in states if h(s) == 0}) == 1)
check('open_state_signature_distinct', source_signature((1, 1)) != source_signature((0, 0)))
check('Q162_unit_gradient_evaluates_quarter_h', [str(q162(s)) for s in states] == ['0','0','0','-1/4'])
check('Q164_unit_difference_evaluates_quarter_h', [str(q164(s)) for s in states] == ['0','0','0','1/4'])
check('Q167_unit_product_evaluates_two_h', [q167(s) for s in states] == [0,0,0,2])
check('closure_set_changes_mask_only_with_transport_one',
      [h(set_closure(s)) for s in states] == [0,1,0,1])
check('transport_set_changes_mask_only_with_closure_one',
      [h(set_transport(s)) for s in states] == [0,0,1,1])
response = [(h(s),h(set_closure(s)),h(set_transport(s))) for s in states]
check('two_diagnostic_intervention_responses_separate_all_states',len(set(response)) == 4)
check('source_signature_cannot_predict_closure_set',
      source_signature((0,0)) == source_signature((0,1)) and
      h(set_closure((0,0))) != h(set_closure((0,1))))
check('source_signature_cannot_predict_transport_set',
      source_signature((0,0)) == source_signature((1,0)) and
      h(set_transport((0,0))) != h(set_transport((1,0))))

rows = []
for s, future in zip(states,response):
    rows.append({'C':s[0], 'T':s[1], 'h':h(s),
                 'Q162_unit_gradient':str(q162(s)),
                 'Q164_unit_difference':str(q164(s)),
                 'Q167_unit_product':str(q167(s)),
                 'diagnostic_h_after_set_C':future[1],
                 'diagnostic_h_after_set_T':future[2]})
out = {
 'claim_class':'EXACT finite Boolean audit of sourced product-gated expressions; interventions diagnostic only; predictive transition OPEN',
 'source_ids':['Q156','Q158','Q160','Q162','Q164','Q167','Q173'],
 'normalizations':'Q156 one addressed boundary edge; Q162 gradient=1; Q164 difference=1; Q167 D*x*y=1; Q173 face mask held fixed',
 'states':rows,'source_observation_partition':{'closed':[[0,0],[0,1],[1,0]],'open':[[1,1]]},
 'diagnostic_interventions':'set_C and set_T are hypothetical counterfactuals, not UD-admitted events',
 'checks':checks,'passed':sum(checks.values()),'physical_promotion':0,
 'lane':'development — no registry entry; non-constructor review pending'
}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'passed':out['passed'],'states':len(rows),'partition':[3,1]}))
