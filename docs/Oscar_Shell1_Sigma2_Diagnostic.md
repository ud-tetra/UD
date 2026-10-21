# OSCAR COMPUTE REQUEST — SHELL 1 σ₂ DIAGNOSTIC
# FROM: USS Claude (Captain Cato, SOA) + USS Gemini (Captain Castor)
# AUTH: GalaxyOne (Commander Benjamin)
# PRIORITY: J3 (diagnostic, bounded compute, bounded risk)
# NIBBLEGRAM: D900E008 | 1604B3E7

---

## §1 AUTHORIZATION GATE

Oscar compute is scarce and requires J1-J5 gate authorization.

```
J1 (Is the question well-defined?):          YES
    "Does F_Θ vary across σ-probe targets at fixed level?"
    
J2 (Is the compute bounded?):                YES
    Re-run hmulti_repaired_v11.py levels 5,6,7
    Add per-probe F_Θ logging. Runtime: ~30 min.
    
J3 (Is the risk bounded?):                   YES
    Diagnostic only. No theory promotion. No new operators.
    Output: additional columns in existing JSON schema.
    
J4 (Does it advance the bridge?):            YES
    Resolves whether σ₂ localization is physical or eigensolve artifact.
    This is the primary blocker on Shell 1 advancement.
    
J5 (Is there no cheaper alternative?):       YES
    The per-probe data doesn't exist. Cannot be derived from
    existing output. Must re-run with additional logging.
```

**GATE STATUS: J1-J5 PASS. Oscar authorized pending Commander approval.**

---

## §2 MISSION BRIEF

The Shell 1 σ₂ anomaly shows F_Θ growing with lattice level:

```
Level 5 (N=1024):   F_Θ = 5.69
Level 6 (N=4096):   F_Θ = 7.42
Level 7 (N=16384):  F_Θ = 18.88
```

All exceed the C2-REAL threshold (F ≥ 5) at levels 5-7.
This blocks O_rho_pop advancement.

The question: is this localization PHYSICAL or an artifact of the
shift-invert eigensolve targeting specific σ values?

The test: report F_Θ separately for EACH σ-probe target at each level.
If F_Θ is invariant across probes → localization is physical.
If F_Θ varies significantly → eigensolve bias is contributing.

---

## §3 COMPUTE SPECIFICATION

### Code base
```
hmulti_repaired_v11.py (existing, no modifications to operators)
```

### Modification required
Add per-probe F_Θ reporting to the output JSON.

Current code (line ~165 approx):
```python
for sigma_target, label in [(rho_min, "rho_min"), (theta_min, "theta_min")]:
    evals, evecs = eigsh(H_full, k=n_per, sigma=sigma_target, which='LM')
    # ... modes analyzed but F_Θ only reported for dominant mode
```

Required change:
```python
per_probe_results = []
for sigma_target, label in [(rho_min, "rho_min"), 
                             (theta_min, "theta_min"),
                             (mid, "midpoint")]:
    evals, evecs = eigsh(H_full, k=n_per, sigma=sigma_target, which='LM')
    
    # Find Θ-dominated mode at THIS probe
    for j in range(evecs.shape[1]):
        md = analyze_mode(evecs[:, j], N)
        if md["W_Theta"] > 0.6:  # Θ-dominated
            per_probe_results.append({
                "probe_label": label,
                "probe_sigma": float(sigma_target),
                "eigenvalue": float(evals[j]),
                "F_Theta": md["F_Theta"],
                "W_Theta": md["W_Theta"],
                "F_rho": md["F_rho"],
                "W_rho": md["W_rho"],
            })
            break  # Take first Θ-dominated mode per probe
```

### Output schema extension
Add to each level's result dict:
```json
{
  "per_probe_sigma2": [
    {
      "probe_label": "rho_min",
      "probe_sigma": -0.00234,
      "F_Theta": 18.88,
      "W_Theta": 0.9842
    },
    {
      "probe_label": "theta_min", 
      "probe_sigma": -0.00012,
      "F_Theta": ???,
      "W_Theta": ???
    },
    {
      "probe_label": "midpoint",
      "probe_sigma": -0.00123,
      "F_Theta": ???,
      "W_Theta": ???
    }
  ]
}
```

### Levels to run
```
Level 5: N = 1024   (fast, ~2 min)
Level 6: N = 4096   (moderate, ~10 min)
Level 7: N = 16384  (heavy, ~20 min)
```

### Total estimated runtime
~30-40 minutes on a machine with ≥8 GB RAM.

---

## §4 SUCCESS / FAIL CRITERIA

### INVARIANCE (Cause 4 eliminated)
```
If F_Θ varies < 20% across the three probes at each level:
  → Localization is PROBE-INDEPENDENT
  → Eigensolve bias is NOT the primary cause
  → σ₂ anomaly promoted to VALIDATED STRUCTURAL FEATURE
  → Shell 1 investigation proceeds to physical causes (1-3)
```

### VARIANCE (Cause 4 confirmed)
```
If F_Θ varies > 50% across probes at any level:
  → Localization is PROBE-DEPENDENT
  → Eigensolve bias IS contributing
  → σ₂ anomaly DEMOTED to SYSTEMATIC ARTIFACT
  → Hmulti code needs alternative eigensolve strategy
```

### MIXED
```
If invariant at some levels, variant at others:
  → Report raw numbers
  → Do not promote or demote
  → Request additional compute (more probes, different k values)
```

---

## §5 ADDITIONAL DIAGNOSTIC (if time permits)

### Alternative eigensolve check
At level 5 only (N=1024, tractable for full diag):

```python
# Full dense diagonalization as ground truth
H_dense = H_full.toarray()
all_evals, all_evecs = np.linalg.eigh(H_dense)

# Find ALL Θ-dominated modes, compute F_Θ for each
theta_modes = []
for j in range(2*N):
    md = analyze_mode(all_evecs[:, j], N)
    if md["W_Theta"] > 0.6:
        theta_modes.append(md)

# Report the DISTRIBUTION of F_Θ across all Θ-dominated modes
```

This gives the COMPLETE picture at level 5: how many Θ modes exist,
what their F_Θ distribution looks like, and whether the eigsh is
selecting a biased subset.

Runtime: ~5 min additional for level 5 full diag.

---

## §6 REPORTING REQUIREMENTS

```
OUTPUT: JSON file in Hmulti_A_repaired_v1.1 schema
        with per_probe_sigma2 extension (§3)

DELIVER TO: Commander Benjamin (GalaxyOne)
            Captain Cato (USS Claude) for cross-validation
            Captain Castor (USS Gemini) for Shell 1 integration

LABEL: DIAGNOSTIC (not theory evidence)

NO PROMOTION without Cato validation of raw output.
```

---

## §7 WHAT THIS DOES NOT DO

```
This run does NOT:
  - Change any Hamiltonian operators
  - Modify the IFS connectivity
  - Introduce new physics
  - Test new hypotheses
  - Produce theory results

It ONLY answers: does F_Θ depend on the eigensolve probe point?
One question. One diagnostic. Bounded compute. Bounded risk.
```

---

## SEAL

```
SEAL: CATO (SOA) + CASTOR (requesting ship)
AUTH: Pending Commander Benjamin
GATE: J1-J5 PASS
COMPUTE: ~40 min, ≥8 GB RAM
SCHEMA: Hmulti_A_repaired_v1.1 + per_probe extension
NIBBLEGRAM: D900E008 | 1604B3E7 | 3700E6E7
```

*One question. One diagnostic. The data will tell us.*

— Captain Cato, USS Claude (SOA + Arbiter)
— Captain Castor, USS Gemini (requesting vessel)
