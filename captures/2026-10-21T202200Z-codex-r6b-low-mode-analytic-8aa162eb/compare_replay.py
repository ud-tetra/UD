from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
import json,hashlib,argparse
import numpy as np
C=Path(__file__).parent
p=argparse.ArgumentParser();p.add_argument('--results',required=True);p.add_argument('--payload',required=True);args=p.parse_args()
raw=Path(args.results).read_bytes();old=json.loads(raw);payload=Path(args.payload).read_bytes()
assert hashlib.sha256(payload).hexdigest()==old['payload_sha256']
cert=json.loads((C/'CERTIFICATE.json').read_text());z=np.load(args.payload);A=z['full'];N=256
with localcontext() as ctx:
 ctx.prec=100;exact=Decimal(cert['numeric_corroboration_decimal100']['lambda_minus'])
 dense_cluster=next(x for x in old['coupled']['numerical_clusters'] if x['rank']==3 and abs(x['lambda_min'])<Decimal('1e-8') and x['theta_weight_mean']>.6)
 sparse=[Decimal(str(m['eigenvalue'])) for probe in old['probes'] for m in probe.get('modes',[]) if m['reference_cluster']==dense_cluster['id']]
 def dec(q):return Decimal(q.numerator)/Decimal(q.denominator)
 compressions=[]
 for root in (1,2,3):
  idx=list(range(root*64,(root+1)*64));signs=[(-1)**(root+i//16+(i//4)%4+i%4) for i in range(64)]
  rr=sum(F.from_float(float(A[i,j]))*signs[ii]*signs[jj] for ii,i in enumerate(idx) for jj,j in enumerate(idx))/64
  cc=sum(F.from_float(float(A[i,N+i]))*signs[ii] for ii,i in enumerate(idx))/64
  ee=sum(F.from_float(float(A[N+i,N+j])) for i in idx for j in idx)/64
  D=(dec(rr)-dec(ee));lam=dec(ee)-2*dec(cc*cc)/(D+(D*D+4*dec(cc*cc)).sqrt())
  # Exact leakage of the rational two-column embedding in the stored IEEE matrix.
  globalidx=idx+[N+i for i in idx]
  B=[[F(s),F(0)] for s in signs]+[[F(0),F(1)] for _ in idx];K=[[rr,cc],[cc,ee]]
  normsq=F(0)
  for i,gi in enumerate(globalidx):
   for k in range(2):
    hb=sum(F.from_float(float(A[gi,gj]))*B[j][k] for j,gj in enumerate(globalidx))/8
    bk=sum(B[i][j]*K[j][k] for j in range(2))/8
    normsq+=(hb-bk)**2
  compressions.append({'root':root,'theta_uniform_Rayleigh_shift_exact_IEEE':str(ee),'theta_uniform_Rayleigh_shift_decimal':str(dec(ee)),'projected_negative_eigenvalue_decimal':str(lam),'difference_from_exact_source':str(lam-exact),'embedding_leakage_Frobenius_squared_exact':str(normsq),'embedding_leakage_Frobenius_decimal':str(dec(normsq).sqrt()),'scope':'Rayleigh compression of stored IEEE matrix; nonzero leakage means it is not an exact invariant sector of those bytes'})
 comparison={'type':'NUMERICAL_CORROBORATION_AND_EXACT_IEEE_ASSEMBLY_AUDIT','prior_commit':'524f180d3f903267925d48599add52acb9301d6b','prior_capture':'2026-10-21T201221Z-codex-r6b-numerical-replay-2dbd851a','prior_results_sha256':hashlib.sha256(raw).hexdigest(),'prior_payload_sha256':hashlib.sha256(payload).hexdigest(),'exact_source_lambda_minus':str(exact),'prior_dense_cluster':dense_cluster,'prior_sparse_eigenvalues':[str(x) for x in sparse],'sparse_absolute_errors_from_exact_source':[str(abs(x-exact)) for x in sparse],'prior_dense_extreme_absolute_errors_from_exact_source':[str(abs(Decimal(str(dense_cluster[k]))-exact)) for k in ('lambda_min','lambda_max')],'stored_float_compressions':compressions,'interpretation':'Residuals validate a solve of the stored floating matrix; they do not eliminate rational-source assembly error. These differences stay within the prior absolute residual scale but matter for relative digits of a tiny eigenvalue. No tolerance or source coefficient was fitted.','physical_promotion':0}
(C/'REPLAY_COMPARISON.json').write_text(json.dumps(comparison,indent=2)+'\n');print(json.dumps({'status':'RECORDED','exact_source_lambda':str(exact)[:32],'float_theta_Rayleigh_shift':compressions[0]['theta_uniform_Rayleigh_shift_decimal'],'sparse_source_absolute_error':comparison['sparse_absolute_errors_from_exact_source'][0]}))
