"""Independent Fraction prefix-minmax one-sided bound; never fits or loads vectors."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
import numpy as np
P=Path(__file__).resolve().parent;R=P.parent/'ud-repo'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def f(p):return F(int(p[0]),int(p[1]))
def pair(v):return [str(v.numerator),str(v.denominator)]
freeze=read(P/'REVIEW_FREEZE.json')
for p,h in freeze['repository_source_sha256'].items():assert sha(R/p)==h
controls=[];records=[]
def ck(n,b):
 assert b,n
 controls.append({'id':n,'pass':True})
for row in read(P/'CERTIFICATE.json')['rows']:
 name=row['case'];a=f(row['inherited_a']);b=f(row['inherited_b']);r=f(row['inherited_r']);q=row['q']
 path=R/'captures/2026-10-20T183427Z-codex-maximal-noise-e5831029/campaign/cases'/name/'results'/name/'SVD_META.npz'
 with np.load(path,allow_pickle=False)as z:s=[F.from_float(float(x))for x in z['singular']]
 lower=[((1-a)*v-r)/(1+b) for v in s[:q]]
 debits=[v-lo for v,lo in zip(s[:q],lower)]
 ck(name+'_all209_positive_prefix_numerators',all(v>0 for v in lower))
 ck(name+'_all209_debit_identities',all(d==(v*(a+b)+r)/(1+b)for v,d in zip(s[:q],debits)))
 ck(name+'_all209_debits_nonnegative',min(debits)>=0)
 ck(name+'_all209_debits_bounded_by_first',max(debits)==debits[0])
 ck(name+'_all112_tail_proposals_bounded_by_s210',max(s[q:])==s[q])
 envelope=max(debits[0],s[q]);all_envelopes=debits+s[q:]
 ck(name+'_all321_bound_identity',len(all_envelopes)==321 and max(all_envelopes)==envelope)
 ck(name+'_strict_2neg41_all321_one_sided',envelope<F(1,1<<41))
 ck(name+'_prefix_q_matches_prior',debits[-1]==f(row['qth_proposal_overstatement_debit_upper']) and lower[-1]==f(row['actual_sigma_q_lower']))
 records.append({'case':name,'prefix_indices':[1,q],'tail_indices':[q+1,len(s)],'prefix_count':len(debits),'tail_count':len(s[q:]),'d1':pair(debits[0]),'saved_s210':pair(s[q]),'all321_ordered_overstatement_upper':pair(envelope),'bound_attained_by_envelope_term':'d1'if envelope==debits[0] else's210','all_prefix_numerators_positive':True,'all321_envelopes_nonnegative':min(all_envelopes)>=0,'all321_one_sided_below_2neg41':True,'qth_debit_matches_prior':True,'readable':{'d1':float(debits[0]),'saved_s210':float(s[q]),'all321_ordered_overstatement_upper':float(envelope)}})
out={'status':'PASS_INDEPENDENT_PREFIX_MINMAX_ORDERED_ONE_SIDED_BOUND','records':records,'controls':controls,'control_count':len(controls),'statement':'For all j=1..321: saved_s_j−sigma_j(Z)≤the per-case envelope, conditional on inherited saved retained Gram/equation premises','not_absolute_error':True,'proposal_underestimation_controlled':False,'two_sided_B1_closed':False,'earlier_all_index_error_false_field_means_absolute_error':'The earlier certificate did not claim or refute this newly derived one-sided extension','new_fits':0,'new_raw_records':0,'new_factor_copies':0,'physical_promotion':0}
with (P/'PREFIX_CERTIFICATE.json').open('x')as z:json.dump(out,z,indent=2);z.write('\n')
print(json.dumps({'status':out['status'],'controls':len(controls),'records':[dict(case=x['case'],**x['readable'])for x in records]}))
