from pathlib import Path
import subprocess,os,time,json,argparse,hashlib,tempfile
p=argparse.ArgumentParser();p.add_argument('--executable',required=True);p.add_argument('--operator',required=True);p.add_argument('--mode',required=True);p.add_argument('--input',required=True);p.add_argument('--output',required=True);p.add_argument('--receipt',required=True);a=p.parse_args();start=time.monotonic()
with tempfile.TemporaryFile()as so,tempfile.TemporaryFile()as se:
 proc=subprocess.Popen([a.executable,a.operator,a.mode,a.input,a.output],stdout=so,stderr=se)
 pid,status,usage=os.wait4(proc.pid,0);proc.returncode=os.waitstatus_to_exitcode(status);assert pid==proc.pid;so.seek(0);se.seek(0);stdout=so.read().decode();stderr=se.read().decode();assert proc.returncode==0,stderr
elapsed=time.monotonic()-start
j={'mode':a.mode,'status':'PASS_ACTUAL_ACTION_EXECUTION','wall_seconds':elapsed,'peak_child_rss_kib':usage.ru_maxrss,'measurement':'os.wait4 specific action child; excludes prior children and Python wrapper','stdout':stdout,'stderr':stderr,'output_sha256':hashlib.sha256(Path(a.output).read_bytes()).hexdigest(),'executable_sha256':hashlib.sha256(Path(a.executable).read_bytes()).hexdigest(),'scope':'Observed Linux standalone action runtime, not worstcase or full decoder benchmark'};Path(a.receipt).write_text(json.dumps(j,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in j.items()if k not in ['stderr','stdout']},indent=2))
