# Finite-window reversible joint carrier: source and scope review v0.1

14 October 2026 UTC. Development — no registry entry. Physical promotion: 0.

Reviewer: Codex `source_program_audit` parallel AI thread. Separate AI source/scope reasoning, not human peer review, empirical evidence, custodian promotion or CRL-2b eligibility. This review concerns the proposed algebraic construction and source support; it does not certify a native implementation.

Source inspected: local `dist/papers/UD_PAPER_IV_REVIEW_DRAFT_v0.1.md` in `/workspace/sites/unified-dynamics-public`, plus prior Hodge-to-RSP obstruction and RSP candidate semantics. Final implementation and proof, including stock-ledger and integer-capacity additions, were subsequently inspected: `joint_carrier.py`, SHA-256 `29f1685df53432edcf2662b07d6fefe81abcc3a35552ebe664f3bc9f2611da71`; `dist/sources/joint-carrier-v0.1/UD_FINITE_WINDOW_JOINT_CARRIER_v0.1.md`, SHA-256 `d2642a6d5f03986e83cc6ab47198de289769fd3204c26e5b903ba3a81b52b911`. Final findings bind these versions.

## Exact reversible compute gate

Take work and each selected history tap in Z_d, one matching record cell in Z_m per tap, and supplied TOTAL maps F:Z_d→Z_d and rho:Z_d→Z_m. The gate

G_i(w,h_i,r)=(h_i+F(w) mod d, w, r+rho(w) mod m)

is a permutation. Given output (w',h_i',r'), its inverse is

w=h_i', h_i=w'−F(h_i') mod d, r=r'−rho(h_i') mod m.

Unused taps are unchanged. No injectivity of F is needed. Computational-basis linear extension is unitary. On a fresh tap h_i=0 the new work label is exactly F(w). Off that prepared subdomain it is generally NOT F(w); a consumed history tap cannot be reused as if blank.

The final construction takes d=|S| and a bijective encoding of a complete finite forward-invariant set S, so every modular label has an admitted state and the supplied F/rho are already total. There are no unused modular labels in this construction. Optional separate binary embedding could introduce unused bit strings, which would then need a declared total reversible extension; that is a separate implementation issue. Encoding s0 as label 0 is a declared bijective convention; it does not make all-zero registers physically free.

## Clock-controlled joint permutation and finite window

For a clock c in Z_L and a payload permutation P_c at each clock address, the master step U(c,z)=(c+1 mod L,P_c z) is a permutation. Its inverse decrements the clock then applies the inverse payload block at that prior address. A scheduled compute gate, SWAP or identity is lawful P_c.

With L=(B+1)(N+1), blocks contain N compute gates followed by one boundary slot. For the first B boundaries, SWAP the COMPLETE active payload with a distinct matched donor. The final boundary is identity. From c=0 with the declared fresh active payload and B fresh donors, the first L−1 transitions complete B+1 N-step episodes and B reset blocks, leaving c=L−1. The next final identity/increment wraps the clock to 0; later compute uses dirty history/record resources and carries no renewed episode guarantee.

The master clock is never reset at an episode boundary. That is essential: the reset exchanges the computational payload, while the progressing controller remains a separate register. This is not the complete-module clock replacement described in Paper IV §8.1. The entire cyclic operator is finite and recurrent; the finite-window guarantee does not evade the earlier global settling-factor obstruction.

To reprepare the whole joint apparatus one would need a fresh matched COMPLETE-joint donor, including master clock, active payload and outgoing donor bank, then export the complete old joint state and its external correlations. No such fresh source is supplied by this construction.

## Correlation and resource assumptions

Paper IV §2 defines complete joint domains and arbitrary spectators; a matched donor means equal carrier dimensions and, for an energy-preserving claim, equal bare energy operators. Equal mean energy is insufficient. This construction can claim an exact label/unitary SWAP from matched dimensions alone. It must NOT inherit energy-preserving exchange without separately specifying and matching bare energies.

Paper IV §8.1, Theorem IV.12, proves

SWAP_AD(rho_AY tensor sigma_D)SWAP_AD = sigma_A tensor rho_DY.

Thus fresh independent donors reset the active payload while retaining all outgoing information and correlations in D/Y. Do not trace out outgoing donors or replace their state by a blank description when making complete joint claims. A donor correlated with the active state or spectator does not provide the assumed independent target preparation; whole-bank correlations require explicit admission.

Paper IV §8.2, Proposition IV.13, charges complete bank error and full-joint operation errors unconditionally. Good single-donor marginals do not prove a good independent bank. Success and failure slots remain part of the resource ledger. Exact prepared-basis calculations do not alone verify a physical bank.

## Source support and scope differences

- Paper IV §4, Theorem IV.4, constructs supplied finite history words through an engineered clock. It explicitly leaves gate synthesis, launch and locality debt. It supports conditional prepared-controller mathematics, not this new modular clock/gate schedule as native Hodge dynamics.
- Paper IV §5.1 states that matched exchange swaps unknown states and correlations without cloning or creating blanks. §5.2 retains record/witness correlations and supplied control costs.
- Paper IV §6, Theorem IV.9, excludes exact permanent first-entry capture for a finite static Hamiltonian under its stated reducing-subspace/analyticity conditions. It permits finite-horizon retention or open/supplied controls. It must not be applied as though a discrete finite-window label guarantee were a continuous-time absorbing theorem.
- Paper IV §8.1 calls static complete-module renewal an algebraic continuation and does not certify an autonomous renewal/router. The new master schedule is an explicitly supplied candidate completion, not recovery of that missing native router.
- Paper IV §8.2 specifies finite END_OF_SUPPLY refusal with NO modular wrap. The proposed cyclic master clock deliberately differs: its finite first window is guaranteed and wrap is disclosed as dirty-resource reuse. Do not cite the source refusal policy as if this schedule implements permanent refusal.
- Paper IV §9 distinguishes total versus subsystem energy, mathematical energy conventions, supplied blank resources and implementation debts. No physical energy, Joule cost, calibrated SI time, Born-rule measurement claim or native coupling follows here.

## Information capacity versus entropy or heat

For this explicit allocation with N history taps, one work label and N Z_m record cells, payload dimension is D=d^(N+1)m^N. B donor payloads plus the active one and an L-address clock give joint label dimension L D^(B+1). This is allocated Hilbert-space/label capacity. It is not a minimal memory theorem, entropy produced or thermodynamic cost.

The history taps retain a redundant full trace. A valid distinguishability lower bound is narrower: a reversible implementation of a many-to-one map F must retain mutually distinguishable records for inputs sharing the same output, so available garbage dimension is at least max_y |F^−1(y)| on the admitted input domain. For an N-step map the corresponding bound uses |(F^N)^−1(y)|, not automatically d^N. No N log2(d) minimal entropy claim follows from this construction.

In the final implementation rho assigns a per-tick dictionary receipt, not a cumulative count. `compile_rsp` uses d complete prepared-trajectory states, m=d+1 record labels, rho(w)=w+1, and dictionary label 0 for BLANK. During the guaranteed window each fresh record cell receives one dictionary label, so no cumulative-count overflow condition is needed. On dirty cells addition can wrap to 0; the proof correctly identifies that as reversible arithmetic rather than restored blank supply.

A deterministic known prepared input can leave all basis records pure, with zero Shannon uncertainty and no global von Neumann entropy increase under the joint unitary. Random ensembles and coherent superpositions have different marginal entropy/correlation behavior. Register dimension alone fixes neither. No bath temperature, Hamiltonian, thermalization or irreversible erasure protocol is specified, so no Landauer heat minimum or Joule number is derived. Supply of fresh independent payloads and eventual disposal/reset remain explicit resource debts.

## Disposition

Exact candidate permutation/unitary and first-window reset/export semantics are supportable under total-map, fresh-tap, matched-dimension and independent complete-bank assumptions. The whole finite carrier preserves information and correlations, then recurs or reuses dirty resources. It does not provide permanent native settling, unlimited renewal, native Hodge realization, physical measurement or SI clock. Physical promotion remains 0.

## Final code/proof reconciliation

The final code uses N separate history cells and N separate dictionary-record cells, validates complete modular domains at every joint step, and implements the displayed inverse with matching recovered pre-state. The master inverse decrements clock before selecting the inverse block; SWAP is its own inverse. The proof's prefix induction, K=L−1 transition count, final no-op/wrap caveat, donor correlation export and complete-restart boundary agree with the implementation.

No concrete final code/proof mismatch was found. The earlier review's single-accumulator capacity description was corrected here to N record cells, and its generic invalid-label/overflow concerns are narrowed to optional binary embeddings and dirty-cell reuse. Exact prepared-trajectory compilation is disclosed as narrower than universal RSP preparation and is not claimed as an independently predictive native bridge. This final disposition is source/scope inspection, not an independent execution receipt, human peer review or scientific promotion.

The final integer expression `(dimension−1).bit_length()` equals ceil(log2(dimension)) for every positive dimension, including dimension 1 where capacity is 0. It avoids floating-point rounding in allocated capacity.

The additional stock ledger sums encoded `available_stock` only on active and donor WORK factors. History and receipt snapshots remain nonspendable descriptions. Inside the prepared window, a fresh compute applies the RSP transition so the total work-factor stock falls by `consumed_tokens`; internal RSP renewal preserves available stock; payload SWAP merely permutes work factors and preserves total. Moving a block to the outgoing prefix removes its remaining stock from runnable supply without deleting it from retained inventory. None of these logical-token changes is a physical energy balance or global entropy claim.

A targeted addition check ran 36 prepared C/H witness windows (N=1–6, B=0–2), checking per-SWAP conservation and initial-minus-final inventory equal to all recorded consumption, and checked the integer-capacity identity for dimensions 1–1000. All passed. This is bounded AI reviewer replay of newly authored code, not an independent physical episode. Short one-tick episodes correctly export cached/remaining state without assuming terminal exhaustion; the window theorem does not assert every N is a complete RSP termination horizon.
