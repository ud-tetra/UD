#!/usr/bin/env python3
"""Parse inert submitted text; verify byte explanation and exact audit-method counterexample."""
from pathlib import Path
from fractions import Fraction as F
import ast,re,json,hashlib,subprocess
C=Path(__file__).parent;R=C.parents[1]
def main():
    b=(C/'SUBMITTED_SCOPE_AMENDMENT.txt').read_bytes();text=b.decode().replace('\r\n','\n')
    code=re.search(r'```python\n(.*?)\n```',text,re.S).group(1)
    tree=ast.parse(code)
    embedded=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='s3_text' for t in n.targets)).encode()
    # Read only the previously captured raw program; never execute attachment code here.
    ref='3f16ab56581a44c0bec43e56cf15e2372c95ae27'
    path='captures/2026-10-21T213835Z-codex-r6b-review-script-8e4c7a02/independent_audit_r6b.py'
    original=subprocess.check_output(['git','show',ref+':'+path],cwd=R)
    digest=lambda q:hashlib.sha256(q).hexdigest()
    assert embedded==original+b'\n'
    assert digest(original)=='507fb13d83438a8462d74adff20f66b823397facf71115a1b31c41b9fb343e81'
    assert digest(embedded)=='627cfd3b28693b2f8e7574dccc35ac231b0fd4b958c589a234a96cb29807f660'
    rec=json.loads((C/'SUBMITTED_RECEIPT.json').read_bytes())
    assert rec['execution_environment']['script_sha256']==digest(original)
    assert rec['claim_evaluations']['C07']['status']=='OPEN' and rec['claim_evaluations']['C08']['status']=='OPEN'
    assert rec['disposition']['physical_promotion']==0 and not rec['disposition']['registry_promotion_requested']
    # An exact vector with an inaccurate reported eigenvalue disproves residual^2/gap about that reported value.
    # A=diag(0,1), v=(1,0), reported eigenvalue eps, true ground0, next eigenvalue1.
    eps=F(1,100);r2=eps**2;assert eps>r2
    out={'status':'PASS_CONSTRUCTOR_SCOPE_INTAKE','physical_promotion':0,
         'submitted_receipt_id':rec['receipt_id'],'amendment_sha256':digest(b),
         'hash_discrepancy':'RESOLVED: embedded source is exactly uploaded bytes plus one final LF',
         'uploaded_bytes':len(original),'embedded_bytes':len(embedded),
         'corrected_binding_matches':True,'C07_C08_reviewer_status':'OPEN',
         'reported_value_counterexample':{'matrix_diagonal':['0','1'],'vector':['1','0'],'reported_value':str(eps),
                                          'true_ground':'0','residual_squared':str(r2),'gap':'1',
                                          'claimed_quadratic_error_bound_fails':True},
         'original_PR358_precision':'not retracted; original trial-vector variance bound is separate from reviewer sample',
         'reviewer_attribution':'Devin Ramos, user-attested non-constructor; AI-assisted',
         'independent_payload_review':'NOT_PERFORMED by this intake'}
    (C/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');return out
if __name__=='__main__':print(json.dumps(main(),indent=2))
