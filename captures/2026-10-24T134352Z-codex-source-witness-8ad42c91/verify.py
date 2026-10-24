"""Exact conditional design arithmetic. No measured calibration or source proof."""
from fractions import Fraction as F
from pathlib import Path
import json,copy,hashlib,sys
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parent;ROOT=P.parents[1]
class Hold(Exception):pass
def need(x,s):
 if not x:raise Hold(s)
def calculate(c):
 try:
  keys=['B_V','A_V','R_V','gain_upper','image_upper','Vref_V','coefficient_l2_V','sample_error_V','digital_RMS_target_V','outside_target_V']
  v={k:F(c[k]) for k in keys};need(all(x>=0 for x in v.values()) and v['Vref_V']>0,'nonnegative bounds and positive voltage reference')
  need(c['source_model']=='finite_complex_spectral_measures' and c['path_model']=='fixed_widely_linear_plus_polynomial_and_bounded_remainder','unsupported source/path model')
  need(c['remainder_scope']=='all_omitted_orders_memory_transients_drift_reference_and_additive','incomplete remainder scope')
  need(c['coefficient_bound_meaning']=='sum_of_absolute_mixed_coefficients_at_each_degree','coefficient aggregation')
  need(c['outside_bound_meaning']=='deterministic_complex_spectral_measure_TV','not spectral TV')
  need(c['primary_included'] is True,'primary signal omitted')
  beta={int(k):F(x) for k,x in c['beta_by_degree'].items()};need(beta and all(d>=2 and b>=0 for d,b in beta.items()),'nonlinear coefficients')
  shares={k:F(x) for k,x in c['D_TV_shares_V'].items()};need(set(shares)=={'additive','higher_order_and_memory','startup_and_drift','primary_reference'} and all(x>=0 for x in shares.values()),'remainder allocations')
  U=v['B_V']+v['A_V']+v['R_V'];linear=v['gain_upper']*v['R_V'];image=v['image_upper']*U;nl={str(d):b*U**d/v['Vref_V']**(d-1) for d,b in beta.items()};D=sum(shares.values());out=linear+image+sum(nl.values())+D
  # Symmetric sampled Gram bound inherited from the fixed1024-sample family.
  gram_upper=F(c['sample_gram_upper']);gram_factor=F(c['sample_gram_norm_factor']);need(gram_upper>0 and gram_factor>=0 and gram_factor**2>=gram_upper,'Gram norm factor')
  observed=gram_factor*v['gain_upper']*v['coefficient_l2_V']+out+v['sample_error_V']
  need(out<=v['outside_target_V'],'outside TV target exceeded');need(observed<=v['digital_RMS_target_V'],'digital RMS sufficient target exceeded')
  direct=v['gain_upper']*v['A_V']+out
  return {'status':'PASS_EXACT_CONDITIONAL_DESIGN','U_V':str(U),'linear_residual_V':str(linear),'image_V':str(image),'nonlinear_by_degree_V':{k:str(x) for k,x in nl.items()},'remainder_V':str(D),'outside_upper_V':str(out),'outside_margin_V':str(v['outside_target_V']-out),'sample_RMS_upper_V':str(observed),'RMS_margin_V':str(v['digital_RMS_target_V']-observed),'direct_source_model_tail_V':str(direct),'approximation':{'outside_upper_V':float(out),'sample_RMS_upper_V':float(observed),'direct_source_model_tail_V':float(direct)},'physical_promotion':0,'empirical_admission':False}
 except (Hold,ValueError,KeyError,TypeError,ZeroDivisionError) as e:return {'status':'HOLD','reasons':[str(e)],'physical_promotion':0,'empirical_admission':False}
c={'version':'0.1','source_model':'finite_complex_spectral_measures','path_model':'fixed_widely_linear_plus_polynomial_and_bounded_remainder','remainder_scope':'all_omitted_orders_memory_transients_drift_reference_and_additive','coefficient_bound_meaning':'sum_of_absolute_mixed_coefficients_at_each_degree','outside_bound_meaning':'deterministic_complex_spectral_measure_TV','primary_included':True,'B_V':'1','A_V':'1/4000','R_V':'1/1000000','gain_upper':'51/50','image_upper':'1/1000000','Vref_V':'1','beta_by_degree':{'2':'1/1000000','3':'1/1000000'},'D_TV_shares_V':{'additive':'1/2000000','higher_order_and_memory':'1/2000000','startup_and_drift':'1/2000000','primary_reference':'1/2000000'},'coefficient_l2_V':'1/40000','sample_gram_upper':'11/10','sample_gram_norm_factor':'21/20','sample_error_V':'1/50000','digital_RMS_target_V':'11/200000','outside_target_V':'1/100000','mode_indices':list(range(100,200)),'line_amplitude_V':'1/400000','nominal_span_s':'1','per_line_frequency_error_Hz':'1/200','monitor_affine_error':'1/100000000','monitor_sample_residual_s':'1/100000000','status':'PROPOSED_REQUIREMENTS_NOT_EMPIRICAL_BOUNDS'}
base=calculate(c);assert base['status']=='PASS_EXACT_CONDITIONAL_DESIGN'
# Exact coefficient budgets for100 equal-amplitude lines; phases arbitrary.
assert 100*F(c['line_amplitude_V'])==F(c['A_V']);assert 100*F(c['line_amplitude_V'])**2==F(c['coefficient_l2_V'])**2
# Replay prior published exact Gram result without executing its artifact-generating code.
prior=ROOT/'captures/2026-10-22T133344Z-codex-sampled-monitor-93e0a217/CERTIFICATE.json';g=json.loads(prior.read_text());lam=F(g['sampled_gram_lower']['fraction']);assert lam>=F(9,10);assert 2-lam<=F(11,10)
controls=[{'case':'frozen_conditional_design',**base}]
def bad(name,fn,reason):
 x=copy.deepcopy(c);fn(x);r=calculate(x);assert r['status']=='HOLD' and r['reasons']==[reason],(name,r);controls.append({'case':name,**r})
bad('source_impurity_100uV',lambda x:x.update(R_V='1/10000'),'outside TV target exceeded')
bad('image100ppm',lambda x:x.update(image_upper='1/10000'),'outside TV target exceeded')
bad('quadratic_beta1e_minus3',lambda x:x['beta_by_degree'].update({'2':'1/1000'}),'outside TV target exceeded')
bad('unbounded_remainder_scope',lambda x:x.update(remainder_scope='polynomial_only'),'incomplete remainder scope')
bad('RMS_not_TV',lambda x:x.update(outside_bound_meaning='sample_RMS'),'not spectral TV')
bad('single_coefficient_not_sum',lambda x:x.update(coefficient_bound_meaning='maximum_coefficient'),'coefficient aggregation')
bad('omit_primary',lambda x:x.update(primary_included=False),'primary signal omitted')
bad('excess_primary',lambda x:x.update(B_V='10'),'outside TV target exceeded')
bad('excess_sample_error',lambda x:x.update(sample_error_V='1/10000'),'digital RMS sufficient target exceeded')
bad('invalid_sqrt_bound',lambda x:x.update(sample_gram_norm_factor='1'),'Gram norm factor')
bad('negative_degree_bound',lambda x:x['beta_by_degree'].update({'2':'-1'}),'nonlinear coefficients')
bad('zero_voltage_reference',lambda x:x.update(Vref_V='0'),'nonnegative bounds and positive voltage reference')
bad('missing_transient_allocation',lambda x:x['D_TV_shares_V'].pop('startup_and_drift'),'remainder allocations')
# Sharp algebra example: b=1 and s=a exp(iwt); quadratic distortion has mixed2ba term.
a=F(1,4000);b=F(1);beta=F(1,1000000);full=beta*(b+a)**2;tail_only=beta*a*a;assert full>tail_only*10**6
controls.append({'case':'primary_mixed_term_required','status':'PASS_EXACT_ALGEBRA','full_quadratic_TV_V':str(full),'incorrect_tail_only_V':str(tail_only)})
# Source family alias: two opposite atoms are invisible on the nominal monitor grid.
assert all(F((1124-100)*j,1024).denominator==1 for j in range(1024));controls.append({'case':'unrestricted_sample_TV_inference_impossible','status':'PASS_EXACT_ALIAS_IDENTITY','source_TV_V':'2','nominal_samples':'all zero'})
cert={**base,'constructor_verification':'PASS','independent_review':'PENDING','source_witness':'NOT_SUPPLIED','calibration_witness':'NOT_SUPPLIED','sampled_gram_certificate_sha256':hashlib.sha256(prior.read_bytes()).hexdigest(),'sampled_gram_upper_from_inherited_row_bound':str(2-lam),'controls':controls,'control_count':len(controls),'conditional_only':True}
(P/'DESIGN.json').write_text(json.dumps(c,indent=2)+'\n');(P/'CERTIFICATE.json').write_text(json.dumps(cert,indent=2)+'\n');print(json.dumps({'status':base['status'],'controls':len(controls),'outside_upper_V':base['outside_upper_V'],'sample_RMS_upper_V':base['sample_RMS_upper_V'],'approximation':base['approximation']}))
