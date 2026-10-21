# Ledger v0.85 recovery and dimensional-normalization preflight

**Result: inventory PASS; EXIT-03 HOLD. Physical promotion 0.**

This capture advances the earlier action-intake audit: the actual v0.85-named ledger has now been recovered from the immutable bootstrap bundles. The original intake's source-blocked statement described availability at that time; it is superseded here only for ledger recovery and inventory coverage. No old source bytes or registry rows are edited.

## Recovery and coverage

The Library and portal copies are byte-identical: 444,587 bytes, SHA-256 `8845ca23e178e043ef0c7bac01be3afba9cabbefd866c366921387a8ca843aec`. Recovery verified all 88 split parts in those two bundles against the bootstrap manifest. Original source identities, hashes and archive paths are in RECOVERY_RECEIPT.json. The portal source commit is 9891d8c82217a12b85518bf7147adfd4dd7bc0ae, Site version 177.

The recovered ledger contains exactly 723 rows and 723 unique IDs. All rows satisfy its ten-field string schema; declared namespace counts and claim-bin counts match recomputation. ROW_COVERAGE.csv accounts for every row. This is an inventory/schema pass, not a complete dimensional proof. The ledger filename says v0.85 and source_baseline names v0.84; its scientific_revision field still says v0.43. These are preserved as separate source metadata, rather than silently repairing version fields.

The archive search inspected 10,450 text members at most 5 MB each with extensions json/md/txt/html/tex/csv. It found no EXIT-03, Dimensional Normalization Verification, or GLOS-2C.3 match. Binary documents, nested archives and larger text members are outside this search. No canonical EXIT-03 acceptance specification was recovered; this capture implements a declared constructor preflight, not a substitute gate definition.

## Action ratio, recurrence and correction

G06/O14 explicitly establish eta_A := A0/hbar. O10/O15 assign A0=B0*a0^2/tau0 and [B0]=M; with [a0]=L and [tau0]=T this has dimensions M L^2/T, so eta_A is dimensionless. Numerical eta_A is not measured by this result.

O09's supplied lifted action map is I=(1/2) sum a_omega*Delta_phi_tilde_omega. A single sector of unit support and one positively oriented winding has Delta_phi_tilde=2*pi, hence I=pi and S_native=pi*A0. Q286 explicitly identifies this as a normalized representative, not support quantization. The map's derivation and primitive quantum-holonomy identification remain separate from this exact substitution.

O13's literal equality chain ends with `A0 = xi_native_phys*hbar = 1/xi_phys_native`. Its final term is dimensionless, whereas A0 has action dimensions. This defect is present in the recovered v0.85 bytes, not just the older snapshot. The append-only O13_CORRECTION_OVERLAY.json splits it into the valid identities xi_native_phys=1/xi_phys_native and A0=xi_native_phys*hbar. It is a constructor-checked correction proposal; original source and status remain preserved.

## Recovered candidate changes the next test

Q282 gives the internal specific action-phase scale S_native/(a*Delta_phi)=A0/2. Q287 postulates the QPB1 physical bridge hbar <-> A0/2 and is QUARANTINED_CANDIDATE. Only under that postulate does Q288 predict eta_A=2/1. O54 keeps physical identification postulated and the independent action anchor OPEN; O55 freezes the prediction with no empirical score. Thus “numerical eta_A remains open” means no validated physical calibration; it must not erase this already recorded conditional prediction or present 2/1 as established physics.

The next useful bridge packet must identify a same-carrier non-target-backsolved A0 anchor, freeze the apparatus-to-native map, uncertainty budget and decision rule, and obtain non-constructor review before an empirical score. The electrical apparatus action S_action=Phi0*Q0 alone does not supply a map to A0 or test QPB1. Equality of their dimensions is insufficient.

## Remaining gate requirements

Recover the canonical EXIT-03 specification; repair O13 through a reviewed append-only source amendment; supply typed expressions, units, assumptions and dependencies for unit-bearing rows and applicability declarations for combinatorial/status rows. The present ledger stores prose without machine-readable dimension fields. Full-ledger dimensional consistency is therefore not certified by scanning its 723 strings. Continue native carrier derivation and physical action anchoring as separate tasks.

**Typed footer:** Development — no registry entry. EXACT: inventory counts/hashes and declared conditional algebra. SOURCE_STRATUM: recovered ledger definitions and status metadata. CANDIDATE: QPB1 and eta_A=2/1. OPEN: EXIT-03 acceptance, global unit audit, primitive holonomy bridge and independent physical anchor. Origin: archived v0.85 copies plus constructor audit. Constructor: Codex root. Non-constructor review: pending. Physical promotion: 0. No experiment performed.
