"""Independent exact-rational conditional backend obligations; no fits or data copies."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent
ORDER='captures/2026-10-20T183427Z-codex-maximal-noise-e5831029/campaign/cases/boundary_pair_block/inputs/PARENT_ORDER.json'
CAPS='captures/2026-10-20T183427Z-codex-maximal-noise-e5831029/campaign/cases/boundary_pair_block/inputs/EQUATION_CAPS.json'
SOURCE='captures/2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda/phase/primary/CERTIFICATE.json'
THEOREM='captures/2026-10-19T230959Z-codex-quality-equation-intake-a735ce68/equation/THEOREMS_v0.2.md'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
read=lambda p:json.loads(Path(p).read_text())
q=lambda p:F(int(p[0]),int(p[1]))
pair=lambda p:[str(p.numerator),str(p.denominator)]
def derive(repo):
 f=read(P/'REVIEW_FREEZE.json')
 assert sha(__file__)==f['code_sha256']
 for path,h in f['repository_sources'].items():assert sha(repo/path)==h
 order=read(repo/ORDER);caps=read(repo/CAPS)['quality_caps'];C=q(read(repo/SOURCE)['sketch']['per_62_vector_noise_multiplier_upper']);delta=F(3,1<<49);debit=q(caps['singular_floor_debit']);tau=q(order['source_precision_cutoff']);s0=q(order['qth_sigma_lower']);u0=q(order['qplus1_sigma_upper']);L=s0-C*delta;U=u0+C*delta;lower=L-tau;upper=tau-U;margin=min(lower,upper);assert 0<U<tau<L and 0<debit<margin
 checks=[]
 def ck(name,value):
  assert value,name;checks.append({'id':name,'pass':True})
 rank_ok=lambda eps:0<=eps<margin
 floor_ok=lambda eps:0<=eps<=debit
 ck('rank_budget_2neg25_qualifies',rank_ok(F(1,1<<25)))
 ck('rank_budget_2neg24_does_not_qualify',not rank_ok(F(1,1<<24)))
 ck('rank_budget_negative_refused',not rank_ok(F(-1,1<<50)))
 ck('rank_strict_margin_equality_refused',not rank_ok(margin))
 ck('required_floor_budget_at2neg41',debit==F(1,1<<41)and floor_ok(debit))
 ck('required_floor_budget_above_refused',not floor_ok(2*debit))
 ck('floor_budget_implies_strict_rank_budget',rank_ok(debit))
 ck('dyadic_rank_budget65536times_floor_budget',F(1,1<<25)/debit==65536)
 # A bound-premise countermodel only: this is NOT an actual raw record or SciPy output.
 eps=F(1,1<<25);sigmas=[L]*209+[F(0)]*112;returned=[x-eps for x in sigmas[:209]]+[F(0)]*112
 ck('scalar_countermodel_max_error_budget',max(abs(a-b)for a,b in zip(sigmas,returned))<=eps)
 ck('scalar_countermodel_sorted_nonnegative',returned==sorted(returned,reverse=True)and min(returned)>=0)
 ck('scalar_countermodel_rank209',sum(x>tau for x in returned)==209)
 ck('scalar_countermodel_source_floor_fails',returned[208]<L-debit)
 # At the upper strict margin, a tail value can equal cutoff; strict count stays209,
 # but the saved-rank admission policy excludes equality.
 ck('upper_margin_exact_tail_cutoff',U+upper==tau)
 ck('equality_HOLD_distinct_from_incorrect_count',sum(x>tau for x in [L]*209+[tau]+[F(0)]*111)==209)
 ck('larger_tail_error_can_create_rank210',sum(x>tau for x in [L]*209+[U+F(1,1<<24)]+[F(0)]*111)==210)
 # Correct singular values do not constrain proposed vectors: Uhat=0 violates Gram.
 ck('rank_does_not_imply_left_Gram',F(1)>q(caps['etaU']))
 # Finite blackbox countermodel. The altered function is not the fixed SciPy code.
 domain=tuple(range(4));tested=(0,1);good=lambda x:'PASS';bad=lambda x:'HOLD'if x==2 else'PASS'
 ck('finite_countermodel_agrees_on_all_tests',all(good(x)==bad(x)for x in tested))
 ck('finite_countermodel_disagrees_on_untested',2 in domain and 2 not in tested and good(2)!=bad(2))
 out={'status':'PASS_EXACT_CONDITIONAL_UNIVERSAL_RANK_AND_FLOOR_OBLIGATIONS','source_scope':'Inherited source singular bounds and sketch perturbation multiplier, not rederived; no actual solver error bound established','source_rank':209,'returned_array_length':321,'cutoff':pair(tau),'noise_radius':pair(delta),'noise_multiplier_upper':pair(C),'source_s209_lower':pair(s0),'source_s210_upper':pair(u0),'perturbed_s209_lower':pair(L),'perturbed_s210_upper':pair(U),'lower_cutoff_margin':pair(lower),'upper_cutoff_margin':pair(upper),'strict_rank_epsilon_margin':pair(margin),'largest_sufficient_dyadic_rank_budget':[1,1<<25],'source_scale_floor':pair(L-debit),'sufficient_absolute_singular_error_for_floor':pair(debit),'rank_to_floor_dyadic_budget_ratio':65536,'scalar_rank_floor_countermodel':{'scope':'Bound-premise scalar model only; not an actual profile raw or fixed backend output','error_budget':pair(eps),'returned_s209':pair(returned[208]),'required_floor':pair(L-debit),'rank':209,'floor_satisfied':False},'finite_blackbox_countermodel':{'scope':'Logical non-entailment from finite tests; altered function is not actual implementation','domain':[0,1,2,3],'tested':[0,1],'untested_counterpoint':2,'actual_implementation_bug_exhibited':False},'new_estimator_calls':0,'new_raw_records':0,'new_factor_copies':0,'backend_success_established':False,'all14gates_established_by_rank':False,'independent_physical_freshness':False,'external_review':'PENDING','physical_promotion':0,'controls':checks}
 return out
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();out=Path(a.out);assert not out.exists();value=derive(Path(a.repo));out.parent.mkdir(parents=True,exist_ok=True)
 with out.open('x')as f:json.dump(value,f,indent=2);f.write('\n')
 print(json.dumps({'status':value['status'],'controls':len(value['controls']),'strict_rank_margin_approx':float(q(value['strict_rank_epsilon_margin'])),'largest_rank_dyad':value['largest_sufficient_dyadic_rank_budget'],'floor_epsilon':value['sufficient_absolute_singular_error_for_floor']}))
