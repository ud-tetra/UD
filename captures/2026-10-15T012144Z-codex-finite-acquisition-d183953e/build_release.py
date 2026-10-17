from pathlib import Path
import hashlib,json,shutil,zipfile,platform
R=Path(__file__).resolve().parent;W=R.parent
base=R/'baseline/UD_Theory_Narrative_Manuscript_v0.15.md'
addition=(R/'MANUSCRIPT_ADDITION.md').read_text()
text=base.read_text().replace('Review candidate 0.15','Review candidate 0.16')
text=text.replace('# Appendix E. Data, code and development declarations',addition+'\n# Appendix E. Data, code and development declarations')
main='''## 10.4 Acquiring a stock is different from writing an outcome

The passive observer used earlier assumes bounded-error stock values. Appendix D.18 now supplies an explicit auxiliary finite write: a normalized real carrier is newly encoded in a 15-level quantum register, three disjoint edge-pair projectors control a four-level pointer, and a second counted register retains its outcome. The complete joint state is given, including the correlations lost by the record coarse-graining. This declaration supplies a quantum encoding; it does not derive one from real incidence dynamics.

One write yields an outcome, not a stock expectation. It generally disturbs the carrier, and repeated writes on the same carrier change the trajectory being observed. The appendix proves an exact zero-disturbance readout obstruction and gives a fresh-ensemble alternative. For the 129-scan fixture, one explicit sufficient allocation uses 12681216 independent preparations and gives the earlier bounded-error contract with failure probability below 1/100. This conservative allocation is not an optimality result. Its record banks, correlation-preserving renewal, pulse controls and latency are charged explicitly; thermal production of pure blanks and calibrated physical cost remain open [31].

'''
text=text.replace('# 11. Renewal, preparation and complete resource cost',main+'# 11. Renewal, preparation and complete resource cost')
text=text.replace('The current version-0.15 additional-research package','The preserved version-0.15 additional-research package')
packet='''The current version-0.16 acquisition-instrument package adds a complete finite carrier/pointer/record state, exact disturbance and marginal-distinguishability examples, a supplied-ensemble concentration contract and a register-level control/renewal/resource ledger. The independently authored replay `verify_acquisition_instrument.py` passes 26 exact finite check families. Written proofs distinguish an auxiliary quantum implementation from native UD and a finite-confidence estimate from a deterministic sensor. The v0.15 manuscript is preserved; its complete evidence release is pinned by hash and capture commit. Earlier proofs and replays are not all rerun. Physical promotion remains zero, and constructor checks are not independent review.

'''
text=text.replace('Source recovery is pinned to repository base commit',packet+'Source recovery is pinned to repository base commit')
text+='''
31. *Finite Stock Acquisition: Joint Write, Disturbance and Preparation Cost*, version 0.1, 15 October 2026 UTC. Companion constructor report and independently authored replay in the v0.16 package. Auxiliary quantum encoding, supplied preparation bank and controls; no independent review, physical promotion or thermodynamic/area normalization.

32. Watrous, John. *The Theory of Quantum Information*. Cambridge University Press, 2018. Author prepublication draft, §2.3.2, equations (2.255)-(2.262), and Theorem 1.16. [Author draft](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf). Standard instrument and concentration background; all specialized finite formulas used here are explicitly derived.

33. Hoeffding, Wassily. “Probability Inequalities for Sums of Bounded Random Variables.” *Journal of the American Statistical Association* 58(301) (1963), 13-30. DOI: [10.1080/01621459.1963.10500830](https://doi.org/10.1080/01621459.1963.10500830). Original concentration-method attribution; D.18 gives the needed bounded-variable proof directly, with the statement also inspected in [32, Theorem 1.16].
'''
(R/'UD_Theory_Narrative_Manuscript_v0.16.md').write_text(text)
intro='''# Finite Stock Acquisition: Joint Write, Disturbance and Preparation Cost

Version 0.1 | 15 October 2026 UTC | Development; physical promotion 0

The next missing interface was a finite instrument behind the bounded-error stock values. The construction below supplies one in a separately declared quantum encoding. It exposes two costs hidden by passive readout: strong measurement changes the observed carrier, and estimating its unperturbed stock values can require a large bank of fresh independent preparations.

The result is a conditional implementation and obstruction package. It does not infer that UD's real amplitudes are quantum states, that a boundary supports these registers, or that pure donor production has a normalized thermodynamic price. The known deterministic fixture can be calculated without a sensor; its role here is a common finite target for comparing observation contracts.

**Derived:** unitary write and full joint state; reduced instrument; exact disturbance and information-loss witnesses; finite-confidence sampling bound; pulse norm upper bounds; exact correlation-exporting renewal.

**Supplied:** amplitude encoding, independent preparations at the scan instants, pure pointer/record blanks, controlled pulses, free-flow cancellation, Born readout, timing, counting and retention.

**Open:** native realization, autonomous controller, physical spatial locality, thermal blank production, calibrated work/area and a horizon entropy density. Full inherited manuscript results are not all replayed. No independent review is claimed.

The report's D.18 section is reproduced verbatim in the revised manuscript, whose references [15] and [31]-[33] identify the primary background and companion evidence. The finite implementation is a construction; the no-disturbance statement is a no-go under its explicitly quantified premises.

'''
(R/'UD_Finite_Acquisition_v0.1.md').write_text(intro+addition+'''
## Review and next closure order

1. Replace the supplied preparation bank with an explicit finite preparation source and synchronize it with acquisition; bound its joint error and exhaustion.
2. Derive a weak or otherwise back-action-aware observer on the same evolving carrier, then compare accuracy, latency, disturbance and consumed preparation capacity against this strong-measurement baseline. Optimal allocation is open.
3. Supply an autonomous counting/readout/controller and donor-production mechanism with Hamiltonians. Only then compare energy and retained information under a common retention/error target.
4. Supply the physical area/metric map before comparing any apparatus capacity to boundary area. No value of G or horizon density is inferred here.

The replay constructs incidence, controls, full write isometry, partial traces and finite certificates independently of imported working-note code. Its 26 finite check families validate examples and identities; the written general proofs carry the concentration, no-disturbance and error-composition conclusions. Constructor verification is not non-constructor peer review.
''')
prior=W/'UD_ADDITIONAL_RESEARCH_v0.15_PACKAGE.zip'
sources={'baseline':{'narrative_version':'0.15','library_file_id':'libfile_950249aa77248191bb59f8460d92e53b','library_version':7,'size_bytes':base.stat().st_size,'sha256':hashlib.sha256(base.read_bytes()).hexdigest(),'capture_commit':'83fd7c0cced45a8a7f8c71d0fd591f1df34b8401','pr':96,'package_sha256':hashlib.sha256(prior.read_bytes()).hexdigest(),'package_library_id':'libfile_79ff03b769c081918d55500910261df6'},'new_external_inputs':[],'primary_background':[{'url':'https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf','scope':'Instrument definitions 2.255-2.262 and Hoeffding Theorem 1.16 inspected; not redistributed.'},{'doi':'10.1080/01621459.1963.10500830','scope':'Original method attribution and publisher metadata; full original paper not imported.'},{'url':'https://arxiv.org/abs/1306.4352','scope':'Thermal erasure has additional assumptions, inherited reference 15.'}],'physical_promotion':0,'status':'DEVELOPMENT_NO_REGISTRY_ENTRY','independent_review':False,'verification_scope':'26 new exact finite check families plus written general proofs; inherited releases pinned, not fully replayed.'}
for name in ['20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md','21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md']:
    p=W/'project_sources'/name;shutil.copyfile(p,R/'baseline'/name)
sources['historical_governance_inputs']=[{'name':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (R/'baseline').glob('*UD_*v*.md') if p.name!=base.name and p.name!='library_baseline.md']
(R/'SOURCE_REGISTER.json').write_text(json.dumps(sources,indent=2)+'\n')
(R/'ENVIRONMENT.json').write_text(json.dumps({'python':platform.python_version(),'platform':platform.platform(),'sympy':__import__('sympy').__version__},indent=2)+'\n')
(R/'README.md').write_text('''# UD finite acquisition v0.16

Read UD_Finite_Acquisition_v0.1.md and the revised narrative. Run `python verify_acquisition_instrument.py` with SymPy to regenerate INSTRUMENT_CHECKS.json and INSTRUMENT_CERTIFICATES.json. No source-document scripts are executed. The previous full evidence package is pinned, not nested or fully replayed. The supplied quantum encoding and preparation bank are candidate apparatus premises, not native UD or physical identifications. Development; no registry entry; physical promotion 0; no independent review.
''')
print(json.dumps({'version':'0.16','checks':26,'baseline_sha256':sources['baseline']['sha256']}))
