import fs from 'node:fs';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url),m=require('./dist/assets/metric-selection-v0.1.js');
const root=JSON.parse(fs.readFileSync(new URL('./dist/sources/metric-selection-v0.1/METRIC_SELECTION_ROOT_VERIFICATION_v0.1.json',import.meta.url)));
const fraction=s=>{const [n,d='1']=s.split('/');return Number(n)/Number(d)};
let count=0;
for(const c of root.metric_witnesses)for(const o of c.observable_cases){
 const r=m.calculate(fraction(c.complement_weight),fraction(o.lambda));
 assert.equal(r.norm,fraction(c.fine_barycenter_norm_squared));assert.equal(r.value,fraction(o.value));assert.ok(Math.abs(r.fraction-fraction(o.fraction))<1e-12);assert.equal(r.complementBlind,o.complement_blind);assert.ok(Math.abs(r.coarseFraction+r.complementFraction-1)<1e-12);count++;
}
for(const [w,l] of [[0,0],[-1,0],[NaN,0],[1,-1],[1,2]])assert.throws(()=>m.calculate(w,l));
const page=fs.readFileSync(new URL('./dist/metric-selection/index.html',import.meta.url),'utf8');
for(const id of ['ms-weight','ms-response','ms-verdict','ms-witness','ms-receipts'])assert.ok(page.includes('id="'+id+'"'));
assert.ok(page.includes('role="status"')&&page.includes('<noscript>'));
const receipt={status:'PASS',exact_fixture_cases:count,complete_receipt_sums:true,invalid_inputs_rejected:true,markup_contract:true,browser_visual_qa:'Not run: control-browser unavailable in managed runtime',physical_promotion:0};fs.writeFileSync(new URL('./dist/sources/metric-selection-v0.1/METRIC_SELECTION_UI_VERIFICATION_v0.1.json',import.meta.url),JSON.stringify(receipt,null,2)+'\n');console.log(JSON.stringify(receipt));
