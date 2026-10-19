"""Synthetic safe-extraction controls; executes no archived code."""
import json,stat,tempfile,zipfile
from pathlib import Path
from offline_replay import archive_plan,extract,safe_name

def main():
 rows=[]
 with tempfile.TemporaryDirectory(prefix='ud-offline-intake-control-') as t:
  p=Path(t)
  bad=['../escape','/absolute','a/../../escape','a\\escape','a//b','a/./b','C:/drive']
  for i,name in enumerate(bad):
   q=p/f'bad{i}.zip'
   with zipfile.ZipFile(q,'w') as z:z.writestr(name,b'x')
   try:extract([q],p/f'out{i}')
   except ValueError:rows.append({'control':name,'status':'REFUSED'})
   else:raise AssertionError('unsafe path admitted')
   assert not (p/f'out{i}').exists()
  q=p/'symlink.zip';info=zipfile.ZipInfo('link');info.create_system=3;info.external_attr=(stat.S_IFLNK|0o777)<<16
  with zipfile.ZipFile(q,'w') as z:z.writestr(info,b'../elsewhere')
  try:extract([q],p/'symlink-out')
  except ValueError:rows.append({'control':'symlink','status':'REFUSED'})
  else:raise AssertionError('symlink admitted')
  one=p/'one.zip';two=p/'two.zip'
  for q in [one,two]:
   with zipfile.ZipFile(q,'w') as z:z.writestr('same',b'x')
  try:extract([one,two],p/'duplicate-out')
  except ValueError:rows.append({'control':'cross-archive duplicate','status':'REFUSED'})
  else:raise AssertionError('duplicate admitted')
  good=p/'good.zip'
  with zipfile.ZipFile(good,'w') as z:z.writestr('nested/a.txt',b'abc')
  r=extract([good],p/'good-out');assert (p/'good-out/nested/a.txt').read_bytes()==b'abc' and r['unique_members']==1;rows.append({'control':'ordinary relative nested file','status':'ACCEPTED'})
 result={'status':'PASS','controls':rows,'archived_scripts_executed':False,'external_review':'PENDING','physical_promotion':0};print(json.dumps(result,indent=2))
if __name__=='__main__':main()
