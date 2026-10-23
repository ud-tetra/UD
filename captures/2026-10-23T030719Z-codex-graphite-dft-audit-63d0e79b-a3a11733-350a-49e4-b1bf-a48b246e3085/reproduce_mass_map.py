#!/usr/bin/env python3
"""Reproduce the collective mass mapping and published frequency inversion.

Only standard-library constants and explicitly transcribed published inputs are
used. This checks units; it does not execute a material simulation.
"""
import json
import math

U_KG = 1.66053906892e-27
M_C = 12 * U_KG  # exact isotope choice for the model, not natural abundance
MEV_PER_ANG2_TO_N_PER_M = 1.602176634e-2
C_CM_PER_S = 2.99792458e10


def wavenumber(k_mev_a2, moving_layers):
    effective_mass = M_C / moving_layers
    return math.sqrt(k_mev_a2 * MEV_PER_ANG2_TO_N_PER_M / effective_mass) / (2 * math.pi * C_CM_PER_S)


def inverse_curvature(nu_cm, moving_layers=2):
    effective_mass = M_C / moving_layers
    return (2 * math.pi * C_CM_PER_S * nu_cm) ** 2 * effective_mass / MEV_PER_ANG2_TO_N_PER_M


def main():
    clamped, relaxed = 1.911869, 1.6825303207477915
    published = {
        "minkin_2023_KC_fixed_height": 9.153,
        "lebedeva_2025_vdW_DF3_rigid": 0.404,
        "lebedeva_2025_vdW_DF3_out_of_plane": 0.510,
        "lebedeva_2025_vdW_DF3_two_atoms_constrained": 0.590,
    }
    result = {
        "constants": {"carbon_12_kg": M_C, "mev_Aminus2_to_N_per_m": MEV_PER_ANG2_TO_N_PER_M, "c_cm_per_s": C_CM_PER_S},
        "collective_14_atom_energy": "E=14*(k_per_upper_atom*x*x/2); mass_relative=7*m_C if both 14-atom layers move, mass_fixed=14*m_C",
        "our_KC_plate": {name: {"k_meV_per_A2_per_upper_atom": k,
                                 "nu_fixed_lower_cm_minus1": wavenumber(k, 1),
                                 "nu_both_mobile_cm_minus1": wavenumber(k, 2)}
                         for name, k in (("clamped", clamped), ("relaxed_height", relaxed))},
        "published_comparators": {name: {"nu_both_mobile_cm_minus1": nu,
                                         "curvature_inverted_meV_per_A2_per_upper_atom": inverse_curvature(nu)}
                                  for name, nu in published.items()},
        "comparisons": {
            "our_relaxed_vs_minkin_KC_frequency_ratio": wavenumber(relaxed, 2) / published["minkin_2023_KC_fixed_height"],
            "our_relaxed_vs_DFT_out_of_plane_curvature_ratio": relaxed / inverse_curvature(0.510),
            "KC_Minkin_vs_DFT_rigid_frequency_ratio": 9.153 / 0.404,
        },
        "sources": ["https://arxiv.org/pdf/2308.06302 Eq(4), Table II", "https://arxiv.org/pdf/2511.01338 Tables 2, 4, 6"],
        "caveat": "Curvature inversions are a common-unit comparison of differing models and reference separations; no friction rate, measured shear frequency, or UD residual follows.",
    }
    assert abs(result["our_KC_plate"]["relaxed_height"]["nu_both_mobile_cm_minus1"] - 8.73244584553223) < 1e-10
    assert result["our_KC_plate"]["clamped"]["nu_both_mobile_cm_minus1"] > result["our_KC_plate"]["relaxed_height"]["nu_both_mobile_cm_minus1"]
    print(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
