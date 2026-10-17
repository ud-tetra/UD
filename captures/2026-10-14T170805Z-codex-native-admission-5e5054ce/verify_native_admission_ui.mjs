import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
import {spawnSync} from 'node:child_process';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
const root=path.dirname(fileURLToPath(import.meta.url)),require=createRequire(import.meta.url),na=require('./dist/assets/native-admission-v0.1.js');
const py=String.raw`
import json,math
from native_admission import optimize,CLASSES
rows=[]
for n in [2,4,6,8,10,12]:
 for c,info in CLASSES.items():
  cert=optimize(n,c);sq=info['squared_positive_frequencies'];ratio=math.sqrt(sq[0]/sq[-1]) if len(sq)>1 else None
  scales=[2*n*i/40 for i in range(41)]+[i[k]['decimal_display'] for i in cert['optimal_high_centre_intervals'] for k in ['min','max']]
  for y in scales:
   centres=[0]+([ratio*y] if ratio else [])+[y]
   b=max(min(abs(p-s) for s in centres) for p in range(2,n+1,2))
   rows.append({'n':n,'c':c,'y':y,'b':b,'certified_min':cert['minimum_relative_spectral_floor']['decimal_display']})
print(json.dumps(rows))
`;
const p=spawnSync('python',['-c',py],{cwd:root,encoding:'utf8',maxBuffer:4*1024*1024});assert.equal(p.status,0,p.stderr);const rows=JSON.parse(p.stdout);let gapValues=0;
for(const x of rows){const r=na.compare(x.n,x.c,x.y);assert.ok(Math.abs(r.relative_floor-x.b)<2e-12);assert.ok(r.relative_floor+2e-12>=x.certified_min);assert.equal(r.rows.length,x.n/2);gapValues+=r.rows.length}
const html=fs.readFileSync(path.join(root,'dist/native-admission/index.html'),'utf8');for(const id of ['class','length','scale','scale-label','best','verdict','spectrum','summary','gaps','certificates','alias'])assert.ok(html.includes(`id="na-${id}"`),id);
const receipt={status:'PASS',native_class_length_combinations:18,comparison_scale_cases:rows.length,positive_frequency_gaps_compared:gapValues,numeric_tolerance:2e-12,script_sha256:crypto.createHash('sha256').update(fs.readFileSync(path.join(root,'dist/assets/native-admission-v0.1.js'))).digest('hex'),scope:'Cross-language spectral calculator, exact-certificate floor checks and markup IDs; no rendered browser/accessibility or empirical validation.',physical_promotion:0};fs.writeFileSync(path.join(root,'dist/sources/native-admission-v0.1/NATIVE_ADMISSION_UI_VERIFICATION_v0.1.json'),JSON.stringify(receipt,null,2)+'\n');console.log(JSON.stringify(receipt));
