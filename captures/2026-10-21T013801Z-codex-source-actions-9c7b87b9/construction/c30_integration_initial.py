from pathlib import Path
import argparse,importlib.util,json,hashlib
ap=argparse.ArgumentParser();ap.add_argument('--workspace',type=Path,required=True);ap.add_argument('--operator',type=Path,required=True);ap.add_argument('--executable',type=Path,required=True);ap.add_argument('--decoder',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False)
def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
O=load('new_source_actions',a.workspace/'c30_oracles.py');D=load('frozen_C29_decoder',a.decoder);assert hashlib.sha256(a.decoder.read_bytes()).hexdigest()=='705808468795a308ee47b9f4cdb6a156307d9205ccda81975d4442ccecde5bf5'
y=[(((13*i+7)%17)-8)*3*2**96//(4*1024)for i in range(253952)];assert sum(v*v for v in y)<(2*2**96)**2
A=O.SourceActions(a.operator,a.executable);got,receipt=D.decode(y,A.adjoint,A.normal,steps=2)
assert len(got)==2640 and receipt['normal_action_calls']==1 and receipt['adjoint_action_calls']==1 and receipt['whole_step_coordinates_checked']==5280
s=''.join(str(v)+'\n'for v in got);(a.out/'OUTPUT.txt').write_text(s)
(a.out/'INTEGRATION.json').write_text(json.dumps({'status':'PASS_ACTUAL2640_STATE_TWO_STEP_DECODER_INTEGRATION','steps':2,'actual_forward_actions':1,'actual_adjoint_actions':2,'decoder_receipt':receipt,'output_sha256':hashlib.sha256(s.encode()).hexdigest(),'data_rule':'y_i=3*(((13i+7)mod17)-8)/4096','data_norm_squared_dyadic_numerator':str(sum(v*v for v in y)),'data_dyadic_bits':96,'source_decoder_sha256':hashlib.sha256(a.decoder.read_bytes()).hexdigest(),'full8192_accuracy_claim':False,'physical_promotion':0,'external_promotion_review':'PENDING'},indent=2,sort_keys=True)+'\n');print('PASS actual2640-state two-step integration; full8192 gate not tested')
