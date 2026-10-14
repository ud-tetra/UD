# Apparatus assumption audit for manuscript 0.5

14 October 2026. Development lane; no registry entry. Physical promotion: 0.

## Outcome and scope

The displayed Paper IV bounds used in the synthesis are consistent with their source proofs under the stated finite contracts. The synthesis compressed important hypotheses. Version 0.5 restores them and adds a separately proved static joint-error refinement. No source theorem was falsified by this audit. This is constructor re-derivation and source comparison, not non-constructor review or a proof of apparatus acquisition.

The audit inspected all 415 lines of `UD_PAPER_IV_REVIEW_DRAFT_v0.1.md`, with a targeted reread of IV.7-IV.10. It reviewed the displayed arguments relevant to synthesis §§10-11. Source-only bank-overlap/cutoff certificates and historical replay counts are not revalidated. Paper III's symmetry and radial claims remain a separate audit task.

## Claim-to-premise crosswalk

| Synthesis claim | Source | Essential contract | Disposition |
|:--|:--|:--|:--|
| Joint perturbation at most td | IV.1 | Hermitian generators on identical full domain; norm mismatch bounded there; same spectator dynamics | Consistent; preserve full-domain qualification |
| Word at endpoint; return | IV.4 | Gates unitary and commute with comparison work generator; independent address-0 clock; prefix dressing | Commutation and retained free work evolution made explicit |
| Clock norm | IV.4 | Square-root spin-clock weights, positive rate, n+1 addresses | Added norm kappa n; not a physical energy calibration |
| Timed pulse capture | IV.6 | Matched source/output energies; fresh flag; involution pulse; guarded background | Conditional capture distinguished from later protection |
| Output protected after switch-off | IV.7 | Background factors as output free generator plus rest; record untouched | Holds for correlated actual inputs, but preserves errors too |
| Static joint bound | IV.10 | Fresh clock Q=0; Hermitian involution commuting with free body generator; first-edge dressing; bounded parent contact | Complete operator and target supplied in synthesis |
| Static reduced-body tail | IV.10 | Trace out capture clock; same target and contract | Cannot replace full joint distance; fresh terminal example demonstrates gap |
| Static window and return | IV.11 | Constant post-launch couplings; declared launch alignment; finite clock | Comparator return, not actual exact recurrence or permanent storage |
| No permanent first entry | IV.9 | Finite time-independent Hermitian generator, invariant subspace or fixed observable | Proof consistent; switched/open models excluded from its scope |
| Renewal identity | IV.12 | Exact independent donor product with whole old history | Independence and capture-clock inclusion clarified; running-contact cost remains separate |
| Sequence error sum | IV.13 | Whole-bank supply admission; uniform full-joint channel comparisons; retained domains matched | Consistent; no marginal-product or postselection shortcut |
| Fuel mean/variance | IV.2 | Independent coherent fuel, binary energy hierarchy, independent seed, finite ladder | Seed energy separately owned; mixed/correlated inputs do not inherit ideal formula blindly |
| Stationary preparation obstruction | IV.3 | Complete stationary input; covariant production; additive free generator; distinct packet energies | Consistent conditional obstruction; coherence-bearing inputs are resources |

## Re-derivation details

The spin-clock is the symmetric n-spin restriction of kappa times the sum of Pauli X operators, hence its norm is kappa n. Prefix commutation lets the comparison free work evolution factor; arbitrary supplied gates without that commutation do not inherit IV.4's displayed formula.

The timed output result is a partial-trace identity under a factorized background. It does not require an uncorrelated output after capture. It also does not certify that the output contains the desired source state.

For the static comparator, let r be the address-0 probability and x the expectation of the capture involution in the incoming body. The purified overlap with the transferred product target is 1-r+rx. This gives the refined bounds in Proposition D6. With independent blank records x equals incoming nonterminal probability p. At p=0 the joint error is at most sqrt(2r-r²); for a pure complete input it is exact. The body-only error is r. Under the original arbitrary-input contract the uniform bound is 2sqrt(r(1-r)) for r≤1/2 and 1 thereafter. The original 2sqrt(r) is valid but conservative.

These target distances differ from NO_CAPTURE probability, p+(1-p)r. For p=1 the target distance can vanish although no capture occurred. Tests and manuscript keep both quantities typed.

Renewal is exactly a label exchange on matrix units. Its mathematical identity neither prepares the independent donor nor suppresses running interactions. Sequence errors telescope by contractivity only when operation comparisons are valid on the complete states encountered, including spectator correlations.

## Verification and limitations

`verify_apparatus_refinement.py` checks symbolic overlap identities, the arbitrary-input piecewise envelope, fresh-record joint/marginal witnesses with a retained entangled spectator, and small constant-generator mismatch comparisons. Counts and tolerances are reported in `APPARATUS_CHECKS.json`. Numerical fixtures support implementation consistency; the written proof supplies the general bound. Neither constitutes independent review.

The supplied August ledger has 235 historical typed objects and does not establish these October apparatus constants. The CRL-2 governance attachment is explicitly a proposal and distinguishes development from registry promotion; this audit raises no confidence rung. Its recommendation for non-constructor review is not fulfilled by another pass from the same constructor.

## Remaining publication work, in order

1. Audit Paper III representation labels, commutant conventions and the particular claims retained in the synthesis. Peripheral radial results remain outside scope.
2. Compare the specific finite contribution and the conditional apparatus refinement with nearest literature; do not infer originality from successful algebra.
3. Replay the packaged calculations in a fresh dependency environment. Current tests ran in the constructor environment.
4. Complete author/venue declarations and formatting; seek independent mathematical review of the complete candidate.

Native event selection, autonomous donor/clock preparation, complete physical energy cost, thermal bath renewal and entropy-area normalization remain open research programmes. They are not silently converted into submission requirements for every finite conditional result.
