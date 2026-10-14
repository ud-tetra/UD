"""Source-preserving validation plus independent conditional polarity/sign checks.
No scripts from an imported source archive are executed.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
import json,hashlib,zipfile,math,subprocess
ROOT=Path(__file__).parent;D=ROOT/'dist'
r=json.loads((D/'assets/reconciliation.json').read_text());ss=json.loads((D/'assets/sources.json').read_text());src={s['id']:s for s in ss};ledger=json.loads((D/'assets/ledger.json').read_text())
assert len(r['rows'])==448 and len({x['row_id'] for x in r['rows']})==448
byid={x['id']:x for x in ledger['rows']}
for x in r['rows']:
 assert x['source_row']==byid[x['row_id']]
 assert x['reuse_limit'] and x['dependency_graph_status'].startswith('OPEN_GATED')
 assert all((y['ref_id'] in byid) if y['in_ledger'] else y['namespace']=='lab-feasibility-criteria' for y in x['explicit_references'])
 assert x['physical_promotion']==0
assert sum(x['version_relation']=='ADDED_AFTER_V0.39' for x in r['rows'])==213
assert sum(x['version_relation']=='UNCHANGED_FIELDS' for x in r['rows'])==229
assert sum(x['version_relation']=='VERSIONED_FIELDS_CHANGED' for x in r['rows'])==6
for a in r['amendments']:assert all(s in src for s in a['sources']) and all(x in byid for x in a['affected_ids'])
recovery=json.loads((D/'assets/source-recovery.json').read_text());assert len(recovery['source_views'])==65
for x in recovery['source_views']:
 s=src[x['source_id']];assert s['original']['sha256']==x['original_sha256'];assert s['sha256']==x['new_sha256'];assert len(s['content'])>500
 assert s['status'] not in ['PLACEHOLDER','PLACEHOLDER ARCHIVE']
 f=D/s['local'].lstrip('/');assert f.exists() and hashlib.sha256(f.read_bytes()).hexdigest()==s['sha256']
 if s['original']['local']:
  f=D/s['original']['local'].lstrip('/');assert hashlib.sha256(f.read_bytes()).hexdigest()==s['original']['sha256']
with zipfile.ZipFile(D/'releases/UD_RECONSTRUCTED_SOURCE_VIEWS_v0.2.zip') as z:
 assert z.testzip() is None;assert len([n for n in z.namelist() if n.startswith('views/')])==55
 assert hashlib.sha256(z.read('original/DistinctionDynamics_Full_Repository_v1.zip')).hexdigest()==src['A05']['original']['sha256']

# Independent standard-library enumeration of the conditional idle correction.
seat=[(T,L,q) for T,L,q in product([0,1],repeat=3) if T*L<=q<=T];assert len(seat)==5
states=[]
for seats in product(seat,repeat=3):
 omega=tuple(T*L for T,L,q in seats);q=tuple(q for T,L,q in seats);h=tuple(a-b for a,b in zip(q,omega));states.append((omega,q,h))
hist=[sum(sum(x[2])==k for x in states) for k in range(4)];assert hist==[64,48,12,1]
equal=0;saturated_pairs=0;saturated_equal=0
for o,q,h in states:
 for op,qp,hp in states:
  mu=sum(q)-sum(qp);index=sum(o)-sum(op);idle=sum(h)-sum(hp)
  assert mu==index+idle
  equal+=mu==index
  if not sum(h):saturated_pairs+=1;saturated_equal+=mu==index
assert equal==6545 and saturated_pairs==8000 and saturated_equal==4096

# A sign witness only; it is not a cosmological fit or a corrected physical law.
ns=Fraction(9,10);rho=Fraction(1,2);contraction=Fraction(1,4)
assert ns<1 and 0<rho<1 and 0<contraction<1
running=-float(ns-1)*abs(math.log(float(rho)))/math.log(1/float(contraction));assert running>0
assert math.isclose(running,float(Fraction(1,20)),rel_tol=1e-14)
claims=json.loads((D/'assets/claims.json').read_text());assert all(x['id'].startswith('ATLAS') and x['id'] not in byid for x in claims)
out={'status':'PASS','ledger_rows_preserved':448,'historical_rows_compared':235,'changed_fields_rows':6,'new_rows':213,'unchanged_rows':229,'amendments':10,'rows_with_amendments':r['summary']['rows_with_amendments'],'substantive_source_views':65,'original_exact_name_derivations_recovered':0,'original_zip_byte_hash_preserved':True,'polarity_conditional_check':{'complete_states':125,'ordered_pairs':15625,'idle_histogram':hist,'index_equals_full_polarity':6545,'saturated_prior_pairs':8000,'saturated_both_equalities':4096,'status':'exact finite check of declared admissible domain; not physical data'},'gap2_sign_audit':{'symbolic_reason':'For n_s<1 and 0<rho,r<1, each factor in -(n_s-1)*abs(ln rho)/ln(1/r) is positive.','numerical_witness':running,'scope':'No sign-repaired physical formula or primordial prediction is inferred.'},'proof_dependency_DAG':'OPEN_GATED; explicit references only','review':'constructor reconciliation and standard-library independent implementation; no human review','physical_promotion':0}
(D/'sources/UD_PRESENTATION_RECONCILIATION_VERIFICATION_v0.2.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
