#!/usr/bin/env python3
"""Conditional overdamped force-observable counterexample for graphite paper.

Inputs Delta and Delta' are the reconstructed local two-shell equilibrium
numbers; the one-dimensional sinusoid is a declared illustrative surrogate.
Gamma and speed are illustrative and are not inferred from Chen et al.
"""
import json
import math

from scipy.integrate import quad

barrier_microev = 75.18
barrier_slope_microev_per_mpa = 0.033228
period_a = 0.9296082124053275
area_atom_a2 = math.sqrt(3) * (math.sqrt(3) * 1.42)**2 / 4
shear_mpa_per_microev_per_a = 0.1602176634 / area_atom_a2
fc = math.pi * barrier_microev / period_a
fc_prime = math.pi * barrier_slope_microev_per_mpa / period_a

def force(pressure, u):
    critical = fc + fc_prime * pressure
    # gamma*v is held at its zero-pressure reference value u*fc.
    return math.hypot(critical, u * fc)

def speed_from_integral(force_value, critical):
    # Set gamma=1 in consistent reduced units; speed has force units.
    integral, _ = quad(lambda theta: 1 / (force_value - critical * math.sin(theta)),
                       0, 2 * math.pi, epsabs=1e-10, epsrel=1e-10)
    return 2 * math.pi / integral

rows = []
for u in (0.1, 1, 10):
    drive = force(0, u)
    analytic = fc_prime / math.sqrt(1 + u * u)
    finite = (force(0.1, u) - force(-0.1, u)) / 0.2
    speed = speed_from_integral(drive, fc)
    assert abs(speed / (u * fc) - 1) < 1e-10
    assert abs(finite / analytic - 1) < 1e-7
    # At the reference load, keeping v fixed while varying gamma locally:
    # dF/dP = (Fc*Fc' + gamma*gamma'*v²)/F.
    # gamma=1, v=u*Fc. Setting this zero defines a valid local positive gamma.
    log_gamma_prime_zero_total = -fc_prime / (u * u * fc)
    # For excess F-gamma*v, instead set d(F-gamma*v)/dP=0.
    log_gamma_prime_zero_excess = fc * fc_prime / ((u * fc) * (drive - u * fc))
    assert abs(fc*fc_prime + log_gamma_prime_zero_total * (u*fc)**2) < 1e-10
    excess_derivative = (fc*fc_prime + log_gamma_prime_zero_excess * (u*fc)**2) / drive - log_gamma_prime_zero_excess * (u*fc)
    assert abs(excess_derivative) < 1e-10
    rows.append(dict(reduced_speed_gamma_v_over_fc=u,
                     drive_force_microev_per_a_per_atom=drive,
                     excess_force_microev_per_a_per_atom=drive - u * fc,
                     load_slope_microev_per_a_per_atom_per_mpa=analytic,
                     load_slope_shear_mpa_per_mpa=analytic * shear_mpa_per_microev_per_a,
                     ratio_to_depinning_slope=analytic / fc_prime,
                     log_gamma_slope_per_mpa_for_zero_total_force_slope=log_gamma_prime_zero_total,
                     log_gamma_slope_per_mpa_for_zero_excess_force_slope=log_gamma_prime_zero_excess))

print(json.dumps(dict(status="EXACT_CONDITIONAL_WASHBOARD_WITH_NUMERICAL_QUADRATURE_CHECK",
                      input_status="Two-shell barrier and local load derivative are a qualified conventional KC reconstruction, not experimental friction.",
                      model="U(x,P)=Delta(P)/2*(1-cos(2*pi*x/ell)); gamma(P)*dx/dt=F-∂xU; constant-force, deterministic, overdamped, 1D, F>Fc.",
                      barrier_microev_per_atom=barrier_microev,
                      barrier_slope_microev_per_atom_per_mpa=barrier_slope_microev_per_mpa,
                      period_a=period_a,
                      depinning_force_microev_per_a_per_atom=fc,
                      depinning_force_slope_microev_per_a_per_atom_per_mpa=fc_prime,
                      depinning_shear_mpa=fc * shear_mpa_per_microev_per_a,
                      estimator_note="F is total drive force; F-gamma*v is excess over bare drag; these are distinct load slopes if gamma depends on pressure.",
                      rows=rows, physical_promotion=0), indent=2))
