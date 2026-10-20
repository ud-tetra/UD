"""Independent exact table comparisons and conditional phase-formula arithmetic.
Source proof premises remain inherited. No actual backend or raw data is read.
"""
import argparse,hashlib,importlib.util,json
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
J=lambda p:json.loads(Path(p).read_text())
q=lambda p:F(int(p[0]),int(p[1]))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--producer',required=True);ap.add_argument('--result',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();repo=Path(a.repo);producer=Path(a.producer);result=Path(a.result);out=Path(a.out);assert not out.exists();f=J(P/'COMPARISON_FREEZE.json');assert sha(__file__)==f['code_sha256']
 for name,h in f['local_inputs'].items():assert sha(P/name)==h
 for name,h in f['repository_sources'].items():assert sha(repo/name)==h
 pf=J(producer/'FREEZE.json')
 for name,h in pf['local_files'].items():assert sha(producer/name)==h
 for name,h in pf['repository_files'].items():assert sha(repo/name)==h
 theirs=J(result/'CERTIFICATE.json');assert theirs['freeze_sha256']==sha(producer/'FREEZE.json');mine=J(P/'CERTIFICATE.json');grid=J(P/'POLAR_CERTIFICATE.json');pairs=[('strict_rank_error_margin','strict_rank_epsilon_margin'),('largest_sufficient_rank_error_dyadic','largest_sufficient_dyadic_rank_budget'),('sufficient_floor_error_debit','sufficient_absolute_singular_error_for_floor')]
 for own,other in pairs:assert q(theirs[own])==q(mine[other])
 for key,value in [('C','noise_multiplier_upper'),('delta','noise_radius'),('cutoff','cutoff'),('s0','source_s209_lower'),('u0','source_s210_upper')]:assert q(theirs['source_constants'][key])==q(mine[value])
 assert q(theirs['data_singular_enclosures']['s209_lower'])==q(mine['perturbed_s209_lower']);assert q(theirs['data_singular_enclosures']['s210_upper'])==q(mine['perturbed_s210_upper']);assert q(theirs['dyadic_budget_ratio'])==mine['rank_to_floor_dyadic_budget_ratio']
 assert theirs['grid_count']==len(theirs['fullfactor_synthetic_grid'])==54
 for t,m in zip(theirs['fullfactor_synthetic_grid'],grid['rows']):
  assert t['m']==m['m']
  for own,other in [('etaL','etaL'),('etaR','etaR'),('f','full_reconstruction_f'),('rational_singular_error_upper','conservative_singular_error_upper')]:assert q(t[own])==q(m[other])
  assert t['implies_rank_and_floor_if_fullfactor_premises_hold']==m['source_scale_floor_sufficient'];assert t['backend_measured']is False
 # Reuse byte-bound independently implemented arithmetic, not producer derive.py.
 path=repo/'captures/2026-10-20T183427Z-codex-maximal-noise-e5831029/output_review/post_math.py';spec=importlib.util.spec_from_file_location('separate_conditional_phase_math',path);mm=importlib.util.module_from_spec(spec);spec.loader.exec_module(mm);caps=J(producer/'inputs/EQUATION_CAPS.json')['quality_caps'];g={k:caps[k]for k in ['etaU','etaV','xi','sA','rho','h','eV','a']};g['proposed_smin']=mine['source_scale_floor'];old=repo/'captures/2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda/phase';phase=mm.implication(g,mm.aa(mine['noise_multiplier_upper']),J(old/'inputs/PARENT_UNIFORM.json'),J(old/'inputs/PARENT_PHASE.json')['metrics'],J(producer/'inputs/PARENT_ORDER.json'));theirphase=theirs['conditional_phase_at_original_caps'];assert phase['certified']and theirphase['status']=='CERTIFIED_UNIFORM_PHASE_TARGET_BIJECTION';comparisons=[]
 for key,value in phase.items():
  if key=='certified':continue
  # Different algebraic polar expressions may produce one outward-quantum difference.
  difference=abs(q(value)-q(theirphase[key]));assert difference<F(1,1<<170),key;comparisons.append({'field':key,'exact_equal':difference==0,'difference':[str(difference.numerator),str(difference.denominator)]})
 assert theirs['new_estimator_calls']==0 and theirs['new_raw_records']==0 and theirs['factor_copies']==0 and theirs['global_backend_obligations_measured']is False
 controls=J(result/'CONTROLS.json');assert all(row['pass']is True for row in controls['rows']);text=producer.joinpath('THEOREMS.md').read_text();assert 'GENERAL alpha formula'in text and 'does not disprove a hypothetical simplification'in text
 receipt={'status':'PASS_INDEPENDENT_ROOT_BACKEND_BUDGET_AND_CONDITIONAL_ARITHMETIC_REVIEW','producer_freeze_sha256':sha(producer/'FREEZE.json'),'producer_theorems_sha256':sha(producer/'THEOREMS.md'),'producer_certificate_sha256':sha(result/'CERTIFICATE.json'),'producer_controls_sha256':sha(result/'CONTROLS.json'),'comparison_code_sha256':sha(Path(__file__)),'exact_grid_rows_compared':54,'floor_sufficient_illustrative_rows':grid['floor_sufficient_rows'],'rank_sufficient_illustrative_rows':grid['rank_sufficient_rows'],'root_controls_verified':len(controls['rows']),'independent_rank_logical_controls':len(mine['controls']),'conditional_phase_comparisons':comparisons,'conditional_phase_readable_upper':float(q(theirphase['phase_error_upper'])),'source_proof_premises':'Inherited hash-bound, not independently validated; calculation only re-evaluates conditional formula at original caps','new_estimator_calls':0,'new_raw_or_factor_copies':0,'actual_backend_bug_exhibited':False,'universal_backend_success_established':False,'external_review':'PENDING','physical_promotion':0}
 with out.open('x')as ff:json.dump(receipt,ff,indent=2);ff.write('\n')
 print(json.dumps({'status':receipt['status'],'root_controls':len(controls['rows']),'grid':54,'conditional_phase':receipt['conditional_phase_readable_upper']}))
if __name__=='__main__':main()
