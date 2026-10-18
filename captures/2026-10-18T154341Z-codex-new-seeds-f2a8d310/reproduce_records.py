"""Regenerate omitted raw records in a new directory from the pinned repository codec."""
import argparse,json,shutil,subprocess,sys
from pathlib import Path
from bindings import P,sha
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--destination',required=True);a=p.parse_args();f=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());out=Path(a.destination).resolve();out.mkdir(parents=True,exist_ok=False)
 for name in f['code_sha256']:shutil.copyfile(P/name,out/name)
 shutil.copytree(P/'inputs',out/'inputs');shutil.copyfile(P/'CAMPAIGN_FREEZE.json',out/'CAMPAIGN_FREEZE.json');(out/'records').mkdir();(out/'codec').mkdir()
 source=Path(a.repo)/f['baseline_codec_repository_path']
 for n,h in f['baseline_codec_sha256'].items():assert sha(source/n)==h;shutil.copyfile(source/n,out/'codec'/n)
 for args in [['record_codec.py','restore','codec','records/BASELINE.i64le'],['make_records.py']]:
  r=subprocess.run([sys.executable,*args],cwd=out);assert r.returncode==0
 expected=json.loads((P/'DATA_FREEZE.json').read_text());got=json.loads((out/'DATA_FREEZE.json').read_text());assert got['records']==expected['records']
 (out/'RAW_REGENERATION_RECEIPT.json').write_text(json.dumps({'status':'PASS_ALL_FIVE_REGENERATED_RAW_HASHES_AND_EXACT_GATES','physical_promotion':0,'source_campaign_sha256':sha(P/'CAMPAIGN_FREEZE.json'),'original_data_freeze_sha256':sha(P/'DATA_FREEZE.json'),'records':got['records']},indent=2));print('All five deterministic raw records regenerated and bound to original hashes')
