#!/usr/bin/env python3
"""
OSCAR EXECUTION — H_MULTI-EIGENSOLVE-v1.0 · VERSION A
Multi-component Hamiltonian on tetrahedral IFS substrate.

The scalar H was channel-blind: one degree of freedom per site.
H_multi has THREE internal degrees of freedom per site: (ρ, θ, χ).

State vector: Ψ = (ρ_1, θ_1, χ_1, ρ_2, θ_2, χ_2, ..., ρ_N, θ_N, χ_N)
Dimension: 3N × 3N

Sector coupling structure (from DT theory):
  - ρ (density/reactive): strong localization expected
    hopping: t_ρ = η (same as scalar)
    on-site: V_ρ = -Δ/N
    
  - θ (angular/phase): WEAK localization or delocalized expected
    hopping: t_θ = η × (b_Θ/d_Θ) where b_Θ/d_Θ < 1
    The theory predicts S_Θ(n) < 1, meaning θ modes spread.
    We use b_Θ/d_Θ = 0.6 (conservative estimate from theory bounds)
    on-site: V_θ = -Δ/N × 0.6 (reduced coupling)
    
  - χ (internal coherence): intermediate
    hopping: t_χ = η × 0.8
    on-site: V_χ = -Δ/N × 0.8

Cross-sector coupling:
  ρ-θ coupling: g_ρθ = 0.05 × η (weak mixing)
  ρ-χ coupling: g_ρχ = 0.03 × η (very weak)
  θ-χ coupling: g_θχ = 0.04 × η (weak)
  
  These are small compared to intra-sector hopping,
  so sectors are approximately independent but not exactly.

VERSION A SCOPE:
  - Static (no disorder, no repair)
  - Symmetric background only
  - N = 4^5 = 1024 and 4^6 = 4096
  - Channel-resolved outputs

LOCKED CONSTANTS — DO NOT CHANGE:
  eta = 185/192 = 0.963542
  r = 4^(-1/3) = 0.629961
  Delta/N = 7/192 = 0.036458
"""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh
import json
import datetime
import sys
import time

# ══════════════════════════════════════════════════════════
# LOCKED CONSTANTS
# ══════════════════════════════════════════════════════════
ETA = 185.0 / 192.0
R_IFS = 4.0 ** (-1.0 / 3.0)
DELTA_OVER_N = 7.0 / 192.0
L_REPAIR = 0.034

# Multi-component coupling parameters
# These are the key physics: θ-sector has WEAKER coupling
B_THETA_OVER_D_THETA = 0.6   # theory: < 1, conservative
CHI_COUPLING_RATIO = 0.8     # intermediate

# Cross-sector mixing (small)
G_RHO_THETA = 0.05
G_RHO_CHI = 0.03
G_THETA_CHI = 0.04

# Channel indices within each site's 3-component block
RHO = 0
THETA = 1
CHI = 2
CHANNEL_NAMES = ["rho", "theta", "chi"]


def site_to_address(idx, level):
    addr = []
    s = idx
    for _ in range(level):
        addr.append(s % 4)
        s //= 4
    return tuple(reversed(addr))


def build_multi_hamiltonian(N, level):
    """
    Build 3N × 3N multi-component Hamiltonian.
    
    Block structure per site pair (i,j):
      H[3i+a, 3j+b] where a,b ∈ {ρ=0, θ=1, χ=2}
    
    Intra-sector hopping (a=b, i≠j connected):
      H[3i+ρ, 3j+ρ] = -t_ρ × η^d(i,j)     = -η^(d+1)
      H[3i+θ, 3j+θ] = -t_θ × η^d(i,j)     = -η^(d+1) × b_Θ/d_Θ
      H[3i+χ, 3j+χ] = -t_χ × η^d(i,j)     = -η^(d+1) × 0.8
    
    Cross-sector hopping (a≠b, i≠j connected):
      H[3i+ρ, 3j+θ] = -g_ρθ × η^(d+1)
      etc.
    
    On-site (i=j):
      H[3i+ρ, 3i+ρ] = V_ρ = -Δ/N
      H[3i+θ, 3i+θ] = V_θ = -Δ/N × b_Θ/d_Θ
      H[3i+χ, 3i+χ] = V_χ = -Δ/N × 0.8
      Cross on-site = 0 (no on-site mixing)
    """
    dim = 3 * N
    addresses = [site_to_address(i, level) for i in range(N)]
    
    rows = []
    cols = []
    vals = []
    
    # Hopping strengths per channel
    t_intra = {
        RHO: 1.0,
        THETA: B_THETA_OVER_D_THETA,
        CHI: CHI_COUPLING_RATIO,
    }
    
    # Cross-sector coupling matrix
    g_cross = {
        (RHO, THETA): G_RHO_THETA,
        (THETA, RHO): G_RHO_THETA,
        (RHO, CHI): G_RHO_CHI,
        (CHI, RHO): G_RHO_CHI,
        (THETA, CHI): G_THETA_CHI,
        (CHI, THETA): G_THETA_CHI,
    }
    
    # On-site potential
    v_onsite = {
        RHO: -DELTA_OVER_N,
        THETA: -DELTA_OVER_N * B_THETA_OVER_D_THETA,
        CHI: -DELTA_OVER_N * CHI_COUPLING_RATIO,
    }
    
    for i in range(N):
        for a in range(3):
            row = 3 * i + a
            rows.append(row)
            cols.append(row)
            vals.append(v_onsite[a])
    
    # Parent groups for d=1 hopping
    parent_groups = {}
    for i in range(N):
        pk = addresses[i][:level - 1]
        if pk not in parent_groups:
            parent_groups[pk] = []
        parent_groups[pk].append(i)
    
    # Grandparent groups for d=2
    gp_groups = {}
    if level >= 2:
        for i in range(N):
            gpk = addresses[i][:level - 2]
            if gpk not in gp_groups:
                gp_groups[gpk] = []
            gp_groups[gpk].append(i)
    
    print(f"  Building multi-component hopping (3N={3*N})...", file=sys.stderr)
    
    # d=1 siblings
    base_hop_1 = ETA ** 1
    for pk, members in parent_groups.items():
        for ai in range(len(members)):
            for bi in range(ai + 1, len(members)):
                si, sj = members[ai], members[bi]
                # Intra-sector
                for ch in range(3):
                    h = -base_hop_1 * t_intra[ch]
                    r1, c1 = 3 * si + ch, 3 * sj + ch
                    rows.append(r1); cols.append(c1); vals.append(h)
                    rows.append(c1); cols.append(r1); vals.append(h)
                # Cross-sector
                for (ca, cb), g in g_cross.items():
                    h = -base_hop_1 * g
                    r1, c1 = 3 * si + ca, 3 * sj + cb
                    rows.append(r1); cols.append(c1); vals.append(h)
                    rows.append(c1); cols.append(r1); vals.append(h)
    
    # d=2 cousins
    if level >= 2:
        base_hop_2 = ETA ** 2
        for gpk, members in gp_groups.items():
            sub_parents = {}
            for i in members:
                pid = addresses[i][:level - 1]
                if pid not in sub_parents:
                    sub_parents[pid] = []
                sub_parents[pid].append(i)
            plist = list(sub_parents.values())
            for ai in range(len(plist)):
                for bi in range(ai + 1, len(plist)):
                    for si in plist[ai]:
                        for sj in plist[bi]:
                            for ch in range(3):
                                h = -base_hop_2 * t_intra[ch]
                                r1, c1 = 3 * si + ch, 3 * sj + ch
                                rows.append(r1); cols.append(c1); vals.append(h)
                                rows.append(c1); cols.append(r1); vals.append(h)
                            for (ca, cb), g in g_cross.items():
                                h = -base_hop_2 * g
                                r1, c1 = 3 * si + ca, 3 * sj + cb
                                rows.append(r1); cols.append(c1); vals.append(h)
                                rows.append(c1); cols.append(r1); vals.append(h)
    
    H = sparse.csr_matrix((vals, (rows, cols)), shape=(dim, dim))
    return H


def channel_weight(eigvec, N, channel):
    """
    Compute the weight of an eigenvector in a given channel.
    W^channel = Σ_i |ψ_{3i+channel}|²
    For normalized ψ: W^ρ + W^θ + W^χ = 1
    """
    indices = np.arange(channel, 3 * N, 3)
    return np.sum(eigvec[indices] ** 2)


def channel_ipr(eigvec, N, channel):
    """
    IPR restricted to one channel:
    IPR^channel = Σ_i |ψ_{3i+channel}|⁴ / (Σ_i |ψ_{3i+channel}|²)²
    
    This measures localization WITHIN that channel.
    If the mode is concentrated on a few sites in this channel, IPR is large.
    If spread uniformly, IPR ≈ 1/N.
    """
    indices = np.arange(channel, 3 * N, 3)
    comp = eigvec[indices]
    comp_sq = comp ** 2
    total_sq = np.sum(comp_sq)
    if total_sq < 1e-30:
        return 0.0  # no weight in this channel
    total_fourth = np.sum(comp_sq ** 2)
    return total_fourth / (total_sq ** 2)


def run_multi_eigensolve(N, level, n_runs, rng):
    """
    Build H_multi, diagonalize, classify modes by channel weight.
    
    For σ₁: the mode with highest W^ρ among localized states
    For σ₂: the mode with highest W^θ among low-energy states
    """
    dim = 3 * N
    baseline = 1.0 / N  # per-channel baseline
    
    all_run_data = []
    
    for run_idx in range(n_runs):
        t0 = time.time()
        
        H = build_multi_hamiltonian(N, level)
        
        # Find low-energy eigenstates
        n_eig = min(50, dim - 2)
        
        # Shift near the on-site energy
        sigma_shift = float(-DELTA_OVER_N)
        
        print(f"    Run {run_idx + 1}/{n_runs}: eigsh(k={n_eig}, dim={dim})...", file=sys.stderr)
        
        try:
            eigenvalues, eigenvectors = eigsh(H, k=n_eig, sigma=sigma_shift, which='LM')
        except Exception:
            try:
                eigenvalues, eigenvectors = eigsh(H, k=n_eig, which='SA')
            except Exception as e:
                print(f"    eigsh failed: {e}", file=sys.stderr)
                continue
        
        # Classify each eigenstate
        mode_data = []
        for k in range(len(eigenvalues)):
            evec = eigenvectors[:, k]
            
            w_rho = channel_weight(evec, N, RHO)
            w_theta = channel_weight(evec, N, THETA)
            w_chi = channel_weight(evec, N, CHI)
            
            ipr_rho = channel_ipr(evec, N, RHO)
            ipr_theta = channel_ipr(evec, N, THETA)
            ipr_chi = channel_ipr(evec, N, CHI)
            
            # Full IPR
            ipr_full = np.sum(evec ** 4)
            
            mode_data.append({
                "eig_index": k,
                "eigenvalue": float(eigenvalues[k]),
                "W_rho": float(w_rho),
                "W_theta": float(w_theta),
                "W_chi": float(w_chi),
                "IPR_rho": float(ipr_rho),
                "IPR_theta": float(ipr_theta),
                "IPR_chi": float(ipr_chi),
                "IPR_full": float(ipr_full),
                "F_rho": float(ipr_rho * N),
                "F_theta": float(ipr_theta * N),
                "F_full": float(ipr_full * dim),
            })
        
        # Sort by eigenvalue (lowest first) for the top-5 table
        mode_data.sort(key=lambda m: m["eigenvalue"])
        
        # σ₁ candidate: highest F_rho among modes with W_rho > 0.3
        rho_candidates = [m for m in mode_data if m["W_rho"] > 0.3]
        if rho_candidates:
            sigma1 = max(rho_candidates, key=lambda m: m["F_rho"])
        else:
            sigma1 = max(mode_data, key=lambda m: m["F_rho"])
        
        # σ₂ candidate: highest W_theta among modes (θ-dominated)
        theta_candidates = [m for m in mode_data if m["W_theta"] > 0.3]
        if theta_candidates:
            sigma2 = max(theta_candidates, key=lambda m: m["W_theta"])
        else:
            sigma2 = max(mode_data, key=lambda m: m["W_theta"])
        
        dt = time.time() - t0
        print(f"    Run {run_idx + 1}: "
              f"σ₁(ρ-dom): F_ρ={sigma1['F_rho']:.2f}, W_ρ={sigma1['W_rho']:.3f} | "
              f"σ₂(θ-dom): F_θ={sigma2['F_theta']:.2f}, W_θ={sigma2['W_theta']:.3f} | "
              f"({dt:.1f}s)", file=sys.stderr)
        
        all_run_data.append({
            "sigma1": sigma1,
            "sigma2": sigma2,
            "top5_by_energy": mode_data[:5],
            "n_modes_found": len(mode_data),
            "n_rho_dominated": len([m for m in mode_data if m["W_rho"] > 0.5]),
            "n_theta_dominated": len([m for m in mode_data if m["W_theta"] > 0.5]),
            "n_chi_dominated": len([m for m in mode_data if m["W_chi"] > 0.5]),
        })
    
    # Aggregate
    s1_F_rho = [r["sigma1"]["F_rho"] for r in all_run_data]
    s2_F_theta = [r["sigma2"]["F_theta"] for r in all_run_data]
    s1_W_rho = [r["sigma1"]["W_rho"] for r in all_run_data]
    s2_W_theta = [r["sigma2"]["W_theta"] for r in all_run_data]
    
    return {
        "runs": all_run_data,
        "sigma1_F_rho_mean": float(np.mean(s1_F_rho)),
        "sigma1_F_rho_std": float(np.std(s1_F_rho, ddof=1)) if len(s1_F_rho) > 1 else 0.0,
        "sigma1_F_rho_min": float(np.min(s1_F_rho)),
        "sigma1_F_rho_max": float(np.max(s1_F_rho)),
        "sigma1_W_rho_mean": float(np.mean(s1_W_rho)),
        "sigma2_F_theta_mean": float(np.mean(s2_F_theta)),
        "sigma2_F_theta_std": float(np.std(s2_F_theta, ddof=1)) if len(s2_F_theta) > 1 else 0.0,
        "sigma2_F_theta_min": float(np.min(s2_F_theta)),
        "sigma2_F_theta_max": float(np.max(s2_F_theta)),
        "sigma2_W_theta_mean": float(np.mean(s2_W_theta)),
        "IPR_baseline": 1.0 / N,
    }


def classify_regime(F):
    if F < 1.0: return "subcritical"
    elif F < 3.0: return "marginal"
    elif F < 10.0: return "intermediate"
    else: return "strong"


def main():
    rng = np.random.default_rng(seed=2026)
    
    # Version A: static, symmetric only
    # 3N dims: 4^5→3072, 4^6→12288
    test_levels = [(5, 1024)]
    
    # Check if 4^6 = 4096 (dim=12288) is feasible
    try:
        _ = np.zeros((12288, 50), dtype=np.float64)
        del _
        test_levels.append((6, 4096))
        print("4^6 (dim=12288) feasible", file=sys.stderr)
    except MemoryError:
        print("4^6 NOT feasible", file=sys.stderr)
    
    # Check 4^7 = 16384 (dim=49152)
    try:
        _ = np.zeros((49152, 50), dtype=np.float64)
        del _
        test_levels.append((7, 16384))
        print("4^7 (dim=49152) feasible", file=sys.stderr)
    except MemoryError:
        print("4^7 NOT feasible for multi-component", file=sys.stderr)
    
    all_blocks = []
    
    for level, N in test_levels:
        dim = 3 * N
        n_runs = 10 if N <= 1024 else (5 if N <= 4096 else 3)
        
        print(f"\n{'='*70}", file=sys.stderr)
        print(f"H_MULTI VERSION A: level={level}, N={N}, dim={dim}, {n_runs} runs", file=sys.stderr)
        print(f"{'='*70}", file=sys.stderr)
        
        stats = run_multi_eigensolve(N, level, n_runs, rng)
        
        F_s1 = stats["sigma1_F_rho_mean"]
        F_s2 = stats["sigma2_F_theta_mean"]
        
        # Gate logic
        gates_passed = []
        gates_failed = []
        
        if F_s1 >= 10.0:
            gates_passed.append("P1-rho")
        elif 3.0 <= F_s1 < 10.0:
            gates_passed.append("C1-rho")
        
        if F_s2 < 2.0:
            gates_passed.append("P3-theta")
            c2_status = "RESOLVED (scalar artifact)"
        elif F_s2 >= 5.0:
            gates_failed.append("C2-theta")
            c2_status = "PERSISTENT (true multi-channel)"
        else:
            c2_status = "AMBIGUOUS (triad review needed)"
        
        # Channel dominance stats
        avg_n_rho = np.mean([r["n_rho_dominated"] for r in stats["runs"]])
        avg_n_theta = np.mean([r["n_theta_dominated"] for r in stats["runs"]])
        avg_n_chi = np.mean([r["n_chi_dominated"] for r in stats["runs"]])
        
        ts = datetime.datetime.now(datetime.timezone.utc)
        
        block = {
            "version": "1.0",
            "schema": "B_rho_raw_multi_component",
            "run_id": f"OSCAR-HMULTI-VA-N{N}-{ts.strftime('%Y%m%dT%H%M%SZ')}",
            "timestamp": ts.isoformat(),
            "executor": "Oscar (Cato-executed, multi-component eigensolve)",
            "profile": "H_MULTI-EIGENSOLVE-VERSION-A",
            "method": "eigsh on 3N×3N multi-component IFS Hamiltonian",
            "N_sites": N,
            "ifs_level": level,
            "dim": dim,
            "background": "symmetric (Version A — no disorder)",
            "eta": round(ETA, 6),
            "r": round(R_IFS, 6),
            "L_repair": L_REPAIR,
            "N_runs_averaged": n_runs,
            
            "coupling_params": {
                "t_rho": 1.0,
                "t_theta": B_THETA_OVER_D_THETA,
                "t_chi": CHI_COUPLING_RATIO,
                "g_rho_theta": G_RHO_THETA,
                "g_rho_chi": G_RHO_CHI,
                "g_theta_chi": G_THETA_CHI,
                "b_theta_over_d_theta": B_THETA_OVER_D_THETA,
            },
            
            "sigma1_label": "ρ-channel dominated eigenstate (W_ρ > 0.3, max F_ρ)",
            "F_sigma1_rho": round(F_s1, 4),
            "F_sigma1_rho_std": round(stats["sigma1_F_rho_std"], 4),
            "F_sigma1_rho_min": round(stats["sigma1_F_rho_min"], 4),
            "F_sigma1_rho_max": round(stats["sigma1_F_rho_max"], 4),
            "W_rho_sigma1_mean": round(stats["sigma1_W_rho_mean"], 4),
            "regime_sigma1": classify_regime(F_s1),
            
            "sigma2_label": "θ-channel dominated eigenstate (W_θ > 0.3, max W_θ)",
            "F_sigma2_theta": round(F_s2, 4),
            "F_sigma2_theta_std": round(stats["sigma2_F_theta_std"], 4),
            "F_sigma2_theta_min": round(stats["sigma2_F_theta_min"], 4),
            "F_sigma2_theta_max": round(stats["sigma2_F_theta_max"], 4),
            "W_theta_sigma2_mean": round(stats["sigma2_W_theta_mean"], 4),
            "regime_sigma2": classify_regime(F_s2),
            
            "IPR_baseline": round(stats["IPR_baseline"], 14),
            
            "c2_status": c2_status,
            "gate_passed": gates_passed,
            "gate_failed": gates_failed,
            
            "channel_dominance": {
                "avg_rho_dominated_modes": round(float(avg_n_rho), 1),
                "avg_theta_dominated_modes": round(float(avg_n_theta), 1),
                "avg_chi_dominated_modes": round(float(avg_n_chi), 1),
            },
            
            "top5_example": stats["runs"][0]["top5_by_energy"] if stats["runs"] else [],
            
            "notes": [
                f"Multi-component eigensolve: 3N×3N = {dim}×{dim}",
                f"Sector coupling: t_ρ=1.0, t_θ={B_THETA_OVER_D_THETA}, t_χ={CHI_COUPLING_RATIO}",
                f"Cross-sector: g_ρθ={G_RHO_THETA}, g_ρχ={G_RHO_CHI}, g_θχ={G_THETA_CHI}",
                "Version A: static, symmetric, no disorder",
                "σ₁ selection: max F_ρ among W_ρ > 0.3 modes",
                "σ₂ selection: max W_θ among W_θ > 0.3 modes",
                f"N_runs = {n_runs}, seed = 2026",
                "b_Θ/d_Θ = 0.6 is a conservative estimate; theory says < 1",
            ],
        }
        
        all_blocks.append(block)
        
        print(f"\n  RESULT: σ₁ F_ρ={F_s1:.2f} (W_ρ={stats['sigma1_W_rho_mean']:.3f})"
              f"  |  σ₂ F_θ={F_s2:.2f} (W_θ={stats['sigma2_W_theta_mean']:.3f})"
              f"  |  C2={c2_status}", file=sys.stderr)
    
    # Summary
    print(f"\n{'='*70}", file=sys.stderr)
    print("H_MULTI VERSION A SUMMARY", file=sys.stderr)
    print(f"{'='*70}", file=sys.stderr)
    for b in all_blocks:
        print(f"  N={b['N_sites']:>6} dim={b['dim']:>6} | "
              f"σ₁ F_ρ={b['F_sigma1_rho']:>8.2f} W_ρ={b['W_rho_sigma1_mean']:.3f} | "
              f"σ₂ F_θ={b['F_sigma2_theta']:>8.2f} W_θ={b['W_theta_sigma2_mean']:.3f} | "
              f"C2: {b['c2_status']}", file=sys.stderr)
    
    print(json.dumps(all_blocks, indent=2))


if __name__ == "__main__":
    main()
