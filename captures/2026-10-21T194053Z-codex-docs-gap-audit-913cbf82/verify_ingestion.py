from pathlib import Path
import hashlib,json,subprocess
c=Path(__file__).parent;r=c.parents[1]
inv=json.loads((c/'SOURCE_INVENTORY.json').read_text())
assert len(inv)==170 and {x['path'] for x in inv}=={str(p.relative_to(r)) for p in (r/'docs').rglob('*') if p.is_file()}
for x in inv:
 b=(r/x['path']).read_bytes();assert len(b)==x['size_bytes'] and hashlib.sha256(b).hexdigest()==x['sha256']
assert sum(x['size_bytes'] for x in inv)==10812767
hashes=json.loads((c/'ARCHIVE_HASH_CHECKS.json').read_text());assert hashes['checks']==hashes['passed']==119 and not hashes['failed']
members=json.loads((c/'RECURSIVE_ARCHIVE_MEMBERS.json').read_text());assert len(members)==139
checks=json.loads(subprocess.run(['python3',str(c/'verify_claims.py')],check=True,capture_output=True,text=True).stdout)
assert checks==json.loads((c/'CLAIM_CHECKS.json').read_text())
print(json.dumps({'status':'PASS','top_level_hashes':len(inv),'archive_hash_entries':119,'archive_member_occurrences':139,'selected_claim_exact_checks':'PASS','scope':'source integrity and selected rational algebra, not archive-wide theorem review or simulation replay','independent_review':False,'physical_promotion':0},indent=2))
