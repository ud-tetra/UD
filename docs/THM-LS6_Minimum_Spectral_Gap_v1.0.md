# THM-LS6: Minimum Spectral Gap

**Version 1.0 | Depends: THM-534 (transport matrix T), THM-561 (T spectrum)**

---

## Statement

The minimum gap between distinct eigenvalues of the transport matrix T is:

    Δλ_min = 1/6

attained between the eigenvalues λ = 1/2 and λ = 1/3.

## Proof

T has three distinct eigenvalues: {1, 1/2, 1/3} (THM-561).

The pairwise gaps are:

    |1 − 1/2| = 1/2
    |1 − 1/3| = 2/3
    |1/2 − 1/3| = 1/6

The minimum is 1/6, attained between the weak sector (λ = 1/2) and the color sector (λ = 1/3).  □

## Derived quantities

The minimum spectral gap determines the smallest energy difference between distinct T eigenspaces under the Hamiltonian H = I − T:

    ΔE_min = |(1 − 1/2) − (1 − 1/3)| = |1/2 − 2/3| = 1/6

This is the energy cost of the cheapest cross-eigenspace transition.

## Non-claims

This result does NOT assign a physical mass value to the gap. It does NOT claim that Δλ_min sets a confinement scale or a threshold for any loop classification. The connection between spectral gaps and physical masses is a separate bridge claim.

---

## Proof-state

**EXACT STRUCTURAL.** Follows from the three distinct eigenvalues of T, all of which are exact rational numbers derived from the tetrahedral channel algebra. No approximations, conventions, or parameters.
