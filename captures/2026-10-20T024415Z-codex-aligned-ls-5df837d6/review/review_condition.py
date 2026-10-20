"""Independent 82-row extra-sketch conditional aligned-phase/rank/lattice audit."""
import argparse,hashlib,importlib.util,json
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
OLD='captures/2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda/phase';BASE='captures/2026-10-20T002112Z-codex-actual-equation-returns-c0caa77d';EQ='captures/2026-10-19T230959Z-codex-quality-equation-intake-a735ce68/equation'
SHA=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();R=lambda p:json.loads(Path(p).read_text());q=lambda p:F(int(p[0]),int(p[1]))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--root-package',required=True);ap.add_argument('--primary',required=True);ap.add_argument('--release',required=True);args=ap.parse_args();repo=Path(args.repo);root=Path(args.root_package);primary=Path(args.primary);f=R(P/'CONDITION_DRIVER_FREEZE.json');assert SHA(__file__)==f['driver_sha256']and SHA(P/'review_math.py')==f['math_sha256'];assert SHA(root/'FREEZE.json')==f['root_freeze_sha256'];assert R(args.release)['conditioning_execution_released']is True
 for name,h in R(root/'FREEZE.json')['files'].items():assert SHA(root/name)==h
 for row in R(root/'SOURCE_BINDINGS.json')['pins']:assert SHA(repo/row['path'])==row['sha256']
 sp=importlib.util.spec_from_file_location('independent_aligned_math',P/'review_math.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);u=R(repo/OLD/'inputs/PARENT_UNIFORM.json');phase=R(repo/OLD/'inputs/PARENT_PHASE.json')['metrics'];order=R(repo/BASE/'estimator/inputs/PARENT_ORDER.json');C=q(R(repo/OLD/'primary/CERTIFICATE.json')['sketch']['per_62_vector_noise_multiplier_upper']);caps=R(repo/EQ/'FREEZE.json')['quality_caps'];cert=R(primary/'CERTIFICATE.json');c={k:q(v)for k,v in caps.items()};c.update(C=C,r=q(u['baseline_low_rank_residual_upper']),s0=q(order['qth_sigma_lower']),tail0=min(q(order['qplus1_sigma_upper']),q(u['baseline_low_rank_residual_upper'])),cutoff=q(order['source_precision_cutoff']),beta=q(u['deleted_two_rows_beta_lower']),lag0=q(u['comparison_shift_residual_upper']),M0=q(u['comparison_shift_norm_upper']),eta0=q(phase['basis_orthogonality_upper']),hD0=q(phase['source_inverse_norm_upper']),rhoD=q(phase['source_inverse_residual_upper']),dD=q(phase['source_reduction_norm_upper']),LJ=q(phase['intertwining_residual_upper']),sep=q(phase['minimum_target_chord_lower']),delta0=F(3,1<<49),quantum=F(1,1<<48));assert {k:q(v)for k,v in cert['constants'].items()}==c
 assert [row['grid_k']for row in cert['rows']]==[None]+list(range(20,101));passed=[];counts={}
 for row in cert['rows']:
  k=row['grid_k'];z=F(0)if k is None else F(1,1<<k);assert q(row['additional_sketch_radius'])==z;noise=C*c['delta0']+z;floor=c['s0']-noise-c['singular_floor_debit'];lower=c['s0']-noise;tail=c['tail0']+noise;margin=min(lower-c['cutoff'],c['cutoff']-tail);nu=z/C;total=c['delta0']+nu
  for key,value in [('future_proposed_singular_floor_required',floor),('additional_raw_radius_conditional_on_projection',nu),('total_raw_radius',total),('exact_data_singular_q_lower',lower),('exact_data_singular_qplus1_upper',tail)]:assert q(row[key])==value
  assert row['additional_encoded_ball_only_zero']==(nu<c['quantum']);assert row['total_encoded_local_patternset_unchanged']==(2*c['quantum']**2<=total**2<3*c['quantum']**2);assert row['exact_order_209_at_cutoff']==(margin>0);assert (row['required_computed_singular_error_strictly_below']is None)==(margin<=0)
  if margin>0:assert q(row['required_computed_singular_error_strictly_below'])==margin
  own=m.phase(m.aa(z),caps,m.aa(C),u,phase,order)
  mapping={'offspan_sine_upper':'projector_distance_upper','polar_distance_upper':'Procrustes_distance_upper','shift_distance_upper':'aligned_shift_distance_upper','eigenvalue_radius_upper':'target_disk_radius_upper','phase_error_upper':'phase_error_upper','phase_matching_margin_lower':'matching_margin_lower'}
  for a,b in mapping.items():
   assert(a in own)==(b in row)
   if a in own:assert abs(m.aa(own[a])-m.aa(row[b]))<m.aa([1,1<<170]),b
  if floor<=0:expected='HOLD_POSITIVE_PROPOSED_FLOOR'
  elif own['status']=='HOLD_SUBSPACE_GAP':expected='HOLD_PROJECTOR_GAP'
  elif own['status']=='HOLD_DELETED_ROW_MARGIN':expected='HOLD_DELETED_ROW_MARGIN'
  elif 'phase_error_upper'not in own:expected='HOLD_DISK_ORIGIN'
  else:expected='CERTIFIED_CONDITIONAL_GAUGE_ALIGNED_REGION'if margin>0 and own['status']=='CERTIFIED_UNIFORM_PHASE_TARGET_BIJECTION'else'HOLD_SOURCE_OR_PHASE_MARGIN'
  assert row['status']==expected
  if 'shift_distance_upper'in own:
   e=m.aa(c['r']+noise);t=(e*(1+m.aa(c['etaV'])).sqrt()+m.aa(c['xi']))/(m.aa(floor)*(1-m.aa(c['etaU'])).sqrt());d=t*(2/(1+(1-t*t).sqrt())).sqrt();beta=m.aa(c['beta']);ls=(d*(beta-d)*(1+1/beta)+d*m.aa(c['lag0']))/(beta-d)**2
   extras={'exact_aligned_LS_map_change_upper':m.up(ls),'reference_exact_LS_to_comparison_upper':m.up(m.aa(c['lag0'])/beta),'unpolarized_deleted_basis_sigma_lower':m.down((1-m.aa(c['etaU'])).sqrt()*(beta-d)),'polar_similarity_condition_upper':m.up(((1+m.aa(c['etaU']))/(1-m.aa(c['etaU']))).sqrt()),'source_half_chord_lower':m.down(m.aa(c['sep'])/2)}
   for key,value in extras.items():assert abs(m.aa(value)-m.aa(row[key]))<m.aa([1,1<<170]),key
  if k is not None and expected=='CERTIFIED_CONDITIONAL_GAUGE_ALIGNED_REGION':passed.append(k)
  counts[expected]=counts.get(expected,0)+1
 chosen=cert['largest_positive_grid_certified'];assert(chosen is None)==(not passed)
 if passed:assert chosen==cert['rows'][min(passed)-19]
 target=P/'CONDITION_REVIEW_RECEIPT.json';assert not target.exists();target.write_text(json.dumps({'status':'PASS_INDEPENDENT_82_ROW_CONDITIONAL_ALIGNED_REGION_AUDIT','source_certificate_sha256':SHA(primary/'CERTIFICATE.json'),'freeze_sha256':SHA(P/'CONDITION_DRIVER_FREEZE.json'),'rows_checked':82,'source_constants_exactly_match':True,'conditional_phase_and_exact_LS_map_bounds_checked':True,'rank_cutoff_margin_and_lattice_flags_checked':True,'status_counts':counts,'selected_k':min(passed)if passed else None,'selected_additional_encoded_ball_only_zero':None if chosen is None else chosen['additional_encoded_ball_only_zero'],'selected_total_patternset_unchanged':None if chosen is None else chosen['total_encoded_local_patternset_unchanged'],'scope':'Hypothetical future outputs must satisfy unchanged measured numerical/encoding hypotheses; no all-input solver success, transfer into fixed-gauge box, or nonzero encoded extra record follows','new_estimator_calls':0,'new_raw_or_factor_copies':0,'source_H_fullfactor_proofs':'Inherited hash-bound, not recomputed','old_top2_Frobenius_HOLD_immutable':True,'external_review':'PENDING','physical_promotion':0},indent=2)+'\n');print(json.dumps({'status':'PASS','rows':82,'selected_k':min(passed)if passed else None,'counts':counts}))
if __name__=='__main__':main()
