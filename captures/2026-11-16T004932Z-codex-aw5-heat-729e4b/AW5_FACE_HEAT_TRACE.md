# AW5 face heat trace and topology-preserving control

**EXACT_INTERNAL.** Fixed signed incidence and unit simplex metric. Constructor replay. Independent review open. **Physical Promotion = 0.**

This addendum follows [UD PR #516](https://github.com/ud-tetra/UD/pull/516), merged at c48ffb8b2f9c82b33bcd25fc24755d16c0053424. Its diffusion parameter t is auxiliary. The trace is invariant under orthonormal coordinate changes of the declared metric; the finite-time trace depends on that metric and triangulation.

## Corrected cavity identity

For the native skew generator A = Bᵀ − B, let L₂ = B₂ᵀB₂ + B₃B₃ᵀ. The two 16-face spaces have identical B₂. Nilpotency gives the orthogonal split im B₂ᵀ ⊕ ker B₂ and confines the B₃ term to the latter block. In that block the filled star has spectrum (2,4,4,4,6), from its five top boundary columns. The hollow star has (0,4,4,4,4), from four mutually orthogonal leaf boundaries and one harmonic direction. The common im B₂ᵀ contribution cancels.

$$
K_{2,h}(t)-K_{2,f}(t)=1-e^{-2t}+e^{-4t}-e^{-6t}=(1-e^{-2t})(1+e^{-4t}).
$$

The second factor has a plus sign. The expansion is 4t − 12t² + O(t³), the initial slope is 68 − 64 = 4, and the limit at infinity is 1. The limit is the Betti-number difference. It tests a change in b₂; a zero difference alone does not identify topology.

## Filled-star 2→3 control

Use hub 0123 and its leaves 1234, 0235, 0136, 0127. Replace 0123 and 1234, which meet on face 123, by 0124, 0134 and 0234. Both local configurations are tetrahedral subdivisions of the same bipyramid, their boundary is identical, and the new interior edge 04 is absent from the original star. The other three leaves stay attached along the same boundary faces. This realizes a bistellar move relative to the boundary of the local ball. The replay verifies the local and global boundary face sets, exact incidence cancellation, spectra and degree-2 nullities.

| Carrier | Face count | b₂ | Tr L₂ | Long-time K₂ |
| --- | ---: | ---: | ---: | ---: |
| Filled AW5 | 16 | 0 | 68 | 0 |
| Hollow AW5 | 16 | 1 | 64 | 1 |
| Flipped filled AW5 | 18 | 0 | 78 | 0 |

The flipped face polynomial is
$$
(x^2-10x+20)^2(x^2-10x+23)(x^2-9x+19)^4(x^2-6x+7)^2.
$$
The raw flipped-minus-filled trace starts at 2 with initial slope −10 and tends to zero. The initial offset reflects the extra face coordinates. Per-face normalization removes that offset and gives initial slope −1/12, since 68/16 − 78/18 = −1/12. Thus the control changes finite-time trace even after normalization. For cavity counts use the unnormalized harmonic limit; for equal-weight per-face comparison declare the normalization. Both full graded AW5 slope peaks previously reported are numerical summaries of all graded modes. No mode-specific attribution follows from the peak values alone.

Replay: `python3 heat_trace_aw5.py` (SymPy). The submitted offline numeric citations lack a bibliography. The calculation uses explicit incidence data.
