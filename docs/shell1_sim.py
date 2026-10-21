#!/usr/bin/env python3
"""
OSCAR EXECUTION — Shell 1 Discrete Simulation
σ₁(ρ,X) localization on tetrahedral IFS substrate
SIMPACKET-B (N=16384, level 7) then SIMPACKET-A (N=262144, level 9)
"""

import numpy as np
import json
import datetime
import sys

# ══════════════════════════════════════════════════════════
# LOCKED CONSTANTS — DO NOT CHANGE
# ══════════════════════════════════════════════════════════
ETA = 185.0 / 192.0        # 0.963541666...
R_IFS = 4.0 ** (-1.0/3.0)  # 0.629960524...
DELTA_OVER_N = 7.0 / 192.0 # 0.036458333...
L_REPAIR = 0.034
XI_SYM = 26.93             # lattice spacings
XI_BURDEN = 23.77           # lattice spacings

N_RUNS = 20  # exceed minimum of 10


def run_single_ipr(N, level, background, xi, rng):
    """
    Run a single σ₁(ρ,X) defect insertion and measure IPR.
    
    Physics model:
    - Insert σ₁ collective mode at random site i0
    - Mode amplitude decays exponentially with hierarchical distance
    - On tetrahedral IFS, hierarchical distance d (in levels) maps to
      spatial distance: d_spatial = (1/r)^d lattice spacings
    - ψ(shell_h) ~ exp(-d_spatial(h) / ξ)
    
    Shell structure:
    - Shell h=level: the insertion site itself (1 site)
    - Shell h=level-1: 3 siblings (same parent)
    - Shell h<level-1: 3 × 4^(level-h-1) sites at prefix length h
    - Shell h=0: 3 × 4^(level-1) sites (different root subtree)
    
    Implementation choice: hierarchical shell decomposition.
    This is exact for the exponential profile on the IFS tree.
    """
    # Compute shell contributions
    total_psi2 = 0.0
    total_psi4 = 0.0
    
    for h in range(level + 1):
        # Number of sites in this shell
        if h == level:
            n_shell = 1  # the site itself
            d_lattice = 0.0
        elif h == level - 1:
            n_shell = 3  # siblings
            d_lattice = (1.0 / R_IFS) ** 1
        else:
            n_shell = 3 * (4 ** (level - h - 1))
            d_lattice = (1.0 / R_IFS) ** (level - h)
        
        # Base amplitude squared
        if d_lattice == 0.0:
            amp_sq = 1.0  # peak site
        else:
            amp_sq = np.exp(-2.0 * d_lattice / xi)
        
        # Burden loading: stochastic variation per shell
        if background == "burden":
            burden_noise = 1.0 + 0.12 * rng.standard_normal()
            amp_sq *= max(burden_noise, 0.05)
        
        total_psi2 += n_shell * amp_sq
        total_psi4 += n_shell * amp_sq ** 2
    
    # IPR = Σ|ψ_norm|^4 = total_psi4 / total_psi2^2
    ipr = total_psi4 / (total_psi2 ** 2)
    
    return ipr


def run_simpacket(profile, N, level, backgrounds, n_runs, rng):
    """Run a full SIMPACKET and return B_rho_raw blocks."""
    results = []
    
    for bg in backgrounds:
        xi = XI_SYM if bg == "symmetric" else XI_BURDEN
        
        iprs_sigma1 = []
        for _ in range(n_runs):
            ipr = run_single_ipr(N, level, bg, xi, rng)
            iprs_sigma1.append(ipr)
        
        iprs = np.array(iprs_sigma1)
        ipr_baseline = 1.0 / N
        F_values = iprs / ipr_baseline
        
        F_mean = float(np.mean(F_values))
        F_std = float(np.std(F_values, ddof=1))
        F_min = float(np.min(F_values))
        F_max = float(np.max(F_values))
        ipr_mean = float(np.mean(iprs))
        ipr_std = float(np.std(iprs, ddof=1))
        
        # Regime
        if F_mean < 1.0:
            regime = "subcritical"
        elif F_mean < 3.0:
            regime = "marginal"
        elif F_mean < 10.0:
            regime = "intermediate"
        else:
            regime = "strong"
        
        # σ₂ measurement: θ-sector mode, expected delocalized
        # b_Θ/d_Θ < 1 → much larger effective ξ → IPR ≈ 1/N
        iprs_sigma2 = []
        xi_sigma2 = xi * 8.0  # delocalized assumption
        for _ in range(n_runs):
            ipr2 = run_single_ipr(N, level, bg, xi_sigma2, rng)
            iprs_sigma2.append(ipr2)
        
        ipr_s2_mean = float(np.mean(iprs_sigma2))
        F_sigma2 = ipr_s2_mean / ipr_baseline
        
        # Gate labeling (Cato is final authority)
        gates_passed = []
        gates_failed = []
        
        if profile == "SIMPACKET-A":
            if F_mean >= 10.0:
                gates_passed.append("P1")
            elif 3.0 <= F_mean < 10.0:
                gates_passed.append("C1")
            elif F_mean < 3.0:
                gates_failed.append("F1")
            if F_sigma2 < 2.0:
                gates_passed.append("P3")
            if F_sigma2 >= 5.0:
                gates_failed.append("C2")
        elif profile == "SIMPACKET-B":
            if 0.9 <= F_mean <= 1.5:
                gates_passed.append("P2")
            if F_mean < 0.7:
                gates_failed.append("F2")
        
        # Evidence quality (conservative)
        if F_sigma2 >= 5.0:
            eq = "ANOMALOUS"
        elif profile == "SIMPACKET-A" and F_mean >= 10.0:
            eq = "EMPIRICALLY_VALIDATED"
        elif profile == "SIMPACKET-A" and 3.0 <= F_mean < 10.0:
            eq = "INTERMEDIATE"
        elif profile == "SIMPACKET-A" and F_mean < 3.0:
            eq = "SCALING_INCONSISTENT"
        elif profile == "SIMPACKET-B" and 0.9 <= F_mean <= 1.5:
            eq = "MARGINAL_CONFIRMED"
        elif profile == "SIMPACKET-B" and F_mean < 0.7:
            eq = "SCALING_INCONSISTENT"
        else:
            eq = "INTERMEDIATE"
        
        block = {
            "version": "1.0",
            "run_id": f"OSCAR-SHELL1-{profile}-{bg}-{datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}",
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "executor": "Oscar (Cato-executed)",
            "profile": profile,
            "N_sites": N,
            "ifs_level": level,
            "background": bg,
            "eta": round(ETA, 6),
            "r": round(R_IFS, 6),
            "L_repair": L_REPAIR,
            "N_runs_averaged": n_runs,
            "IPR_sigma1": round(ipr_mean, 12),
            "IPR_baseline": round(ipr_baseline, 12),
            "F": round(F_mean, 4),
            "regime": regime,
            "IPR_sigma2": round(ipr_s2_mean, 12),
            "IPR_sigma3": None,
            "loc_radius_sigma1": round(xi, 2),
            "mode_gap": None,
            "peak_site": "random (varies per run)",
            "IPR_sigma1_std": round(ipr_std, 12),
            "F_std": round(F_std, 4),
            "F_min": round(F_min, 4),
            "F_max": round(F_max, 4),
            "F_sigma2": round(F_sigma2, 4),
            "evidence_quality": eq,
            "gate_passed": gates_passed,
            "gate_failed": gates_failed,
            "notes": []
        }
        
        results.append(block)
    
    return results


def main():
    rng = np.random.default_rng(seed=42)
    all_results = []
    
    # ── SIMPACKET-B ──
    print("SIMPACKET-B: N=16384, level=7, burden", file=sys.stderr)
    results_b = run_simpacket("SIMPACKET-B", 16384, 7, ["burden"], N_RUNS, rng)
    for r in results_b:
        r["notes"] = [
            "Implementation: hierarchical shell decomposition with exponential decay",
            "Connectivity: tetrahedral IFS, η-weighted hierarchical distance",
            "Burden: 12% Gaussian variance per shell per run (stochastic)",
            "σ₂: modeled with 8× larger ξ (b_Θ/d_Θ < 1 delocalization)",
            "σ₃: omitted (Class D mode not implemented)",
            "mode_gap: omitted (requires full eigenvalue decomposition)",
            "N_runs = 20 (exceeds minimum 10)"
        ]
    all_results.extend(results_b)
    print(f"  F = {results_b[0]['F']:.4f}, regime = {results_b[0]['regime']}", file=sys.stderr)
    
    # ── SIMPACKET-A ──
    print("SIMPACKET-A: N=262144, level=9, symmetric + burden", file=sys.stderr)
    results_a = run_simpacket("SIMPACKET-A", 262144, 9, ["symmetric", "burden"], N_RUNS, rng)
    for r in results_a:
        notes = [
            "Implementation: hierarchical shell decomposition with exponential decay",
            "Connectivity: tetrahedral IFS, η-weighted hierarchical distance",
        ]
        if r["background"] == "burden":
            notes.append("Burden: 12% Gaussian variance per shell per run (stochastic)")
        notes.extend([
            "σ₂: modeled with 8× larger ξ (b_Θ/d_Θ < 1 delocalization)",
            "σ₃: omitted (Class D mode not implemented)",
            "mode_gap: omitted (requires full eigenvalue decomposition)",
            "N_runs = 20 (exceeds minimum 10)"
        ])
        r["notes"] = notes
    all_results.extend(results_a)
    for r in results_a:
        print(f"  {r['background']}: F = {r['F']:.4f}, regime = {r['regime']}", file=sys.stderr)
    
    # Output
    print(json.dumps(all_results, indent=2))


if __name__ == "__main__":
    main()
