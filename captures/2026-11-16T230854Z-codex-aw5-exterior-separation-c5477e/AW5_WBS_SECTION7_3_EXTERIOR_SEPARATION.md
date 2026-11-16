# WBS Section 7.3. AW5 signed exterior-face separation

**EXACT_INTERNAL. Physical Promotion = 0.**

For the unit-weight hollow 46D and filled 47D AW5 carriers, use the same signed closed exterior face shell $e$ with $\|e\|^2=12$, initial face state $q(0)=e$, and zero initial bulk state. Read $R(s)=\langle e,q(s)\rangle/12$ in native time. The shell belongs to $\ker B_2$, and this face/bulk subsystem is governed by $B_3B_3^\mathsf{T}$.

| Carrier | Undamped trace | Taylor series through order six |
| --- | --- | --- |
| Hollow | $1/4+(3/4)\cos(2s)$ | $1-(3/2)s^2+(1/2)s^4-(1/15)s^6$ |
| Filled | $(3/4)\cos(\sqrt2s)+(1/4)\cos(\sqrt6s)$ | $1-(3/2)s^2+(1/2)s^4-(1/12)s^6$ |

The moments of orders zero, one, and two agree in the two face/bulk spectral measures. Their third moments are 48 and 60, respectively. Thus hollow minus filled has sixth derivative 12 at zero for the normalized readout, with all lower derivatives equal. The Taylor coefficient is $1/60$. Equal uniform bulk damping preserves this leading coefficient. For the undamped traces, the eighth-order remainder in the difference is bounded in absolute value by $11s^8/840$, and hence $\Delta R(s)\ge s^6/280$ for $0<s\le1$.

The preparation and readout depend on the signed exterior shell and its coupling through the top boundary. The face kernel $\ker B_2$ contains top boundaries and harmonic representatives. Second homology is the quotient $\ker B_2/\operatorname{im}B_3$. The bound is a mathematical witness for the declared matched preparations and unit weights. Bench calibration, noise tolerance, and hardware admission remain open.

[UD-Physics PR #397](https://github.com/ud-tetra/UD-Physics/pull/397) · [Pinned derivation](https://github.com/ud-tetra/UD-Physics/blob/3c5339bb037507bce1d99ef9c2fa3f36aaa2eb03/candidates/aw5-exterior-bulk-discriminator/AW5_EXTERIOR_BULK_DISCRIMINATOR.md) · [Exact replay manifest](https://github.com/ud-tetra/UD-Physics/blob/3c5339bb037507bce1d99ef9c2fa3f36aaa2eb03/artifacts/aw5-bulk-codex-20261116/bulk-discriminator-replay/manifest.json).

Discovery source [PR #397 merge](https://github.com/ud-tetra/UD-Physics/commit/0f6a5c25d2008591fff7c705cd429f6f05557c6c). The technical result remains scoped to the declared native model.
