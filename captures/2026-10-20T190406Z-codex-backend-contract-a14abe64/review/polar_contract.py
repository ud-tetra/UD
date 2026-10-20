"""Exact conservative complete-factor obligations and cross-term countermodel.
Synthetic illustrative inputs only; no floating backend/factor data read.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
P=Path(__file__).resolve().parent
q=lambda p:F(int(p[0]),int(p[1]))
pair=lambda p:[str(p.numerator),str(p.denominator)]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
f=json.loads((P/'POLAR_REVIEW_FREEZE.json').read_text());assert sha(__file__)==f['code_sha256']
for name,h in f['local_inputs'].items():assert sha(P/name)==h
prior=json.loads((P/'CERTIFICATE.json').read_text());mu=q(prior['strict_rank_epsilon_margin']);debit=q(prior['sufficient_absolute_singular_error_for_floor']);rows=[]
for m in [1,8,128]:
 for eb in [40,43,46,49,50,52]:
  eta=F(1,1<<eb)
  for fb in [40,44,48]:
   residual=F(1,1<<fb);budget=residual+m*(eta*(1+eta)+eta);rank=budget<mu;floor=budget<=debit;assert not floor or rank
   rows.append({'m':m,'etaL':pair(eta),'etaR':pair(eta),'full_reconstruction_f':pair(residual),'conservative_singular_error_upper':pair(budget),'strict_rank_sufficient':rank,'source_scale_floor_sufficient':floor,'actual_backend_or_measured_factor':False})
assert len(rows)==54
# Generic polar-correction bound alphaL/alphaR, distinct from d(eta) function envelope.
alphaL=alphaR=F(1,5);right_norm=F(6,5);m=F(2);left=right=F(6,5);s=F(2);z=left*s*right;actual=abs(z-s);full=m*(alphaL*right_norm+alphaR);missing=m*(alphaL+alphaR)
assert actual==full==F(22,25) and missing==F(4,5)<actual
assert left*left-1==right*right-1==F(11,25)
# At eta=11/25 the generic alpha=1/5 is not d(eta)=1-sqrt(14)/5.
assert (1-alphaL)**2==F(16,25)!=1-F(11,25)
controls=[{'id':'generic_cross_factor_required_with_exact_polar_corrections','pass':True},{'id':'generic_exact_alpha_distinct_from_d_of_eta','pass':True},{'id':'floor_sufficient_rows_also_rank_sufficient','pass':True},{'id':'all54illustrative_rows_unmeasured','pass':all(not x['actual_backend_or_measured_factor']for x in rows)}]
out={'status':'PASS_INDEPENDENT_SYNTHETIC_COMPLETE_FACTOR_ENVELOPE','rows':rows,'row_count':len(rows),'rank_sufficient_rows':sum(r['strict_rank_sufficient']for r in rows),'floor_sufficient_rows':sum(r['source_scale_floor_sufficient']for r in rows),'formula':'f + m*(etaL*(1+etaR)+etaR), etaL,etaR in[0,1), m,f>=0','scope':'Sufficient conditional bounds on COMPLETE-factor inputs. No actual factor, complete reconstruction or uniform backend/error theorem established. Illustrative grid values are not new caps.','cross_term_countermodel':{'U':pair(left),'V':pair(right),'s':pair(s),'Z':pair(z),'exact_full_reconstruction_residual':pair(F(0)),'actual_singular_error':pair(actual),'etaL_etaR':pair(F(11,25)),'actual_polar_corrections_alphaL_alphaR':pair(alphaL),'right_polar_norm':pair(right_norm),'complete_generic_polar_bound':pair(full),'incorrect_generic_bound_without_right_norm':pair(missing),'scope':'Counterexample uses exact polar-correction norms alpha=1/5, not the conservative d(eta)=1-sqrt(1-eta) function. It does not refute the different d(eta)-only formula.'},'controls':controls,'new_estimator_calls':0,'new_raw_or_factor_copies':0,'actual_backend_bug_exhibited':False,'external_review':'PENDING','physical_promotion':0}
with(P/'POLAR_CERTIFICATE.json').open('x')as g:json.dump(out,g,indent=2);g.write('\n')
print(json.dumps({'status':out['status'],'rows':len(rows),'rank_sufficient':out['rank_sufficient_rows'],'floor_sufficient':out['floor_sufficient_rows']}))
