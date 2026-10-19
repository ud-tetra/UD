"""Postexecution staging guard; joins frozen parent record and output bindings."""
import json
from uniform import P,sha
f=json.loads((P/'FREEZE.json').read_text());root=P.parent/'rounding-replay-work';parent=json.loads((root/'FREEZE.json').read_text());raw=json.loads((P/'inputs/PARENT_INTEGER_REPLAY.json').read_text())
assert sha(root/'RAW_PROJECTION_REPLAY.json')==f['input_sha256']['PARENT_INTEGER_REPLAY.json']
assert raw['raw_sha256']==parent['record_sha256'] and raw['exact_binary64_projection_for_encoded_ball'] and raw['vector_integer_squared_error_max']==1
assert raw['integer_projection_entries_checked']==2629311 and raw['readings_checked']==18790154
for name in ['legacy_gemm','integer_projection']:
 d=json.loads((root/'results'/name/'DISCOVERY.json').read_text());assert d['record_sha256']==parent['record_sha256'] and d['order']==209 and d['cutoff']==f['source_cutoff']
 assert sha(root/'results'/name/'CERTIFICATE.json')==f['actual_certificates_sha256'][name]
assert parent['source_cutoff'] if 'source_cutoff' in parent else parent['cutoff']==f['source_cutoff']
(P/'LINEAGE_RECEIPT.json').write_text(json.dumps({'status':'PASS_RAW_RECORD_FULL_FACTOR_AND_EMISSION_BINDINGS','raw_sha256':raw['raw_sha256'],'eligible_encoded_ball_member':True,'actual_paths_bound':2,'raw_readings_checked_in_parent':18790154,'parent_raw_recipe_and_reprojection_repeated_here':False,'physical_promotion':0},indent=2))
print('PASS parent raw record/fullfactor/discovery bindings')
