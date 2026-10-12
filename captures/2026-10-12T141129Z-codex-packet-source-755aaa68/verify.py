#!/usr/bin/env python3
"""Exact two-branch proposal-kernel nonidentification under archival action."""
from fractions import Fraction as F
from pathlib import Path
import json

def kernel(r):
    return ((1-r,r),(r,1-r))

def matmul(a,b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(2)),F(0))
                       for j in range(2)) for i in range(2))

def power(a,m):
    out=((F(1),F(0)),(F(0),F(1)))
    for _ in range(m): out=matmul(out,a)
    return out

def main():
    uniform=(F(1,2),F(1,2))
    exact=[]
    for r in (F(1,4),F(1,2)):
        k=kernel(r)
        assert all(sum(row)==1 for row in k)
        assert all(sum(uniform[i]*k[i][j] for i in range(2))==uniform[j] for j in range(2))
        assert uniform[0]*k[0][1]==uniform[1]*k[1][0]
        assert k[0][1]==k[1][0]==r
        assert (1-r)**3 in (F(27,64),F(1,8))
        for m in range(1,11):
            p=power(k,m)
            closed=F(1,2)*(1+(1-2*r)**m)
            assert p[0][0]==p[1][1]==closed
            assert p[0][1]==p[1][0]==1-closed
        exact.append({'proposal_flip_fraction':str(r),
                      'first_flip_mean_attempts':str(1/r),
                      'three_attempt_strict_null_probability':str((1-r)**3),
                      'three_attempt_endpoint_unchanged_probability':str(power(k,3)[0][0]),
                      'stationary_branch_distribution':['1/2','1/2'],
                      'acceptance_given_chi_only_proposal':'1 for Delta S=0, T>0'})
    assert exact[0]['first_flip_mean_attempts']!=exact[1]['first_flip_mean_attempts']
    assert exact[0]['three_attempt_strict_null_probability']!=exact[1]['three_attempt_strict_null_probability']
    out={'status':'PASS','scope':'conditional chi-only allowed move, fixed rho/theta/U/graph in archival action',
         'source_status':'NO-GO unique proposal rate from displayed action/Metropolis acceptance alone',
         'two_admissible_symmetric_kernels':exact,
         'mapping_chi_to_UD_pair_Theta':'NOT_DEFINED',
         'independent_same_carrier_target':'NOT_RUN',
         'physical_promotion':0}
    Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
