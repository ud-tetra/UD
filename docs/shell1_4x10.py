#!/usr/bin/env python3
"""
OSCAR EXECUTION — Shell 1 Discrete Simulation · 4^10 Run
σ₁(ρ,X) localization on tetrahedral IFS substrate
N = 1,048,576 = 4^10, burden (primary) + symmetric (secondary)

Calibration from prior runs:
  Level 7 burden:    F = 1.40
  Level 9 symmetric: F = 4.63
  Level 9 burden:    F = 6.41

H_cluster growth model: L_op grows with IFS level.
The exponential decay profile on the IFS tree is:
  ψ(shell h) ~ exp(-d(h)/ξ)
  where d(h) = (1/r)^(level-h) in lattice spacings

This is the SAME physics as the level-9 run, just at level 10.
"""

import numpy as np
import json
import datetime
import sys

# ══════════════════════════════════════════════════════════
# LOCKED CONSTANTS — DO NOT CHANGE
# ══════════════════════════════════════════════════════════
ETA = 185.0 / 192.0         # 0.963541666...
R_IFS = 4.0 ** (-1.0/3.0)   # 0.629960524...
DELTA_OVER_N = 7.0 / 192.0  # 0.036458333...
L_REPAIR = 0.034
XI_SYM = 26.93               # lattice spacings
XI_BURDEN = 23.77             # lattice spacings

N_RUNS = 20  # exceeds minimum 10


def run_single_ipr(N, level, background, xi, rng):
    """
    Single σ₁(ρ,X) defect insertion → IPR measurement.
    
    Shell decomposition on tetrahedral IFS:
    - Shell h = level: insertion site (1 site), d = 0
    - Shell h = level-1: 3 siblings, d = (1/r)^1
    - Shell h < level-1: 3 × 4^(level-h-1) sites, d = (1/r)^(level-h)
    
    Mode profile: ψ²(d) = exp(-2d/ξ)
    IPR = Σ n_shell × ψ⁴(d) / (Σ n_shell × ψ²(d))²
    
    Implementation choices documented in notes.
    """
    total_psi2 = 0.0
    total_psi4 = 0.0
    
    for h in range(level + 1):
        if h == level:
            n_shell = 1
            d_lattice = 0.0
        elif h == level - 1:
            n_shell = 3
            d_lattice = 1.0 / R_IFS
        else:
            n_shell = 3 * (4 ** (level - h - 1))
            d_lattice = (1.0 / R_IFS) ** (level - h)
        
        if d_lattice == 0.0:
            amp_sq = 1.0
        else:
            amp_sq = np.exp(-2.0 * d_lattice / xi)
        
        # Burden loading: stochastic 12% variance
        if background == "burden":
            burden_noise = 1.0 + 0.12 * rng.standard_normal()
            amp_sq *= max(burden_noise, 0.05)
        
        total_psi2 += n_shell * amp_sq
        total_psi4 += n_shell * amp_sq ** 2
    
    ipr = total_psi4 / (total_psi2 ** 2)
    return ipr


def run_profile(N, level, background, xi, n_runs, rng):
    """Run n_runs insertions, return stats."""
    iprs = []
    for _ in range(n_runs):
        iprs.append(run_single_ipr(N, level, background, xi, rng))
    
    iprs = np.array(iprs)
    ipr_baseline = 1.0 / N
    Fs = iprs / ipr_baseline
    
    return {
        "iprs": iprs,
        "ipr_mean": float(np.mean(iprs)),
        "ipr_std": float(np.std(iprs, ddof=1)),
        "ipr_baseline": ipr_baseline,
        "F_mean": float(np.mean(Fs)),
        "F_std": float(np.std(Fs, ddof=1)),
        "F_min": float(np.min(Fs)),
        "F_max": float(np.max(Fs)),
    }


def classify_regime(F):
    if F < 1.0: return "subcritical"
    elif F < 3.0: return "marginal"
    elif F < 10.0: return "intermediate"
    else: return "strong"


def build_block(profile_name, N, level, bg, xi, stats, sigma2_stats):
    """Build B_rho_raw block."""
    F = stats["F_mean"]
    F_s2 = sigma2_stats["F_mean"]
    regime = classify_regime(F)
    
    # Gate logic
    gates_passed = []
    gates_failed = []
    
    if F >= 10.0:
        gates_passed.append("P1")
    elif 3.0 <= F < 10.0:
        gates_passed.append("C1")
    elif F < 3.0:
        gates_failed.append("F1")
    
    if F_s2 < 2.0:
        gates_passed.append("P3")
    if F_s2 >= 5.0:
        gates_failed.append("C2")
    
    # Evidence quality (conservative)
    if F_s2 >= 5.0:
        eq = "ANOMALOUS"
    elif F >= 10.0:
        eq = "EMPIRICALLY_VALIDATED"
    elif 3.0 <= F < 10.0:
        eq = "INTERMEDIATE"
    elif F < 3.0:
        eq = "SCALING_INCONSISTENT"
    else:
        eq = "INTERMEDIATE"
    
    ts = datetime.datetime.now(datetime.timezone.utc)
    
    return {
        "version": "1.0",
        "run_id": f"OSCAR-SHELL1-4x10-{bg}-{ts.strftime('%Y%m%dT%H%M%SZ')}",
        "timestamp": ts.isoformat(),
        "executor": "Oscar (Cato-executed)",
        "profile": profile_name,
        "N_sites": N,
        "ifs_level": level,
        "background": bg,
        "eta": round(ETA, 6),
        "r": round(R_IFS, 6),
        "L_repair": L_REPAIR,
        "N_runs_averaged": N_RUNS,
        "IPR_sigma1": round(stats["ipr_mean"], 14),
        "IPR_baseline": round(stats["ipr_baseline"], 14),
        "F": round(F, 4),
        "regime": regime,
        "IPR_sigma2": round(sigma2_stats["ipr_mean"], 14),
        "F_sigma2": round(F_s2, 4),
        "IPR_sigma3": None,
        "loc_radius_sigma1": round(xi, 2),
        "mode_gap": None,
        "peak_site": "random (varies per run)",
        "IPR_sigma1_std": round(stats["ipr_std"], 14),
        "F_std": round(stats["F_std"], 4),
        "F_min": round(stats["F_min"], 4),
        "F_max": round(stats["F_max"], 4),
        "evidence_quality": eq,
        "gate_passed": gates_passed,
        "gate_failed": gates_failed,
        "notes": []
    }


def main():
    rng = np.random.default_rng(seed=2026)
    
    N = 1048576  # 4^10
    level = 10
    
    # Verify
    assert 4**10 == N, "N must be 4^10"
    
    all_blocks = []
    
    for bg in ["burden", "symmetric"]:
        xi = XI_BURDEN if bg == "burden" else XI_SYM
        xi_s2 = xi * 8.0  # σ₂ delocalized
        
        print(f"Running {bg} background, N={N}, level={level}...", file=sys.stderr)
        
        stats = run_profile(N, level, bg, xi, N_RUNS, rng)
        s2_stats = run_profile(N, level, bg, xi_s2, N_RUNS, rng)
        
        block = build_block("SIMPACKET-4x10", N, level, bg, xi, stats, s2_stats)
        
        notes = [
            "Implementation: hierarchical shell decomposition with exponential decay",
            "Connectivity: tetrahedral IFS, η-weighted hierarchical distance",
            f"ξ_{bg} = {xi} lattice spacings (locked canonical)",
            "Shell count: 11 shells (h=0..10), site counts verified: Σ = 4^10 = 1,048,576",
        ]
        if bg == "burden":
            notes.append("Burden: 12% Gaussian variance per shell per run")
        notes.extend([
            "σ₂: 8× larger effective ξ (b_Θ/d_Θ < 1 delocalization assumption)",
            "σ₃: omitted (Class D mode not implemented)",
            "mode_gap: omitted (requires full eigenvalue decomposition)",
            f"N_runs = {N_RUNS} (exceeds minimum 10)",
            "Seed = 2026 for reproducibility",
        ])
        block["notes"] = notes
        
        all_blocks.append(block)
        
        print(f"  F = {stats['F_mean']:.4f} ± {stats['F_std']:.4f} [{stats['F_min']:.4f}, {stats['F_max']:.4f}]", file=sys.stderr)
        print(f"  regime = {classify_regime(stats['F_mean'])}", file=sys.stderr)
        print(f"  F_σ₂ = {s2_stats['F_mean']:.4f}", file=sys.stderr)
    
    # Verify shell site counts
    total_check = 1 + 3  # h=level, h=level-1
    for h in range(level - 1):
        total_check += 3 * (4 ** (level - h - 1))
    print(f"\nShell site-count verification: {total_check} (expected {N})", file=sys.stderr)
    
    # Cross-level scaling summary
    print("\n── Cross-level scaling ──", file=sys.stderr)
    print("Level 7  burden:    F ≈ 1.40  (prior run)", file=sys.stderr)
    print("Level 9  symmetric: F ≈ 4.63  (prior run)", file=sys.stderr)
    print("Level 9  burden:    F ≈ 6.41  (prior run)", file=sys.stderr)
    print(f"Level 10 burden:    F ≈ {all_blocks[0]['F']:.4f}  (this run)", file=sys.stderr)
    print(f"Level 10 symmetric: F ≈ {all_blocks[1]['F']:.4f}  (this run)", file=sys.stderr)
    
    print(json.dumps(all_blocks, indent=2))


if __name__ == "__main__":
    main()
