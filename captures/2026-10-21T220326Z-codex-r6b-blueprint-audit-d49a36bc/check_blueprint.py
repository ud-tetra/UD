#!/usr/bin/env python3
"""Constructor counterexample audit of the preserved numerical blueprint."""
from pathlib import Path
from fractions import Fraction as F
import ast,json,hashlib,numpy as np
C=Path(__file__).parent

def main():
    raw=(C/'SUBMITTED_BLUEPRINT.txt').read_bytes();text=raw.decode().replace('\r\n','\n')
    code=text[text.index('def evaluate_variational_enclosure('):text.index('5.3 Module-Specific Gap Register')].strip()
    tree=ast.parse(code);assert len(tree.body)==1 and isinstance(tree.body[0],ast.FunctionDef)
    # Function manually inspected: only numerical numpy operations, no I/O or network.
    scope={'np':np};exec(compile(tree,'preserved_blueprint_function','exec'),scope)
    A=np.array([[1.,1e-9],[1e-9,2.]]);v=np.array([1.,0.])
    out=scope['evaluate_variational_enclosure'](A,v,1.,2.)
    direct=np.linalg.norm(A@v-float(out['rayleigh_quotient'])*v)
    assert out['residual_variance']==0 and out['residual_norm']==0 and direct>0
    assert out['enclosure_interval']==(1.,1.)
    # Exact symmetric example, beta2 is a valid lower bound on the second eigenvalue:
    # characteristic polynomial at1 is -epsilon²<0, so ground<1<lambda2.
    eps=F(1,10**9);assert -eps**2<0
    indexraw=(C/'EVIDENCE_INDEX_SNAPSHOT.json').read_bytes();index=json.loads(indexraw)
    assert 'files' not in index and len(index['upstream'])==6
    entries=[f for e in index['upstream'] for f in e['files']]
    assert len(entries)==44
    arrays=[e['path'] for e in entries if e['path'].endswith(('.npy','.npz'))]
    assert len(arrays)==2 and all(p.endswith('.npz') for p in arrays)
    result={'status':'PASS_CONSTRUCTOR_BLUEPRINT_DEFECT_CONTROLS','physical_promotion':0,
            'blueprint_status':'NOT_READY_FOR_CERTIFIED_PAYLOAD_AUDIT','submission_sha256':hashlib.sha256(raw).hexdigest(),
            'index_snapshot_sha256':hashlib.sha256(indexraw).hexdigest(),
            'counterexample':{'matrix':[['1','1e-9'],['1e-9','2']],'trial':['1','0'],
                              'valid_second_eigenvalue_lower':'2','returned_variance':out['residual_variance'],
                              'returned_interval':out['enclosure_interval'],'direct_residual_norm_display':float(direct),
                              'exact_residual_squared':str(eps**2),'exact_ground_strictly_less_than_1':True,
                              'returned_point_interval_excludes_true_ground':True},
            'actual_schema':{'top_level':list(index),'upstream_captures':6,'inventoried_files':44,
                             'separately_pinned_manifests':6,'separately_pinned_source_files':len(index['source_files']),
                             'array_container_paths':arrays},
            'frozen_criterion':'residual at stored solver return over full512 coordinates with original matrix scale; retain separately from Rayleigh variance',
            'reviewer':'Devin Ramos; user-attested non-constructor, AI-assisted',
            'independent_payload_execution':'NOT_SUBMITTED in this blueprint','promotion':'NONE'}
    (C/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');return result
if __name__=='__main__':print(json.dumps(main(),indent=2))
