# UD-PM-PRED06-PAR-003 v1.0 — Finite opposite-edge parity cannot additively supply integer winding

**Kind:** NO-GO (finite-torsion group bridge). **Status:** EXACT_CONDITIONAL / VERIFIED_SCOPED. **Review:** DEFERRED. **Physical promotion:** 0.

## Statement and objects

Take the typed opposite-edge parity carrier as the additive group \(\Theta\cong(\mathbb Z/2\mathbb Z)^3\) of eight states, following the project's historical parity-fiber convention. Take the winding carrier as the additive group \(\mathbb Z\), whose nonzero elements represent distinct integer cohomology periods. Suppose a proposed *native linear/additive bridge* \(f:\Theta\to\mathbb Z\) respects composition: \(f(x+y)=f(x)+f(y)\).

**Theorem:** Every such homomorphism \(f\) is identically zero; in particular the parity group cannot, by a deterministic additive state homomorphism alone, produce nonzero arbitrary integer winding \(n\).

**Proof.** For each \(x\in\Theta\), \(2x=0\). Therefore \(2f(x)=f(2x)=f(0)=0\). Since \(\mathbb Z\) is torsion-free, \(f(x)=0\) for every \(x\). QED.

**Independent check:** exhaustively tested 125 candidate assignments of integer images \((-2,-1,0,1,2)^3\) to the three generators, checking all \(64\) ordered pairs of parity states per assignment. Only the trivial triple was additive. The theorem above establishes the result beyond the checked range.

## Scope and reopening

The obstruction applies to **additive homomorphisms** from this finite parity group. A nonhomomorphic map can assign a finite list of integer labels, but cannot inject the unrestricted integer set into eight static states. A multi-event integer counter, a noncompact phase lift, an oriented history/cohomology register, or a graph covering construction can extend the state space; those are additional typed objects and mechanisms, not a contradiction of this no-go.

The finite parity variable is not equal to the 1-cochain \(a\), its periods, a physical phase, or elapsed time merely because numerical outputs coincide. Which additional variable UD's admitted dynamics actually supplies is OPEN_GATED. Physical promotion 0.
