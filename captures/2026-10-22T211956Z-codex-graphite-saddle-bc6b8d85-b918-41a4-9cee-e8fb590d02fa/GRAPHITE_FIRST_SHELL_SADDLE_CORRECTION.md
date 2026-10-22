# Correction: corrugation range versus minimum-path sliding barrier

22 October 2026. **EXACT conditional first-shell stationary-point audit; supersedes a physical interpretation in draft PRs #416–#417; physical promotion 0.** The previous captures correctly derived the six first common reciprocal vectors and the **global max-to-min range** (9|V_*|). They incorrectly called that quantity a sliding barrier in several places. The lowest saddle that connects adjacent minima determines a quasistatic minimum-energy-path barrier, and its coefficient is generally different. Preserve the original captures as evidence; use this correction and the new manuscript version for the barrier statements.

## 1. Exact stationary landscape

After the previously derived origin shift, the rigid first-shell energy per top Bravais cell is

\[
 U(a,b;z)=2V_*(z)S(a,b),\qquad
 S(a,b)=\cos a+\cos b+\cos(a+b).\tag{1}
\]

The two independent phases (a,b) cover a torus; the three reciprocal vectors sum to zero. Critical points solve (\sin a=\sin b=-\sin(a+b)). In one phase torus:

| Points modulo (2\pi) | (S) | Hessian type of (S) | Count |
|---|---:|---|---:|
| ((0,0)) | (3) | maximum | 1 |
| ((2\pi/3,2\pi/3),(-2\pi/3,-2\pi/3)) | (-3/2) | minima | 2 |
| ((\pi,0),(0,\pi),(\pi,\pi)) | (-1) | saddles | 3 |

The exact factorization

\[
 S(a,b)+1=4\cos(a/2)\cos(b/2)\cos((a+b)/2)\tag{2}
\]

shows the saddle level (S=-1) on the phase lines (a=\pi), (b=\pi), or (a+b=\pi\pmod{2\pi}). Those lines separate the two minimum basins when (V_*>0), and separate periodic copies of the unique minimum when (V_*<0). A path through a saddle reaches that separating level, so it is the minimum-energy-path (mountain-pass) barrier for the ideal periodic first-shell model. At (V_*=0) the landscape is flat and the sign-specific branches are undefined.

## 2. Three different energy quantities

For real nonzero (V_*), the exact *global range* remains

\[
 U_{\max}-U_{\min}=9|V_*|.\tag{3}
\]

The minimum-path barrier above a stable registry instead depends on the sign of the real first-shell coefficient:

\[
 \boxed{\Delta U_{\rm mp}=c_\pm |V_*|,\qquad
 c_+=1\ (V_*>0),\quad c_-=8\ (V_*<0).}\tag{4}
\]

For (V_*>0), the minimum is at (S=-3/2), with energy (-3V_*); the saddle is at (S=-1), with energy (-2V_*), giving (V_*). For (V_*<0), the minimum is at (S=3), with energy (-6|V_*|); the saddle has energy (2|V_*|), giving (8|V_*|). Equation (4) is an equilibrium rigid-interface *energy barrier*, still not a finite-speed friction force. Graphite's sign, higher Fourier terms and physical stacking energies must be independently sourced before selecting either branch.

## 3. Corrected normal-load response

The earlier envelope theorem is valid for any smooth stationary pair. For a smooth minimum-to-saddle barrier after minimizing vertical separation (z) under compressive load (L) per Bravais cell,

\[
 \frac{d\Delta\mathcal H_{\rm mp}}{dL}=z_{\rm saddle}(L)-z_{\rm min}(L).\tag{5}
\]

This is the relevant barrier-height relation, rather than a comparison of global maximum and minimum unless those happen to be the chosen endpoints. If (E(t,z)=E_0(z)+2V_*(z)S(t)), (E_0'(z_0)+L=0), (k_z=E_0''(z_0)>0), and the first-shell corrugation is weak enough not to change branch ordering, then

\[
 \Delta\mathcal H_{\rm mp}=c_\pm|V_*(z_0)|+O(V_*'^2/k_z),\qquad
 z_{\rm saddle}-z_{\rm min}
 =-\frac{c_\pm\,\partial_z|V_*(z_0)|}{k_z}
 +O(\text{higher corrugation}).\tag{6}
\]

For the global range, the earlier coefficient 9 remains correct, but its two endpoints are **global max and global min**. For a special exponential (V_*=V_0e^{-\kappa z}), the leading *logarithmic* slope (\partial_L\log\Delta\mathcal H_{\rm mp}\simeq\kappa/k_z) has the same form because (c_\pm) cancels. The measured load slope of friction still cannot be identified with either energy-barrier slope without a dynamical force model.

## 4. Downstream corrections

- Draft PR #416 `GRAPHITE_FIRST_COMMON_FOURIER_SHELL.md`: Eq. (6) remains an exact *global energy range*, but the sentence calling 9 the “barrier multiplier,” Eq. (9)'s use of (9|V_*|) for an unspecified barrier, and the associated interpretation are superseded by Eqs. (4)–(6) here.
- Draft PR #416 `GRAPHITE_OCTAHEDRAL_UD_MANUSCRIPT_DRAFT_v3.md`: its abstract and Section 9 should call 9 a corrugation-range multiplier; its barrier load coefficient should use (c_\pm), with saddle and minimum endpoints.
- Draft PR #417 `GRAPHITE_PLANAR_HARMONIC_MANUSCRIPT_DRAFT.md`: its abstract and Section 4 describe 9 as a “barrier range” or “total barrier.” The corrected focused manuscript in this capture uses “global range” and gives the sign-dependent minimum-path barrier. The exact planar torus topology, spectrum and harmonic port are unaffected.
- Verifiers in PRs #416–#417 established the global range and topology; they did **not** test a mountain-pass barrier. The new verifier does.

No result here establishes the sign of (V_*) for real graphite, quantifies measured friction, or derives a UD-specific residual. Physical promotion remains 0.
