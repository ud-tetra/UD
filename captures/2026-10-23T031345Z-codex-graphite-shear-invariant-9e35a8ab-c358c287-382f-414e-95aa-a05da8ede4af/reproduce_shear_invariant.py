#!/usr/bin/env python3
"""Single-harmonic PES static-strength/shear-frequency ratio audit.

Transcribed inputs are from Lebedeva et al., arXiv:2511.01338,
Tables 4–6. The tabulated strength and frequency share the same PES fit;
this is a replay and rounding audit, not independent empirical validation.
"""
import json
import math

M_C = 12 * 1.66053906892e-27  # kg; specified carbon-12 model
A = 2.4660e-10  # m; lattice parameter stated in the DFT paper
C_CM_PER_S = 2.99792458e10
EV_TO_J = 1.602176634e-19
Q = -(1 + math.sqrt(33)) / 8
C_II = (16 * math.pi / 3) * math.sqrt(1 - Q * Q) * abs(1 + 2 * Q)
C_I = 16 * math.pi / math.sqrt(3)


def ratio(branch, n_cell):
    if branch == "II":
        return (C_II / 2) * M_C * C_CM_PER_S**2 / (A * math.sqrt(n_cell))
    return (C_I / 4) * M_C * C_CM_PER_S**2 / (A * math.sqrt(n_cell))


def forward_from_u1(branch, n_cell, u1_micro_eV):
    u = abs(u1_micro_eV) * 1e-6 * EV_TO_J
    f_cm = math.sqrt((2 if branch == "II" else 4) * n_cell * u / M_C) / A / C_CM_PER_S
    tau_pa = (C_II if branch == "II" else C_I) * math.sqrt(n_cell) * u / A**3
    return f_cm, tau_pa


def main():
    cases = [
        ("2_1_rigid", "II", 7, 0.0793, 0.404, 1.39e4),
        ("2_1_out_of_plane", "II", 7, 0.126, 0.510, 2.20e4),
        ("2_1_two_atoms_constrained", "II", 7, 0.169, 0.590, 2.95e4),
        ("3_1_rigid", "I", 13, -0.00598, 0.214, 6.68e3),
    ]
    rows = []
    for name, branch, n_cell, u1, table_f, table_tau in cases:
        f, tau = forward_from_u1(branch, n_cell, u1)
        from_rounded_f = ratio(branch, n_cell) * table_f**2
        rows.append({"case": name, "branch": branch, "N_c": n_cell,
                     "U1_micro_eV_per_upper_atom": u1,
                     "ratio_Pa_per_cm_inverse_squared": ratio(branch, n_cell),
                     "frequency_from_U1_cm_inverse": f,
                     "strength_from_U1_Pa": tau,
                     "published_frequency_cm_inverse": table_f,
                     "published_strength_Pa": table_tau,
                     "strength_from_rounded_frequency_Pa": from_rounded_f,
                     "rounded_table_relative_delta": table_tau / from_rounded_f - 1})
        assert abs(table_tau / from_rounded_f - 1) < 0.005
    assert 6.182 < C_II < 6.184
    print(json.dumps({"constants": {"carbon_12_mass_kg": M_C,
                                    "lattice_a_m": A, "c_cm_per_s": C_CM_PER_S,
                                    "type_II_strength_coefficient": C_II,
                                    "type_I_strength_coefficient": C_I},
                      "cases": rows,
                      "scope": "Single-harmonic infinite-cell static area shear strength and two-mobile-layer rigid shear frequency; no dynamic friction or UD-specific effect inferred."}, indent=2) + "\n")


if __name__ == "__main__":
    main()
