"""Exact arithmetic for a proposed short-window CD-1 certificate.

Inputs are certified bounds that an apparatus return must supply. Defaults
are a mathematical design example, not measured calibration or experiment.
"""
from fractions import Fraction as F
import json

def encode(x):
    if isinstance(x,F):return {'exact':str(x),'decimal':float(x)}
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,list):return [encode(v) for v in x]
    return x

def certificate(*,e0=F(1,10000),measurement=F(1,10000),delta=F(1,100),
                h=F(1,100),clock=F(1,100000),age=F(1,100000),
                plant_L=F(1),node=F(1,400),grid=F(1,400),other=F(1,400)):
    L=F(97,4); LG=F(6); M=F(81,10); hmin=h-clock; hmax=h+clock
    assert all(x>=0 for x in [e0,measurement,delta,clock,age,plant_L,node,grid,other])
    assert hmin>0 and L*hmax<1
    eta=(e0+delta*hmax)/(1-L*hmax)
    # Sup error of the measured drift interval's certified endpoint:
    # state transfer contributes LG*(eta+e0), measurement is counted twice
    # because a robust PASS/FAIL uses |observed drift| +/- interval radius.
    measurement_drift_radius=2*LG*measurement
    B=LG*(eta+e0)+2*measurement_drift_radius
    q_wrong=2*hmin-8*hmin*hmin-F(11,8)*hmin**3
    q_frozen=2*hmin-F(8,3)*hmin**3
    gate_lower=F(1,100)*(1+hmin)
    gate_upper=F(1,100)*(1+hmax)
    delay=(L+plant_L)*M*age
    total=node+grid+delay+other
    age_cap=F(1,400)/((L+plant_L)*M)
    tube=F(3,4)+3*hmax+eta+measurement
    margins={'nominal_pass':gate_lower-B,'wrong_species_fail':q_wrong-B-gate_upper,
             'frozen_electric_fail':q_frozen-B-gate_upper,
             'initial_Gauss_gate':F(1,100)-LG*e0-2*LG*measurement,
             'tube':1-tube,'residual_budget':delta-total,
             'delay_allocation':F(1,400)-delay}
    okay=all(v>0 for v in margins.values())
    return {'status':'PASS_CONDITIONAL_DESIGN' if okay else 'HOLD_NOT_CERTIFIED',
      'input_kind':'illustrative certified-bound inputs; no apparatus data',
      'physical_promotion':0,
      'inputs':{'initial_error':e0,'snapshot_error':measurement,'vectorfield_defect':delta,
       'nominal_window':h,'clock_radius':clock,'control_age':age,'plant_L':plant_L,
       'aggregate_calibration_node_bound':node,'aggregate_grid_bound':grid,
       'unmodeled_bound':other},
      'constants':{'vectorfield_L':L,'Gauss_L':LG,'speed_M':M},
      'hmin':hmin,'hmax':hmax,'trajectory_error':eta,
      'decision_error_B':B,'wrong_sign_ideal_drift_lower':q_wrong,
      'frozen_electric_ideal_drift_lower':q_frozen,
      'CD1_gate_lower':gate_lower,'CD1_gate_upper':gate_upper,
      'max_age_for_delay_allocation':age_cap,'delay_bound':delay,
      'total_defect_bound':total,'margins':margins}

def selftest():
    base=certificate()
    assert base['status']=='PASS_CONDITIONAL_DESIGN'
    assert base['max_age_for_delay_allocation']==F(1,81810)
    assert certificate(measurement=F(1,1000))['status']=='HOLD_NOT_CERTIFIED'
    assert certificate(age=F(1,1000))['status']=='HOLD_NOT_CERTIFIED'
    # Check the exact zero-clock simplification independently.
    z=certificate(clock=F(0),delta=F(1,1000))
    assert z['decision_error_B']==F(391,101000)
    # Finite scalar samples cannot bound between-node residual without a
    # derivative bound: P(x)=A*product(x-gridpoint) vanishes on each node.
    nodes=[F(-1),F(0),F(1)]
    def bump(x,A):return A*(x+1)*x*(x-1)
    assert all(bump(x,F(1000))==0 for x in nodes)
    assert abs(bump(F(1,2),F(1000)))==F(375)
    return {'status':'PASS','exact_controls':7,
            'scope':'Arithmetic and finite-sampling obstruction controls; not independent review'}

if __name__=='__main__':
    output={'certificate':certificate(),'controls':selftest(),
      'negative_examples':{'too_coarse_metrology':certificate(measurement=F(1,1000)),
                           'control_update_at_readout_interval':certificate(age=F(1,1000))}}
    print(json.dumps(encode(output),indent=2))
