# Offline raw-record and floating-witness replay runner

This single-command runner checks immutable PR208 and PR204 evidence without network access, a proposer, or a new SVD. It verifies pinned root manifests and every listed file before safely extracting the retained archives into a new output directory. Existing sources and evidence remain unchanged.

**External nonconstructor review remains PENDING.** The runner cannot determine who executed it or convert its own PASS into independent review. Its receipt deliberately leaves reviewer identity null. A separately attributable reviewer must supply their identity, independence declaration, environment, signed findings and any disagreements. Running this package within the constructor team provides constructor replay only.

## Requirements

Python3.12 and the already-installed versions in requirements.txt; a local complete checkout of ud-tetra/UD containing the five pinned parent captures. This tool does not download source code or dependencies. Provide enough working storage for extracted witnesses and, in raw mode, reconstructed source records. An output path must not exist before invocation; retained source directories are never edited.

## One-command witness replay

```bash
OPENBLAS_NUM_THREADS=1 python offline_replay_v2.py --repo /absolute/path/to/UD --out /absolute/path/to/new-review
```

The default equals explicit `--witness`. It executes PR208 and PR204 `replay_entry.py` in separate safely extracted folders. PR208 verifies both complete actual full-factor SVD witnesses and cutoff209; PR204 checks two actual phase certificates, the outside-ball raw HOLD and four negative controls. This uses archived raw-projection Grams and saved factors; it does not regenerate omitted raw sources.

## One-command complete raw recovery and replay

```bash
OPENBLAS_NUM_THREADS=1 python offline_replay_v2.py --repo /absolute/path/to/UD --out /absolute/path/to/new-raw-review --raw
```

Raw mode first performs the same witness replay. It then reconstructs all four PR195 records with its unmodified captured generator and verifies all four exact hashes and generation rows. The frozen stress record is staged at its original sibling path. The unmodified PR201 script reconstructs cyclic-unit; an explicitly implemented frozen PR200 dense-unit recipe reconstructs the dense control and checks every difference plus its expected full hash. The runner separately copies PR204 evidence, removes only generated raw-replay receipts from that copy, and executes its full raw replay. Finally PR208 raw_verify.py checks every cyclic raw difference and all2629311 integer sketch entries.

The raw branch of PR204 project.py contains no SVD call; its non-replay proposal-generating branch is never invoked. Parent generator execution reconstructs synthetic source bytes; it is not apparatus measurement or a new estimator run. These controls remain conditional on their pinned learned source model.

## Evidence and acceptance

RUN_RECEIPT.json records every command, exit code, hash-bound log, intake manifest and scope. A failure raises an error, preserves the completed logs, and writes FAIL rather than claiming successful replay. PASS_CONSTRUCTOR_REPLAY_ONLY means the requested calculations completed; external review remains PENDING. Original-frequency ambiguity modulo pi, O03 protocol-control status, native observer mapping and physical promotion0 remain unchanged.

The source files were frozen before runner tests. Synthetic hostile extraction controls test traversal/absolute/backslash/noncanonical/drive paths, symlinks and cross-archive duplicates; all are refused before extraction. A normal relative nested file is accepted. These fixture tests do not constitute an exhaustive security audit.

Runtime receipt/logs supplied beside this runner identify which modes were actually executed. A prior constructor run of equivalent parent scripts is separate evidence and does not establish that a new convenience runner succeeded. The review receipt may not replace missing externally attributable evidence.

Development — no registry entry. Same-team verification; external nonconstructor review pending. Physical promotion **0**.

## Disclosed I/O correction

The original frozen v1 runner is retained as offline_replay.py. Its separate witness-mode run produced the full expected output. In the v1 raw-mode run, the PR204 witness child returned0 but its stdout log was empty. That step is treated as exit-code-only evidence until a separately frozen explicit replay captures and validates its complete phase/control summary. The original empty log is retained. No mathematical source, recipe or threshold was changed.

The separately frozen v2 runner captures stdout through a pipe and fails closed unless PR208 prints its full-factor replay marker and PR204 provides a parsed PASS summary with two actual phase replays, one outside-ball HOLD and four negative controls. The recommended command above uses v2. The supplied execution receipts distinguish the actually executed full raw pipeline (v1 plus explicit supplemental replay) from v2 witness-only testing. No fresh end-to-end v2 raw execution is claimed.
