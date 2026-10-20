"""Exact sufficient budgets for a proposed sampled CD-1 controller.

All numerical defaults are supplied design inputs. They are not measured
hardware capabilities. The first-order actuator and residual premises must
be established independently before any apparatus decision.
"""
from fractions import Fraction as F
from math import factorial
import json

def encode(x):
    if isinstance(x,F):return {'exact':str(x),'decimal':float(x)}
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,list):return [encode(v) for v in x]
    return x

def certificate(*,period=F(1,400000),latency=F(1,400000),
                input_error=F(1,1000000),command_error=F(1,100000),
                actuator_error=F(1,100000),omega=F(400000),
                initial_tracking=F(1,1000),other_residual=F(3,400),
                actuator_range=F(10),input_bits=22,output_bits=22):
    assert omega>0 and input_bits>0 and output_bits>0
    assert all(v>=0 for v in [period,latency,input_error,command_error,
       actuator_error,initial_tracking,other_residual,actuator_range])
    L=F(97,4);plant_L=F(1);K=L+plant_L;M=F(81,10)
    age=period+latency
    held_error=K*(M*age+input_error)+command_error
    steady=held_error+actuator_error+K*M/omega
    tracking=max(initial_tracking,steady)
    total=other_residual+tracking
    command_max=F(129,16)+plant_L+command_error
    # Reconstructed samples must remain in K. Hence |U(sample)| <= Umax;
    # error q is the complete command-formation error at that input.
    actuator_max=max(F(129,16)+plant_L+initial_tracking,
                     command_max+actuator_error)
    iq=F(1,2**input_bits);oq=F(10,2**output_bits)
    margins={'tracking_allocation':F(1,400)-tracking,
       'total_residual':F(1,100)-total,
       'speed_bootstrap':M-F(129,16)-total,
       'saturation':actuator_range-actuator_max,
       'input_nonquantization_allowance':input_error-iq,
       'command_nonquantization_allowance':command_error-oq}
    return {'status':'PASS_CONDITIONAL_DESIGN' if all(v>0 for v in margins.values()) else 'HOLD_NOT_CERTIFIED',
      'input_kind':'Illustrative supplied bounds; no apparatus observations',
      'physical_promotion':0,'constants':{'target_L':L,'plant_L':plant_L,'command_L':K,'speed':M},
      'inputs':{'period':period,'latency':latency,'input_error':input_error,
        'command_error':command_error,'actuator_distortion':actuator_error,
        'actuator_pole':omega,'initial_tracking_error':initial_tracking,
        'other_residual':other_residual,'actuator_range':actuator_range,
        'input_bits':input_bits,'output_bits':output_bits},
      'max_sample_age':age,'held_command_error':held_error,
      'actuator_lag_error':K*M/omega,'steady_tracking_bound':steady,
      'uniform_tracking_bound':tracking,'total_residual':total,
      'command_range_bound':command_max,'actuator_range_bound':actuator_max,
      'input_quantization':iq,'output_quantization':oq,'margins':margins}

def startup():
    K=F(101,4);r=nu=F(1,1000000);q=ea=F(1,100000)
    # exp(10) exceeds this exact Taylor partial sum, which exceeds 20000.
    partial=sum(F(10**k,factorial(k)) for k in range(25))
    assert partial>20000
    floor=K*(2*r+nu)+q+ea
    bound=F(145,16)/20000+floor
    assert bound==F(4391,8000000) and bound<F(1,1000)
    return {'status':'PASS_CONDITIONAL_DESIGN','assumptions':[
      'zero initial actuator output','state held within r of one fixed center',
      'all sampled true states in the hold tube and all reconstructed arguments in K',
      'same selected law and actuator distortion bound throughout preload',
      'speed at most 81/10 in the input prehistory at release',
      'no unbudgeted switching kick at release'],
      'hold_radius':r,'preload_duration':'10/omega; 1/40000 in the example',
      'exp10_Taylor_lower':partial,'exp10_coarse_lower':20000,
      'tracking_floor':floor,'tracking_bound_at_release':bound}

def selftest():
    z=certificate()
    assert z['uniform_tracking_bound']==F(25267,16000000)
    assert z['total_residual']==F(145267,16000000)
    assert z['margins']['total_residual']==F(14733,16000000)
    assert certificate(period=F(1,1000))['status']=='HOLD_NOT_CERTIFIED'
    assert certificate(omega=F(10000))['status']=='HOLD_NOT_CERTIFIED'
    assert certificate(initial_tracking=F(145,16))['status']=='HOLD_NOT_CERTIFIED'
    assert certificate(input_bits=16)['status']=='HOLD_NOT_CERTIFIED'
    assert certificate(actuator_range=F(9))['status']=='HOLD_NOT_CERTIFIED'
    assert startup()['tracking_bound_at_release']<F(1,1000)
    return {'status':'PASS','exact_controls':9,
      'scope':'Exact algebraic allocations, negative controls and Taylor startup bound; constructor checks only'}

if __name__=='__main__':
    print(json.dumps(encode({'certificate':certificate(),'startup':startup(),
      'controls':selftest(),'negative_examples':{
        'readout_spacing_used_as_control_period':certificate(period=F(1,1000)),
        'insufficient_actuator_bandwidth':certificate(omega=F(10000)),
        'cold_start_without_preload':certificate(initial_tracking=F(145,16)),
        'sixteen_bit_input_quantization':certificate(input_bits=16),
        'insufficient_actuator_range':certificate(actuator_range=F(9))}}),indent=2))
