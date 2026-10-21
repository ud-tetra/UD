"""Qualify, rather than repair, the incomplete construction progress journal."""
from pathlib import Path
import argparse,json,hashlib
ap=argparse.ArgumentParser();ap.add_argument('--frame',type=Path,required=True);a=ap.parse_args();P=Path(__file__).resolve().parent;H=lambda b:hashlib.sha256(b).hexdigest();fb=(a.frame/'FULL_FRAME.json').read_bytes();full=json.loads(fb);jb=(a.frame/'CHECKPOINT.jsonl').read_bytes();lines=jb.splitlines();rows=[json.loads(x)for x in lines];assert len(rows)==1989 and len({r['column']for r in rows})==1989
for row in rows:assert row==full['rows'][row['column']]
gaps=sorted(set(range(1999))-{r['column']for r in rows});assert gaps==[307,309,336,337,615,1008,1046,1079,1617,1977]
out={'status':'PASS_ALL_RETAINED_JOURNAL_ENTRIES_MATCH_FINAL_FRAME_WITH_RECORDED_GAPS','final_frame_sha256':H(fb),'journal_sha256':H(jb),'journal_entries_compared':1989,'missing_progress_columns':gaps,'cause':'UNDETERMINED','journal_repair_performed':False,'final_row_admission':'All1999 final payloads/metadata separately checked in ROWS_CHECKS; progress journal does not provide full contemporaneous trace.','followup':'Root separate10gap-row replay must be bound in final workflow receipt; no mathematical gate change.','scope':{'not_a_full_journal_completeness_claim':True,'no_invented_failure_cause':True,'physical_promotion':0,'external_review':'PENDING'}}
(P/'JOURNAL_CHECKS.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n');print(out['status'])
