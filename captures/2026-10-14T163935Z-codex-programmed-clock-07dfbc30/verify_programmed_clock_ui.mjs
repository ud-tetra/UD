import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
import {spawnSync} from 'node:child_process';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
const root=path.dirname(fileURLToPath(import.meta.url)),require=createRequire(import.meta.url),pc=require('./dist/assets/programmed-clock-v0.1.js');
const py=String.raw`
from programmed_clock import compiled_word,clock_snapshot
import json
out=[]
for branch in ['C','H']:
 for N in [1,2,4,8]:
  for B in [0,1,2,3]:
   for pad in [False,True]:
    w=compiled_word(branch,N,B,pad)
    out.append({'branch':branch,'N':N,'B':B,'pad':pad,'n':w['word_length'],'K':w['original_word_length'],'dimension':str(w['complete_joint_dimension']),'snapshots':[clock_snapshot(w['word_length'],xi) for xi in [0,.125,.25,.5,.75,.875,1]]})
print(json.dumps(out))
`;
const p=spawnSync('python',['-c',py],{cwd:root,encoding:'utf8',maxBuffer:8*1024*1024});assert.equal(p.status,0,p.stderr);const cases=JSON.parse(p.stdout),w=JSON.parse(fs.readFileSync(path.join(root,'dist/sources/programmed-clock-v0.1/PROGRAMMED_CLOCK_WITNESS_v0.1.json')));let phases=0,values=0;
for(const c of cases){const r=pc.parameters(w.branches[c.branch].specification,c.N,c.B,c.pad);assert.equal(r.n,c.n);assert.equal(r.K,c.K);assert.equal(r.dimension.toString(),c.dimension);for(const s of c.snapshots){const ps=pc.probabilities(c.n,s.xi);assert.equal(ps.length,s.clock_probabilities.length);assert.ok(Math.abs(ps.reduce((a,b)=>a+b,0)-1)<2e-12);ps.forEach((v,j)=>{assert.ok(Math.abs(v-s.clock_probabilities[j])<2e-12);values++});phases++}}
const html=fs.readFileSync(path.join(root,'dist/programmed-clock/index.html'),'utf8');for(const id of ['branch','ticks','resets','pad','phase','phase-label','prefix','verdict','clock-chart','probability','prefix-detail','probability-table','resource-table','metrics'])assert.ok(html.includes(`id="pc-${id}"`),id);
const receipt={status:'PASS',selector_cases:cases.length,phase_cases:phases,probability_values_compared:values,trace_probability_tolerance:2e-12,exact_bigint_dimensions:true,script_sha256:crypto.createHash('sha256').update(fs.readFileSync(path.join(root,'dist/assets/programmed-clock-v0.1.js'))).digest('hex'),scope:'Cross-language model formulas, selector parameter space and markup IDs; no rendered browser/accessibility certification or empirical clock.',physical_promotion:0};fs.writeFileSync(path.join(root,'dist/sources/programmed-clock-v0.1/PROGRAMMED_CLOCK_UI_VERIFICATION_v0.1.json'),JSON.stringify(receipt,null,2)+'\n');console.log(JSON.stringify(receipt));
