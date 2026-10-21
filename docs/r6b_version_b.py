#!/usr/bin/env python3
"""
OSCAR — R6b VERSION B: Burden in ρ channel only.

H_ρρ: sibling (−η²), diagonal + λ_ρ(1−η^h) + σ_ρ·z_i  [BURDENED]
H_ΘΘ: cousin+2nd-cousin (−η⁴,−η⁶), degree-only diagonal  [CLEAN]
H_ρΘ: P_i·ν·X_i·Y_i  [UNCHANGED]

σ_ρ = 0.12 × λ_ρ ≈ 0.004375
N_runs ≥ 10 per level (fresh disorder each run)
"""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh
import json, datetime, sys, time

ETA = 185.0 / 192.0
ETA2 = ETA ** 2
ETA4 = ETA ** 4
ETA6 = ETA ** 6
LAMBDA_RHO = 7.0 / 192.0
SIGMA_RHO = 0.12 * LAMBDA_RHO  # burden strength
NU = ETA2 * (1.0 - ETA)

N_RUNS = 10


def site_to_address(idx, level):
    addr = []
    s = idx
    for _ in range(level):
        addr.append(s % 4)
        s //= 4
    return tuple(reversed(addr))


def get_variable_depth(idx, level):
    addr = site_to_address(idx, level)
    for k in range(level):
        if addr[k] != 0:
            return k + 1
    return level


def compute_parity(idx, level):
    addr = site_to_address(idx, level)
    return (-1) ** (sum(addr) % 2)


def build_static_parts(N, level):
    """Build connectivity and static arrays (reused across runs)."""
    addresses = [site_to_address(i, level) for i in range(N)]
    depths = np.array([get_variable_depth(i, level) for i in range(N)])
    parities = np.array([compute_parity(i, level) for i in range(N)])

    # Siblings (d=1)
    parent_groups = {}
    for i in range(N):
        pk = addresses[i][:level-1]
        if pk not in parent_groups:
            parent_groups[pk] = []
        parent_groups[pk].append(i)
    sib_pairs = []
    for members in parent_groups.values():
        for a in range(len(members)):
            for b in range(a+1, len(members)):
                sib_pairs.append((members[a], members[b]))

    # Cousins (d=2)
    cousin_pairs = []
    if level >= 2:
        gp_groups = {}
        for i in range(N):
            gpk = addresses[i][:level-2]
            if gpk not in gp_groups:
                gp_groups[gpk] = []
            gp_groups[gpk].append(i)
        for members in gp_groups.values():
            sub = {}
            for i in members:
                pid = addresses[i][:level-1]
                if pid not in sub:
                    sub[pid] = []
                sub[pid].append(i)
            plist = list(sub.values())
            for a in range(len(plist)):
                for b in range(a+1, len(plist)):
                    for i in plist[a]:
                        for j in plist[b]:
                            cousin_pairs.append((i, j))

    # Second-cousins (d=3)
    sc_pairs = []
    if level >= 3:
        ggp_groups = {}
        for i in range(N):
            ggpk = addresses[i][:level-3]
            if ggpk not in ggp_groups:
                ggp_groups[ggpk] = []
            ggp_groups[ggpk].append(i)
        for members in ggp_groups.values():
            sub_gp = {}
            for i in members:
                gpid = addresses[i][:level-2]
                if gpid not in sub_gp:
                    sub_gp[gpid] = []
                sub_gp[gpid].append(i)
            gplist = list(sub_gp.values())
            for a in range(len(gplist)):
                for b in range(a+1, len(gplist)):
                    for i in gplist[a]:
                        for j in gplist[b]:
                            sc_pairs.append((i, j))

    # Precompute static H_ΘΘ (doesn't change between runs)
    t_r, t_c, t_v = [], [], []
    theta_deg = np.zeros(N)
    for i, j in cousin_pairs:
        t_r.append(i); t_c.append(j); t_v.append(-ETA4)
        t_r.append(j); t_c.append(i); t_v.append(-ETA4)
        theta_deg[i] += ETA4; theta_deg[j] += ETA4
    for i, j in sc_pairs:
        t_r.append(i); t_c.append(j); t_v.append(-ETA6)
        t_r.append(j); t_c.append(i); t_v.append(-ETA6)
        theta_deg[i] += ETA6; theta_deg[j] += ETA6
    for i in range(N):
        t_r.append(i); t_c.append(i); t_v.append(theta_deg[i])

    # Precompute sibling degree
    sib_deg = np.zeros(N)
    for i, j in sib_pairs:
        sib_deg[i] += 1; sib_deg[j] += 1

    return {
        "sib_pairs": sib_pairs, "cousin_pairs": cousin_pairs, "sc_pairs": sc_pairs,
        "depths": depths, "parities": parities, "sib_deg": sib_deg,
        "theta_rows": t_r, "theta_cols": t_c, "theta_vals": t_v,
    }


def build_full_H(N, level, static, rng):
    """Build 2N×2N H with fresh burden disorder in ρ."""
    s = static
    burden = SIGMA_RHO * rng.standard_normal(N)

    f_r, f_c, f_v = [], [], []

    # H_ρρ with burden
    for i, j in s["sib_pairs"]:
        f_r.append(i); f_c.append(j); f_v.append(-ETA2)
        f_r.append(j); f_c.append(i); f_v.append(-ETA2)
    for i in range(N):
        h = s["depths"][i]
        diag = ETA2 * s["sib_deg"][i] + LAMBDA_RHO * (1 - ETA**h) + burden[i]
        f_r.append(i); f_c.append(i); f_v.append(diag)

    # H_ΘΘ (static, no burden)
    for i, j, v in zip(s["theta_rows"], s["theta_cols"], s["theta_vals"]):
        f_r.append(N+i); f_c.append(N+j); f_v.append(v)

    # H_ρΘ coupling
    for i in range(N):
        h = s["depths"][i]
        X = 1.0 - ETA**h
        Y = ETA**h - ETA**(2*h)
        c = s["parities"][i] * NU * X * Y
        if abs(c) > 1e-18:
            f_r.append(i); f_c.append(N+i); f_v.append(c)
            f_r.append(N+i); f_c.append(i); f_v.append(c)

    return sparse.csr_matrix((f_v, (f_r, f_c)), shape=(2*N, 2*N))


def analyze_mode(eigvec, N):
    psi_rho = eigvec[:N]
    psi_theta = eigvec[N:]
    W_rho = float(np.sum(psi_rho**2))
    W_theta = float(np.sum(psi_theta**2))
    IPR_rho = float(np.sum(psi_rho**4) / max(W_rho**2, 1e-30))
    IPR_theta = float(np.sum(psi_theta**4) / max(W_theta**2, 1e-30))
    return {"W_rho": W_rho, "W_Theta": W_theta,
            "F_rho": IPR_rho * N, "F_Theta": IPR_theta * N}


def run_single(N, level, static, rng):
    """Single burden realization → find σ₁ and σ₂."""
    H = build_full_H(N, level, static, rng)

    # Probe: we know from Version A that ρ min ≈ 0.00133, θ min ≈ 0
    # Burden shifts ρ eigenvalues slightly
    results = {}
    for sigma, label in [(0.00133, "rho"), (1e-8, "theta")]:
        try:
            evals, evecs = eigsh(H, k=5, sigma=sigma, which='LM', maxiter=N*20)
            for j in range(evecs.shape[1]):
                md = analyze_mode(evecs[:, j], N)
                key = round(float(evals[j]), 6)
                if key not in results:
                    results[key] = {"eigenvalue": float(evals[j]), **md}
        except:
            pass

    modes = sorted(results.values(), key=lambda m: abs(m["eigenvalue"]))

    s1 = next((m for m in modes if m["W_rho"] > 0.6), None)
    s2 = next((m for m in modes if m["W_Theta"] > 0.6), None)

    return s1, s2


def run_level(level, N, n_runs, rng):
    print(f"\n{'='*60}", file=sys.stderr)
    print(f"VERSION B: H={level}, N={N}, {n_runs} burden runs", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)

    t0 = time.time()
    static = build_static_parts(N, level)
    print(f"  Static parts built in {time.time()-t0:.1f}s", file=sys.stderr)

    all_F_s1 = []
    all_F_s2 = []
    all_ratios = []

    for run in range(n_runs):
        s1, s2 = run_single(N, level, static, rng)
        f1 = s1["F_rho"] if s1 else 0
        f2 = s2["F_Theta"] if s2 else 0
        ratio = f1 / max(f2, 0.01)
        all_F_s1.append(f1)
        all_F_s2.append(f2)
        all_ratios.append(ratio)
        print(f"    Run {run+1}/{n_runs}: F_σ₁^ρ={f1:.2f}  F_σ₂^Θ={f2:.2f}  ratio={ratio:.1f}", file=sys.stderr)

    F_s1 = np.array(all_F_s1)
    F_s2 = np.array(all_F_s2)
    ratios = np.array(all_ratios)

    result = {
        "level": level, "N": N, "n_runs": n_runs,
        "F_sigma1_rho_mean": float(np.mean(F_s1)),
        "F_sigma1_rho_std": float(np.std(F_s1, ddof=1)),
        "F_sigma1_rho_min": float(np.min(F_s1)),
        "F_sigma1_rho_max": float(np.max(F_s1)),
        "F_sigma2_Theta_mean": float(np.mean(F_s2)),
        "F_sigma2_Theta_std": float(np.std(F_s2, ddof=1)),
        "ratio_mean": float(np.mean(ratios)),
        "ratio_std": float(np.std(ratios, ddof=1)),
        "all_F_sigma1": [round(f, 2) for f in F_s1.tolist()],
        "all_F_sigma2": [round(f, 2) for f in F_s2.tolist()],
    }

    # Gate evaluation
    f1m = result["F_sigma1_rho_mean"]
    f2m = result["F_sigma2_Theta_mean"]
    rm = result["ratio_mean"]

    if f1m >= 10:
        result["sigma1_gate"] = "P1-ELIGIBLE (F ≥ 10)"
    elif f1m >= 3:
        result["sigma1_gate"] = "C1 (intermediate)"
    else:
        result["sigma1_gate"] = "F1 (weak)"

    if rm > 10:
        result["P3_hier"] = "PASSED"
    elif rm >= 3:
        result["P3_hier"] = "AMBIGUOUS"
    else:
        result["P3_hier"] = "FAILED"

    print(f"\n  MEAN: F_σ₁^ρ={f1m:.2f} ± {result['F_sigma1_rho_std']:.2f}", file=sys.stderr)
    print(f"  MEAN: F_σ₂^Θ={f2m:.2f} ± {result['F_sigma2_Theta_std']:.2f}", file=sys.stderr)
    print(f"  RATIO: {rm:.1f} ± {result['ratio_std']:.1f}", file=sys.stderr)
    print(f"  σ₁ gate: {result['sigma1_gate']}", file=sys.stderr)
    print(f"  P3_hier: {result['P3_hier']}", file=sys.stderr)

    return result


def main():
    rng = np.random.default_rng(seed=2026)
    results = []

    for level, N in [(5, 1024), (6, 4096), (7, 16384)]:
        r = run_level(level, N, N_RUNS, rng)
        results.append(r)

    # Try H=8
    try:
        print("\nAttempting H=8 (N=65536)...", file=sys.stderr)
        r8 = run_level(8, 65536, 5, rng)  # fewer runs
        results.append(r8)
    except Exception as e:
        print(f"H=8 failed: {e}", file=sys.stderr)

    # Scaling summary
    print(f"\n{'='*60}", file=sys.stderr)
    print("VERSION B SCALING SUMMARY", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)
    print(f"{'H':>3} {'N':>6} {'F_σ₁^ρ':>10} {'F_σ₂^Θ':>10} {'Ratio':>8} {'P3_hier':>10} {'σ₁ gate':>20}", file=sys.stderr)
    for r in results:
        print(f"{r['level']:>3} {r['N']:>6} {r['F_sigma1_rho_mean']:>10.2f} "
              f"{r['F_sigma2_Theta_mean']:>10.2f} {r['ratio_mean']:>8.1f} "
              f"{r['P3_hier']:>10} {r['sigma1_gate']:>20}", file=sys.stderr)

    # Check ratio trend
    if len(results) >= 2:
        ratios = [r["ratio_mean"] for r in results]
        increasing = all(ratios[i+1] >= ratios[i] * 0.9 for i in range(len(ratios)-1))
        print(f"\n  Ratio trend: {' → '.join(f'{r:.1f}' for r in ratios)}", file=sys.stderr)
        print(f"  Increasing (within 10%): {increasing}", file=sys.stderr)

    class Enc(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, (np.integer,)): return int(o)
            if isinstance(o, (np.floating,)): return float(o)
            if isinstance(o, (np.bool_,)): return bool(o)
            return super().default(o)

    ts = datetime.datetime.now(datetime.timezone.utc)
    output = {
        "schema": "R6b_VersionB_raw",
        "run_id": f"OSCAR-R6b-VB-{ts.strftime('%Y%m%dT%H%M%SZ')}",
        "timestamp": ts.isoformat(),
        "executor": "Oscar (Version B burden eigensolve)",
        "operator": "R6b + burden in ρ only",
        "burden_sigma": round(SIGMA_RHO, 8),
        "burden_channel": "rho only",
        "theta_burden": "none (clean)",
        "gate_family": "B (hierarchical/relative)",
        "results": results,
    }
    print(json.dumps(output, indent=2, cls=Enc))


if __name__ == "__main__":
    main()
