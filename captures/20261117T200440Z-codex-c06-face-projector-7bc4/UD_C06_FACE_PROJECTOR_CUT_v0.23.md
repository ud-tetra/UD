# C06 face projector cut v0.23

**EXACT / CONDITIONAL** for the incidence and fixed-port masking tests. **CANDIDATE** for shared actuation. **Physical Promotion = 0.**

## Detector correction

On the three-dimensional odd space the v0.22 observation of one face is one scalar sum. It has rank one and a two-dimensional kernel. Two distinct scalar face sums have rank two and a one-dimensional common kernel. Any three have rank three. Among three selected faces exactly one can see a preparation, since sum-zero face data proportional to \((1,0,0,-1)\) can occur. The raw restriction to a face's three edges, if the global state is already odd, is a different map of rank three.

Let \(H\) be unsigned face-edge incidence on the mean-zero ordinary edge space \(X\). Let \(P_-\) be the opposite-pair odd projector, \(P_+=I-P_-\) on \(X\), and \(G\) the v0.20 Whitney flag copy. The v0.22 balance uses the square of each face sum, with alignment of primal records. Its global identity follows from \(H^\mathsf TH|_X=2P_-\), including cancellation of the mean-zero even sector. Counting two copies of each edge only establishes the sum-of-squares identity for raw edge restrictions.

## Saturation and collapse tests

The retained-sector null theorem in the Q156 source audit §2.1 leaves the hard gate open while its closure receipts and transport-integrity predicates pass. The face balance alone supplies no failure of either predicate. Under the declared orthogonal port, total stock is constant through the crossing, so a gate depending only on total stock cannot distinguish its two sides.

Model incidence collapse as pointwise deletion or reweighting of the twelve cooriented output flags, with forward map \(DG\) for diagonal \(D\). Each flag copies a particular edge. For any nonzero entry of \(D\), the associated opposite-edge difference has nonzero value on that flag. Thus \(DGP_-=0\) forces \(D=0\), in which case even transfer also stops. This includes all binary masks, and extends the v0.13 edgewise mask obstruction to independent output flags. The result concerns fixed original coordinates and pointwise flag suppression. A collapse with new boundary maps and explicit stock transport would require its own analysis.

## Exact projector and three-face alternative

The identities give the target cut in the original coordinates:
\[
G_{\mathrm{hold}}=G\left(I_X-\tfrac12 H^\mathsf T H|_X\right)=GP_+.
\]
A local receipt from any qualifying face can serve as a candidate trigger for one shared transition that applies the full projector. A single face row contributes rank one to the correction, so that row alone cannot cancel the three-dimensional odd space. This applies even if that face detects the event correctly.

With exactly three faces, let \(L=H_{\mathrm{three}}P_-\). The rows are the three projected face rows, and \(LL^\mathsf T=2I_3-\tfrac12 J_3\) from v0.22. The inverse is \(\tfrac12(I_3+J_3)\). Therefore
\[
P_-=L^\mathsf T \tfrac12(I_3+J_3)L.
\]
The \(J_3\) term reconstructs the fourth face contribution using its negative-sum relation. No diagonal gain on the three selected scalar sums can give the projector, since \(L\) is invertible between the odd space and three face readings, making the needed middle matrix unique. Four-face aggregation uses the fixed \(1/2\) factor and avoids reconstructing the missing sum.

Applying the projector under the v0.20 metric and reciprocal adjoint preserves the identity amplitude reset, total stock, both held odd registers and active even exchange. Neither the projector identity nor the native gate audit supplies the shared same-event authority. Timing, native aggregation and Stage 2 remain open.

Run python3 replay_c06_face_projector.py for the 4096 fixed flag masks, all four three-face projector comparisons, six blind pairs and a one-visible-face witness.
