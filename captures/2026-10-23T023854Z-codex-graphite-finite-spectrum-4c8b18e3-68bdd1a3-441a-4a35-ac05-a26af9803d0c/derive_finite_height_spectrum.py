"""Replay the v20 stationary Hessian and audit its finite conservative spectrum.

Usage: python3 derive_finite_height_spectrum.py /path/to/minkin_svn.zip [cutoff_A]
Only code in the UD repository is executed; the source ZIP is read as data by v19.
"""
import contextlib
import hashlib
import io
import json
import runpy
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2] if "captures" in Path(__file__).parts else Path(__file__).resolve().parent
SOURCE = next((ROOT / "captures").glob("*graphite-nonlinear-relax-a7f309c2*")) / "derive_nonlinear_graphite_relaxation.py"
ARCHIVE = Path(sys.argv[1])
RC = float(sys.argv[2]) if len(sys.argv) > 2 else 16.0
SOURCE_SHA = "b1ccf62a3e75928e1382cbdd6c669b99675fef9ad5f077e79057a142a0a07875"
assert hashlib.sha256(ARCHIVE.read_bytes()).hexdigest() == SOURCE_SHA
args = sys.argv
sys.argv = [str(SOURCE), str(ARCHIVE), str(RC)]
try:
    with contextlib.redirect_stdout(io.StringIO()):
        ns = runpy.run_path(str(SOURCE))
finally:
    sys.argv = args
assert ns["res"].success
H = ns["numerical_hess"](ns["res"].x, 1e-4, 1e-3)
K, C = H[2:, 2:], H[:2, 2:]
k, V = np.linalg.eigh(K)
assert min(k) > 0
B = C @ V

# Ebar is energy per 14 upper atoms. The kinetic term in this normalization
# is (m_C/28) sum_j dot(h_j)^2, hence Mbar = m_C/14 for each h_j.
u_kg = 1.66053906892e-27  # NIST 2022 CODATA; illustrative isotope 12C.
mev_per_a2_to_n_per_m = 1.602176634e-2
f_thz = np.sqrt(14 * k * mev_per_a2_to_n_per_m / (12 * u_kg)) / (2 * np.pi * 1e12)
soft = np.einsum("ij,kj->ik", B / k, B)
inv2 = np.einsum("ij,kj->ik", B / (k * k), B)
rows = []
for j in range(14):
    rows.append(dict(mode=j + 1,
                     height_stiffness_mev_per_a2_per_mean_atom=float(k[j]),
                     illustrative_12C_frequency_THz=float(f_thz[j]),
                     lateral_coupling_squared=float(B[:, j] @ B[:, j]),
                     isotropic_static_softening_mev_per_a2_per_mean_atom=float(B[:, j] @ B[:, j] / (2 * k[j])),
                     scalar_rayleigh_coefficient_per_unit_d=float(B[:, j] @ B[:, j] / (2 * k[j] ** 2))))
H2 = ns["numerical_hess"](ns["res"].x, 3e-4, 3e-3)
K2, C2 = H2[2:, 2:], H2[:2, 2:]
k2, V2 = np.linalg.eigh(K2)
B2 = C2 @ V2
soft2 = C2 @ np.linalg.solve(K2, C2.T)
inv22 = C2 @ np.linalg.solve(K2, np.linalg.solve(K2, C2.T))
out = dict(model="v20 stationary 14-height finite conservative KC plus plate, fixed pair roster",
           provenance_archive_sha256=SOURCE_SHA,
           cutoff_angstrom=RC,
           mass_assumption="one 12C nucleus per mobile upper atom; lower layer fixed; mass only converts model eigenvalues to frequencies",
           mode_rows=rows,
           height_stiffness_min_max=[float(min(k)), float(max(k))],
           static_softening_matrix=soft.tolist(),
           static_softening_scalar=float(np.trace(soft) / 2),
           static_softening_direct=(C @ np.linalg.solve(K, C.T)).tolist(),
           scalar_rayleigh_coefficient_per_unit_d=float(np.trace(inv2) / 2),
           rayleigh_coefficient_matrix_per_unit_d=inv2.tolist(),
           low_frequency_ohmic_coefficient_closed_finite_harmonic=0.0,
           sum_static_softening_from_rows=float(sum(r["isotropic_static_softening_mev_per_a2_per_mean_atom"] for r in rows)),
           sum_rayleigh_from_rows=float(sum(r["scalar_rayleigh_coefficient_per_unit_d"] for r in rows)),
           hessian_step_angstrom=[1e-4, 1e-3])
out["second_hessian_step_check"] = dict(hessian_step_angstrom=[3e-4, 3e-3],
           active_mode_numbers=[j + 1 for j in range(14) if (B2[:, j] @ B2[:, j] / (2 * k2[j])) > 1e-6],
           active_mode_stiffness=[float(k2[j]) for j in range(14) if (B2[:, j] @ B2[:, j] / (2 * k2[j])) > 1e-6],
           static_softening_scalar=float(np.trace(soft2) / 2),
           scalar_rayleigh_coefficient_per_unit_d=float(np.trace(inv22) / 2))
assert np.allclose(soft, C @ np.linalg.solve(K, C.T), rtol=1e-12, atol=1e-12)
assert np.allclose(soft, np.einsum("ij,kj->ik", B / k, B), rtol=1e-12)
assert abs(sum(r["isotropic_static_softening_mev_per_a2_per_mean_atom"] for r in rows) - np.trace(soft) / 2) < 1e-10
print(json.dumps(out, indent=2))
