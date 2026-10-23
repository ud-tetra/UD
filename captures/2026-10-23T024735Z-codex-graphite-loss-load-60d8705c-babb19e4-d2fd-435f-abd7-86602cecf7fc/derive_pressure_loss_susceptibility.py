"""Conditional pressure response of v20 KC height modes and per-unit loss.

Usage: python3 derive_pressure_loss_susceptibility.py /path/to/minkin_svn.zip [cutoff_A]
The fixed pair roster at each cutoff is inherited from the v20 source.
The public ZIP supplies data and is SHA checked; no code in it is executed.
"""
import contextlib
import hashlib
import io
import json
import runpy
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

ROOT = Path(__file__).resolve().parents[2] if "captures" in Path(__file__).parts else Path(__file__).resolve().parent
SOURCE = next((ROOT / "captures").glob("*graphite-nonlinear-relax-a7f309c2*")) / "derive_nonlinear_graphite_relaxation.py"
ARCHIVE = Path(sys.argv[1]); SHA = "b1ccf62a3e75928e1382cbdd6c669b99675fef9ad5f077e79057a142a0a07875"
RC = float(sys.argv[2]) if len(sys.argv)>2 else 16.
assert hashlib.sha256(ARCHIVE.read_bytes()).hexdigest() == SHA
oldargs = sys.argv; sys.argv = [str(SOURCE), str(ARCHIVE), str(RC)]
try:
    with contextlib.redirect_stdout(io.StringIO()):
        ns = runpy.run_path(str(SOURCE))
finally:
    sys.argv = oldargs

baseq = ns["res"].x.copy(); assert ns["res"].success
base_load = float(ns["load"])
dp_to_dload = float(ns["d"]["Aatom"] * 1000 / 160217.6634)
g = ns["fn"].__globals__
assert abs(g["load"] - base_load) < 1e-12
cart = ns["cart"]; z = ns["z"]; top = ns["top"]; bottom = ns["bottom"]; rc = ns["rc"]; mask = ns["mask"]
bounds = [(cart[0]-.03, cart[0]+.03), (cart[1]-.03, cart[1]+.03)] + [(-.015,.015)]*14
results=[]; blocks={}; secondary={}
for dp in (-5., -2.5, 0., 2.5, 5.):
    g["load"] = base_load + dp * dp_to_dload
    rr = (ns["res"] if dp == 0. else
          minimize(ns["fn"], baseq, jac=ns["grad"], method="L-BFGS-B", bounds=bounds,
                   options={"ftol":1e-15, "gtol":1e-8, "maxiter":300}))
    assert rr.success and max(abs(ns["grad"](rr.x))) < 5e-6, (RC, dp, rr.message, rr.success, max(abs(ns["grad"](rr.x))),rr.nit)
    H = ns["numerical_hess"](rr.x, 1e-4, 1e-3)
    K, C = H[2:,2:], H[:2,2:]
    eig, v = np.linalg.eigh(K)
    assert min(eig)>0
    Y = np.linalg.solve(K,C.T)
    S = C @ Y
    G = Y.T @ Y  # C K^{-2} C^T, dimensionless.
    newmask = np.sum((top[:,None,:]+rr.x[:2]-bottom[None,:,:])**2,axis=-1)+(z+rr.x[2:,None])**2 < rc*rc
    assert np.sum(newmask != mask) == 0
    active = [(j+1,float(eig[j]),float(np.linalg.norm(C @ v[:,j])**2/(2*eig[j]**2)))
              for j in range(14) if np.linalg.norm(C @ v[:,j])**2/(2*eig[j]) > 1e-6]
    blocks[dp]=(K,C,G)
    if dp in (-2.5,0.,2.5):
        H2=ns["numerical_hess"](rr.x,3e-4,3e-3)
        K2,C2=H2[2:,2:],H2[:2,2:]
        Y2=np.linalg.solve(K2,C2.T)
        secondary[dp]=float(np.trace(Y2.T@Y2)/2)
    results.append(dict(delta_pressure_MPa=dp, shifted_load_mev_per_a_per_atom=float(g["load"]),
                        max_stationary_gradient=float(max(abs(ns["grad"](rr.x)))),
                        mean_height_angstrom=float(np.mean(rr.x[2:])),
                        height_min_max_angstrom=[float(min(rr.x[2:])),float(max(rr.x[2:]))],
                        fixed_roster_changed=0, min_height_stiffness=float(min(eig)),
                        active_modes=active,
                        clamped_curvature=float(np.trace(H[:2,:2])/2),
                        static_softening=float(np.trace(S)/2),
                        relaxed_curvature=float(np.trace(H[:2,:2]-S)/2),
                        per_unit_isotropic_rayleigh_coefficient=float(np.trace(G)/2),
                        per_unit_rayleigh_matrix=G.tolist()))
g["load"]=base_load
G0=float(np.trace(blocks[0.][2])/2)
slopes=[]
for width in (2.5,5.):
    centered=(blocks[width][2]-blocks[-width][2])/(2*width)
    slopes.append(dict(half_interval_MPa=width, scalar_slope_per_MPa=float(np.trace(centered)/2),
                       matrix_slope_per_MPa=centered.tolist(),
                       logarithmic_slope_per_MPa=float(np.trace(centered)/2/G0)))

# Product rule at 0 pressure for G=C K^-2 C^T; evaluate K' and C'
# by the centered +/-2.5-MPa stationary Hessians, without relying on
# independent eigenvector phases or nearly degenerate mode labels.
K0,C0,_ = blocks[0.]
Kprime=(blocks[2.5][0]-blocks[-2.5][0])/5.
Cprime=(blocks[2.5][1]-blocks[-2.5][1])/5.
Y0=np.linalg.solve(K0,C0.T)
Yprime_C=np.linalg.solve(K0,Cprime.T)
Yprime_K=-np.linalg.solve(K0,Kprime @ Y0)
term_C=Yprime_C.T@Y0+Y0.T@Yprime_C
term_K=Yprime_K.T@Y0+Y0.T@Yprime_K
check=(np.trace(term_C+term_K)/2)
assert abs(check-slopes[0]["scalar_slope_per_MPa"]) < 2e-6
secondary_slope=(secondary[2.5]-secondary[-2.5])/5.
out=dict(model="v20 fixed-roster nonlinear KC plus D=1.44-eV plate, stationary pressure sweep",
         archive_sha256=SHA, reference_load_mev_per_a_per_atom=base_load,
         cutoff_angstrom=RC,
         pressure_to_load_mev_per_a_per_atom_per_MPa=dp_to_dload,
         conditional_loss_assumption="height Rayleigh D_h=d I; d independent of pressure, unmeasured",
         per_unit_damping_G_definition="C K^-2 C^T dimensionless, gamma_add(P)=d G(P)",
         rows=results, centered_slopes=slopes,
         secondary_hessian_step_check=dict(steps_angstrom=[3e-4,3e-3],
             per_unit_coefficients_at_minus2p5_zero_plus2p5=[secondary[-2.5],secondary[0.],secondary[2.5]],
             centered_slope_per_MPa=secondary_slope),
         product_rule_terms_at_reference_per_MPa=dict(C_variation=float(np.trace(term_C)/2),
             K_variation=float(np.trace(term_K)/2),sum=float(check),
             finite_difference_scalar=slopes[0]["scalar_slope_per_MPa"]),
         diagnostic="No kinetic force law, no UD-specific residual, no measured damping coefficient")
print(json.dumps(out, indent=2))
