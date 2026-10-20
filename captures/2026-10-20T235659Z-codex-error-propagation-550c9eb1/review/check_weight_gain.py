#!/usr/bin/env python3
"""Source-data-only exact calibration gain for declared absolute top weights."""
from pathlib import Path
import json,zipfile,hashlib
P=Path(__file__).resolve().parent;W=P.parent
Z=W/'ud-repo/captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/recovered/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.zip'
with zipfile.ZipFile(Z)as z:
 raw=z.read('sources/COMPLEX_AND_ACTION.json');s=json.loads(raw)['simplices']
assert list(map(len,s))==[120,720,1200,600]
ix={tuple(f):i for i,f in enumerate(s[2])};cols=[];rows=[0]*1200
for tet in s[3]:
 col={ix[tuple(tet[:k]+tet[k+1:])]:(-1)**k for k in range(4)};cols.append(col)
 for face in col:rows[face]+=1
assert max(rows)==2 and all(len(c)==4 for c in cols)
J=[0,9,227,432,447,582,538,347,332,141]
gram=[[sum(v*cols[j].get(f,0)for f,v in cols[i].items())for j in J]for i in J]
assert gram==[[4 if i==j else 0 for j in range(10)]for i in range(10)]
# B_J diag(delta)^T B_J diag(delta)=4 diag(delta²).
# The skew coupling block has the same operator norm as this weighted boundary.
from fractions import Fraction as F
u=F(1,2**67);assert 2*u==F(1,2**66)
assert 8<9
out={'status':'PASS_SOURCE_SELECTED_WEIGHT_OPERATOR_GAIN','source_archive_sha256':hashlib.sha256(Z.read_bytes()).hexdigest(),'complex_member_sha256':hashlib.sha256(raw).hexdigest(),'J':J,'selected_Gram':gram,'selected_Gram_entries_checked':100,'all_boundary_columns':600,'max_abs_boundary_row_sum':2,'max_abs_boundary_column_sum':4,'selected_support_exact_identity':'||DeltaK||=2 max_{j in J}|delta d_j|','arbitrary600_support_bound':'||DeltaK||<=sqrt8 max|delta d_j|<=3 max|delta d_j|','strict_sqrt8_vs3_requires_positive_error_cap':True,'conditional_profile_connection':{'absolute_selected_weight_error_upper':str(u),'generator_error_upper':str(2*u),'actual_error_measurement':'NOT_SUPPLIED'},'scope':{'absolute_weight_errors_not_relative':True,'nominal_D_and_actual_error_need_not_preserve_C10':True,'only_top_constitutive_weight_error_class':True,'other_operator_errors_need_separate_budget':True,'physical_units_or_weight_law_not_certified':True,'no_archived_program_execution':True,'physical_promotion':0,'external_review':'PENDING'}}
(P/'WEIGHT_GAIN_CHECKS.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'selected_Gram':'4I10'}))
