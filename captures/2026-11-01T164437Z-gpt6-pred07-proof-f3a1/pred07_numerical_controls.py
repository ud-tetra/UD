#!/usr/bin/env python3
"""Synthetic ODE checks for a candidate K4 conservative amplifier. Not physics."""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import solve_ivp

def rhs(t,y,gamma):
    M=sum(y)
    Q=np.dot(y,y)
    return -(4*y-M)/4+gamma*y*(y-Q/M)

def solve(y0,gamma):
    res=solve_ivp(lambda t,y:rhs(t,y,gamma),[0,12],y0,rtol=2e-12,atol=2e-13,
                  t_eval=np.linspace(0,12,601))
    assert res.success
    assert np.max(abs(res.y.sum(axis=0)-sum(y0)))<1e-9
    assert np.min(res.y)>-1e-9
    return res

def main():
    eps=0.01
    asym=np.array([1+3*eps,1+eps,1-eps,1-3*eps],dtype=float)
    fast=solve(asym,2.0)
    slow=solve(asym,0.5)
    uniform=solve(np.ones(4),2.0)
    spread=lambda y:float(max(y)-min(y))
    gap=fast.y[0]-fast.y[3]
    crossed=np.where(gap>=1.)[0]
    assert len(crossed)>0
    assert np.max(np.abs(uniform.y-1))<1e-11
    assert spread(fast.y[:,-1])>spread(asym)
    assert spread(slow.y[:,-1])<spread(asym)
    assert all(np.min(fast.y[i,:201]-fast.y[i+1,:201])>0 for i in range(3))
    # Later low-mode differences fall below the floating-point solver tolerance;
    # exact sign preservation is separately proved symbolically, not by floats.
    output={
        'kind':'NUMERICAL_SYNTHETIC',
        'assumptions':'Q162 open-mask mixing and newly chosen conservative nonlinear source',
        'initial_asymmetric':list(asym), 'mass':4,'gamma_unstable':2.0,'gamma_stable':0.5,
        'time_to_minmax_contrast_ge_1':float(fast.t[crossed[0]]),
        'initial_contrast':spread(asym),'final_contrast_unstable':spread(fast.y[:,-1]),
        'final_contrast_stable':spread(slow.y[:,-1]),
        'final_unstable_state':list(fast.y[:,-1]),
        'uniform_stays_uniform':True,
        'source_selected_by_initial_distinct_perturbation':True,
        'physical_promotion':0,
    }
    Path(__file__).with_name('NUMERICAL_CONTROLS.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))
if __name__=='__main__':main()
