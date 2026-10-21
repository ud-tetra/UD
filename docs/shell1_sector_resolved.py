#!/usr/bin/env python3
"""
OSCAR EXECUTION — H_SIGMA1-EIGENSOLVE-SECTOR-RESOLVED v1.0
Same Hamiltonian as prior run. ONLY the mode-identification is changed.

Repair:
  OLD: σ₁ = argmax |<ψ_k|δ_i0>|²,  σ₂ = second-highest overlap
  NEW: σ₁ = argmax |<ψ_k|P_ρ δ_i0>|²  (even-parity / reactive sector)
       σ₂ = argmax |<ψ_k|P_Θ δ_i0>|²  (odd-parity / Θ-proxy sector)

P_ρ and P_Θ constructed from sibling-group parity:
  G = {i0, s1, s2, s3} = 4 siblings sharing parent
  P_ρ|δ_i0⟩ = (1/2)(|δ_i0⟩ + (1/3)Σ_{j∈G\i0} |δ_j⟩)  [symmetric]
  P_Θ|δ_i0⟩ = (1/2)(|δ_i0⟩ − (1/3)Σ_{j∈G\i0} |δ_j⟩)  [antisymmetric]

Labels:
  σ₁ = sector-resolved within current scalar operator
  σ₂ = parity-odd Θ-proxy, not full Θ-sector closure
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

NEAR_DEGEN_THRESHOLD = 0.15  # 15% relative gap


def site_to_address(idx, level):
    addr = []
    s = idx
    for _ in range(level):
        addr.append(s % 4)
        s //= 4
    return tuple(reversed(addr))


def get_sibling_group(i0, level):
    """Return the 4 siblings sharing the same parent (including i0)."""
    addr = list(site_to_address(i0, level))
    last_digit = addr[-1]
    siblings = []
    for d in range(4):
        sib_addr = addr[:-1] + [d]
        idx = 0
        for k in range(level):
            idx += sib_addr[k] * (4 ** (level - 1 - k))
        siblings.append(idx)
    return siblings


def build_sector_defects(i0, N, level):
    """
    Build P_ρ|δ_i0⟩ and P_Θ|δ_i0⟩.
    
    G = {i0, s1, s2, s3} siblings
    P_ρ = (1/2)(|δ_i0⟩ + (1/3)Σ_{j≠i0} |δ_j⟩)  [even/symmetric]
    P_Θ = (1/2)(|δ_i0⟩ − (1/3)Σ_{j≠i0} |δ_j⟩)  [odd/antisymmetric]
    
    Then normalize each.
    """
    siblings = get_sibling_group(i0, level)
    others = [s for s in siblings if s != i0]
    
    v_rho = np.zeros(N)
    v_rho[i0] = 0.5
    for j in others:
        v_rho[j] = 0.5 / 3.0
    # Normalize
    norm = np.linalg.norm(v_rho)
    if norm > 0:
        v_rho /= norm
    
    v_theta = np.zeros(N)
    v_theta[i0] = 0.5
    for j in others:
        v_theta[j] = -0.5 / 3.0
    norm = np.linalg.norm(v_theta)
    if norm > 0:
        v_theta /= norm
    
    return v_rho, v_theta


def build_hamiltonian_sparse(N, level, version, rng):
    """
    IDENTICAL to prior run — same H construction.
    """
    addresses = [site_to_address(i, level) for i in range(N)]
    
    rows = []
    cols = []
    vals = []
    
    diag = np.full(N, -DELTA_OVER_N)
    burden_noise = None
    
    if version in ["V2", "V3"]:
        sigma_burden = 0.12 * DELTA_OVER_N
        burden_noise = sigma_burden * rng.standard_normal(N)
        diag += burden_noise
    
    # Parent groups
    parent_groups = {}
    for i in range(N):
        pk = addresses[i][:level-1]
        if pk not in parent_groups:
            parent_groups[pk] = []
        parent_groups[pk].append(i)
    
    # Grandparent groups
    grandparent_groups = {}
    if level >= 2:
        for i in range(N):
            gpk = addresses[i][:level-2]
            if gpk not in grandparent_groups:
                grandparent_groups[gpk] = []
            grandparent_groups[gpk].append(i)
    
    # d=1 hopping
    hop_1 = ETA ** 1
    for pk, members in parent_groups.items():
        for a in range(len(members)):
            for b in range(a+1, len(members)):
                i, j = members[a], members[b]
                rows.append(i); cols.append(j); vals.append(-hop_1)
                rows.append(j); cols.append(i); vals.append(-hop_1)
    
    # d=2 hopping
    if level >= 2:
        hop_2 = ETA ** 2
        for gpk, members in grandparent_groups.items():
            sub_parents = {}
            for i in members:
                pid = addresses[i][:level-1]
                if pid not in sub_parents:
                    sub_parents[pid] = []
                sub_parents[pid].append(i)
            plist = list(sub_parents.values())
            for a in range(len(plist)):
                for b in range(a+1, len(plist)):
                    for i in plist[a]:
                        for j in plist[b]:
                            rows.append(i); cols.append(j); vals.append(-hop_2)
                            rows.append(j); cols.append(i); vals.append(-hop_2)
    
    # V3 repair
    if version == "V3" and burden_noise is not None:
        damage_threshold = 0.12 * DELTA_OVER_N
        damaged = np.abs(burden_noise) > damage_threshold
        for pk, members in parent_groups.items():
            dmg = [i for i in members if damaged[i]]
            for a in range(len(dmg)):
                for b in range(a+1, len(dmg)):
                    i, j = dmg[a], dmg[b]
                    rows.append(i); cols.append(j); vals.append(-L_REPAIR)
                    rows.append(j); cols.append(i); vals.append(-L_REPAIR)
            for i in members:
                if damaged[i]:
                    nd = sum(1 for j in members if j != i and damaged[j])
                    diag[i] += L_REPAIR * nd * 0.5
    
    for i in range(N):
        rows.append(i); cols.append(i); vals.append(diag[i])
    
    H = sparse.csr_matrix((vals, (rows, cols)), shape=(N, N))
    return H, diag


def measure_ipr(eigvec):
    psi_sq = eigvec ** 2
    return np.sum(psi_sq ** 2)


def sector_overlap(eigvectors, sector_vec):
    """Compute |<ψ_k|sector_vec>|² for all eigenvectors."""
    overlaps = (eigvectors.T @ sector_vec) ** 2
    return overlaps


def run_sector_eigensolve(N, level, version, n_runs, rng):
    """
    Eigensolve with sector-resolved mode identification.
    """
    results_sigma1 = []  # per-run best σ₁
    results_sigma2 = []  # per-run best σ₂
    all_top3_sigma1 = []
    all_top3_sigma2 = []
    all_flags = []
    
    for run_idx in range(n_runs):
        t0 = time.time()
        
        H, diag = build_hamiltonian_sparse(N, level, version, rng)
        
        i0 = rng.integers(0, N)
        v_rho, v_theta = build_sector_defects(i0, N, level)
        
        sigma_shift = float(diag[i0])
        n_eig = min(30, N - 2)
        
        try:
            eigenvalues, eigenvectors = eigsh(H, k=n_eig, sigma=sigma_shift, which='LM')
        except Exception:
            eigenvalues, eigenvectors = eigsh(H, k=n_eig, which='SA')
        
        # Sector overlaps
        ov_rho = sector_overlap(eigenvectors, v_rho)
        ov_theta = sector_overlap(eigenvectors, v_theta)
        
        # ── σ₁: best P_ρ overlap ──
        sorted_rho = np.argsort(-ov_rho)
        top3_s1 = []
        for rank in range(min(3, len(sorted_rho))):
            k = sorted_rho[rank]
            evec = eigenvectors[:, k]
            ipr = measure_ipr(evec)
            top3_s1.append({
                "rank": rank + 1,
                "eig_index": int(k),
                "eigenvalue": float(eigenvalues[k]),
                "P_rho_overlap": float(ov_rho[k]),
                "P_theta_overlap": float(ov_theta[k]),
                "IPR": float(ipr),
                "F": float(ipr * N),
            })
        
        best_s1_k = sorted_rho[0]
        ipr_s1 = measure_ipr(eigenvectors[:, best_s1_k])
        results_sigma1.append(ipr_s1)
        all_top3_sigma1.append(top3_s1)
        
        # Near-degeneracy flag for σ₁
        s1_flag = None
        if len(sorted_rho) > 1:
            gap = abs(ov_rho[sorted_rho[0]] - ov_rho[sorted_rho[1]])
            if ov_rho[sorted_rho[0]] > 0 and gap / ov_rho[sorted_rho[0]] < NEAR_DEGEN_THRESHOLD:
                s1_flag = "NEAR_DEGENERATE_SIGMA1"
        
        # ── σ₂: best P_Θ overlap ──
        sorted_theta = np.argsort(-ov_theta)
        top3_s2 = []
        for rank in range(min(3, len(sorted_theta))):
            k = sorted_theta[rank]
            evec = eigenvectors[:, k]
            ipr = measure_ipr(evec)
            top3_s2.append({
                "rank": rank + 1,
                "eig_index": int(k),
                "eigenvalue": float(eigenvalues[k]),
                "P_rho_overlap": float(ov_rho[k]),
                "P_theta_overlap": float(ov_theta[k]),
                "IPR": float(ipr),
                "F": float(ipr * N),
            })
        
        best_s2_k = sorted_theta[0]
        ipr_s2 = measure_ipr(eigenvectors[:, best_s2_k])
        results_sigma2.append(ipr_s2)
        all_top3_sigma2.append(top3_s2)
        
        # Near-degeneracy flag for σ₂
        s2_flag = None
        if len(sorted_theta) > 1:
            gap = abs(ov_theta[sorted_theta[0]] - ov_theta[sorted_theta[1]])
            if ov_theta[sorted_theta[0]] > 0 and gap / ov_theta[sorted_theta[0]] < NEAR_DEGEN_THRESHOLD:
                s2_flag = "NEAR_DEGENERATE_SIGMA2"
        
        flags = [f for f in [s1_flag, s2_flag] if f is not None]
        all_flags.append(flags)
        
        dt = time.time() - t0
        print(f"    Run {run_idx+1}/{n_runs}: "
              f"σ₁(P_ρ): F={ipr_s1*N:.2f}, ov={ov_rho[best_s1_k]:.4f} | "
              f"σ₂(P_Θ): F={ipr_s2*N:.2f}, ov={ov_theta[best_s2_k]:.4f} | "
              f"flags={flags} ({dt:.1f}s)", file=sys.stderr)
    
    # Aggregate
    iprs1 = np.array(results_sigma1)
    iprs2 = np.array(results_sigma2)
    baseline = 1.0 / N
    Fs1 = iprs1 / baseline
    Fs2 = iprs2 / baseline
    
    return {
        "sigma1": {
            "IPR_mean": float(np.mean(iprs1)),
            "IPR_std": float(np.std(iprs1, ddof=1)) if len(iprs1) > 1 else 0.0,
            "F_mean": float(np.mean(Fs1)),
            "F_std": float(np.std(Fs1, ddof=1)) if len(Fs1) > 1 else 0.0,
            "F_min": float(np.min(Fs1)),
            "F_max": float(np.max(Fs1)),
            "all_F": Fs1.tolist(),
            "top3_per_run": [[{
                "rank": t["rank"],
                "F": round(t["F"], 4),
                "P_rho_ov": round(t["P_rho_overlap"], 6),
                "P_theta_ov": round(t["P_theta_overlap"], 6),
            } for t in run] for run in all_top3_sigma1],
        },
        "sigma2": {
            "IPR_mean": float(np.mean(iprs2)),
            "IPR_std": float(np.std(iprs2, ddof=1)) if len(iprs2) > 1 else 0.0,
            "F_mean": float(np.mean(Fs2)),
            "F_std": float(np.std(Fs2, ddof=1)) if len(Fs2) > 1 else 0.0,
            "F_min": float(np.min(Fs2)),
            "F_max": float(np.max(Fs2)),
            "all_F": Fs2.tolist(),
            "top3_per_run": [[{
                "rank": t["rank"],
                "F": round(t["F"], 4),
                "P_rho_ov": round(t["P_rho_overlap"], 6),
                "P_theta_ov": round(t["P_theta_overlap"], 6),
            } for t in run] for run in all_top3_sigma2],
        },
        "flags_per_run": all_flags,
        "IPR_baseline": float(baseline),
    }


def classify_regime(F):
    if F < 1.0: return "subcritical"
    elif F < 3.0: return "marginal"
    elif F < 10.0: return "intermediate"
    else: return "strong"


def build_block(version, bg_label, N, level, stats, n_runs):
    F_s1 = stats["sigma1"]["F_mean"]
    F_s2 = stats["sigma2"]["F_mean"]
    regime_s1 = classify_regime(F_s1)
    
    gates_passed = []
    gates_failed = []
    
    if F_s1 >= 10.0:
        gates_passed.append("P1")
    elif 3.0 <= F_s1 < 10.0:
        gates_passed.append("C1")
    elif F_s1 < 3.0:
        gates_failed.append("F1")
    
    if F_s2 < 2.0:
        gates_passed.append("P3")
    if F_s2 >= 5.0:
        gates_failed.append("C2")
    
    # C2 resolution check
    c2_resolved = F_s2 < 2.0
    c2_status = "RESOLVED (selector artifact)" if c2_resolved else "PERSISTENT (real physics challenge)"
    
    # Evidence quality
    if F_s2 >= 5.0:
        eq = "ANOMALOUS"
    elif F_s1 >= 10.0:
        eq = "EIGENSOLVE_STRONG_SECTOR_RESOLVED"
    elif 3.0 <= F_s1 < 10.0:
        eq = "EIGENSOLVE_INTERMEDIATE_SECTOR_RESOLVED"
    else:
        eq = "EIGENSOLVE_WEAK_SECTOR_RESOLVED"
    
    # Count flags
    total_flags = sum(len(f) for f in stats["flags_per_run"])
    
    ts = datetime.datetime.now(datetime.timezone.utc)
    
    return {
        "version": "1.0",
        "schema": "B_rho_raw_sector_resolved",
        "run_id": f"OSCAR-SECTOR-{version}-{bg_label}-{ts.strftime('%Y%m%dT%H%M%SZ')}",
        "timestamp": ts.isoformat(),
        "executor": "Oscar (Cato-executed, sector-resolved eigensolve)",
        "profile": f"H_SIGMA1-SECTOR-RESOLVED-{version}",
        "method": "eigsh + P_ρ/P_Θ sibling-parity projectors",
        "selector_version": "SECTOR-ID-REPAIR v1.0",
        "N_sites": N,
        "ifs_level": level,
        "background": bg_label,
        "eta": round(ETA, 6),
        "r": round(R_IFS, 6),
        "L_repair": L_REPAIR,
        "N_runs_averaged": n_runs,
        
        "sigma1_label": "sector-resolved (current scalar-operator lane)",
        "IPR_sigma1": round(stats["sigma1"]["IPR_mean"], 14),
        "F_sigma1": round(F_s1, 4),
        "F_sigma1_std": round(stats["sigma1"]["F_std"], 4),
        "F_sigma1_min": round(stats["sigma1"]["F_min"], 4),
        "F_sigma1_max": round(stats["sigma1"]["F_max"], 4),
        "regime_sigma1": regime_s1,
        
        "sigma2_label": "parity-odd Θ-proxy (not full Θ-sector closure)",
        "IPR_sigma2": round(stats["sigma2"]["IPR_mean"], 14),
        "F_sigma2": round(F_s2, 4),
        "F_sigma2_std": round(stats["sigma2"]["F_std"], 4),
        "F_sigma2_min": round(stats["sigma2"]["F_min"], 4),
        "F_sigma2_max": round(stats["sigma2"]["F_max"], 4),
        "regime_sigma2": classify_regime(F_s2),
        
        "IPR_baseline": round(stats["IPR_baseline"], 14),
        "IPR_sigma1_std": round(stats["sigma1"]["IPR_std"], 14),
        
        "c2_prior_status": "ANOMALOUS (from overlap-rank selector)",
        "c2_sector_resolved_status": c2_status,
        "c2_outcome": "RESOLVED" if c2_resolved else "PERSISTENT",
        
        "near_degeneracy_flags_total": total_flags,
        "flags_per_run": stats["flags_per_run"],
        
        "top3_sigma1": stats["sigma1"]["top3_per_run"],
        "top3_sigma2": stats["sigma2"]["top3_per_run"],
        
        "evidence_quality": eq,
        "gate_passed": gates_passed,
        "gate_failed": gates_failed,
    }


def main():
    rng = np.random.default_rng(seed=2026)
    
    test_levels = [(5, 1024), (6, 4096)]
    try:
        _ = np.zeros((16384, 30), dtype=np.float64)
        del _
        test_levels.append((7, 16384))
    except MemoryError:
        pass
    
    N_RUNS = 10
    all_blocks = []
    
    for level, N in test_levels:
        print(f"\n{'='*70}", file=sys.stderr)
        print(f"LEVEL {level}, N = {N} — SECTOR-RESOLVED RERUN", file=sys.stderr)
        print(f"{'='*70}", file=sys.stderr)
        
        n_runs = N_RUNS if N <= 4096 else 5
        
        for version, bg_label in [("V2", "burden"), ("V3", "burden+repair"), ("V1", "symmetric")]:
            print(f"\n  {version}: {bg_label} (N={N}, {n_runs} runs)...", file=sys.stderr)
            stats = run_sector_eigensolve(N, level, version, n_runs, rng)
            block = build_block(version, bg_label, N, level, stats, n_runs)
            
            notes = [
                f"Sector-resolved eigensolve on {N}×{N} IFS Hamiltonian",
                "σ₁ selector: argmax |<ψ_k|P_ρ δ_i0>|² (even-parity/reactive)",
                "σ₂ selector: argmax |<ψ_k|P_Θ δ_i0>|² (odd-parity/Θ-proxy)",
                "P_ρ/P_Θ from sibling-group parity decomposition",
                f"Near-degeneracy threshold: {NEAR_DEGEN_THRESHOLD*100:.0f}%",
                "H is IDENTICAL to prior eigensolve — only selector changed",
            ]
            if "burden" in bg_label:
                notes.append("Burden disorder: σ = 0.12 × Δ/N")
            if "repair" in bg_label:
                notes.append(f"Repair coupling: L_repair = {L_REPAIR}")
            notes.append(f"N_runs = {n_runs}, seed = 2026")
            block["notes"] = notes
            
            all_blocks.append(block)
            
            print(f"  RESULT: σ₁ F={stats['sigma1']['F_mean']:.2f}  |  "
                  f"σ₂ F={stats['sigma2']['F_mean']:.2f}  |  "
                  f"C2={'RESOLVED' if stats['sigma2']['F_mean'] < 5.0 else 'PERSISTENT'}", file=sys.stderr)
    
    # Summary
    print(f"\n{'='*70}", file=sys.stderr)
    print("SECTOR-RESOLVED SUMMARY", file=sys.stderr)
    print(f"{'='*70}", file=sys.stderr)
    print(f"{'Ver':>4} {'BG':>15} {'N':>6} {'F_σ₁':>10} {'F_σ₂':>10} {'C2':>12}", file=sys.stderr)
    for b in all_blocks:
        print(f"{b['profile'].split('-')[-1]:>4} {b['background']:>15} {b['N_sites']:>6} "
              f"{b['F_sigma1']:>10.2f} {b['F_sigma2']:>10.2f} {b['c2_outcome']:>12}", file=sys.stderr)
    
    print(json.dumps(all_blocks, indent=2))


if __name__ == "__main__":
    main()
