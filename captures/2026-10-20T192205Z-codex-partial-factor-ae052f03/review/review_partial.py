"""Independent Fraction review of retained thin-factor minmax bounds. No fits."""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json
import numpy as np
HERE=Path(__file__).resolve().parent
BASE=Path('captures/2026-10-20T183427Z-codex-maximal-noise-e5831029')
SOURCE=Path('captures/2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda/phase/primary/CERTIFICATE.json')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p): return json.loads(Path(p).read_text())
def frac(p): return F(int(p[0]),int(p[1]))
def pair(f): return [str(f.numerator),str(f.denominator)]
def dump(p,j):
 with Path(p).open('x') as f: json.dump(j,f,indent=2);f.write('\n')
def main(repo,out):
 freeze=load(HERE/'REVIEW_FREEZE.json')
 assert sha(__file__)==freeze['review_script_sha256']
 for p,h in freeze['repository_source_sha256'].items(): assert sha(repo/p)==h,p
 C=frac(load(repo/SOURCE)['sketch']['per_62_vector_noise_multiplier_upper']);delta=F(3,1<<49)
 rows=[];controls=[]
 def ck(name,b):
  assert b,name
  controls.append({'id':name,'pass':True})
 for case in ('boundary_pair_block','boundary_pair_rotating'):
  cert=load(repo/BASE/'primary'/case/'CERTIFICATE.json');row=cert['row'];meas=row['measured']
  p=repo/BASE/'campaign/cases'/case/'results'/case/'SVD_META.npz'
  ck(case+'_saved_meta_hash_bound',sha(p)==row['saved_witness_set']['SVD_META.npz'])
  with np.load(p,allow_pickle=False) as z:
   # Read only saved singular scalars, never load right_transpose/factors.
   s=[F.from_float(float(v)) for v in z['singular']]
  q=int(row['learned_order']);a=frac(meas['etaU']);b=frac(meas['etaV']);r=frac(meas['xi'])
  sq=s[q-1];s1=s[0];order=load(repo/BASE/'campaign/cases'/case/'inputs/PARENT_ORDER.json')
  tau=frac(order['source_precision_cutoff']);tail=frac(order['qplus1_sigma_upper'])+C*delta
  floor=frac(row['required_singular_floor_lower'])
  ck(case+'_sorted_nonnegative_finite_saved_scalars',s==sorted(s,reverse=True) and min(s)>=0 and len(s)==321)
  ck(case+'_q209',q==209)
  ck(case+'_saved_q_matches_certificate',sq==frac(meas['proposed_smin']))
  ck(case+'_thin_Gram_domains',0<=a<1 and 0<=b<1 and r>=0)
  for k,t in [('left_Gram_F',a),('right_Gram_F',b),('singular_equation_F',r)]:
   ck(case+'_'+k+'_upper_wrapper',t*t>=frac(meas['exact_squared'][k])>=0)
  num=(1-a)*sq-r;ell=num/(1+b);debit=sq-ell
  K=((1+a)*s1+r)/(1-b);cond=K/ell
  ck(case+'_positive_rational_numerator',num>0)
  ck(case+'_debit_identity',debit==(sq*(a+b)+r)/(1+b))
  ck(case+'_debit_nonnegative',debit>=0)
  ck(case+'_debit_below_2neg41',debit<F(1,1<<41))
  ck(case+'_strict_cutoff_separation',0<=tail<tau<ell)
  ck(case+'_actual_q_lower_above_existing_proposed_floor',ell>floor)
  ck(case+'_restricted_condition_below2029',cond<F(2029))
  ck(case+'_condition_upper_at_least_one',cond>=1)
  rows.append({'case':case,'q':q,'inherited_a':pair(a),'inherited_b':pair(b),'inherited_r':pair(r),'saved_s1':pair(s1),'saved_sq':pair(sq),'rational_numerator':pair(num),'actual_sigma_q_lower':pair(ell),'qth_proposal_overstatement_debit_upper':pair(debit),'restricted_sigma_max_upper':pair(K),'restricted_condition_upper':pair(cond),'inherited_sigma_qplus1_upper_after_perturbation':pair(tail),'source_cutoff':pair(tau),'lower_cutoff_margin':pair(ell-tau),'upper_cutoff_margin':pair(tau-tail),'actual_lower_minus_existing_proposed_floor':pair(ell-floor),'readable':{'actual_sigma_q_lower':float(ell),'qth_proposal_overstatement_debit_upper':float(debit),'restricted_sigma_max_upper':float(K),'restricted_condition_upper':float(cond),'tail_upper':float(tail)}})
 # Scalar/rational logical controls, not numerical-backend or raw-data cases.
 def ell(a,b,r,s):return ((1-a)*s-r)/(1+b)
 ck('orthonormal_zero_residual_exact_bound',ell(F(0),F(0),F(0),F(2))==2)
 ck('positive_residual_debits_lower',ell(F(0),F(0),F(1,4),F(2))==F(7,4))
 ck('nonorthogonal_debit_formula',F(2)-ell(F(1,10),F(1,5),F(1,20),F(2))==(F(2)*F(3,10)+F(1,20))/F(6,5))
 ck('numerator_zero_not_positive',((1-F(1,2))*F(2)-F(1))==0)
 ck('gram_a_one_outside_domain',not (0<=F(1)<1))
 ck('gram_b_one_outside_domain',not (0<=F(1)<1))
 ck('cutoff_equality_is_not_strict',not(F(1)>F(1)))
 # Z=diag(5/3,0), U=e1, V=(3/5,4/5), S=[1].
 ck('underestimate_model_right_Gram_exact',F(3,5)**2+F(4,5)**2==1)
 ck('underestimate_model_equation_exact',F(5,3)*F(3,5)==1)
 ck('underestimate_model_actual_rank1',F(5,3)>F(1,2)>F(0))
 ck('underestimate_model_error_positive_despite_zero_debit',F(5,3)-F(1)==F(2,3) and ell(F(0),F(0),F(0),F(1))==1)
 # Z=diag(M,2,1), U=V=[e2,e3], S=diag(2,1).
 # Compression is diag(2,1), whereas leading ambient q=2 condition is M/2.
 M=F(100)
 ck('ambient_condition_countermodel_sorted',M>2>1)
 ck('ambient_condition_exceeds_compression_bound',M/2>2/1)
 ck('ambient_countermodel_exact_cutoff_count2',sum(x>F(3,2) for x in [M,F(2),F(1)])==2)
 ck('ambient_countermodel_saved_q_understates',F(2)>F(1))
 ck('omitted_tail_can_cross_cutoff_without_source_bound',sum(x>F(1,2) for x in [M,F(2),F(1)])==3)
 # Dropping positive-numerator requirement fails to establish any nonzero floor.
 ck('negative_numerator_cannot_certify_positive_floor',ell(F(0),F(0),F(2),F(1))<0)
 result={'status':'PASS_INDEPENDENT_PARTIAL_FACTOR_CONDITIONAL_REVIEW','premise_status':'Saved exact norm certificates, source tail bound, sketch multiplier and noise lineage inherited and hash-bound; no fresh raw/factor validation','rows':rows,'controls':controls,'control_count':len(controls),'countermodels_scope':'Exact low-dimensional logical examples; not actual saved data or a backend bug','cutoff_rank_not_algebraic_rank':True,'all_index_singular_errors_established':False,'ambient_kappa_q_upper_established':False,'uniform_backend_completeness_established':False,'new_fits':0,'new_raw_records':0,'new_factor_copies':0,'external_promotion_review':'PENDING','lane':'development — no registry entry','physical_promotion':0}
 dump(out,result)
 print(json.dumps({'status':result['status'],'controls':len(controls),'rows':[dict(case=x['case'],**x['readable'])for x in rows]}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();main(a.repo,a.out)
