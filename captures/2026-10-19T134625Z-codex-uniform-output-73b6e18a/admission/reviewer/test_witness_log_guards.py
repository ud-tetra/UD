"""Synthetic v2 subprocess-log controls; not archived proof replays."""
import json,tempfile
from pathlib import Path
from offline_replay_v2 import run_command
cases=[('empty','pass',False),('wrong_counts',"print('{\"status\":\"PASS\",\"actual_saved_array_replays\":1,\"outside_ball_HOLD_replays\":1,\"negative_controls\":4}')",False),('valid_guard_fixture',"print('{\"status\":\"PASS\",\"actual_saved_array_replays\":2,\"outside_ball_HOLD_replays\":1,\"negative_controls\":4}')",True)]
rows=[]
with tempfile.TemporaryDirectory(prefix='ud-witness-log-guards-') as t:
 for name,code,should_pass in cases:
  out=Path(t)/name;out.mkdir();commands=[];accepted=False;reason=None
  try:run_command(out,['-c',code],out,'contract-witness',commands);accepted=True
  except RuntimeError as e:reason=str(e)
  assert accepted==should_pass
  rows.append({'fixture':name,'accepted':accepted,'reason':reason,'child_returncode':commands[0]['returncode'],'log_sha256':commands[0]['log_sha256']})
print(json.dumps({'status':'PASS','synthetic_guard_controls_only':True,'archived_proof_replays':0,'physical_promotion':0,'external_review':'PENDING','rows':rows},indent=2))
