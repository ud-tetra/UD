import assert from 'node:assert/strict';
import fs from 'node:fs';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url),m=require('./dist/assets/metric-admission-v0.1.js');
const root=JSON.parse(fs.readFileSync(new URL('./dist/sources/metric-admission-v0.1/METRIC_ADMISSION_ROOT_VERIFICATION_v0.1.json',import.meta.url)));
const fraction=s=>{const [a,b='1']=s.split('/');return Number(a)/Number(b)};
let cases=0;
for(const c of root.gram_cases){
  const r=m.calculate(fraction(c.q),c.p);
  for(let i=0;i<5;i++)assert.ok(Math.abs(r.squares[i]-fraction(c.squared_frequencies[i]))<1e-12);
  assert.ok(Math.abs(r.relation-2)<1e-12);assert.deepEqual(r.multiplicities,c.signed_multiplicities);cases++;
}
for(const c of root.degree_cases){const r=m.degree(c.g.map(fraction),'adjoint');for(let i=0;i<3;i++)assert.ok(Math.abs(r[i]**2-fraction(c.squared_frequencies[i]))<1e-12)}
for(const s of [.25,1,4,9])for(const g of [[1,1,1,1],[2,3,5,7]]){
 const ratio=m.degree(g,'adjoint'),mass=m.degree(g,'mass');
 m.degree(g.map(v=>v*s),'adjoint').forEach((v,i)=>assert.ok(Math.abs(v-ratio[i])<1e-12));
 m.degree(g.map(v=>v*s),'mass').forEach((v,i)=>assert.ok(Math.abs(v-mass[i]/s)<1e-12));
}
assert.throws(()=>m.calculate(0,1));assert.throws(()=>m.calculate(4,3));assert.throws(()=>m.degree([1,0,1,1],'mass'));
const page=fs.readFileSync(new URL('./dist/metric-admission/index.html',import.meta.url),'utf8');
for(const id of ['mf-rule','mf-shape','mf-verdict','mf-spectrum','mf-invariant'])assert.ok(page.includes('id="'+id+'"'));
assert.ok(page.includes('role="status"')&&page.includes('<noscript>'));
const receipt={status:'PASS',exact_fixture_cases:cases,metric_scaling_cases:16,invalid_inputs_rejected:true,markup_contract:true,browser_visual_qa:'Not run: control-browser unavailable in managed runtime',physical_promotion:0};
fs.writeFileSync(new URL('./dist/sources/metric-admission-v0.1/METRIC_ADMISSION_UI_VERIFICATION_v0.1.json',import.meta.url),JSON.stringify(receipt,null,2)+'\n');console.log(JSON.stringify(receipt));
