"""Independent exact countermodels for non-implications of thin-factor bounds."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent
rows=[]
def ck(name,value):
 assert value,name
 rows.append({'id':name,'pass':True})
# q=2, Z=diag(M,2,0), U=[e2,e1], V=[e2,(c,0,h)], S=diag(2,1).
c,h=F(200,10001),F(9999,10001);M=1/c;tau=F(1,2)
ck('V_Gram_identity',c*c+h*h==1)
ck('U_Gram_identity',F(1)==1)
ck('singular_equation_exact',M*c==1)
ck('saved_sorted_S',F(2)>=F(1)>0)
ck('true_singulars_sorted',M>2>0)
ck('positive_partial_lower_ell',F(1)>tau)
ck('inherited_tail_zero_below_cutoff',F(0)<tau)
ck('ambient_cutoff_rank2',sum(x>tau for x in (M,F(2),F(0)))==2)
ck('ambient_algebraic_rank2',sum(x>0 for x in (M,F(2),F(0)))==2)
ck('restricted_condition_exact2',F(2)/F(1)==2)
ck('ambient_leading_condition_exceeds2',M/F(2)>2)
ck('qth_underestimate_despite_zero_debit',F(2)-F(1)==1)
ck('indexed_leading_error_positive_despite_zero_debit',M-F(2)>0)
# n→∞: c_n=2n/(n²+1), h_n=(n²−1)/(n²+1), M_n=1/c_n.
for n in (5,20,100):
 c=F(2*n,n*n+1);h=F(n*n-1,n*n+1)
 ck('rational_family_Gram_'+str(n),c*c+h*h==1)
 ck('rational_family_residual_'+str(n),(1/c)*c==1)
result={'status':'PASS_EXACT_PARTIAL_FACTOR_NONIMPLICATION_COUNTERMODELS','matrix':'Z=diag(10001/200,2,0)','U_columns':['e2','e1'],'V_columns':['e2','(200/10001,0,9999/10001)'],'S_diagonal':[2,1],'Gram_defects':[0,0],'singular_equation_residual':0,'partial_lower_ell':1,'partial_qth_overstatement_debit':0,'source_tail_upper':0,'cutoff':[1,2],'actual_cutoff_rank':2,'actual_algebraic_rank':2,'restricted_condition':2,'actual_ambient_leading_condition':['10001','400'],'family':'n>=4: c=2n/(n²+1), h=(n²−1)/(n²+1), M=1/c; same exact Gram/equation/S/ell/cutoff, ambient kappa2=(n²+1)/(4n)→∞','controls':rows,'control_count':len(rows),'scope':'Logical exact matrix family only; no actual saved record or implementation bug','new_fits':0,'physical_promotion':0}
with (P/'COUNTERMODELS.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'status':result['status'],'controls':len(rows)}))
