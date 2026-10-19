# Current replay entrypoint: replay_v2.py

Append-only operational correction. All original17 files, their source freeze, both raw record recipes and all numerical certificates remain byte-identical. The original `counterexample.py` only protected its own package directory; it did not enforce the old README's broader requirement to stay outside every immutable ancestor capture. No in-capture replay write occurred in either original run. Those limitations and original files are retained.

`replay_v2.py` is a thin wrapper. It verifies its own source against `WRAPPER_FREEZE.json`, checks the unchanged original source freeze and source hash, refuses optimized Python runtimes where `__debug__` is false, and rejects output paths lexically or after symlink resolution inside the package or any MANIFEST-bearing ancestor. It also rejects an output that is an ancestor of the source, and requires a new directory. It then invokes unchanged original `main()` with unchanged CLI arguments. No numerical, source-data, recipe, cap or precision change is made.

The six separately frozen post-known-outcome guard controls pass: package child, sibling under an outer capture, symlink into a capture, lexical capture path escaping by symlink, ancestor of source, and a permitted new external directory. Tests construct temporary synthetic directories with two nested MANIFEST-bearing ancestors; they read no raw record and perform no numerical replay or estimator call. Wrapper correction is not a new experiment or a retry of scientific outcomes.

Use normal Python, the explicit repository and original baseline, and a NEW external output directory:

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python replay_v2.py --repo /absolute/UD --baseline /absolute/ramp_clock_stress.i64le --out /absolute/new-output
```

The scientific no-go and exclusions are unchanged: the fixed top1 recipe lies in the closed q-ball and obstructs rank209 reconstruction cap2^-41; this is not a phase-failure or physical claim. Physical Promotion=0, development—no registry entry, external review PENDING. The root publisher will run this wrapper once after relocation and retain its result separately; this wrapper package itself performs only six guard controls.
