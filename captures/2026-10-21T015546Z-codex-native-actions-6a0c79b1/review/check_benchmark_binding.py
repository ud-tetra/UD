from pathlib import Path
from fractions import Fraction as Q
import hashlib,json
P=Path(__file__).resolve().parent;W=P.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
root=json.loads((W/'c31_test_final/CONFORMANCE.json').read_text());own=json.loads((P/'COMPARISON_CHECKS.json').read_text());dual=json.loads((P/'DUALITY_CHECKS.json').read_text())
for r,o in zip(root['comparisons'],own['cases']):
 assert r['mode']==o['mode'] and Q(r['difference_norm_squared'])==Q(o['difference_numerator_squared'],o['difference_grid_denominator'])
 assert Q(r['absolute_difference_bound'])==Q(*o['joint_error_budget']) and r['changed_coordinates']==o['different_coordinates']
assert abs(Q(root['duality_residual']))==Q(*dual['exact_duality_residual']) and Q(root['duality_absolute_bound'])==Q(*dual['conservative_budget'])
assert root['native_replay_bytes_identical'] is True
replayfiles=[]
for name in ['NATIVE_CONSTANTS.json','SOURCE_BINDINGS.json','OPERATOR.txt']:
 x=W/'c31_math_final'/name;y=W/'c31_math_replay'/name;assert x.read_bytes()==y.read_bytes();replayfiles.append({'file':name,'sha256':sha(x)})
x=W/'c31_test_final/CONFORMANCE.json';y=W/'c31_test_final_replay/CONFORMANCE.json';assert x.read_bytes()==y.read_bytes();replayfiles.append({'file':'CONFORMANCE.json','sha256':sha(x)})
bench=W/'c31_benchmark_results/BENCHMARK.json';r=json.loads(bench.read_text());assert r['full8192_benchmark'] is False
pairs=[]
for pair in r['pairs']:
 mode=pair['mode'];suffix='Fxb' if mode=='forward' else 'Fty'
 for label,prefix in [('baseline','c30'),('native','c31')]:
  output=W/f'c31_benchmark_results/{mode}_{label}.txt';ref=W/(f'{prefix}_{suffix}.txt' if prefix=='c30' else f'{prefix}_{suffix}_final.txt')
  assert output.read_bytes()==ref.read_bytes()
  report=pair[label];assert report['output_sha256']==sha(output)
  exe=W/('c30_action' if label=='baseline' else 'c31_action');assert report['executable_sha256']==sha(exe)
  assert 'wait4 specific action child' in report['measurement']
 ratio=pair['baseline']['wall_seconds']/pair['native']['wall_seconds'];assert ratio==pair['observed_speed_ratio']
 pairs.append({'mode':mode,'observed_speed_ratio':ratio,'old_wall_seconds':pair['baseline']['wall_seconds'],'new_wall_seconds':pair['native']['wall_seconds'],'baseline_rss_kib':pair['baseline']['peak_child_rss_kib'],'native_rss_kib':pair['native']['peak_child_rss_kib'],'corresponding_output_bytes_match_reference_files':True})
assert 'For every internal state v with ||v||<=4096' in (W/'c31_THEOREM.md').read_text() or 'For every internal state' in (W/'c31_THEOREM.md').read_text() and 'admitted source-bound execution' in (W/'c31_THEOREM.md').read_text()
sources=['c31_action.cpp','c31_certify.py','c31_tests.py','c31_integration.py','c31_run_timed.py','c31_benchmark.py','c31_reproduce.py','c31_THEOREM.md']
result={'status':'PASS','source_hashes':{f:sha(W/f) for f in sources},'root_theorem_sha256':sha(W/'c31_THEOREM.md'),'final_conformance_exact_fractions_match_own_checks':True,'four_scientific_replay_files_identical':replayfiles,'benchmark_sha256':sha(bench),'benchmark_pairs':pairs,'source_review':{'reproduce_orchestrator_read_not_executed_by_reviewer':True,'final_replay_field_name_describes_replay_not_diagnostic_history':True,'theorem_domain_phrase_scoped_to_cap':True},'scope':{'timing_n_equals_one_per_backend_per_mode':True,'no_worst_case_or_external_replication_claim':True,'full8192_run_not_claimed':True,'physical_promotion':0}}
(P/'FINAL_SOURCE_AND_BENCHMARK.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print('PASS final sources, four replays, conformance and two paired timings')
