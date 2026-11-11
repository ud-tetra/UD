"""Independent mathematical checks of RSP-1; constructor-team AI verification only."""
from pathlib import Path
import hashlib, importlib.util, itertools, json, sys, time

SITE = Path(sys.argv[1] if len(sys.argv)>1 else '/workspace/sites/unified-dynamics-public').resolve()
OUT = Path(sys.argv[2] if len(sys.argv)>2 else '/workspace/scratch/384298a218b5/rsp1-parallel-results.json').resolve()
INPUT_HASHES={name:hashlib.sha256((SITE/name).read_bytes()).hexdigest() for name in ['rsp1.py','response_contract.py']}
sys.path.insert(0, str(SITE))
spec = importlib.util.spec_from_file_location('rsp1_actual', SITE/'rsp1.py')
model = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = model
spec.loader.exec_module(model)

def checksum(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def independent_duration(T,L,q,r,bank,cursor):
    # Count each site's alternating pulse/closure schedule, then serial refill stages.
    site_lengths = [2*amount + occupied for amount, occupied in zip(r,q)]
    source_cleanup = int(any(latent and not intact for latent,intact in zip(L,T)))
    return max(site_lengths+[source_cleanup]) + sum(1+2*max(packet) for packet in bank[cursor:])

start = time.monotonic()
cases = covariance_cases = source_nulls = zero_refills = budget_null_bit_events = 0
max_duration = {'C':0,'H':0}
halt_counts = {'C':{},'H':{}}
perms = list(itertools.permutations(range(3)))

def inspect_case(state, full_covariance=True):
    global cases,covariance_cases,source_nulls,zero_refills,budget_null_bit_events
    result = model.run(state)
    trace = result['trace']
    assert result['committed_updates']==len(trace)
    assert result['terminal']['transition_kind']=='HALT'
    assert result['terminal']['pre_state']==result['terminal']['post_state']
    assert result['physical_promotion']==0
    total_consumed = 0
    for row in trace:
        pre, post, e = row['pre_state'], row['post_state'], row['event']
        assert pre!=post and row['changed']
        assert row['potential_after']<row['potential_before']
        assert e['mu_theta']==e['viable_index']+sum(e['h_prior_aligned'])-sum(e['h_output'])
        assert e['closure_capacity_change']==-2*e['mu_theta']
        assert all(w<=qq<=t for w,qq,t in zip(e['omega_output'],post['q'],post['T']))
        assert row['available_stock_after']<=row['available_stock_before']
        total_consumed+=row['consumed_tokens']
        if row['response_tag']=='RESPONSE_NULL':
            assert e['gross_pair_toggles']==0
            source_nulls+=1
        if e['mu_theta']==0 and e['gross_pair_toggles']>0:
            budget_null_bit_events+=1
        if row['transition_kind']=='RENEWAL_ONLY':
            assert post['cursor']==pre['cursor']+1
            assert post['q']==pre['q']==(0,0,0)
            assert row['consumed_tokens']==0
            assert row['available_stock_after']==row['available_stock_before']
            if post['r']==(0,0,0):zero_refills+=1
    assert total_consumed==result['initial_stock']-result['remaining_stock']
    d=result['committed_updates']
    if state.branch=='C':
        expected=independent_duration(state.T,state.L,state.q,state.r,state.bank,state.cursor)
        assert d==expected==model.close_duration(state)
        assert result['remaining_stock']==0
        assert result['opening_toggles']==result['initial_stock']
        assert result['closure_toggles']==result['initial_stock']+sum(state.q)
        assert result['terminal']['halt_reason']=='EXHAUSTED_QUIESCENT'
    else:
        delta=int(any(l and not t for l,t in zip(state.L,state.T)))
        assert d<=len(state.bank)-state.cursor+2+delta
        # Responses are latched monotonically on the fixed integrity domain.
        assert all(all(a<=b for a,b in zip(row['pre_state']['q'],row['post_state']['q'])) for row in trace)
        assert result['closure_toggles']==0
        assert result['opening_toggles']<=3-sum(state.q)
    max_duration[state.branch]=max(max_duration[state.branch],d)
    why=result['terminal']['halt_reason']
    halt_counts[state.branch][why]=halt_counts[state.branch].get(why,0)+1
    if full_covariance:
        original=model.transition(state)
        for p in perms:
            relabeled=model.transition(model.relabel(state,p))
            assert relabeled['state']==model.relabel(original['state'],p)
            for key in ['transition_kind','response_tag','changed','halt_reason','consumed_tokens','potential_before','potential_after']:
                assert relabeled[key]==original[key]
            for key in ['viable_index','mu_theta','closure_capacity_change','gross_pair_toggles']:
                assert relabeled['event'][key]==original['event'][key]
            for key in ['theta_prior_aligned','omega_prior_aligned','h_prior_aligned','theta_output','q_output','omega_output','h_output','close_mask','reopen_mask']:
                transformed=[0]*3
                for old,current in enumerate(p):transformed[current]=original['event'][key][old]
                assert tuple(transformed)==relabeled['event'][key]
            covariance_cases+=1
    cases+=1
    return result

for T in itertools.product((0,1),repeat=3):
    allowed=[v for v in itertools.product((0,1),repeat=3) if all(x<=t for x,t in zip(v,T))]
    banks=[()]+[(v,) for v in allowed]+list(itertools.product(allowed,repeat=2))
    for L in itertools.product((0,1),repeat=3):
        for q in itertools.product((0,1),repeat=3):
            if any(t*l>x or x>t for t,l,x in zip(T,L,q)):continue
            for r in allowed:
                for bank in banks:
                    for branch in 'CH':inspect_case(model.State(T,L,q,r,bank,0,branch))

adversaries={
 'H_viability_extinction':model.State((1,0,0),(1,0,0),(1,0,0),(0,0,0),branch='H'),
 'C_balanced_swap':model.State((1,1,0),(1,0,0),(1,0,0),(0,1,0),branch='C'),
 'broken_seat_cache_cleanup':model.State((0,0,0),(1,0,0),(0,0,0),(0,0,0),branch='C'),
 'zero_refill_pointer_progress':model.State((1,0,0),(0,0,0),(0,0,0),(0,0,0),((0,0,0),(1,0,0)),branch='C'),
 'H_unspent_bank_stranding':model.State((1,0,0),(0,0,0),(1,0,0),(0,0,0),((1,0,0),),branch='H'),
 'nonzero_cursor_ignores_spent_prefix':model.State((1,0,0),(0,0,0),(0,0,0),(0,0,0),((2,0,0),(1,0,0)),1,'C'),
}
adversary_results={name:inspect_case(state) for name,state in adversaries.items()}
ext=adversary_results['H_viability_extinction']['trace'][0]
assert ext['response_tag']=='RESPONSE_NULL' and ext['event']['viable_index']==1 and ext['event']['mu_theta']==0
assert ext['event']['h_output']==(1,0,0)
assert adversary_results['C_balanced_swap']['trace'][0]['event']['gross_pair_toggles']==2
assert adversary_results['C_balanced_swap']['trace'][0]['event']['mu_theta']==0
assert adversary_results['broken_seat_cache_cleanup']['committed_updates']==1
assert adversary_results['zero_refill_pointer_progress']['committed_updates']==4
assert adversary_results['H_unspent_bank_stranding']['terminal']['halt_reason']=='LATCHED_OR_STRANDED'

assert all(checksum(SITE/name)==digest for name,digest in INPUT_HASHES.items()), 'Checked implementation changed during verification.'
report={
 'status':'PASS','scope':'Constructor-team AI verification; reviewer helped design the model. No independent external review, native-source derivation, empirical execution or registry promotion.',
 'physical_promotion':0,
 'implementation':{'path':str(SITE/'rsp1.py'),'sha256':checksum(SITE/'rsp1.py')},
 'response_contract_sha256':checksum(SITE/'response_contract.py'),
 'checker_sha256':checksum(__file__),
 'exhaustive_initial_states':cases-len(adversaries),
 'targeted_adversarial_states':len(adversaries),
 'relabel_covariance_comparisons':covariance_cases,
 'domain':'All admitted binary T,L,q; r entries0..1 supported on T; bank lengths0..2 with binary packets supported on T; exhaustive cursor0 plus targeted nonzero cursor.',
 'checks':['C exact duration independently counted from pulse schedules and refill stages','H duration upper bound','full-state fixed-point stopping','resource conservation on refills and nonincrease on inspections','token/toggle balance','idle-corrected index','no-bit source/cache changes committed','zero-budget gross bit swaps committed','zero refill cursor advances','H stock/queue stranding','pair relabel covariance of state, event masks and scalar receipts'],
 'observed':{'max_committed_updates':max_duration,'halt_reasons':halt_counts,'committed_response_nulls':source_nulls,'zero_refill_updates':zero_refills,'zero_budget_nonzero_toggle_updates':budget_null_bit_events},
 'adversarial_traces':adversary_results,
 'elapsed_seconds':round(time.monotonic()-start,3)
}
OUT.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['adversarial_traces','checks','observed']},indent=2))
print('Result SHA256: '+checksum(OUT))
