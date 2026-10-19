# Same-team final graph review

Status: no material defect found. Physical promotion 0. This is not external
independent review or a new estimator execution.

The frozen graph verifier was executed in read-only replay mode. All certificate
rows agreed exactly; watched parent source/certificate/proposal bytes remained
unchanged. GRAPH_REPLAY_RECEIPT.json records hashes and process status.

Mathematical checks:

- Source normalization uses Q0=U0(U0^T U0)^(-1/2), with the corresponding
  inverse-Gram factor charged to weighted perturbations.
- The inverse proposal only supplies an untrusted dyadic M. K=C0^T M is formed
  exactly; the Neumann correction therefore recovers the Moore-Penrose inverse
  rather than an arbitrary right inverse.
- The CYCLIC anchor's known projected perturbation is subtracted. The restored
  baseline is checked against its exact norm and old exact residual fraction.
- Rowwise source weights cover the entire encoded one-quantum ball, without
  independence assumptions. They do not cover arbitrary real vectors by fiat.
- Riccati self-map, contraction, spectral gap, and leading-subspace gates are
  all explicit strict interval comparisons.
- The graph Frobenius forcing and operator coefficients remain norm-typed.
  sqrt(209) is retained for operator-only helper error, while the stronger
  returned-F lane relies on the established Frobenius helper certificate.
- The rounded-up graph radius is tested against the strict self-map rather
  than accepted merely as a floating quadratic root.
- Graph alignment is simultaneous in 2/F norms. Returned-factor normalization
  keeps the existing 2p(eta) term.
- Exact-LS shift sufficiency and a returned solver's normal-residual premise
  remain separate. No universal floating-SVD/LS success is asserted.

The full-radius ideal exact-LS shift upper is approximately
4.339081588094236e-10, below the unchanged published allowance
5.563206409135001e-10. The returned-F full-quality upper is approximately
7.540375831823565e-10 and remains an inconclusive sufficient-bound HOLD.
Neither result proves all other policy gates. Prior receipts stay unchanged.

This replay recomputed the graph certificate from its pinned weight receipt;
it did not independently rerun the large exact weight reconstruction. The
weight implementation and source correction were reviewed read-only.
