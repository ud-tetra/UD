# Global PB3/PB5 radial spectral separator

**Physical Promotion = 0.** Constructor evidence for issue #604, pending independent review.


Fix \(g>0\) and define \(\sigma=11g/[10(g^2+4)]\). Translate each monic stable factor \(p(z,g)\) by \(p(z-\sigma,g)\). A root of the translated polynomial lies in the right half-plane exactly when the original root lies to the right of \(-\sigma\).

For PB3, all leading Hurwitz minors of the two quadratics and cubic are positive. Their explicit factorizations as rational functions of \(g\) appear in replay-results.txt. Each numerator has positive coefficients and each denominator is positive.

For the PB5 sextic the fifth leading Hurwitz minor is

\[
\Delta_5^{\rm H}=-\frac{g^3 A(g^2)B(g^2)}{30517578125(g^2+4)^{15}}.
\]

The replay prints both polynomials. All coefficients of \(B\) are positive. In \(A(x)\), the only negative coefficient is \(-68905x^3\). Grouping that term with \(429600x^4\) and \(10750319x^2\) yields

\[
x^2\big[429600(x-1)^2+790295x+10320719\big].
\]

The remaining terms have positive coefficients. Thus the fifth minor is strictly negative. If all shifted PB5 sextic roots lay in the closed left half-plane, a shift of all roots farther left by any \(\epsilon>0\) would make the polynomial strictly Hurwitz. Taking \(\epsilon\downarrow0\) would make all its leading Hurwitz minors nonnegative, a contradiction. Hence this sextic has a root strictly to the right of the line.

The replay also checks that the PB5 sextic's reduced shifted resultant \(\operatorname{Res}_s(E,O)\) equals the negative of this fifth minor on the chosen curve. This uses the factorwise resultant approach in [#604](https://github.com/ud-tetra/UD/issues/604). Therefore

\[
\Delta_{\mathrm{PB5}}(g)<\frac{11g}{10(g^2+4)}<\Delta_{\mathrm{PB3}}(g),\qquad g>0.
\]

The bound concerns the smallest positive decay rates of the pinned stable factors from [#597](https://github.com/ud-tetra/UD/pull/597). The global supremum of their ratio and the visibility of the rightmost stable pole in the memory transfer at every finite coupling are separate questions.


The PB3 factors used here are exhaustive after removing the neutral sector. The PB5 proof only needs one stable factor. The exact pencil construction and factorizations are in the pinned [strong-coupling replay](https://github.com/ud-tetra/UD/blob/f3aa0ee3bbaf59bcb6a57c5154dd9f985cbfd612/captures/20261121T214445Z-codex-bipyramid-strong-gaps-4527fd99/replay_bipyramid_strong_gaps.py).

## Independent review packet

1. Verify the PB3 factor inventory and PB5 sextic against the source pencil above.
2. Run `python3 replay_separator.py` with SymPy and compare stdout to `replay-results.txt`.
3. Verify the direction of the shift and the closed half-plane continuity argument for the negative PB5 minor.
4. Confirm that the certificate gives a strict all-coupling spectral-gap ordering. A global ratio supremum proof and an all-coupling pole visibility proof remain open.

Please attach the independent disposition to the examined PR head and include these scope locks.
