import fs from 'node:fs';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url),m=require('./dist/assets/refinement-tower-v0.1.js');
const r=JSON.parse(fs.readFileSync(new URL('./dist/sources/refinement-tower-v0.1/REFINEMENT_TOWER_ROOT_VERIFICATION_v0.1.json',import.meta.url)));
for(const c of r.counts){const v=m.counts(c.level).at(-1);assert.deepEqual(v.f,c.f_vector);assert.equal(v.dimension,c.dimension);assert.equal(v.newDirections,c.new_directions);assert.equal(v.totalDetails,c.total_details)}
for(const c of r.factorial_detail_witnesses){const w=m.witness(c.degree);assert.equal(w.factor,c.factor);assert.equal(w.sequentialDetail,Number(c.sequential_norm_squared));assert.equal(w.freshDetail,Number(c.fresh_composite_norm_squared))}
assert.equal(m.witness(1).sequentialTotal,Number(r.mixed_witness.sequential_total));assert.equal(m.witness(1).freshTotal,Number(r.mixed_witness.fresh_composite_total));
for(const v of [-1,1.5,5])assert.throws(()=>m.counts(v));assert.throws(()=>m.witness(0));
const html=fs.readFileSync(new URL('./dist/refinement-tower/index.html',import.meta.url),'utf8');
for(const id of ['rt-level','rt-degree','rt-counts','rt-verdict','rt-witness'])assert.ok(html.includes('id="'+id+'"'));
assert.ok(html.includes('role="status"')&&html.includes('<noscript>'));
const receipt={status:'PASS',integer_count_levels:5,exact_detail_witnesses:3,mixed_stock_fraction_agreement:true,invalid_inputs_rejected:true,markup_contract:true,browser_visual_qa:'Not run: control-browser unavailable in managed runtime',physical_promotion:0};fs.writeFileSync(new URL('./dist/sources/refinement-tower-v0.1/REFINEMENT_TOWER_UI_VERIFICATION_v0.1.json',import.meta.url),JSON.stringify(receipt,null,2)+'\n');console.log(JSON.stringify(receipt));
