"""Prepare the versioned sampled-actuator theorem and evidence contracts."""
import hashlib,json,shutil
from pathlib import Path
R=Path('/workspace/scratch/1544cec576c6');REPO=R/'ud-repo'
C=REPO/'captures/2026-10-20T163500Z-codex-sampled-actuator-9c71de42'
FRC=REPO/'captures/2026-10-20T140000Z-codex-finite-calibration-f4b96720'
def write(name,data):(C/name).write_text(json.dumps(data,indent=2)+'\n')
for src,dst in [('sac-tex/UD_SAMPLED_ACTUATOR_THEOREM_v0.1.pdf','UD_SAMPLED_ACTUATOR_THEOREM_v0.1.pdf'),('sampled_actuator_certificate.py','sampled_actuator_certificate.py'),('sac-results.json','SAMPLED_ACTUATOR_CERTIFICATE_v0.1.json')]:shutil.copy2(R/src,C/dst)
shutil.copy2(FRC/'finite_record_certificate.py',C/'finite_record_certificate_dependency.py')
# Source-bound replay; this is our earlier reviewed-by-constructor code, not
# an imported archive. exec avoids creating unmanifested bytecode in captures.
scope={'__name__':'certificate_dependency'}
exec(compile((C/'finite_record_certificate_dependency.py').read_text(),'finite_record_certificate_dependency.py','exec'),scope)
newscope={'__name__':'sampled_certificate'}
exec(compile((C/'sampled_actuator_certificate.py').read_text(),'sampled_actuator_certificate.py','exec'),newscope)
tracking=newscope['certificate']()['uniform_tracking_bound']
F=newscope['F']
joined=scope['certificate'](age=F(0),other=F(1,400)+tracking)
assert joined['status']=='PASS_CONDITIONAL_DESIGN'
assert joined['total_defect_bound']==F(145267,16000000)
write('GAUSS_INTEGRATION_v0.1.json',scope['encode']({'status':'PASS','scope':'New tracking replaces the ideal-delay term, counted exactly once in the inherited residual budget. Continuous defect remains conservatively 1/100.','inherited_prefix_result':joined,'physical_promotion':0}))
(C/'requirements.txt').write_text('# Python 3 standard library only; pdflatex for manuscript reproduction.\n')
write('APPARATUS_COMPONENT_CONTRACT_v0.1.json',{
 'version':'0.1','status':'PROPOSED_OPEN','physical_promotion':0,
 'lane':'development; no registry entry','apparatus_kind':'Actively controlled classical flux-charge simulator',
 'not_observations':True,'independent_review':'PENDING','execution':'NONE',
 'architecture':['Calibrated canonical flux-charge pairs','Timestamped 24-coordinate acquisition','Sampled digital command evaluation','Held voltage/current commands','Identified first-order actuation','LC plant','Independent coupling/work/source and endpoint readout'],
 'units':{'model_time':'tau=t/t0','physical_t0':'S_action/E_energy seconds; actual calibrated interval OPEN','normalized_input_box':'[-1,1] per coordinate','normalized_output_range':'[-10,10] per actuator'},
 'design_bounds':{'T':'1/400000','additional_latency':'1/400000','maximum_coordinate_sample_age':'1/200000','input_error':'1/1000000','complete_command_error':'1/100000','actuator_model_distortion':'1/100000','minimum_actuator_rate':'400000','initial_tracking_error':'1/1000','static_and_other_residual':'3/400','prehistory_speed':'81/10','actuator_range_magnitude':'10','proposed_input_and_output_bits':22},
 'physical_requirements':{'sampling_period_seconds':'<=t0/400000','additional_latency_seconds':'<=t0/400000','actuator_time_constant_seconds':'<=t0/400000','minimum_voltage_range':'+-10*Phi0_c/t0 volts','minimum_current_range':'+-10*Q0_c/t0 amperes','example_preload_seconds':'>=t0/40000','clock_uncertainty':'Use worst-case normalized bounds across the joint t0 calibration interval'},
 'startup':{'status':'OPEN','zero_initial_actuator':True,'hold_radius':'1/1000000','hold_history':'Every sample used in preload is within the same hold tube','preload_duration':'at least 10 time constants','required_release_records':['initial state error','actuator tracking error','prehistory speed','no unbudgeted switching kick','work exchanged by holding system'],'conditional_tracking_upper':'4391/8000000'},
 'quantization':{'model':'Ideal uniform midrise, no clipping','input_error_floor':'1/4194304','output_error_floor':'5/2097152','note':'22 nominal bits do not establish attainable rate, noise, linearity or effective resolution; all additional errors must fit remaining allowances'},
 'evidence_required':[
  {'kind':'port/component design','status':'OPEN','records':['C and L with units','readout loading','port gains and signs','Phi0 Q0 common-action mismatch','E0 and t0 interval']},
  {'kind':'actuator identification','status':'OPEN','records':['identified first-order model over domain','distortion envelope','cross-channel errors','latency and bandwidth','bidirectional saturation and slew limits']},
  {'kind':'timing','status':'OPEN','records':['raw sensing/computation/application timestamps','jitter and frame drop indicators','maximum true coordinate age','release-clock origin']},
  {'kind':'metrology','status':'OPEN','records':['input error decomposition','command computation and quantization error','independent endpoint reconstruction','independent coupling witnesses','work/source records']},
  {'kind':'calibration regularity','status':'OPEN','records':['node residuals with joint uncertainty','cover radius','separately justified derivative bounds','unmodeled remainder and drift']},
  {'kind':'non-constructor review','status':'OPEN','records':['attributable adversarial premise and proof review']}
 ],
 'hold_rules':['Missing or unsupported bounds','Outside identified actuator domain','Unbudgeted delay, ringing, saturation, slew or coupling','Cold startup with no tracking certificate','Computed coupling used as the sole coupling witness','Failure of any exact margin','Per-run confidence misrepresented as campaign coverage'],
 'scope':'Short Gauss-discriminator prefix only; no full CD-1 campaign or SDW endpoint admission'
})
deps=[]
for rel in ['captures/2026-10-20T133000Z-codex-canonical-diamond-6d82a19f/UD_CANONICAL_APPARATUS_MAP_v0.1.tex','captures/2026-10-20T140000Z-codex-finite-calibration-f4b96720/UD_FINITE_CALIBRATION_FAULT_CERTIFICATE_v0.1.tex','captures/2026-10-20T140000Z-codex-finite-calibration-f4b96720/finite_record_certificate.py']:
    p=REPO/rel;deps.append({'path':rel,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
governance=[]
for name in ['20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md','21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md']:
    p=R/'project_sources'/name;governance.append({'name':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
write('PROVENANCE_v0.1.json',{'origin':'User: continue next steps after finite-calibration theorem','constructor':'Codex','reviewers':[],'lane':'development; no registry entry','physical_promotion':0,'repo_derivation_base':'73d23f983f54a0dc5a5c986f5410513e5f3fe937','site_source_base':'a8847b287e6648a9a3e84c4fe29eba611fdbcfb0','dependencies':deps,'governance_sources':governance,'added_premises':['Actual canonical LC port variables','Bounded static residual and identified first-order actuator','Timestamped maximum sample age','Input and complete command error bounds','Startup hold history and release bounds','Independent apparatus metrology'],'verification':'Nine exact rational controls, exact Taylor startup bound and source-bound Gauss-budget replay; four-page visual PDF QA; constructor checks only','status_limits':['No dependency promoted through citation','No actual hardware selection or observations','No physical or GUT identification','No full CD-1 or SDW admission'],'notation_firewall':'Physical common action S0 is distinct from the coefficient ledger structural S0=43/7','unavailable_attachments':['Gap2_FINAL_Finite_Genesis.png','Notes Backup 17-04-2026 07-13.txt','ASTER_Project_Folder_Instruction_Block_v1.md']})
write('PDF_QA_v0.1.json',{'status':'PASS','pages':4,'method':'pdflatex and full-page Poppler PNG render inspection','checks':['No overfull boxes or unresolved references','Readable equations and tables','Headers footers and pagination inspected'],'constructor_QA_only':True})
print(json.dumps({'files_prepared':len(list(C.iterdir())),'Gauss_integration':'PASS','nine_controls':'PASS'}))
