"""Independent exact retained-spectrum two-residual budget preview; no fits."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
P=Path(__file__).resolve().parent;R=P.parent/'ud-repo'
SOURCE=Path('captures/2026-10-20T192205Z-codex-partial-factor-ae052f03/primary/CERTIFICATE.json')
def f(x):return F(int(x[0]),int(x[1]))
def pair(x):return [str(x.numerator),str(x.denominator)]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
source=json.loads((R/SOURCE).read_text());rows=[]
for row in source['records']:
 a=f(row['inherited_etaU']);b=f(row['inherited_etaV']);r=f(row['inherited_equation_upper']);s1=f(row['saved_s1']);sq=f(row['saved_s209']);tail=f(row['inherited_tail_upper']);gate=F(1,1<<41)
 gram=s1*(a/(2-a)+b/(2-b))
 cR=(gram+r)/(1-b)
 forward_offdiag=r/(1-b)
 remaining=gate-cR
 adjoint_limit=(1-a)*remaining
 assert 0<=a<1 and 0<=b<1 and r>=0 and remaining>forward_offdiag>0
 # At this closed adjoint cap, e<=remaining, cR+e<=gate and gap remains strict.
 e=max(forward_offdiag,adjoint_limit/(1-a));eps=cR+e
 assert eps==gate and sq-cR>tail+e and sq-eps>0
 rows.append({'case':row['case'],'a':pair(a),'b':pair(b),'forward_residual_upper':pair(r),'s1':pair(s1),'sq':pair(sq),'source_tail_upper':pair(tail),'gram_compression_debit':pair(gram),'forward_compression_error_upper':pair(cR),'forward_offdiagonal_upper':pair(forward_offdiag),'sufficient_closed_adjoint_residual_upper_for_2neg41':pair(adjoint_limit),'maximum_offdiagonal_budget':pair(remaining),'error_at_closed_adjoint_limit':pair(eps),'strict_gap_margin_at_closed_adjoint_limit':pair(sq-cR-tail-e),'ambient_condition_upper_at_closed_limit':pair((s1+eps)/(sq-eps)),'readable':{'forward_compression_error_upper':float(cR),'forward_offdiagonal_upper':float(forward_offdiag),'sufficient_closed_adjoint_residual_upper':float(adjoint_limit),'ambient_condition_upper_at_closed_limit':float((s1+eps)/(sq-eps))}})
out={'status':'EXACT_CONDITIONAL_BUDGET_PREVIEW_NOT_MEASURED_ADJOINT_VALIDATION','repository_source':str(SOURCE),'repository_source_sha256':sha(R/SOURCE),'gate':[1,1<<41],'records':rows,'actual_adjoint_norm_supplied':False,'source_norm_premises_inherited':True,'no_actual_backend_completeness_claim':True,'new_fits':0,'physical_promotion':0}
with (P/'BUDGET_PREVIEW.json').open('x')as z:json.dump(out,z,indent=2);z.write('\n')
print(json.dumps({'status':out['status'],'records':[dict(case=x['case'],**x['readable'])for x in rows]}))
