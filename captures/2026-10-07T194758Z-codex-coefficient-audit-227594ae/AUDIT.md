# UD 7/768 provenance audit v0.1

Status: DERIVED / development — no registry entry. Constructor checked; independent review pending. Physical promotion: 0.

## Source-bound result

The attached v0.39 ledger and the captured v0.85 reconciliation agree on rows P01–P09, C01 and C03. This audit compares those rows only; it does not certify v0.85 as the latest global project state or establish the proofs behind the ledger entries. Source bytes and hashes accompany this capture.

| Step | Object | Exact value | Ledger status / remaining gate |
|---|---|---|---|
| P03 | Automorphisms of K4 | 4! = 24 | EXACT_INTERNAL |
| P04 | Declared three-bit Theta register | 2^3 = 8 | Reference-state admissibility proof must be preserved |
| P05 | N1 | 24 × 8 = 192 | Observable interpretation separately gated |
| P06 | Delta_theta | 8 − 1 = 7 | Arithmetic given one distinguished reference; exclusion law not reconstructed here |
| C01 | r_Delta | 7/192 | Internal structural ratio |
| P07 / P09 | Default selector / N2 | 4 / (192 × 4 = 768) | COMPUTED_BRIDGE / DERIVED_STRUCTURAL; selection generalization open |
| C03 | C_vertex | (7/192)/4 = 7/768 | DERIVED_STRUCTURAL; local admissibility law open |

Factorization: 192 = 2^6 × 3; 768 = 2^8 × 3. Hence 7/768 is reduced. On the declared default branch, the arithmetic identity is

\[
C_{\rm vertex}=\frac{2^3-1}{4!\,2^3\,G_{1,\rm default}}
=\frac{7}{24\cdot8\cdot4}=\frac7{768}.
\]

## Two uses of four require separate receipts

Four vertices (P01) and selector G1_default=4 (P07) have equal values and different provenance. Dividing r_Delta into four equal vertex shares also gives 7/768, but the numeric agreement does not prove that this allocation is the selector mechanism.

Conditional allocation lemma: assume an S4-invariant total r_Delta, an S4-equivariant vertex allocation, and conservation sum_i a_i=r_Delta. Transitivity of S4 on vertices forces all a_i equal, hence a_i=r_Delta/4. These assumptions prove the equal-share result, not the existence or physical meaning of such an allocation law. Without equivariance, conservation alone admits the family a_i=r_Delta/4+d_i with sum_i d_i=0.

The dense alternate P08 has G1_dense=12 and P09 gives N2_dense=2304. Applying the same ratio formula produces the conditional alternate 7/2304, exactly one third of 7/768. This is an arithmetic control, not an admitted replacement for C03. Retaining both branches makes the selection dependency visible.

## Open gates and next work

1. Recover the source predicate that distinguishes the single Theta reference state; enumerate admissible states against that predicate.
2. Recover and replay the source selector defining G1=4 versus G1=12, preserving its tested scope and larger-scope limits.
3. Recover the actual local allocation map; establish its conservation/equivariance and any identification with the branch selector.
4. Keep capacity, cutoff, coupling and physical-unit aliases gated until their own source bridge and independent review exist.

The attached CRL-2 subdivision file explicitly labels itself a governance proposal. This audit records that proposal without silently adopting or promoting it. Constructor checks below are arithmetic and source-consistency checks; they are not non-constructor adversarial review.

## Administrative observation

The user reports branch protection enabled. At this turn's read, the main branch endpoint reports protected=false, the ruleset collection is empty, and detailed branch protection returns integration access denied (403). Enforcement is therefore unverified from this connection. Publication uses a unique branch and PR, with no direct main update or bypass.

Missing source: Gap2_FINAL_Finite_Genesis.png was unavailable; it was not read or used. Unexported chats and hidden state remain outside capture scope.
