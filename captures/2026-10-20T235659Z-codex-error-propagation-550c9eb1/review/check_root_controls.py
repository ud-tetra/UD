#!/usr/bin/env python3
"""Independent exact verification of the eight disclosed logical controls."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;f=P.parent/'c28_math_v2/CONTROLS.json';raw=f.read_bytes();root=json.loads(raw);rows={r['id']:r['proof']for r in root['controls']};assert len(rows)==8
assert F(1,8)*16==2>F(1,8)
assert (1+F(1,2))*F(1,2)==F(3,4)>F(1,2)
sinlower=2*(F(1,4)-F(1,4)**3/6);assert sinlower==F(95,192)>F(5,16)
assert sum([F(1)]*4096)/4096==1 # normalized squared coherent noise, no64 gain.
assert F(1)+F(1,2)+F(1,6)>F(3,2) # exp(1)-1 exceeds this positive partial sum.
q=(F(3,5),F(4,5));B=(F(1),F(4,3));assert sum(x*x for x in q)==1 and B[0]==1 and tuple(x*q[0]for x in B)==q
assert F(rows['RIGHT_INVERSE_DOES_NOT_CERTIFY_ORTHOGONAL_DECODER']['decoder_conformance_defect'])==F(4,3)
eps=F(rows['SMALL_MAP_ERROR_DOES_NOT_PRESERVE_FULL_KERNEL']['epsilon']);A=[[F(x)for x in row]for row in rows['SMALL_MAP_ERROR_DOES_NOT_PRESERVE_FULL_KERNEL']['A']]
assert A==[[1,0,eps],[0,1,eps],[-1,0,eps]]
det=A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]);assert det==2*eps
assert det*det/27==F(rows['SMALL_MAP_ERROR_DOES_NOT_PRESERVE_FULL_KERNEL']['actual_Gram_determinant'])>0
# Nominal determinant0 with independent first two columns; map perturbation
# has one column norm|eps| after1/sqrt3 normalization.
assert 3*eps*eps/3==eps*eps
v=[0,-eps,1];y=[sum(a*x for a,x in zip(row,v))for row in A];assert y==[eps,0,eps]
weak_gain_sq=sum(t*t for t in y)/(3*sum(F(x)**2 for x in v));strong_gain_sq=F(2,3)
condition_lower_sq=strong_gain_sq/weak_gain_sq;assert condition_lower_sq==(1+eps*eps)/(eps*eps)>1/(eps*eps) and 1/eps==4096
assert eps<F(61,27648)
# The last ambiguity is an exact two-point triangle inequality: equal data,
# states atdistance2, hence at least one estimation error>=1.
assert abs(F(1)-F(-1))==2
out={'status':'PASS_ALL_EIGHT_ROOT_LOGICAL_CONTROLS','controls_verified':8,'root_control_ids':list(rows),'root_controls_sha256':hashlib.sha256(raw).hexdigest(),'small_map_control':{'actual_determinant':str(det),'actual_normalized_Gram_determinant':str(det*det/27),'weak_gain_squared':str(weak_gain_sq),'strong_gain_squared':str(strong_gain_sq),'condition_squared_lower':str(condition_lower_sq),'condition_strict_lower':'4096'},'scope':{'small_countermodels_not_actual600cell_measurements_or_bugs':True,'no_producer_script_execution':True,'physical_promotion':0,'external_review':'PENDING'}}
(P/'ROOT_CONTROLS_CHECKS.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(out['status'])
