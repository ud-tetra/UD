# External Reviewer Brief — Winding & Response Pre-Registration Packet

**For a reviewer who did not construct this packet.** Your job is to break it.
The construction author has run two self-adversarial passes and found six of
his own errors (two material); the base rate says more remain. Physical
promotion is 0 and is not in question — do not spend effort there.

---

## What you are reviewing

A pre-registration packet (CRL-2a) proposing amendments to the frozen
discriminators of *Tetrahedral Packet Complexes* v2.40:

- **Part A** — winding-burden formation law. Claims the frozen 2-class scorer
  (§7.29) has a *false-positive channel*: an autocatalytic law (WBX1, κ≠0) and
  the quadratic law (WBQ1/HCB1) produce identical R_B on the k=0,1 sample.
  Proposed fix: add a third slip, test D₂ = ε₂−2ε₁+ε₀.

- **Part B** — response sidecar. Proposes parameter-free family falsifiers
  (V=0, replay, monotonicity) and a shell-coverage requirement.

- **Part C** — §4.10 scope note. Held pending a §7.6 custodian ruling.

## Verified independently (spend no time re-checking)

```
chain complex B1B2=0, B2B3=0; ranks (3,3,1); Betti (1,0,0,0)
A skew, A² = −4(I−P_H0), spectrum 1 zero + 14 at |λ|=2, A³+4A=0
receipts (I,T,B_k) = (1/4, 3/4, k/2)
H_seed = 101/6;  Θ≅F₂³ shells (1,3,3,1)
Lemma 1 (ω_p ≤ g_p) by exhaustion, class (1,0) empty
J²=−P₂, α_A = A₀/2 both routes, single-cell period π, no glued clock
```

## The load-bearing claim to attack

**A.3: the false-positive channel.** Everything in Part A depends on it. It
does NOT depend on the four framing gaps below. If A.3 is wrong, Part A falls.
If A.3 is right, Part A stands regardless of framing. Attack A.3 first.

## Known weaknesses the author already found (do not re-report; verify the fixes)

```
E.1  D₂≠0 is NOT unambiguous — needs Λ₂ returned to separate
     autocatalysis from non-stationary PLB1 leakage.        MATERIAL
E.2  Part A needs n=2 AND n=3 carriers that §7.13 says are
     unvalidated / unconstructed. Carrier-contingent, not
     schedule-contingent.                                   MATERIAL
A.1  R_B = 1+C/A needs A>0 domain condition.
A.2  family not confined to physical cone ε_k ≥ 0.
A.4  D₂ falsifies family only up to quadratic; cubic+
     needs Tier-3 E₃.
L.2  (0,1)=partial-integrity is definitional, not derived.
```

## Where the author most expects to be wrong next

1. **Part B replay (A2) feasibility.** Claimed ~10 same-class pairs at N=24
   under uniform occupancy. Occupancy is not uniform. Is the estimate real?
2. **Gate B necessity.** Is shell coverage actually needed, or does the
   existing §7.5 acquisition already hit w_H ∈ {1,2} incidentally?
3. **AICc interaction.** Does adding a 2-parameter WBX1 to a 36-run fit
   actually behave as claimed, or does small-n instability dominate?
4. **The physical-cone constraint (A.2).** Does ε_k ≥ 0 for all k bound
   (c,κ) to a region that excludes the very autocatalytic laws the packet
   is trying to detect? If so, the false-positive channel may be empty in
   the physical cone and the whole Part A remedy is moot.

Item 4 is the one that could collapse Part A. Start there if A.3 survives.

## Files

```
UD_PREREGISTRATION_PACKET_v1.0.md          the packet
UD_PACKET_v1.1_ERRATA.md                   first-pass corrections
UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md     governance proposal
this brief
```
