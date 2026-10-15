# Critical curved-branch bifurcation v0.1

Conditional theorem for the unchanged finite unitary link-matter model. The carrier stays fixed; pattern labels refer to a critical phase-amplitude representation.

## Replay

Python3 with SymPy, NumPy and SciPy: run `python3 verify_bifurcation.py`. It writes the exact receipt (66 constructor checks), replays the inherited directed integer certificate, and runs separately typed numerical diagnostics. Frozen graph and critical helpers are copied unchanged and hashed in provenance.

The numerical solver uses the full lowest-eigenvalue energy on all fourteen physical connection directions. It solves three representative branch families at four excess values and computes the full 42-pair scalar Hessian spectrum, including Gauss backreaction. It does not use a quartic-truncated stationary energy or integrate a new nonlinear trajectory. Numerical solves do not certify the theorem's unquantified epsilon0.

## Result and limits

Above epsilon=kappa/(r*N)-kappa_star(N)/N=0, six balanced branches are stable, twelve branches have one unstable scalar pair and eight have two. The scalar local diagram is complete. Stability/instability persists for their finite-rank embeddings; exhaustive higher-rank classification remains open. Radii scale as sqrt(epsilon), energy gains as epsilon^2, soft squared frequencies as epsilon. Conserved energy prevents interpreting the minima as attractors or a sourced branch-selection rule.

The release ZIP holds proof, replay and prepublication receipts. The immutable GitHub capture additionally retains site validation, release and a complete binary source patch with exact source-tree reconstruction. Prior artifacts are preserved. Development lane; action and registry unchanged; independent review pending; physical promotion 0.
