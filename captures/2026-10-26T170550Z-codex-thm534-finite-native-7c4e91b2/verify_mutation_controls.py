"""Reject fixed-trace corruptions; a constructor integrity control."""
from pathlib import Path
import tempfile,shutil,subprocess,json,os
ROOT=Path(__file__).resolve().parent
def main():
    controls=[
      ('mask_flip',lambda d:d['steps'][0]['mask'].__setitem__(0,1-d['steps'][0]['mask'][0])),
      ('wrong_step',lambda d:d['steps'][0].__setitem__('t','1')),
      ('wrong_state',lambda d:d['steps'][0]['q_numerators'].__setitem__(14,d['steps'][0]['q_numerators'][14]+10**10))]
    out=[]
    for label,change in controls:
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)
            for f in ['native_model.py','verify_schedule.py','SCHEDULE_CERTIFICATE.json']:
                shutil.copyfile(ROOT/f,dest/f)
            data=json.loads((dest/'SCHEDULE_CERTIFICATE.json').read_text())
            change(data)
            (dest/'SCHEDULE_CERTIFICATE.json').write_text(json.dumps(data))
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
            result=subprocess.run(['python3',str(dest/'verify_schedule.py')],capture_output=True,text=True,env=env)
            assert result.returncode!=0
            assert 'AssertionError' in result.stderr
            out.append({'mutation':label,'rejected':True,'returncode':result.returncode})
    (ROOT/'MUTATION_CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
if __name__=='__main__':main()
