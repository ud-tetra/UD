import assert from 'node:assert/strict';
import fs from 'node:fs';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url),s=require('./dist/assets/subdivision-v0.1.js');
const r=JSON.parse(fs.readFileSync(new URL('./dist/sources/subdivision-v0.1/SUBDIVISION_METRIC_ROOT_VERIFICATION_v0.1.json',import.meta.url)));
assert.deepEqual(s.inspect('ordinary').factors,r.source_subdivision_gram_factors);
assert.equal(s.inspect('ordinary').defect,Number(r.unit_euclidean_generator_vertex_defect_squared[0]));
assert.equal(s.inspect('bounded').defect,7/24);
assert.equal(s.inspect('diagonal').defect,Number(r.naive_factorial_metric_vertex_generator_defect_squared[0]));
assert.equal(s.inspect('retraction').defect,0);assert.equal(s.inspect('retraction').complement,r.dimensions.complement);
assert.equal(s.inspect('degree').boundary,'Fails');assert.equal(s.inspect('degree').defect,null);
for(const branch of ['ordinary','bounded','degree','diagonal','retraction']){
 const x=s.inspect(branch);assert.equal(x.old,r.dimensions.old);assert.equal(x.fine,r.dimensions.subdivided);assert.equal(x.normFactors.length,4);
}
assert.throws(()=>s.inspect('unknown'));assert.throws(()=>s.inspect('__proto__'));
const html=fs.readFileSync(new URL('./dist/subdivision/index.html',import.meta.url),'utf8');
for(const id of ['sg-branch','sg-verdict','sg-conditions','sg-factors'])assert.ok(html.includes('id="'+id+'"'));
assert.ok(html.includes('role="status"')&&html.includes('<noscript>'));
const receipt={status:'PASS',declared_branches:5,root_receipt_agreement:true,invalid_inputs_rejected:true,markup_contract:true,browser_visual_qa:'Not run: control-browser unavailable in managed runtime',physical_promotion:0};
fs.writeFileSync(new URL('./dist/sources/subdivision-v0.1/SUBDIVISION_UI_VERIFICATION_v0.1.json',import.meta.url),JSON.stringify(receipt,null,2)+'\n');console.log(JSON.stringify(receipt));
