#!/usr/bin/env python3
"""Synthetic normalized ODE control; NOT measured dynamics or physical evidence."""
import json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp

def run(gamma=2.,R_before=2.,R_scale=1.,eps=0.1,t_end=20.):
    initial=np.array([1+eps,1-eps,1,1,R_before-eps**2,0.],dtype=float)
    assert initial[4]>=0
    def rhs(t,y):
        b=y[:4]; R=max(y[4],0.);M=b.sum();Q=float(b@b)
        u=R/(R+R_scale)
        A=float(np.sum(b**3)-Q**2/M)
        return np.r_[M/4-b+u*gamma*b*(b-Q/M),-u*gamma*A,float(np.sum((b-M/4)**2))]
    sol=solve_ivp(rhs,(0,t_end),initial,rtol=1e-11,atol=1e-13,dense_output=True)
    assert sol.success
    data=[]
    for t in (0.,.2,.5,1.,2.,3.,5.,10.,20.):
        if t>t_end:continue
        z=sol.sol(t);b=z[:4];V=float(np.sum((b-b.mean())**2)/2)
        data.append({'model_time':t,'max_min_burden_gap':float(max(b)-min(b)),
                    'contrast_V':V,'reserve_R':float(z[4]),
                    'dissipation_D':float(z[5]),'ledger_total':V+z[4]+z[5]})
    worst=max(abs(z['ledger_total']-R_before) for z in data)
    assert worst<1e-7,worst
    return {'model':'finite-stock conservative K4 candidate (not native UD constitutive law)',
            'parameters':{'M':'4','gamma':'2','reserve_before_stochastic_seed':'2','reserve_scale':'1','epsilon':'1/10'},
            'synthetic_only':True,'ledger_max_error':worst,'observations':data,'physical_promotion':0}
if __name__=='__main__':
    result=run()
    Path(__file__).with_name('NUMERICAL_CONTROL.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'synthetic_only':True,'ledger_error':result['ledger_max_error'],
          'contrast_t3':result['observations'][5]['max_min_burden_gap'],
          'contrast_t20':result['observations'][-1]['max_min_burden_gap']},indent=2))
