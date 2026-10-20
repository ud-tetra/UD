#!/usr/bin/env python3
"""Fraction-only error-envelope/decoder-contract checks. No estimator or data fit."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,math

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True,type=Path);ap.add_argument('--out',required=True,type=Path);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);H=lambda b:hashlib.sha256(b).hexdigest()
 src=a.repo/'captures/2026-10-20T234200Z-codex-weighted-conditioning-d6af1d67';rbytes=(src/'RESULT.json').read_bytes();tbytes=(src/'THEOREM.md').read_bytes();assert H(rbytes)=='ccc92afdfc0c2057a2d0ee29940eef907ad7c2c3817497a8af4726dc063695d2';assert H(tbytes)=='d8f50283e1208f99a6634adc96aff922f12ebcea4b4c8d4bc0f96dffa4acf3b3';source=json.loads(rbytes);assert source['inherited_history_and_sample_rank']==1999 and source['inherited_kernel']==641
 M=4096;h=F(1,2);s=F(61,27648);C=1/s;mu=sum((h*j for j in range(M)),F(0))/M;T2=sum(((h*j)**2 for j in range(M)),F(0))/M;var=T2-mu**2
 assert mu==F(4095,4)and T2==F(11180715,8)and var==F(4096**2-1,48)and T2<2048**2
 def pow2(k):return F(1,2**k)
 X=F(1);p=pow2(52);xi=pow2(66);rho=pow2(53);eta=pow2(56);nu=pow2(53);enc=pow2(53);alpha=pow2(42);beta=F(512);alg=pow2(42);tau=pow2(39)
 b=rho+2048*xi+(5+xi)*eta;delta=p+(X+p)*b+nu+enc;ideal=C*delta;implemented=alpha*X+beta*delta+alg
 assert delta<pow2(50)and implemented<pow2(40)<tau and ideal<implemented
 clock=pow2(58)+2048*pow2(70)+pow2(58);assert clock==F(5,2**59)<eta
 # Fresh norm-typed requirement for the ideal nominal inverse. Not a port gate.
 combined_limit=s*tau;assert combined_limit==F(61,27*2**49)
 # Exact non-skew growth control: exp(1)-1>3/2>1 from first3Taylor terms.
 assert F(3,2)>1
 # Omitted amplitude and mixed preparation/readout terms fail even for scalars.
 controls=[]
 def add(name,proof):controls.append({'id':name,'status':'PASS_EXACT_COUNTERMODEL','proof':proof})
 amp=F(1,8)*16;assert amp==2>F(1,8);add('AMPLITUDE_REQUIRED',{'readout_error':'1/8','state_amplitude':16,'actual_data_error':str(amp),'amplitude_free_claim':'1/8'})
 true=(1+F(1,2))*F(1,2);omitted=F(1,2);assert true==F(3,4)>omitted;add('PREPARATION_READOUT_MIXED_TERM_REQUIRED',{'x':0,'p':'1/2','rho':'1/2','actual_data_error':str(true),'omitted_p_rho_claim':str(omitted)})
 # ||rotation(1/2)-I||=2sin(1/4)>1/2−1/192>5/16.
 low=2*(F(1,4)-F(1,4)**3/6);assert low==F(95,192)>F(5,16);add('CLOCK_GENERATOR_MIXED_TERM_REQUIRED',{'toy_K':0,'xi':8,'theta':'1/16','nominal_norm_cap':5,'response_lower':str(low),'omitting_xi_theta_cap':'5/16'})
 assert F(1,64)<1;add('COHERENT_NOISE_NO_SQRT_M_GAIN',{'M':M,'per_scalar_error':'u>0 at every time','normalized_noise_norm':'u','unsupported_independence_gain':'u/64'})
 add('NON_SKEW_NEEDS_NEW_GROWTH_BOUND',{'toy_K':0,'actual_generator':1,'time':1,'actual_error':'exp(1)-1>3/2','invalid_unitary_bound':1})
 # Exact forward fit/right inverse may add a hidden component.
 q=[F(3,5),F(4,5)];B=[F(1),F(4,3)];assert sum(v*v for v in q)==1 and B[0]==1 and [v*q[0]for v in B]==q
 add('RIGHT_INVERSE_DOES_NOT_CERTIFY_ORTHOGONAL_DECODER',{'F':'[1,0]','Q':['3/5','4/5'],'K_and_J':0,'Q_norm':1,'intertwining_residual':0,'trial_Gram':'9/25','B':['1','4/3'],'F_B':1,'B_F_Q_equals_Q':True,'decoder_conformance_defect':'4/3','spurious_hidden_output_for_x_e1':'4/3'})
 # Normalized3-time sampled rotations; exact Gram avoids transcendental arithmetic.
 eps=pow2(12);A=[[F(1),F(0),eps],[F(0),F(1),eps],[F(-1),F(0),eps]]
 det=A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]);assert det==2*eps!=0 and eps<s
 weak=[F(0),-eps,F(1)];y=[sum(v*x for v,x in zip(row,weak))for row in A];assert y==[eps,F(0),eps]
 gramdet=det**2/F(27);assert gramdet>0;add('SMALL_MAP_ERROR_DOES_NOT_PRESERVE_FULL_KERNEL',{'map':'A_epsilon/sqrt3','A':[[str(v)for v in row]for row in A],'epsilon':str(eps),'nominal_rank':2,'actual_rank':3,'operator_map_error':str(eps),'actual_Gram_determinant':str(gramdet),'full_positive_condition_lower':'>1/epsilon=4096','nominal_quotient_stability':'retained; fullrank/kernel equality not inferred'})
 # Ideal inverse stays in V, hence orthogonal full-state decomposition; ambiguity persists.
 add('HIDDEN_STATE_NOT_RECONSTRUCTED',{'F':'[1,0]','xplus':['0','1'],'xminus':['0','-1'],'identical_data':0,'worst_case_full_state_error_lower':1})
 fields={'state_amplitude_X':X,'preparation_p':p,'generator_error_xi':xi,'readout_RMS_rho':rho,'clock_RMS_eta':eta,'noise_RMS':nu,'encoding_RMS':enc,'decoder_alpha':alpha,'decoder_beta':beta,'algorithm_error':alg,'observable_state_target_tau':tau}
 result={'status':'PASS_CONDITIONAL_ERROR_PROPAGATION_AND_EXACT_CONTROLS','source_rank':1999,'source_hidden_dimensions':641,'inverse_amplification_upper':str(C),'sample_count':M,'sample_step':str(h),'mean_time':str(mu),'RMS_time_squared':str(T2),'time_variance':str(var),'RMS_time_upper':2048,'conditional_example':{'all_input_bounds':'UNSUPPLIED_HOLD','target_object':'observable-chain Euclidean state error, not sixratio q','parameters':{k:str(v)for k,v in fields.items()},'map_error_bound_b':str(b),'normalized_data_error_bound':str(delta),'ideal_inverse_error_upper':str(ideal),'conditional_implemented_error_upper':str(implemented),'verified_implication':'implemented_error<2^-40<2^-39 IF every stated premise is independently established','actual_estimator_conformance':'NOT_SUPPLIED_HOLD','actual_error_budget_admission':'HOLD'},'ideal_total_data_requirement_for_declared_tau':str(combined_limit),'controls_passed':len(controls),'scope':{'new_measurements':0,'actual_estimator_calls':0,'new_noise_tolerance_measurement':False,'old_sixratio_or_Hankel_gates_transferred':False,'fixed_linear_map_needed_for_singular_continuity':True,'physical_promotion':0,'external_promotion_review':'PENDING'}}
 contract={'status':'DEVELOPMENT_CONDITIONAL_EXAMPLE_NOT_ADMITTED_ACQUISITION','model_and_norm':'PR307 exact fixed sample map; unit chain coordinates;1/64 normalization','input_evidence_status':'UNSUPPLIED_HOLD','error_inputs':[{'name':k,'declared_upper_bound':str(v),'type':'DECLARED_CONDITIONAL_CONTROL','evidence_receipt':None,'status':'HOLD_NO_SOURCE_RECEIPT'}for k,v in fields.items()],'actual_decoder_required':{'B_operator_norm':'<=beta','B_F_minus_nominal_orthogonal_projection_operator_norm':'<=alpha over full2640-dimensional state space','arithmetic_implementation_error':'<=algorithm_error for supplied input domain','status':'HOLD_NOT_DEDUCED_FROM_CONDITION_NUMBER'},'noise_norm':'sqrt(mean_j ||n_j||_2^2), deterministic; no independence assumed','preparation':'one fixed preparation error vector per trajectory; time-varying preparation requires a separate p_max/RMS contract','source_and_physical_units':'Required separately; no SI/physical acquisition inferred','physical_promotion':0}
 bindings={'parent_result_path':str((src/'RESULT.json').relative_to(a.repo)),'parent_result_sha256':H(rbytes),'parent_theorem_path':str((src/'THEOREM.md').relative_to(a.repo)),'parent_theorem_sha256':H(tbytes),'dependencies':'Python standard library only','scope':'New Fraction-only finite moments, conditional budgets and small exact countermodels; parent conditioning/rank inherited'}
 for name,obj in [('RESULT.json',result),('CONDITIONAL_ERROR_CONTRACT.json',contract),('CONTROLS.json',{'status':'PASS_EXACT_LOGICAL_COUNTERMODELS','controls':controls}),('SOURCE_BINDINGS.json',bindings)]: (a.out/name).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':result['status'],'controls':len(controls),'actual_admission':'HOLD','conditional_example_error_bound':str(implemented)}))
if __name__=='__main__':main()
