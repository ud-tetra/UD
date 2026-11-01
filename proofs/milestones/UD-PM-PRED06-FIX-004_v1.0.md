# UD-PM-PRED06-FIX-004 v1.0 — Fixed-incidence K4 dynamics cannot change the carrier's homology

**Kind:** NO-GO (typed dynamical/topological boundary). **Status:** EXACT_CONDITIONAL / VERIFIED_SCOPED. **Review:** DEFERRED. **Physical promotion:** 0.

## Source and theorem

The August 2026 typed ledger Q169 gives a skew Hodge–Dirac support generator on a fixed unique-simplex chain carrier \(C_0\oplus C_1\oplus C_2\oplus C_3\); Q165 fixes its normalized quadratic support ledger; Q153/Q162 govern burden fields/currents on supplied incidences. These source equations do **not**, by themselves, define a rule replacing the simplicial boundary matrices.

Let \(K\) be a fixed finite simplicial complex with boundary maps \(\partial_k\) satisfying \(\partial_{k-1}\partial_k=0\). Let \(x(t)\) be arbitrary time-dependent chain/cochain amplitudes, possibly under a state-dependent generator \(\dot x=A(x,t)x\), and let burden, parity and gates vary. Assume the **carrier and all incidence/boundary maps are fixed** throughout the evolution.

**Theorem:** The Betti numbers \(\beta_k(K;\mathbb F)\) and integral homology groups \(H_k(K;\mathbb Z)\) are constant under that evolution, regardless of amplitude redistribution or contact masking in \(A\). In particular it cannot change the original 3-ball from \(H_1=0\) into a tunnel with \(H_1\cong\mathbb Z\).

**Proof.** Homology is \(H_k=\ker\partial_k/\operatorname{im}\partial_{k+1}\). Its groups depend on the fixed chain modules and fixed boundary maps, not on the coefficients of \(x(t)\). Since both maps and modules are unchanged, their kernels and images are unchanged; so is homology. QED.

## Exact scope

The no-go does **not** prohibit topology-changing UD dynamics. A state-dependent support rule \(K\mapsto K'\), stellar collapse, declared excision or cell creation can change the chain groups or incidence matrices, defining a new evolution model. It is not contained in a generator acting only on amplitudes of a fixed carrier. A change in **support of a vector** is not automatically a change in the **underlying simplicial complex**: converting support into an active subcomplex requires a type-correct occupancy/threshold operation with its own source derivation. Similarly a Pachner move preserving PL topology cannot change integral homology.

**Required next proof:** a genuinely native occupancy/update operation, fed by a source-derived gate and explicit source/sink conservation, that changes the carrier and preserves legal glueing. Source Q153 alone is a continuity identity, not this operation. Physical promotion 0.
