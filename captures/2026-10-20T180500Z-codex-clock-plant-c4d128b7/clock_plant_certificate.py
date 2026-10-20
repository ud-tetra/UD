"""Exact clock/plant and alternative component-budget checks.
Supplier limits are conditional specifications, not measurements. Budget
obstructions apply to the inherited sufficient controller certificate.
"""
from fractions import Fraction as F
import json
def encode(x):
    if isinstance(x,F):return {'exact':str(x),'decimal':float(x)}
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,list):return [encode(v) for v in x]
    return x
def report():
    K=F(101,4);M=F(81,10);nu=F(1,100000);q=F(1,25000)
    b=K*(M*F(1,200000)+nu)+q+F(1,100000)+K*M/400000
    total=F(3,400)+max(F(1,1000),b)
    warm=F(145,16)/20000+K*(F(2,1000000)+nu)+q+F(1,100000)
    dac_quant=F(10,2**20);dac_inl=F(20,2**20)
    adc_inl=F(2)*F(2,1000000)
    output_period=F(1024,1000000);moment=F(512,1000000);processing=F(100,1000000)
    t0_min=400000*max(output_period,moment+processing)
    assert b==F(29383,16000000)
    assert total==F(149383,16000000)
    assert F(1,100)-total==F(10617,16000000)
    assert warm==F(6449,8000000) and warm<F(1,1000)
    assert dac_quant+dac_inl==F(15,524288) and dac_quant+dac_inl<q
    assert adc_inl<nu
    assert t0_min==F(2048,5)
    assert t0_min**2==F(4194304,25) and t0_min**2>1
    assert M*F(1,625)==F(81,6250)>F(1,400)
    weights=[F(2),F(-2),F(1)];ages=[F(0),F(1),F(2)]
    assert sum(weights)==1 and sum(w*a for w,a in zip(weights,ages))==0
    assert sum(abs(w)*a for w,a in zip(weights,ages))==4
    return {
      'status':'PASS_CONDITIONAL_MATHEMATICS_HARDWARE_HOLD','physical_promotion':0,
      'alternative_budget':{'input_error':nu,'command_error':q,'tracking':b,
       'total_residual':total,'slack':F(1,100)-total,'preload_tracking_upper':warm,
       'endpoint_Gauss_parameters_unchanged':True},
      'supplier_screen':{'AD5791B_quantization_plus_INL':dac_quant+dac_inl,
       'AD5791B_other_error_allowance':q-dac_quant-dac_inl,
       'AD5791B_conditions':'+/-10V references; B grade; 0 to 105 C; affine errors independently calibrated',
       'LTC2500_32_INL_normalized':adc_inl,
       'LTC2500_32_other_input_error_allowance':nu-adc_inl,
       'note':'Neither remaining allowance has been empirically demonstrated'},
      'clock_screen':{'output_period_seconds':output_period,
       'assumed_absolute_filter_moment_seconds':moment,'assumed_other_latency_seconds':processing,
       'required_t0_lower_seconds':t0_min,'required_each_LC_product_seconds_squared':t0_min**2,
       'illustrative_t0_seconds':F(512),'LC_at_illustrative_t0_seconds_squared':F(512)**2,
       'illustrative_prefix_seconds':F(512,100),'LC_le_one_seconds_squared_has_no_clock_overlap':True},
      'certificate_floor_example':{'scope':'Inherited conservative L+lambda certificate; not a lower bound on actual physical error',
       'A_seconds_lower':F(1,625),'r_seconds_upper':F(1),'clock_independent_cost_lower':M*F(1,625),
       'tracking_allocation':F(1,400),'fails_this_sufficient_allocation':True},
      'controls':{'status':'PASS','exact_controls':10,'constructor_only':True},
      'hardware_status':'HOLD: canonical scales, calibrated residuals, finite-record identification, noise/latency coverage and independent review OPEN'}
if __name__=='__main__':print(json.dumps(encode(report()),indent=2))
