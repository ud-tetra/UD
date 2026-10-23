#!/usr/bin/env python3
"""Analyze independently run QE total energies for the designed off-line pairs."""
import argparse
import json
import math
from pathlib import Path
from xml.etree import ElementTree as ET

HA_TO_MICROEV = 27.211386245988 * 1_000_000
N_UPPER = 14
U1 = .0793396654
KY = 2 * math.pi * math.sqrt(7) / (math.sqrt(3) * 2.4660)


def energy(path):
    root = ET.parse(path).getroot()
    converged = root.findtext(".//convergence_info/scf_conv/convergence_achieved")
    if converged is None:  # QE versions differ in one wrapper element
        converged = root.findtext(".//convergence_info/convergence_achieved")
    if converged is None or converged.strip().lower() != "true":
        raise ValueError(f"no positive QE XML SCF convergence flag: {path}")
    value = root.findtext(".//total_energy/etot")
    if value is None:
        raise ValueError(f"missing total_energy/etot: {path}")
    return float(value)  # QE XML schema energy in Hartree


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--center", required=True, type=Path)
    for label in ("04", "08"):
        p.add_argument(f"--minus-{label}", required=True, type=Path)
        p.add_argument(f"--plus-{label}", required=True, type=Path)
    p.add_argument("--sigma-microev-atom", type=float, default=None,
                   help="independent one-run standard uncertainty, if defensible")
    a = p.parse_args()
    if a.sigma_microev_atom is not None and a.sigma_microev_atom <= 0:
        p.error("sigma must be positive")
    e0 = energy(a.center)
    out = {"status": "ANALYSIS_OF_SUPPLIED_OUTPUTS", "center_Ha": e0, "pairs": [],
           "uncertainty_assumption": "independent equal per-run errors; systematic error excluded"}
    for label, h in (("04", .04), ("08", .08)):
        em, ep = energy(getattr(a, "minus_" + label)), energy(getattr(a, "plus_" + label))
        # Differences before unit conversion. XML carries more digits than struct.out.
        d = (ep + em - 2 * e0) * HA_TO_MICROEV / N_UPPER
        beta = math.sqrt(3) * KY * h
        f = 4 * math.sin(beta / 2) ** 2
        F = (1 - math.cos(2 * beta)) * (1 + math.cos(beta)) ** 2
        pair = {"h_A": h, "E_minus_Ha": em, "E_plus_Ha": ep,
                "symmetric_contrast_microeV_atom": d,
                "curvature_estimate_microeV_atom_A2": d / h ** 2,
                "first_shell_contrast_microeV_atom": 2 * U1 * f,
                "illustrative_epsilon_microeV_atom": (d - 2 * U1 * f) / (2 * F)}
        if a.sigma_microev_atom is not None:
            pair["contrast_standard_uncertainty_microeV_atom"] = math.sqrt(6) * a.sigma_microev_atom
            pair["contrast_z_from_zero"] = d / (math.sqrt(6) * a.sigma_microev_atom)
        out["pairs"].append(pair)
    d04, d08 = (x["curvature_estimate_microeV_atom_A2"] for x in out["pairs"])
    # D(h)/h^2 = kappa + c*h^2 + O(h^4); shared center correlates the pair errors.
    out["quadratic_h2_extrapolation_microeV_atom_A2"] = (d04 * .08 ** 2 - d08 * .04 ** 2) / (.08 ** 2 - .04 ** 2)
    out["warning"] = "One-parameter epsilon estimate and h^2 extrapolation are conditional; DFT settings and errors must be independently audited."
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
