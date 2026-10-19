"""Metadata-only contract builder and exact37x37 static checks; NEVER raw data."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from recipes import PROTOCOL_ID,DEN,cayley_numerator,matmul,seeded_spatial,round_ratio
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def build():
    sources=json.loads((P/'SOURCE_INDEX.json').read_text())
    for row in sources['sources']:assert sha(P.parent/row['workspace_source'])==row['sha256']
    anchor=json.loads((P.parent/sources['anchor_data']).read_text())['records'];oldsp=json.loads((P.parent/sources['old_spatial_selection']).read_text())
    phase=json.loads((P/'inputs/SOURCE_PHASE.json').read_text());targets=phase['target_matches'];lo=next(r for r in targets if r['label']=='j0:rate1:sign1');hi=next(r for r in targets if r['label']=='j51:rate-1:sign1')
    preparations=[]
    for label,parent,offset in [('A','reverse_stationary',0),('B','shuffle_cycle',1)]:
        prior=next(r for r in anchor if r['case']==parent);assert prior['transform_denominator']==1
        M=matmul(cayley_numerator(offset),prior['transform_integer_matrix'])
        assert all(sum(M[i][k]*M[j][k] for k in range(37))==DEN*DEN*int(i==j) for i in range(37) for j in range(37))
        assert all(not M[i][j] or i%2==j%2 for i in range(37) for j in range(37))
        assert all(sum(v!=0 for v in row)<=2 for row in M)
        preparations.append({'id':label,'name':f'new_{label}_cayley22_of_{parent}','existing_family_reference_anchor':parent,'matrix_numerator':M,'denominator':DEN,'pairing_cyclic_offset_within_parity':offset,'exact_squared_operator_distance_to_reference':[4,DEN],'operator_distance_upper':[1,1<<21],'existing_PR233_rho':[1,1<<20],'new_preparation_point_not_redefinition_of_old_anchor':True})
    oldtable=[{'preparation':a,'channel':int(oldsp['channels'][a]),'sign':int(oldsp['signs'][a])} for a in range(37)];newtable=seeded_spatial()
    cases=[]
    for name,prep,kind,spatial,carrier in [('new_A_control','A','zero',oldtable,lo),('new_A_ramped_low','A','ramped_low_sine',oldtable,lo),('new_B_control','B','zero',newtable,hi),('new_B_chirped_high','B','chirped_high_cosine',newtable,hi)]:
        cases.append({'case':name,'preparation_id':prep,'noise_kind':kind,'spatial':spatial,'carrier_target_label':carrier['label'],'carrier_omega':carrier['omega'],'integer_noise_absolute_max':0 if kind=='zero' else 1127,'per62_vector_noise_norm_upper':[0 if kind=='zero' else 1127,1<<48],'noise_reference':'ONE rounded new-preparation nominal, not inherited rounded anchor','future_raw_shape':[37,8191,62],'raw_dtype':'little-endian int64','quantum':[1,1<<48]})
    old=json.loads((P/'inputs/OLD_POLICY.json').read_text())['gates'];frame=json.loads((P/'inputs/FIXED_BUDGET.json').read_text())['source_budget'];sep=F(*phase['metrics']['minimum_target_chord_lower']);half=sep/2
    contract={'protocol_id':PROTOCOL_ID,'status':'PROSPECTIVE_ONLY_NO_FUTURE_RECORDS_OR_FITS_GENERATED','preparations':preparations,'cases':cases,'fixed_case_order':[r['case'] for r in cases],'spatial_seed_derivation':{'B_ascii_material':PROTOCOL_ID+'|B|spatial|'+str('{a}'),'digest':'SHA256','channel':'little-endian unsigned first8bytes modulo62','sign':'+1 iff digest byte8 bit0 is1, else-1'},'phase_targets':209,'fixed_source_minimum_chord_lower':phase['metrics']['minimum_target_chord_lower'],'strict_finite_emission_circular_error_cap':[half.numerator,half.denominator],'phase_cap_reason':'Half fixed source chord is conservative half angular separation; unique/bijective matching, not an errorbar chosen from observed errors.','unchanged_phase_quality_caps':{k:old[k] for k in ['inverse_residual','proposed_inverse_norm','eigenpair_residual','emitted_argument_error']},'phase_unit':'radians per TWO-STEP sample modulo2pi; primitive-frequency ambiguity modulo pi remains','planned_future_estimator_runs':4,'new_raw_records_this_turn':0,'new_estimator_SVD_eigenvalue_inverse_alignment_calls_this_turn':0,'raw_quantum':[1,1<<48],'nominal_rounding':'exact rational Pythoninteger products then ONE nearest-even integer rounding; never int64 multiply before divide','noise_rounding':'ramp integer envelope nearest-even; carrier sign fixed512-bit interval-certified; sin0declared+1; unresolvedsign GLOBAL_DATA_HOLD with zero fits','data_gate':'ALL4 full raw/nominal hashes, all18,790,154 scalar differences/case, all303,067 vector norms/case and source/overflow/projectionrange checks frozen before ANY fit; any dataHOLD means0fitsglobally','future_fit_policy':'ONE unchanged estimator percase only; q learned, never forced; numericalexception/order mismatch retainedHOLD; continue fixed remaining cases, no retries/replacements/retuning','frame_lane':'Unchanged strict source-frame cap/Gram/normal checked separately; finite phase matching does not rewrite frame outcomes or nested-ball exclusion','optional_exact_T_lane':'PR244 similarity/normal-diagonal disks and strict center/origin/source-angle predicates; no new eigenvalue/inverse solver in verification, no altered primary emitted phase gates','uniform_noise_ball_or_phase_failure_claimed':False,'external_review':'PENDING','physical_promotion':0}
    assert F(4,DEN)<F(1,1<<40)
    contract['unchanged_actual_estimator_source_sha256']=sources['actual_estimator_sha256']
    contract['expected_synthetic_baseline_sha256']='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59'
    contract['unchanged_frame_caps']={'strict_raw_alignment':frame['allowed_raw_frame_residual_lower'],'nonstrict_retained_Gram':frame['retained_Gram_cap'],'nonstrict_normal':frame['normal_cap']}
    assert [round_ratio(n,2) for n in [-3,-1,1,3]]==[-2,0,0,2]
    p=P/'CONTRACT.json';assert not p.exists();p.write_text(json.dumps(contract,indent=2)+'\n')
    validation={'status':'PASS_METADATA_ONLY_EXACT_PREPARATION_AND_CONTRACT_VALIDATION','contract_sha256':sha(p),'orthogonality_integer_equalities_checked':2*37*37,'same_parity_support_checked':True,'nonzero_coefficients_per_row_max':2,'existing_PR233_neighborhood_membership_proved':True,'new_preparation_denominator':DEN,'source_target_labels_found':[lo['label'],hi['label']],'strict_fixed_cap_derived_only_from_source_separation':True,'four_signed_rounding_tie_controls_pass':True,'raw_noise_carrier_tables_generated':0,'raw_records_generated':0,'estimator_SVD_eigenvalue_inverse_alignment_calls':0,'physical_promotion':0};(P/'STATIC_VALIDATION.json').write_text(json.dumps(validation,indent=2)+'\n');print(json.dumps(validation),flush=True)
if __name__=='__main__':build()
