// Exact cross-language checks of every interactive branch/window/supply selection.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
import {spawnSync} from 'node:child_process';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
const root=path.dirname(fileURLToPath(import.meta.url));
const require=createRequire(import.meta.url),jc=require('./dist/assets/joint-carrier-v0.1.js');
const py=String.raw`
import json
from dataclasses import asdict
from joint_carrier import Carrier,witness
rows=[]
for b in ['C','H']:
 s=witness(b)['specification']
 for n in [1,2,4,8]:
  for z in [0,1,2,3]:
   c=Carrier(s['successor'],s['receipt'],s['record_dimension'],n,z)
   for extra in [False,True]:
    x=c.prepared();states=[asdict(x)]
    for _ in range(c.L-1+(n+1 if extra else 0)):x=c.step(x);states.append(asdict(x))
    rows.append({'branch':b,'n':n,'z':z,'extra':extra,'states':states,'resources':c.resources()})
print(json.dumps(rows))
`;
const p=spawnSync('python',['-c',py],{cwd:root,encoding:'utf8',maxBuffer:8*1024*1024});
assert.equal(p.status,0,p.stderr);
const cases=JSON.parse(p.stdout),w=JSON.parse(fs.readFileSync(path.join(root,'dist/sources/joint-carrier-v0.1/JOINT_CARRIER_WITNESS_v0.1.json')));
let points=0;
for(const c of cases){const spec=w.branches[c.branch].specification;
 const states=jc.trace(spec,c.n,c.z,c.extra);assert.deepEqual(states,c.states);points+=states.length;
 const r=jc.resources(spec.states.length,spec.record_dimension,c.n,c.z);
 assert.equal(r.L,c.resources.clock_addresses);assert.equal(r.K,c.resources.certified_transitions);
 assert.equal(r.D.toString(),String(c.resources.payload_dimension));
 // JSON numbers can lose precision: compare dimension with exact integer formula from dimensions.
 const expected=BigInt(r.L)*BigInt(spec.states.length)**BigInt((c.n+1)*(c.z+1))*BigInt(spec.record_dimension)**BigInt(c.n*(c.z+1));
 assert.equal(r.joint,expected);assert.equal(r.bits,c.resources.allocated_binary_capacity_bits);
 assert.equal(r.history,c.resources.history_cells_total);assert.equal(r.records,c.resources.record_cells_total);
}
const html=fs.readFileSync(path.join(root,'dist/joint-carrier/index.html'),'utf8');
for(const id of ['branch','ticks','resets','post','step','position','prev','next','verdict','clock','payloads','dictionary','resources','stock'])assert.ok(html.includes(`id="jc-${id}"`),id);
const receipt={status:'PASS',selector_cases:cases.length,exact_joint_trace_points:points,selectors:'both C/H branches, four windows, four donor counts, with/without post-window reuse',bigint_capacity:true,script_sha256:crypto.createHash('sha256').update(fs.readFileSync(path.join(root,'dist/assets/joint-carrier-v0.1.js'))).digest('hex'),scope:'Cross-language model/parameter and markup checks. No rendered browser or accessibility certification.',physical_promotion:0};
fs.writeFileSync(path.join(root,'dist/sources/joint-carrier-v0.1/JOINT_CARRIER_UI_VERIFICATION_v0.1.json'),JSON.stringify(receipt,null,2)+'\n');
console.log(JSON.stringify(receipt));
