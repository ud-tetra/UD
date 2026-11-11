#!/usr/bin/env python3
"""Constructor tests of corrected blueprint; no submitted file/network operations executed."""
from pathlib import Path
import ast,json,hashlib,numpy as np
C=Path(__file__).parent
s=(C/'SUBMITTED_AMENDMENT.txt').read_text()
a=s.index('from pathlib import Path');b=s.index('6. Audit Findings & Ledger Realignment',a)
tree=ast.parse(s[a:b].strip())
assert all(isinstance(n,(ast.Import,ast.ImportFrom,ast.FunctionDef)) for n in tree.body)
ns={};exec(compile(tree,'preserved_blueprint_definitions','exec'),ns)
f=ns['evaluate_mode_verification']
control=f(np.array([[1.,1e-9],[1e-9,2.]]),np.array([1.,0.]),1.,2.)
assert control['direct_residual_eta']==1e-9
# Two negative roots: passing a block beta into a full matrix creates a false ground enclosure.
A=np.diag([-2e-8,-5e-10,1.]);v=np.array([1.,1e-4,0.])
out=f(A,v,-2e-8,.000664605)
lower=out['rayleigh_quotient']-out['enclosure_half_width']
assert out['acceptance_passed'] and out['enclosure_valid'] and lower>-2e-8
result={'status':'PASS_CONSTRUCTOR_BLUEPRINT_CONTROLS','direct_residual_fix':'confirmed on previous cancellation control',
        'full_matrix_gap_counterexample':{'diagonal':list(np.diag(A)),'vector':list(v),'passed_module_beta':.000664605,
                                         'actual_ground':-2e-8,'returned_lower':lower,'returned_valid':out['enclosure_valid'],
                                         'frozen_style_numerical_acceptance_passed':out['acceptance_passed'],
                                         'claimed_ground_lower_bound_false':True},
        'reason':'A_full has another negative eigenvalue; supplied positive beta is not a lower bound for its second eigenvalue',
        'reviewer_execution':'NOT_PERFORMED','physical_promotion':0}
(C/'BLUEPRINT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
