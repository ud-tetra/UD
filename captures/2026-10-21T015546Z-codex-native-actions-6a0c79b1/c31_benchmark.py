from pathlib import Path
import argparse,subprocess,json,hashlib
p=argparse.ArgumentParser();p.add_argument('--workspace',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False);P=a.workspace;rows=[]
for mode,inp in [('forward','c30_x_boundary.txt'),('adjoint','c30_y.txt')]:
 pair={}
 for label,exe in [('baseline','c30_action'),('native','c31_action')]:
  receipt=a.out/(mode+'_'+label+'.json');out=a.out/(mode+'_'+label+'.txt')
  subprocess.run(['python',str(P/'c31_run_timed.py'),'--executable',str(P/exe),'--operator',str(P/'c31_math/OPERATOR.txt'),'--mode',mode,'--input',str(P/inp),'--output',str(out),'--receipt',str(receipt)],check=True,capture_output=True,text=True);pair[label]=json.loads(receipt.read_text())
 rows.append({'mode':mode,'baseline':pair['baseline'],'native':pair['native'],'observed_speed_ratio':pair['baseline']['wall_seconds']/pair['native']['wall_seconds']})
(a.out/'BENCHMARK.json').write_text(json.dumps({'status':'PASS_OBSERVED_PAIRED_ACTION_BENCHMARK','measurement':'Sequential baseline then native per mode; os.wait4 perchild resource; environment-specific, not worstcase','pairs':rows,'full8192_benchmark':False,'physical_promotion':0},indent=2,sort_keys=True)+'\n');print('PASS paired standalone action benchmark')
