"""Exact backend-error budgets plus conditional source phase implication; zero fits."""
import argparse,json,hashlib,importlib.util
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
pair=lambda x:[str(x.numerator),str(x.denominator)]
Q=lambda x:F(int(x[0]),int(x[1]))
def new(path,obj):
 with path.open('x')as f:json.dump(obj,f,indent=2);f.write('\n')
def bound(repo):
 f=json.loads((P/'FREEZE.json').read_text())
 for n,h in f['local_files'].items():assert sha(P/n)==h,n
 for n,h in f['repository_files'].items():assert sha(repo/n)==h,n
 return f

def controls():
 rows=[]
 def ck(name,condition):assert condition,name;rows.append({'id':name,'pass':True})
 L,U,tau=F(3),F(1),F(2);b=min(L-tau,tau-U)
 ck('rank_strict_interior',L-F(1,2)>tau and U+F(1,2)<tau)
 ck('cutoff_equality_is_not_admission',U+b==tau and not U+b<tau)
 debit=F(1,16);eps=F(1,2);proposal=L-eps
 ck('rank_count_alone_does_not_imply_floor',proposal>tau and proposal<L-debit)
 ck('closed_floor_debit_boundary',L-debit>=L-debit)
 ck('zero_frames_equation_can_vanish',F(3)*0-0*3==0 and abs(0*0-1)>F(1,16))
 ck('wrong_orthonormal_direction_breaks_equation',abs(F(1)-F(3))>F(1,16))
 ck('exact_factors_do_not_bound_arbitrary_shift',abs(F(1)*1-F(0))>F(1,16))
 eta=F(11,25);dev=F(1,5);norm=F(6,5);m=F(2);actual=F(22,25)
 ck('scalar_fullfactor_reconstruction_zero',F(72,25)-norm*m*norm==0)
 ck('scalar_Gram_defects',norm*norm-1==eta and eta<1)
 ck('fullfactor_cross_factor_required',m*(dev*norm+dev)==actual and m*(dev+dev)<actual)
 ck('conservative_rational_envelope',m*(eta*(1+eta)+eta)>=actual)
 # Exhaustive finite logical example, not a model of the actual floating program.
 D=range(7);S={0,1,2,3,4};good=lambda x:True;bad=lambda x:x!=5
 ck('finite_tests_match',all(good(x)==bad(x)for x in S))
 ck('universal_results_differ',all(good(x)for x in D)and not all(bad(x)for x in D))
 ck('retained_equation_does_not_charge_tail',3*1-1*3==0 and F(1)>0)
 ck('no_truth_from_PASS_string',bool('PASS')and ('PASS'!='VALIDATED_ACTUAL_ARITHMETIC'))
 return rows

def run(repo,out):
 f=bound(repo);out.mkdir(parents=True,exist_ok=False);o=json.loads((P/'inputs/PARENT_ORDER.json').read_text());phase=json.loads((P/'inputs/SOURCE_PHASE_CERTIFICATE.json').read_text());caps=json.loads((P/'inputs/EQUATION_CAPS.json').read_text())['quality_caps'];C=Q(phase['sketch']['per_62_vector_noise_multiplier_upper']);delta=F(3,1<<49);tau=F(1,1<<24);s0=Q(o['qth_sigma_lower']);u0=Q(o['qplus1_sigma_upper']);e=C*delta;L=s0-e;U=u0+e;b=min(L-tau,tau-U);debit=Q(caps['singular_floor_debit']);assert 0<U<tau<L and 0<debit<b
 ks=[k for k in range(100)if F(1,1<<k)<b];k=min(ks);assert k==25 and F(1,1<<(k-1))>=b;grid=[]
 for m in[1,8,128]:
  for keta in[40,43,46,49,50,52]:
   for kf in[40,44,48]:
    eta=F(1,1<<keta);ff=F(1,1<<kf);E=ff+m*(eta*(1+eta)+eta);grid.append({'m':m,'etaL':pair(eta),'etaR':pair(eta),'f':pair(ff),'rational_singular_error_upper':pair(E),'implies_rank_and_floor_if_fullfactor_premises_hold':E<=debit,'backend_measured':False})
 path=repo/'captures/2026-10-19T230959Z-codex-quality-equation-intake-a735ce68/equation/certify.py';spec=importlib.util.spec_from_file_location('conditional_only_phase_source',path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);_,arithmetic=module.bound(repo);conditional=module.evaluate(repo,arithmetic,arithmetic.aa(pair(C)),[3,1<<49]);assert conditional['status']=='CERTIFIED_UNIFORM_PHASE_TARGET_BIJECTION'
 result={'status':'DERIVED_CONDITIONAL_BACKEND_OBLIGATIONS_NOT_ACTUAL_CONFORMANCE','freeze_sha256':sha(P/'FREEZE.json'),'source_constants':{'C':pair(C),'delta':pair(delta),'cutoff':pair(tau),'s0':pair(s0),'u0':pair(u0)},'data_singular_enclosures':{'s209_lower':pair(L),'s210_upper':pair(U)},'strict_rank_error_margin':pair(b),'largest_sufficient_rank_error_dyadic':pair(F(1,1<<k)),'sufficient_floor_error_debit':pair(debit),'dyadic_budget_ratio':pair(F(1,1<<k)/debit),'readable':{'strict_rank_error_margin':float(b),'floor_debit':float(debit),'source_floor':float(L-debit)},'fullfactor_synthetic_grid':grid,'grid_count':len(grid),'conditional_phase_at_original_caps':conditional,'conditional_scope':'For all actual tuples satisfying measured gates and inherited premises; not forall actual backend inputs','global_backend_obligations_measured':False,'complete_left321_columns_available_in_PR279':False,'new_estimator_calls':0,'new_raw_records':0,'factor_copies':0,'old_verdicts_changed':False,'physical_promotion':0,'external_promotion_review':'PENDING'}
 new(out/'CERTIFICATE.json',result);new(out/'CONTROLS.json',{'status':'PASS_EXACT_LOGICAL_AND_RATIONAL_CONTROLS','rows':controls(),'new_estimator_calls':0});bound(repo);print(json.dumps({'status':result['status'],'rank_error_margin':float(b),'rank_dyadic':[1,1<<k],'floor_debit':float(debit),'grid_rows':len(grid),'phase_conditional_bound':conditional.get('readable_phase_error_upper')}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--out',required=True);args=p.parse_args();run(Path(args.repo).resolve(),Path(args.out).resolve())
