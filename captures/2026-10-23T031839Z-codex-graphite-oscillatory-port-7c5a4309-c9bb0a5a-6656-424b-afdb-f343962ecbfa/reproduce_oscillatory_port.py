#!/usr/bin/env python3
"""Unit and normalization replay of the conditional local loss port.

This uses v22/v23 KC plus plate model coefficients; it does not fit a
graphite linewidth, pressure law, or measured sliding friction.
"""
import json
import math

N_UPPER = 14
G = 5.28544758e-4
G_PRIME_PER_MPA = 4.260349e-7
A_MEAS_ANG = 0.01
OMEGA_RAD_PER_PS = 1.0
M_C_KG = 12 * 1.66053906892e-27
MEV_J = 1.602176634e-22
M_PER_ANG = 1e-10
S_PER_PS = 1e-12


def main():
    # Mean-energy normalized height mode: Tbar=(m_C/28)*sum hdot_i^2.
    mode_mass_mev_ps2_ang2 = (M_C_KG / N_UPPER) * M_PER_ANG**2 / S_PER_PS**2 / MEV_J
    # FWHM of a weak isolated damped oscillator: Delta_omega=d/mu.
    d_per_1_thz_linewidth = mode_mass_mev_ps2_ang2 * 2 * math.pi
    # If d=1 meV ps / Ang^2 per upper atom, these are per 14-atom cell.
    gamma_per_unit_d = N_UPPER * G
    quadrature_force = gamma_per_unit_d * OMEGA_RAD_PER_PS * A_MEAS_ANG
    dissipated_mev_per_cycle = math.pi * gamma_per_unit_d * OMEGA_RAD_PER_PS * A_MEAS_ANG**2
    si_gamma_per_unit_d = gamma_per_unit_d * (MEV_J / M_PER_ANG**2) * S_PER_PS
    result = {
        "conditional_KC_plate_input": {"upper_atoms_per_cell": N_UPPER,
                                         "G_dimensionless_per_atom": G,
                                         "G_prime_per_MPa": G_PRIME_PER_MPA,
                                         "reference_pressure_MPa_compression_positive": -10.734},
        "units": {"d": "meV ps Angstrom^-2 per mean upper atom",
                  "gamma_cell": "meV ps Angstrom^-2 per 14-upper-atom cell",
                  "drive_angular_frequency": "rad ps^-1",
                  "drive_amplitude": "Angstrom"},
        "illustrative_drive": {"amplitude_Angstrom": A_MEAS_ANG,
                               "angular_frequency_rad_per_ps": OMEGA_RAD_PER_PS},
        "per_d_equal_1": {"gamma_cell_meV_ps_Angstrom_minus2": gamma_per_unit_d,
                          "gamma_cell_kg_per_s": si_gamma_per_unit_d,
                          "quadrature_force_meV_per_Angstrom": quadrature_force,
                          "dissipated_energy_meV_per_cycle": dissipated_mev_per_cycle},
        "one_mode_orthonormal_height_mass": {"kg_in_mean_energy": M_C_KG / N_UPPER,
                                               "meV_ps2_Angstrom_minus2": mode_mass_mev_ps2_ang2,
                                               "d_per_1_THz_FWHM_meV_ps_Angstrom_minus2": d_per_1_thz_linewidth},
        "flat_conditional_gamma_requires_d_log_slope_per_MPa": -G_PRIME_PER_MPA / G,
        "boundary": "Oscillatory linear loss around one minimum, not sliding across cells; no physical damping coefficient or measured friction is supplied."
    }
    assert abs(result["per_d_equal_1"]["dissipated_energy_meV_per_cycle"] / quadrature_force - math.pi * A_MEAS_ANG) < 1e-15
    print(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
