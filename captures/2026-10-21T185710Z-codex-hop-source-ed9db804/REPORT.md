# THM534 recovery attempt and microscopic-law identifiability v0.1

**SOURCE_BLOCKED / Development — no registry entry / Physical promotion0.**

## Recovery result
The original THM534 hop-probability derivation was not located in the bounded searches recorded in RECOVERY_RECEIPT.json. THM561 Weak-Color Mass Split v1.0 explicitly cites it and supplies T_self=1/2, T_opposite=1/6, T_cross=1/12 (§1.4), then derives the sector spectra (§3). That supplies a declared matrix and its downstream algebra, not the missing source probability measure or event map. The original source may exist elsewhere. No claim of its nonexistence is made. The July residue recovery references a separate7-channel matrix and cannot substitute for this6-channel source.

## What a complete THM534 return must contain
1. Exact event/sample space and source state variables, including which transitions are allowed and their orientation convention.
2. Source-derived probability/weight measure and normalization, not weights chosen to reproduce the desired matrix.
3. Map from each event and current state to its next channel, with exact conditional counts giving all three orbit probabilities.
4. Temporal law: whether event labels are resampled, correlated or persistent; memory state and renewal/reset mechanism.
5. Any asserted map from this update to energy, action, physical time or second-order motion. Hop probabilities alone supply none of those identities.
6. Source version/hash and proof dependencies; independent review remains separately required.

## Exact illustrative microrealization ambiguity
This is an inverse mathematical construction, expressly NOT a recovered UD derivation. On the unsigned six-edge states, take48 equally weighted deterministic permutation labels:20 identity labels,4 opposite-edge swap labels, and the24 vertex-permutation actions. Uniform averaging gives

T=(20I+4S+sum_g R_g)/48=(5I+S+J)/12.

The group average is J/6. Hence both processes below have exactly the declared first-step kernel:

A. Resample the label independently at each step. The second-step transition is T², with return probability11/36 for every channel.
B. Draw one label initially and retain it. The second-step transition is average(P_label²), with return probability3/4 for every channel.

The difference is exactly4/9. Both ensemble transition matrices remain nonnegative and doubly stochastic. ProcessB has hidden label memory and is not assumed Markov on the observed channel alone. No contradiction to THM561's declared Markov model is claimed. Rather, one-step probabilities do not recover the microscopic event/renewal law; an original derivation must specify it.

The coefficients20/4/24 were selected to realize the given T. Presenting them as first-principles UD counts would violate source governance. This example cannot justify the prior quadratic f(H), action calibration or a particle assignment. It is a countermodel to inferring a complete microscopic process from the first-step kernel alone.

## Disposition and stopping rule
Preserve the exact declared-matrix spectra, transfer obstructions, conditional11D lift and conserved-mean result. Keep microscopic provenance and conversion law SOURCE_BLOCKED. No new physical or registry claim advances. Further rescaling, matrix reconstruction or invented event counts cannot discharge this missing-source gate. Reopen this branch only upon a source-complete original or a newly declared, independently testable forward microscopic programme. A new model must carry a new origin label; it cannot be retroactively called THM534.

## Verification
verify_hop.py reconstructs all24 unsigned permutation matrices, exactly averages the48 event labels, checks both two-step laws and their positive/doubly-stochastic properties, and rejects their equality by the exact4/9 witness. It uses only standard-library Fraction arithmetic. Saved JSON replay is byte-identical. Constructor verification is not non-constructor review. No particle target dataset or external physical value was retrieved or scored. Gap2_FINAL_Finite_Genesis.png remains unavailable and unused; re-upload if it contains the missing source.
