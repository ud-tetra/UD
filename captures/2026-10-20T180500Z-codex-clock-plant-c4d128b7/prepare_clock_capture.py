"""Prepare source-bound audit, identification records and budget replays."""
import hashlib,json,shutil
from pathlib import Path
R=Path('/workspace/scratch/1544cec576c6');REPO=R/'ud-repo'
C=REPO/'captures/2026-10-20T180500Z-codex-clock-plant-c4d128b7'
SAC=REPO/'captures/2026-10-20T163500Z-codex-sampled-actuator-9c71de42'
def write(name,obj):(C/name).write_text(json.dumps(obj,indent=2)+'\n')
for src,dst in [('clock_plant_certificate.py','clock_plant_certificate.py'),('cpc-results.json','CLOCK_PLANT_CERTIFICATE_v0.1.json'),('cpc-tex/UD_CLOCK_PLANT_COMPATIBILITY_v0.1.pdf','UD_CLOCK_PLANT_COMPATIBILITY_v0.1.pdf')]:shutil.copy2(R/src,C/dst)
for src,dst in [('sampled_actuator_certificate.py','sampled_actuator_dependency.py'),('finite_record_certificate_dependency.py','finite_record_dependency.py')]:shutil.copy2(SAC/src,C/dst)
def scope(file):
    d={'__name__':'dependency'};exec(compile((C/file).read_text(),file,'exec'),d);return d
sac=scope('sampled_actuator_dependency.py');frc=scope('finite_record_dependency.py');F=sac['F']
sampled=sac['certificate'](input_error=F(1,100000),command_error=F(1,25000),input_bits=24,output_bits=20)
assert sampled['status']=='PASS_CONDITIONAL_DESIGN'
assert sampled['total_residual']==F(149383,16000000)
gauss=frc['certificate'](age=F(0),other=F(1,400)+sampled['uniform_tracking_bound'])
assert gauss['status']=='PASS_CONDITIONAL_DESIGN'
assert gauss['total_defect_bound']==sampled['total_residual']
write('INHERITED_BUDGET_REPLAY_v0.1.json',sac['encode']({'status':'PASS_CONDITIONAL_MATHEMATICS','sampled_actuator':sampled,'Gauss_prefix':gauss,'hardware':'HOLD','note':'Alternative nu/q only; tracking counted once; endpoint tolerances unchanged; no actual observations','physical_promotion':0}))
sources=[
 {'id':'ADI_AD5791_F','title':'AD5791 Rev. F','url':'https://www.analog.com/media/en/technical-documentation/data-sheets/AD5791.pdf','pages':[3,17],'facts':'20-bit DAC; B-grade one-LSB maximum INL at +/-10 V references, 0 to 105 C; settling statements depend on step/buffer.','scope':'Supplier limits under conditions; affine and reference errors require calibration'},
 {'id':'ADI_LTC2500_B','title':'LTC2500-32 Rev. B','url':'https://www.analog.com/media/en/technical-documentation/data-sheets/250032fb.pdf','pages':[4,7,33],'facts':'32-bit filtered output; no-latency composite includes 24 differential bits; 2 ppm max INL; averaging DF1024 at 1MHz has 1.024 ms spacing and 512 us listed delay.','scope':'Group delay is not automatically an absolute history bound; no noise-tail certificate'},
 {'id':'TI_ADS127L21_C','title':'ADS127L21 Rev. C August 2025','url':'https://www.ti.com/lit/ds/symlink/ads127l21.pdf','pages':[1,7],'facts':'Filtered ADC alternative; characteristics depend on mode.','scope':'Full mode-specific audit remains OPEN'}]
write('MANUFACTURER_AUDIT_v0.1.json',{'accessed_UTC_date':'2026-10-20','status':'SUPPLIER_SPECIFICATION_SCREEN_ONLY','physical_promotion':0,'sources':sources,'verbatim_excerpts':[],'hardware_selection':'NONE','empirical_observations':'NONE','screen_result':'HOLD; clock/plant compatibility and calibrated error/model premises required'})
write('IDENTIFICATION_PLAN_v0.1.json',{
 'status':'PROPOSED_OPEN','physical_promotion':0,'lane':'development; no registry entry',
 'review':'non-constructor adversarial review PENDING','execution':'NONE',
 'admission':'HOLD; supplier specifications are not apparatus observations',
 'alternative_design_bounds':{'nu':'1/100000','q':'1/25000','remaining_SAC_bounds':'unchanged','total_residual':'149383/16000000','new_clock_parameters':'not measured'},
 'clock_gate':{'condition':'400000*max(Tp,mu_p+ell_p,tau_p) <= t0 <= min_c sqrt(Lc*Cc)','interval_method':'use joint calibration intervals; no optimistic endpoint selection','filter_mode_screen':'nominal averaging-mode spacing requires t0 >=2048/5 s under this allocation','every_pair_LC_requirement':'at least 4194304/25 s^2 for that mode','physical_component_values':'OPEN'},
 'records':[
  {'stage':'clock_and_plant','status':'OPEN','required':['L and C per canonical pair with units','loading','Phi0 Q0 common action products','energy and physical time scale joint intervals','nonempty compatibility interval']},
  {'stage':'readout_history','status':'OPEN','required':['frozen mode and filter coefficients','absolute coefficient sum and first age moment','aperture/output availability timestamps','startup tails','channel synchronization/skew','all computation transfer and command-application delays']},
  {'stage':'static_and_noise','status':'OPEN','required':['reference-traceable gain offset INL maps','temperature drift and reference error','crosstalk and independent regularity bounds','simultaneous uncertainty including noise and reconstruction','no substitution of RMS for peak bound']},
  {'stage':'actuator_identification','status':'OPEN','residual':'r_a=physical_derivative(a)/omega_physical+a-c','target_infinity_bound':'1/100000','required':['independent command/output measurements','bounded derivative reconstruction error','rate interval uncertainty','held-segment cover and regularity bound','one-sided command transitions and glitches','initial tails and loads','bidirectional range and slew']},
  {'stage':'release_and_blinded_CD1','status':'OPEN','required':['hold radius and prehistory speed','release tracking','holding work','frozen rule and review receipt','nominal wrong-sign and frozen-electric controls']}
 ],
 'hold_conditions':['Empty clock compatibility interval','Missing raw history or unbounded latency','Unidentified actuator or unbounded derivative error','Missing simultaneous error coverage','Unbudgeted calibration drift saturation or crosstalk','No attributable non-constructor review for registration'],
 'scope':'Short Gauss prefix; not full CD-1 campaign, SDW endpoint or physical bridge'})
deps=[]
for rel in ['captures/2026-10-20T163500Z-codex-sampled-actuator-9c71de42/UD_SAMPLED_ACTUATOR_THEOREM_v0.1.tex','captures/2026-10-20T163500Z-codex-sampled-actuator-9c71de42/sampled_actuator_certificate.py','captures/2026-10-20T140000Z-codex-finite-calibration-f4b96720/UD_FINITE_CALIBRATION_FAULT_CERTIFICATE_v0.1.tex']:
    p=REPO/rel;deps.append({'path':rel,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
gov=[]
for name in ['20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md','21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md']:
    p=R/'project_sources'/name;gov.append({'name':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
write('PROVENANCE_v0.1.json',{'origin':'User: continue next steps after sampled-actuator certificate','constructor':'Codex','reviewers':[],'lane':'development; no registry entry','physical_promotion':0,'repo_derivation_base':'d01945104084db51877ff15df8fff890120771be','site_source_base':'f9368b468e8dc78f3c07fa0cbf91b5020fc3b356','dependencies':deps,'governance_sources':gov,'external_sources':[x['url'] for x in sources],'external_source_role':'Manufacturer facts only; no actual apparatus data or physical promotion','added_premises':['Physical component values and loading','Calibrated clock and mode-specific timing/history','Filtered reconstruction model and error coverage','Alternate input/command allocation','Identified actuator and derivative regularity bounds'],'verification':'Ten exact arithmetic controls; inherited SAC and FCAL replay; analytic proofs; four-page visual PDF QA','limits':['Conservative-certificate obstruction is not physical impossibility','No component or apparatus admitted','No experiment or independent review','No dependency status strengthened by citation'],'unavailable_attachment':'Gap2_FINAL_Finite_Genesis.png unavailable and unused'})
write('PDF_QA_v0.1.json',{'status':'PASS','pages':4,'method':'pdflatex and Poppler full-page visual inspection','checks':['No overfull boxes or unresolved references','Readable tables proofs equations and references','Pagination and footer inspected'],'constructor_only':True})
(C/'requirements.txt').write_text('# Python 3 standard library; pdflatex for manuscript.\n')
print(json.dumps({'files_prepared':len(list(C.iterdir())),'alternative_budget_replay':'PASS','hardware':'HOLD'}))
