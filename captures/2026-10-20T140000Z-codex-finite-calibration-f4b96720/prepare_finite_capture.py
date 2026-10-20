"""Generate finite-calibration capture metadata from verified local artifacts."""
import hashlib,json,shutil
from pathlib import Path
R=Path('/workspace/scratch/1544cec576c6');REPO=R/'ud-repo'
C=REPO/'captures/2026-10-20T140000Z-codex-finite-calibration-f4b96720'
def write(name,obj):(C/name).write_text(json.dumps(obj,indent=2)+'\n')
for src,name in [('frc-tex/UD_FINITE_CALIBRATION_FAULT_CERTIFICATE_v0.1.pdf','UD_FINITE_CALIBRATION_FAULT_CERTIFICATE_v0.1.pdf'),('finite_record_certificate.py','finite_record_certificate.py'),('verify_finite_record.py','verify_finite_record.py'),('frc-calculator.json','RATIONAL_CERTIFICATE_v0.1.json'),('frc-symbolic.json','SYMBOLIC_VERIFICATION_v0.1.json')]:
    shutil.copy2(R/src,C/name)
(C/'requirements.txt').write_text('sympy==1.14.0\n')
write('FINITE_CALIBRATION_RETURN_v0.1.json',{
 'version':'0.1','status':'OPEN_APPARATUS_RETURN','physical_promotion':0,
 'scope':'Short-window CD-1 Gauss discriminator; not full campaign or endpoint admission',
 'design_inputs_kind':'Illustrative supplied mathematical bounds; no measurements',
 'design_example':{
  'initial_state_error_infinity':'1/10000','endpoint_reconstruction_error_infinity':'1/10000',
  'continuous_vectorfield_residual_infinity':'1/100','nominal_time':'1/100','time_radius':'1/100000',
  'controller_input_age':'1/100000','max_age_for_allocated_delay':'1/81810',
  'plant_L_upper':'1','prehistory_and_actual_speed_upper':'81/10',
  'residual_allocations':{'node_uncertainty':'1/400','regularity_times_cover_radius':'1/400','controller_age':'1/400','other':'1/400'},
  'units':'All above normalized model units; physical time = model time * t0 seconds'},
 'required_records':[
  {'type':'port_design','status':'OPEN','records':['actual flux-charge port equations','component values with units','loading and actuator topology','input saturation and controller work']},
  {'type':'canonical_scale','status':'OPEN','records':['Phi0 and Q0 per channel','common action S0 and mismatch bounds','physical energy E0','t0 in seconds','joint uncertainty and traceability']},
  {'type':'finite_calibration','status':'OPEN','records':['domain and module decomposition','crosstalk remainder','nodes with true-residual uncertainty intervals','cover radii','independently justified derivative bounds','drift over planned experiment interval']},
  {'type':'control_timing','status':'OPEN','records':['timestamped sensing and actuation','maximum coordinate input age','initialization and prehistory speed','mode-switch transients','plant Lipschitz bound']},
  {'type':'metrology','status':'OPEN','records':['raw state records','independent coupling witnesses','preparation bound','endpoint reconstruction bound','clock bound','joint systematic and statistical uncertainty','missing channels and saturation flags']},
  {'type':'blinded_controls','status':'OPEN','records':['nominal law','wrong entire second-species sign','frozen electric response','unrounded decision inputs','same preparation and budget']},
  {'type':'review','status':'OPEN','records':['attributable non-constructor review','premise audit','joint coverage statement']}
 ],
 'hold_conditions':['Any required premise unsupported','Finite node samples with no regularity certificate','Residual or decision margin fails','Missing channels or unbounded saturation','Per-run coverage used as whole-campaign coverage without joint correction'],
 'campaign_coverage':{'original_CD1_per_run':'at least 99% joint','optional_300_run_joint_target':'99%','equal_union_bound_failure_allocation':'1/30000 per run','includes_shared_systematics':True},
 'independent_review':'PENDING','experimental_execution':'NONE'
})
deps=[]
for rel in [
 'captures/2026-10-20T133000Z-codex-canonical-diamond-6d82a19f/UD_CANONICAL_APPARATUS_MAP_v0.1.tex',
 'captures/2026-10-20T133000Z-codex-canonical-diamond-6d82a19f/CLOSED_DIAMOND_PROTOCOL_v0.1.json',
 'captures/2026-10-15T022222Z-codex-joint-hamiltonian-f51873da/UD_JOINT_HAMILTONIAN_THEOREM_v0.1.tex']:
    p=REPO/rel;deps.append({'path':rel,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
write('PROVENANCE_v0.1.json',{'origin':'User: continue next steps after canonical map and instrumented CD-1','constructor':'Codex','reviewers':[],'lane':'development; no registry entry','physical_promotion':0,'repo_derivation_base':'8bfcbd64848212cc12833df4b3f9a6e143474a96','site_source_base':'78db53a4e47d296e0d604fba164a28a0b0bbcc09','dependencies':deps,'added_inputs':['convex calibration domains and independently justified regularity bounds','actual normalized plant and active-port control law','controller input-age and prehistory-speed bounds','preparation reconstruction and clock-error bounds','proposed explicit residual allocation'],'source_status':'No dependency status strengthened by citation','verification':'Exact symbolic constructor checks plus seven rational controls; six-page PDF visual QA; independent review pending','scope_limits':['Short-prefix Gauss discriminator only','No actual hardware measurements or experimental execution','No full CD-1 horizon or SDW endpoint admission','No physical or GUT bridge'],'missing_attachment':'Gap2_FINAL_Finite_Genesis.png unavailable and unused; user notified'})
write('PDF_QA_v0.1.json',{'status':'PASS','pages':6,'method':'pdflatex; Poppler full-page renders visually inspected','scope':'Readable equations and tables, no clipped content or unresolved references','constructor_QA_only':True})
print(json.dumps({'capture':C.name,'files_prepared':len(list(C.iterdir()))}))
