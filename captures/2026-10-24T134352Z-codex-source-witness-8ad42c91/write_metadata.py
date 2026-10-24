from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;R=P.parents[1]
def save(n,x):(P/n).write_text(json.dumps(x,indent=2)+'\n')
c=json.loads((P/'DESIGN.json').read_text());cert=json.loads((P/'CERTIFICATE.json').read_text());old=R/'captures/2026-10-23T185253Z-codex-monitor-admission-6bf719d2';cfg=json.loads((old/'CONFIG.json').read_text())
roles=['source_line_inventory','source_primary','source_impurity','nominal_path','image_path','nonlinear_path','additive_remainder','omitted_dynamics','initial_state_drift','primary_reference','monitor_readout','clock_transfer']
save('WITNESS_REQUIREMENTS.json',{'version':'0.1','lane':'development; no registry entry','physical_promotion':0,'empirical_admission':False,'independent_review':'PENDING','status':'HOLD_MISSING_PHYSICAL_WITNESSES','requirements':c,'mandatory_binding_fields':list(cfg['binding']),'coverage':cfg['coverage'],'records':[{'role':r,'status':'NOT_SUPPLIED','reviewer':None,'witness_sha256':None,'receipt_sha256':None} for r in roles],'independence':'Source/path bounds cannot come from the target monitor FFT. Reviewer identity and method truth require external review authority.','graph_integration':'Proposed scientific support bundle for the existing source_class/outside_tv/transfer/IQ roles. No existing graph or admission checker changed; no approved receipt emitted.','first_blocker':'Physical parameter/source reconstruction model and deterministic spectral-TV witness for impurity and aggregate omitted residual.'})
attachments=[]
for n in ['20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md','21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md']:
 p=R.parent/'project_sources'/n;attachments.append({'filename':n,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
save('PROVENANCE.json',{'constructor':'Codex','reviewer':'PENDING_NONCONSTRUCTOR_REVIEW','lane':'development; no registry entry','physical_promotion':0,'base':'f22659b9fa9e9f3ab5ca34d7215ea53ebf2adc71','dependencies':['captures/2026-10-22T133344Z-codex-sampled-monitor-93e0a217/THEOREM.md','captures/2026-10-22T133344Z-codex-sampled-monitor-93e0a217/CERTIFICATE.json','captures/2026-10-23T185253Z-codex-monitor-admission-6bf719d2/CONTRACT.json'],'attachment_sources':attachments,'attachment_interpretation':'v0.39 is historical235-object source, not a replacement for later723-object ledger; CRL2 subdivision is a governance proposal, not independent review.','missing_attachment':'Gap2_FINAL_Finite_Genesis.png unavailable and unused','verification_scope':'New conditional measure-convolution proof, exact rational16-case design controls, source-controlled apparatus requirements. No empirical data, calibration or experiment.'})
(P/'REPORT.md').write_text('''# Source-to-path leakage theorem and witness requirements v0.1

**RESULT: PASS_SCOPED — conditional theorem and exact proposed design.** A source-to-path spectral-TV inequality now makes the monitor\'s independent outside-model requirement explicit.16 constructor controls pass. All12 physical witness categories remain NOT_SUPPLIED; independent review pending. Physical Promotion0; EXIT-03 HOLD.

The theorem bounds the remainder by

\\[
T_{\\rm out}\\le MR+JU+\\sum_{d\\ge2}\\beta_d U^d/V_*^{d-1}+D,\\qquad U=B+A+R.
\\]

It includes full-input image leakage and primary-driven mixed nonlinear terms. A polynomial fit residual, noise RMS or a finite calibration sweep does not establish the required deterministic spectral-TV or uniform path bounds. Omitted orders, memory, drift, initial conditions and reference errors remain explicit witness obligations.

For the source-controlled I/Q demonstrator, the proposed numbers yield outside TV≤6.021506252020 µV and sampled RMS≤52.796506252020 µV. Exact fractions and every contribution appear in CERTIFICATE.json. The sampled-Gram upper bound is inherited from the same published row-sum certificate used for the lower bound; no continuous RMS interpolation is used.

The source assumptions already imply direct tail TV≤0.261021506253 mV. Thus this fixture checks calibration and consistency. It does not infer the structure of an unknown UD source, validate the historical circuit run or determine a native action scale. The prior general monitor ceiling0.90675 mV is unchanged.

THEOREM.md supplies the proof; PROTOCOL.md gives the apparatus scope,12 physical witness categories, planned blinded controls and review sequence; WITNESS_REQUIREMENTS.json records all missing roots. Neither existing admission checker is changed and no approved receipt is created. The design remains a proposal until a nonconstructor reviews the source/reconstruction and path model with defensible impurity and remainder TV bounds.

Verification: exact rational arithmetic,13 expected HOLD controls, a positive conditional design, an exact primary/mixed-term demonstration and the nominal alias identity (16 total). These are constructor mathematical/software checks, not executed experimental controls. No raw experimental dataset was downloaded or reanalyzed this milestone.

A. **CURRENT MISSION TRAJECTORY** — Convert the monitor\'s spectral assumptions into independently reviewable source/path evidence before measurement.

B. **WHAT WAS DONE** — Proved a conditional source-to-path leakage theorem, certified one exact design and specified the missing calibration/source witnesses and planned controls.

C. **FINDING** — The numerical requirements are algebraically compatible. Their physical validity and attainability remain unverified; all witness categories are missing.

D. **UD GAP IMPACT** — Exposes the actual deterministic source-impurity and remainder bottlenecks. No physical identification or action normalization is closed.

**NEXT TRAJECTORY STEP** — Determine whether a concrete source/reconstruction model can supply the1 µV impurity and2 µV aggregate residual TV witnesses; audit primary published methods/data against those exact requirements. Physical Promotion0.
''')
print({'metadata':'written','missing_witness_categories':len(roles),'controls':cert['control_count']})
