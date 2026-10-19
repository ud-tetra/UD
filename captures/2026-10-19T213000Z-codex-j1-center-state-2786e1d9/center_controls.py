"""Malformed frozen sparse-state witness controls."""
import sys
sys.dont_write_bytecode=True
from center_solve import *
def main(folder):
 p=Path(folder);raw=(p/'CENTER_WITNESS.json').read_bytes();source=json.loads(raw);checks=[]
 for name,mutate in [('nonfinite state word',lambda w:w['hi_real_hex'].__setitem__(0,'nan')),('truncated correction words',lambda w:w['low_imag_hex'].pop()),('wrong frequency target',lambda w:w.__setitem__('omega','4'))]:
  bad=json.loads(json.dumps(source));mutate(bad)
  try:decode_state(bad)
  except (AssertionError,ValueError,OverflowError):checks.append(name)
  else:raise AssertionError(name+' accepted')
 result={'status':'PASS','source_witness_sha256':hashlib.sha256(raw).hexdigest(),'expected_rejections':checks,'independent_review':False,'physical_promotion':0};t=p/'CENTER_CONTROLS_RESULTS.json'
 if t.exists():assert json.loads(t.read_text())==result;print('read-only replay matches CENTER_CONTROLS_RESULTS.json')
 else:t.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS3 malformed state controls')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('folder');main(a.parse_args().folder)
