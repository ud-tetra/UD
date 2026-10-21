# Recovered transport to J1/Kminus: exact obstruction and conditional phase lift v0.1

**Development — no registry entry / constructor verification only / Physical promotion 0.**

## Definitions and source binding
Source carrier: real six-edge realization of historical THM561 transport T, self/opposite/cross entries1/2,1/6,1/12 in ascending edge order01,02,03,12,13,23. H=I-T is symmetric with eigenvalues0(1),1/2(2),2/3(3). Complexification is possible but the phase-lift/parity statements below specify real coordinates.

Target: oriented nonaugmented Kminus chain space R23 with tetrahedra0123,0124, unit simplex metric, A=d-d^T, L=-A² and spectra0(1),3(8),5(14). This is the incidence model of a filled diagonal J1, not a geometric metric model. Sources: copied THM561 v1.0 §1.4/§3 and J1 geometry v0.1 §§4–5, previously recovered in captures/2026-10-21T173357Z-codex-fivevertex-recovery-2cd18615. No physical units, particle targets or species labels are inputs.

## Exact no-go1: direct dissipative-to-skew intertwining
Claim: no injective J:R6→R23 satisfies AJ=J s(T-I), for any real s>0. If Hx=hx with h>0, AJx=-shJx. Taking its Euclidean inner product with Jx gives0=-sh||Jx||² by A^T=-A, hence Jx=0. Thus the five-dimensional active source is killed and rank(J)≤1. This is an evolution-class obstruction. It does not prohibit a dilation with an environment, complex time substitution, a second-order lift or a different generator; each changes premises.

## Exact no-go2: one positive scalar cannot match the second-order spectra
No injective E satisfies LE=sEH with s>0. The two positive source eigenvalues must go to distinct members of{3,5}. Matching1/2→3 and2/3→5 requires s=6 and15/2 simultaneously. Swapping requires10 and9/2. Both are inconsistent. Overall clock scaling alone therefore cannot supply this particular transfer. This is not a no-go for nonlinear spectral functions, geometric metric changes or a different transport.

## Conditional construction: polynomial spectral conversion
Define f(H)=(3/2)H+9H². It sends0,1/2,2/3 to0,3,5. This polynomial was obtained by solving against the target's native spectrum: it is an INVERSE SPECTRAL INTERPOLATION, not an independent UD source law or a particle fit. The alternative (53/2)H-33H² sends the same three values to0,5,3 and is also admissible at the spectral level. Hence this matching does not select itself.

Choose rational mutually orthogonal target position axes: one harmonic, two in L=3 and three in L=5, additionally imposing v_i^T A v_j=0. The target multiplicities permit these choices. U is the explicitly declared rational orthogonal eigenbasis of H. E=V U^-1 gives LE=Ef(H), rank6. The six-dimensional position image is not claimed A-invariant.

For a full real phase space, retain harmonic displacement q0 but fix its velocity to zero. Let z=(q0,q1,...,q5,v1,...,v5)∈R11 and define K by q0'=0, qj'=vj, vj'=-lambda_j qj with lambda=(3,3,5,5,5). The exact target embedding D has position columns V_j and velocity columns -AV_j/lambda_j. Direct calculation gives

AD=DK, G=D^T D>0, K^T G+GK=0.

All matrices are saved as exact rational strings. G is explicitly pulled back, not silently identified with a legacy unit phase metric. The saved diagonal G is(5,1/2,1/3,4/5,3/4,2/3,1/6,1/9,4/25,3/20,2/15). The mathematical readout B=G^-1 D^T obeys BD=I11 and BAD=K. W=DB is an orthogonal invariant projector. Its twelve-dimensional complement is invisible to B. This is a conditional realization/readout, not an apparatus construction or six-channel acquisition theorem.

## Why the harmonic momentum cannot be restored in this closed skew model
The unrestricted twelve-dimensional second-order system includes q0'=v0,v0'=0, a nonzero nilpotent Jordan block. If an injective intertwiner existed, target vectors p,q would satisfy Ap=q≠0 and Aq=0. Skewness gives||q||²=<q,Ap>=-<Aq,p>=0, contradiction. The eleven-dimensional restriction is therefore a real change of state domain, recorded explicitly; it is not a full twelve-dimensional admission. Its physical source justification is OPEN.

## Compatibility is not uniqueness
A rational orthogonal C commuting with A is constructed by a Cayley phase rotation on each positive eigenspace. Dalt=CD differs from D while ADalt=DaltK and Dalt^T Dalt=G. Thus even fixed conversion, metric and evolution admit multiple maps. The chosen axes/phase are construction conventions, not source-selected particle properties. No signed group-action intertwiner, geometric J1 metric, native phase-selection principle, physical clock or action-unit calibration has been supplied.

## Verification and disposition
Run verify_map.py in a fresh directory: it writes exact MAP_WITNESSES.json and prints RESULTS.json. Run check_witness.py against those witnesses; it uses separate multiplication loops, verifies transfer/readout/Gram identities and rejects perturbed embedding/readout and scalar6. Saved replays are byte-identical. Both checks are by the same constructor, not a non-constructor review. The analytic no-go proofs are above; computational cases do not replace their stated hypotheses.

Result: direct transport transfer fails, but an explicit eleven-dimensional conditional phase lift exists. Registration remains CRL-2a, target release false, no particle score or promotion. Highest-value next gate is a native source law selecting f and the reduced harmonic domain (or an independently sourced alternative); further fits or arbitrary basis refinements cannot close that gate. The recalled C5 carrier is still not identified by this Kminus calculation. Gap2_FINAL_Finite_Genesis.png remains unavailable/unused.
