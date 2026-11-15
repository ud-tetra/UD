# Triangular Transport Symbol Alphabet

## Purpose
This file replaces the placeholder with the current symbolic transport alphabet summary for the triangular/face-based routing layer.

## 1. Motivation
Triangular faces are the primitive admissible transport surfaces of the current simplicial substrate. A symbolic alphabet attached to these faces is useful for:

- tracking local admissibility,
- encoding seam orientation,
- recording phase/framing transitions,
- supporting later simulation and symbolic-computation pipelines.

## 2. Minimal symbol set
A current working symbolic alphabet for a triangular face \(t=[ijk]\) is the tuple

\[
\Sigma_t = (A_t,\varepsilon_t,\varphi_t,\sigma_t,\chi_t).
\]

with:

- \(A_t\in\{0,1\}\): face admissibility,
- \(\varepsilon_t\in\{+,-\}\): oriented face sign,
- \(\varphi_t\in[0,2\pi)\): seam phase label,
- \(\sigma_t\in\mathbb{Z}_2\): framing class,
- \(\chi_t\): closure-branch marker.

## 3. Admissibility symbol
The first symbol is fixed by the trion rule:

\[
A_t=1-\delta_{b_i b_j}\delta_{b_j b_k}.
\]

Thus the symbol string immediately distinguishes allowed faces from dead/uniform faces.

## 4. Transport use
When two packet faces are stitched along a seam, the local transfer law depends on the symbol tuple mismatch:

\[
\Delta\Sigma_{tt'} = (\Delta A,\Delta\varepsilon,\Delta\varphi,\Delta\sigma,\Delta\chi).
\]

The transport operator is then a function of these symbol differences:

\[
U_{tt'} = \mathcal{U}(\Delta\Sigma_{tt'}).
\]

## 5. Practical role
This alphabet is currently a bookkeeping and simulation-architecture object rather than a finalized physical observable set. It is intended to become the compact symbolic language for face-level transport, admissibility, and branch/framing transitions in future formal and computational work.
