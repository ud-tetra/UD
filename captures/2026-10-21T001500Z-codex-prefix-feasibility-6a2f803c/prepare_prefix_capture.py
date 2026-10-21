"""Prepare prefix feasibility results and a physical-return contract."""
import hashlib,json,shutil
from pathlib import Path
R=Path('/workspace/scratch/1544cec576c6');REPO=R/'ud-repo'
C=REPO/'captures/2026-10-21T001500Z-codex-prefix-feasibility-6a2f803c'
def write(n,x):(C/n).write_text(json.dumps(x,indent=2)+'\n')
for src,dst in [('verify_prefix_box.py','verify_prefix_box.py'),('prefix_feasibility_certificate.py','prefix_feasibility_certificate.py'),('prefix-box.json','LOCAL_BOX_VERIFICATION_v0.1.json'),('prefix-results.json','PREFIX_FEASIBILITY_CERTIFICATE_v0.1.json'),('pfx-tex/UD_PREFIX_FEASIBILITY_THEOREM_v0.1.pdf','UD_PREFIX_FEASIBILITY_THEOREM_v0.1.pdf')]:shutil.copy2(R/src,C/dst)
sources=[
 {'id':'H193','url':'https://www.hammfg.com/electronics/transformers/choke/193','facts':'193S: 1H,5.75ohm;15% series tolerances; L measured at rated DC current.','status':'SUPPLIER_SCREEN_NOT_OPERATING_BAND_CERTIFICATE'},
 {'id':'NUES','url':'https://www.nichicon.com/en-us/part/ues1c102mhm/5398/','series_url':'https://www.nichicon.com/getmedia/069aeeb2-784e-41be-9621-207263576a6d/e-ues.pdf','facts':'UES1C102MHM: bipolar1000uF;20% capacitance tolerance at catalogue conditions;480uA leakage limit under rated-voltage test.','status':'SUPPLIER_SCREEN_NOT_LOW_VOLTAGE_LEAKAGE_CERTIFICATE'},
 {'id':'A4630','url':'https://www.analog.com/media/en/technical-documentation/data-sheets/ad4630-24_ad4632-24.pdf','revision':'B','facts':'AD4630-24: dual24bit;2MSPS/channel maximum;300ns maximum conversion time under conditions.','status':'PIPELINE_AND_NOISE_TAILS_OPEN'},
 {'id':'A5791','url':'https://www.analog.com/media/en/technical-documentation/data-sheets/AD5791.pdf','revision':'F','facts':'24bit write frame;35MHz maximum write clock; settling depends on step/buffer.','status':'ACTUATOR_MODEL_OPEN'}]
write('COMPONENT_ROUTE_v0.1.json',{
 'status':'CLOCK_INTERVAL_PASS_CONDITIONAL_HARDWARE_HOLD','physical_promotion':0,
 'lane':'development; no registry entry','independent_review':'PENDING','experiment':'NONE',
 'sources_accessed_UTC':'2026-10-21','sources':sources,
 'clock':{'lower_strict_seconds':'8/575','upper_seconds':'1/48','example_seconds':'1/60','prefix_duration_seconds':'1/6000'},
 'operating_band_premises':{'L_min_H':'17/20','C_min_F':'1/1250','R_max_ohms':'529/80','status':'OPEN; catalogue screening does not prove these at actual bias or during transient'},
 'physical_plant':'Phi_dot=Q/C-(R/L)Phi+V; Q_dot=-Phi/L+I; actual unmodeled terms bounded separately',
 'scales':{'nominal_Q0_C':'1/10000','nominal_Phi0_Wb':'sqrt(10)/1000','common_action_J_s':'sqrt(10)/10000000','rule':'After calibration choose per-channel balanced gains with the same action; no reuse of unequal action products'},
 'timing':{'ADC_proposed_sample_period_s':'1/2000000','command_period_s':'1/1000000','additional_true_input_to_command_latency_s':'<=1/500000','identified_actuator_time_constant_s':'<=1/1000000','independent_endpoint_clock_radius_model':'1/100000','status':'PROPOSED_NOT_MEASURED','DAC_reason':'A24bit frame at35MHz exceeds500ns, so command update is1MHz rather than2MHz'},
 'mathematical_results':{'local_target_L':'4','actual_speed_bound':'8/5','Gauss_L':'4','tracking':'53/25000','total_residual':'481/50000','residual_slack':'19/50000'},
 'accuracy':{'input_nu':'3/100000','complete_command_q':'1/25000','actuator_distortion':'1/100000','static_residual_p':'3/400','initial_e0':'1/10000','endpoint_m':'1/10000','status':'SUPPLIED_BOUNDS_NOT_OBSERVATIONS'},
 'startup':{'zero_initial_actuator':True,'hold_radius':'1/20000','preload':'at least10timeconstants;10us in example','tracking_upper':'33/40000','required':['every used sample history in hold tube','reconstructed inputs in D','prehistory speed bound','release kick bound','holding work record']},
 'noise_gate':{'controller_input_count_max':10000,'deterministic_input_allowance':'6ppm','noise_allowance':'24ppm','marginal_tail_premise':'two-sided subGaussian scale <=4ppm for every input error','family_failure_bound':'<1/500','status':'OPEN; not inferred from supplier RMS or SNR','other_uncertainties':'Separate joint allocation required for calibration, endpoints, clocks and witnesses'},
 'critical_identification_gates':[
  {'gate':'Flux/current law','status':'OPEN','records':['inductance at operating bias and transient spectrum','hysteresis and cross-coupling','resistance versus temperature','state reconstruction uncertainty']},
  {'gate':'Capacitor state and leakage','status':'OPEN','records':['charge-voltage relation including ESR and memory','actual low-voltage leakage or compensation residual','loading and uncertainty'],'nominal_whole_p_current_allowance_A':'45/1000000','warning':'Published480uA rated-voltage limit cannot certify45uA allowance; do not extrapolate linearly to test voltage'},
  {'gate':'Timing and actuation','status':'OPEN','records':['parallel ADC and DAC architecture','all timestamps and skew','code evaluation and write/latch timing','actual first-order residual','glitches tails range and slew']},
  {'gate':'Metrology and review','status':'OPEN','records':['traceable gains offsets references and drift','qualified noise-tail model','independent coupling/work sensing','joint coverage accounting','attributable non-constructor adversarial review']}
 ],
 'scope':'Only the specified short preparation prefix; no full campaign, SDW admission or physical/GUT bridge'})
deps=[]
for rel in ['captures/2026-10-20T140000Z-codex-finite-calibration-f4b96720/UD_FINITE_CALIBRATION_FAULT_CERTIFICATE_v0.1.tex','captures/2026-10-20T163500Z-codex-sampled-actuator-9c71de42/UD_SAMPLED_ACTUATOR_THEOREM_v0.1.tex','captures/2026-10-20T180500Z-codex-clock-plant-c4d128b7/UD_CLOCK_PLANT_COMPATIBILITY_v0.1.tex']:
    p=REPO/rel;deps.append({'path':rel,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
gov=[]
for n in ['20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md','21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md']:
    p=R/'project_sources'/n;gov.append({'name':n,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
write('PROVENANCE_v0.1.json',{'origin':'User: continue next steps after CPC theorem; find a plant/converter clock overlap','constructor':'Codex','reviewers':[],'lane':'development; no registry entry','physical_promotion':0,'repo_derivation_base':'fa8176d24e45f2d30bca2b0f2bc9e669988e1892','site_source_base':'ebdf1ab2447a86a8b0225758214b2b7119abe6d9','dependencies':deps,'governance_sources':gov,'external_sources':[s['url'] for s in sources],'verification':'Exact symbolic preparation-box majorants and twelve rational controls; five-page visual PDF QA. Constructor only.','added_premises':['Operating-band L C R and parasitic residual bounds','Fast SAR data path and1MHz command path','Two-microsecond complete latency','Qualified input noise tails and joint uncertainty','Identified actuator and release/prehistory bounds'],'status_limits':['Clock overlap conditional, hardware HOLD','Supplier catalogue conditions are not operating measurements','No full-box/full-horizon replacement of CPC or SAC','No experiment or independent review','No physical/GUT promotion'],'missing_attachment':'Gap2_FINAL_Finite_Genesis.png unavailable and unused'})
write('PDF_QA_v0.1.json',{'status':'PASS','pages':5,'method':'pdflatex; all Poppler page renders visually inspected','checks':['No overfull boxes or unresolved references','Readable equations tables and sources','Header footer pagination inspected'],'constructor_only':True})
(C/'requirements.txt').write_text('sympy==1.14.0\n')
print(json.dumps({'capture':C.name,'files_prepared':len(list(C.iterdir())),'hardware':'HOLD'}))
