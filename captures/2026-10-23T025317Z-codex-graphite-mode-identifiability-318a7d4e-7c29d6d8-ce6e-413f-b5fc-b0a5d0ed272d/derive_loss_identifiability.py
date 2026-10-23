"""Audit identifiability of two active KC height-loss doublets.

Reads immutable v21/v22 numerical captures, not the experimental force data.
No fitted damping coefficient or measured linewidth is supplied.
"""
import json
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parents[2] if "captures" in Path(__file__).parts else Path(__file__).resolve().parent
v21=next((ROOT/'captures').glob('*graphite-finite-spectrum-4c8b18e3*'))
v22=next((ROOT/'captures').glob('*graphite-loss-load-60d8705c*'))
spec=json.loads((v21/'FINITE_HEIGHT_SPECTRUM_16A.json').read_text())
out={'model':'two E-doublet per-unit-loss identifiability, conditional v21/v22 finite KC model',
     'source_captures':[v21.name,v22.name], 'status':'conditional numerical design, not experimental friction'}
pressure={}
for rc in (14,16,18):
    x=json.loads((v22/f'PRESSURE_LOSS_{rc}A_RESULTS.json').read_text())
    P=np.array([r['delta_pressure_MPa'] for r in x['rows']])
    A=np.array([[sum(m[2] for m in r['active_modes'][:2]),
                 sum(m[2] for m in r['active_modes'][2:])] for r in x['rows']])
    assert np.allclose(A.sum(axis=1),[r['per_unit_isotropic_rayleigh_coefficient'] for r in x['rows']],rtol=1e-10)
    normalized=A/np.linalg.norm(A,axis=0)[None,:]
    pressure[str(rc)]={'pressure_MPa':P.tolist(), 'mode_pair_coefficients':A.tolist(),
                       'raw_two_parameter_condition':float(np.linalg.cond(A)),
                       'unit_column_condition':float(np.linalg.cond(normalized)),
                       'unit_column_singular_values':np.linalg.svd(normalized)[1].tolist(),
                       'ratio_at_minus5_and_plus5':[float(A[0,0]/A[0,1]),float(A[-1,0]/A[-1,1])],
                       'coefficient_log_slopes_per_MPa':[(float((A[3,j]-A[1,j])/5/A[2,j])) for j in range(2)]}
out['pressure_only_identifiability']=pressure

# The two rotationally equivalent modes in each active E doublet sum to
# a scalar lateral residue. Per pair: a_i = r_i/kappa_i^2, where a_i is
# the dimensionless coefficient multiplying an independent Rayleigh d_i.
rows=spec['mode_rows']; pair_indices=((4,5),(7,8))
doublets=[]
for inds in pair_indices:
    k=float(sum(rows[i]['height_stiffness_mev_per_a2_per_mean_atom'] for i in inds)/2)
    r=float(sum(rows[i]['lateral_coupling_squared'] for i in inds)/2)
    a=r/k**2
    doublets.append({'mode_numbers':[i+1 for i in inds], 'height_stiffness':k,
                     'scalar_lateral_residue':r, 'per_unit_dc_loss_weight':a,
                     'illustrative_frequency_THz':float(sum(rows[i]['illustrative_12C_frequency_THz'] for i in inds)/2)})
assert abs(sum(d['per_unit_dc_loss_weight'] for d in doublets)-sum(pressure['16']['mode_pair_coefficients'][2]))<2e-11
k1,k2=[d['height_stiffness'] for d in doublets]
f1,f2=[d['illustrative_frequency_THz'] for d in doublets]

# Weak-loss spectral measurement at omega=0 and omega=2 omega_1.
# Unknowns t_i=a_i d_i are channel contributions to the DC loss.
frequency_ratio=2.0
factors=[1/(1-frequency_ratio**2*k1/k)**2 for k in (k1,k2)]
F=np.array([[1.,1.],factors])
out['two_frequency_weak_loss_design']={'doublets':doublets,
    'measurement_frequencies_model_THz':[0.,frequency_ratio*f1],
    'measurement_frequency_ratio_to_first_active_pole':frequency_ratio,
    'unknowns':'t_i=a_i*d_i, mode-pair contributions to DC damping',
    'normalized_measurement_matrix':F.tolist(),
    'matrix_determinant':float(np.linalg.det(F)),
    'two_norm_condition_in_t_coordinates':float(np.linalg.cond(F)),
    'equal_weight_nonzero_frequency_model_THz':float(f1*np.sqrt(2*k2/(k1+k2))),
    'weak_loss_requirement':'|omega*d_i| much smaller than |kappa_i-mu*omega^2| at both samples',
    'observable':'Im Sigma(omega)/omega from a calibrated dynamic lateral susceptibility, conventional background separately measured'}
print(json.dumps(out,indent=2))
