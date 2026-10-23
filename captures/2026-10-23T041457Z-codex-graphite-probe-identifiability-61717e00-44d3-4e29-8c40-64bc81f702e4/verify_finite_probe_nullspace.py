#!/usr/bin/env python3
"""Check the conditional finite-probe algebraic nullspace numerically."""
import json
import math

KY = 2*math.pi*math.sqrt(7)/(math.sqrt(3)*2.4660)
U1 = .0793396654
HS = (.04, .08)
SADDLE = (5*math.pi/2, 3*math.pi/2)
Q0 = -1.


def f(u, v):
    return 2*math.cos(v)*math.cos(u)+math.cos(2*v)


def F(u, v):
    return (1-math.cos(u-3*v))*(1-math.cos(u+3*v))*(1-math.cos(2*u))


def g(u, v):
    q = f(u, v)
    scale = 1.
    for h in HS:
        beta = math.sqrt(3)*KY*h
        qh = Q0+4*math.sin(beta/2)**2
        scale *= ((q-qh)/(Q0-qh))**2
    return F(u, v)*scale


def point(h):
    beta = math.sqrt(3)*KY*h
    return SADDLE[0]+beta/2, SADDLE[1]-beta/2


def derivative(h, step=1e-7):
    u1, v1 = point(h+step)
    u2, v2 = point(h-step)
    return (g(u1, v1)-g(u2, v2))/(2*step)


def main():
    line_max = max(abs(g(3*math.pi*j/36, 2*math.pi/3+math.pi*j/36)) for j in range(37))
    values = [{"h_A": h, "G": g(*point(h)), "normal_derivative_numeric": derivative(h)} for h in (0.,-.08,-.04,.04,.08)]
    # G(h) = 24*k_y^2*h^2 + O(h^3) at the saddle: its second derivative is 48*k_y^2.
    h = 1e-5
    hess = (g(*point(h))+g(*point(-h))-2*g(*point(0)))/h**2
    target = 48*KY**2
    a, b = HS
    alpha = b*b/(a*a*(b*b-a*a))
    beta = -a*a/(b*b*(b*b-a*a))
    noise_multiplier = math.sqrt(6*alpha**2+6*beta**2+8*alpha*beta)
    truncation_multiplier = (b*b*a**4+a*a*b**4)/(360*(b*b-a*a))
    def model_delta(h, eps_ratio):
        q = math.sqrt(3)*KY*h
        fh = 4*math.sin(q/2)**2
        Fh = (1-math.cos(2*q))*(1+math.cos(q))**2
        return 2*U1*(fh+eps_ratio*Fh)
    illustrative_extrapolation = alpha*model_delta(a,-.2)+beta*model_delta(b,-.2)
    assert line_max < 1e-12
    assert all(abs(v["G"]) < 1e-12 and abs(v["normal_derivative_numeric"]) < 1e-6 for v in values)
    assert abs(hess-target)/target < 1e-6
    print(json.dumps({"status": "PASS_NUMERIC_WITH_EXACT_ALGEBRA_IN_NOTE",
                      "sample_line_max_abs": line_max, "five_probe_values": values,
                      "saddle_G_normal_hessian_numeric_inverse_A2": hess,
                      "saddle_G_normal_hessian_exact_inverse_A2": target,
                      "epsilon_over_U1_to_flip_first_shell_hessian": -1/8,
                      "two_step_alpha_inverse_A2": alpha, "two_step_beta_inverse_A2": beta,
                      "two_step_noise_multiplier_inverse_A2": noise_multiplier,
                      "C6_truncation_bound_multiplier_A4": truncation_multiplier,
                      "illustrative_minus_0p2U1_extrapolated_curvature_microeV_atom_A2": illustrative_extrapolation,
                      "illustrative_at_sigma_0p001_z_from_zero_without_truncation": -illustrative_extrapolation/(noise_multiplier*.001),
                      "meaning": "Arbitrary epsilon*G leaves line and five probe energies and forces unchanged, but changes saddle curvature; no graphite coefficient inferred."}, indent=2))


if __name__ == "__main__":
    main()
