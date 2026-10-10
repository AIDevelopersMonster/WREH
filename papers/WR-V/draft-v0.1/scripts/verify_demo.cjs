/* MIT License; Copyright (c) 2026 A. A. Malachevsky. */
'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const os=require('node:os');
const {pathToFileURL}=require('node:url');
const playwright=require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES
  ?path.join(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES,'playwright'):'playwright');
(async()=>{
 const root=path.resolve(__dirname,'..');
 const qa=process.env.WRV_QA_DIR||fs.mkdtempSync(path.join(os.tmpdir(),'wreh-wrv-qa-'));
 fs.mkdirSync(qa,{recursive:true});
 const browser=await playwright.chromium.launch({headless:true,args:['--no-sandbox'],
  ...(process.env.WRV_BROWSER?{executablePath:process.env.WRV_BROWSER}:{})});
 try{
  const page=await browser.newPage({viewport:{width:1360,height:1100}});
  const errors=[],external=[];
  page.on('pageerror',e=>errors.push(e.message));
  page.on('request',r=>{if(/^https?:/.test(r.url()))external.push(r.url());});
  await page.goto(pathToFileURL(path.join(root,'WREH_WR-V_Demo_v0.1_EN-RU.html')).href);
  const configure=async(m,u,epsilon,second)=>page.evaluate(args=>{
   for(const [id,v] of Object.entries(args)){
    const el=document.getElementById(id);
    if(id==='second')el.checked=v;else el.value=v;
    el.dispatchEvent(new Event('input',{bubbles:true}));
   }
   return {model:window.wrehModel.getModel(),kind:document.getElementById('status').dataset.kind};
  },{m,position:u,epsilon,second});
  assert.equal(await page.locator('#status').getAttribute('data-kind'),'class');
  assert.equal((await configure(0,0,0,false)).kind,'unique');
  assert.equal((await configure(0,0,.01,false)).kind,'class');
  assert.equal((await configure(1,0,.05,false)).kind,'class');
  assert.equal((await configure(1,0,.05,true)).kind,'unique');
  const mix=await configure(.5,1,0,false);
  assert.deepEqual(mix.model.k,[.5,0,.5]);assert.equal(mix.kind,'class');
  assert.equal((await configure(.5,1,0,true)).kind,'unique');
  assert.equal((await configure(.5,0,.1,true)).kind,'class');
  const geometryCases=await page.evaluate(()=>{
   let count=0;
   for(let i=0;i<=10;i++)for(const epsilon of [0,.01,.1])
    for(const u of [0,.4,1])for(const second of [false,true]){
     for(const [id,value] of Object.entries({m:i/10,position:u,epsilon,second})){
      const el=document.getElementById(id);
      if(id==='second')el.checked=value;else el.value=value;
      el.dispatchEvent(new Event('input',{bubbles:true}));
     }
     const z=window.wrehModel.getModel(),a=[0,.5,1];
     if(z.k.some(v=>v< -1e-9)||Math.abs(z.k.reduce((s,v)=>s+v,0)-1)>1e-9)
      throw Error('Invalid candidate');
     if(Math.abs(.5*z.k[1]+z.k[2]-z.m)>1e-9)throw Error('Wrong response');
     let poly=[[1,0,0],[0,1,0],[0,0,1]];
     poly=window.wrehModel.clip(poly,a,z.m+z.epsilon);
     poly=window.wrehModel.clip(poly,a.map(v=>-v),-z.m+z.epsilon);
     if(second){poly=window.wrehModel.clip(poly,[0,0,1],z.t);
      poly=window.wrehModel.clip(poly,[0,0,-1],-z.t);}
     if(!poly.length)throw Error('Empty feasible geometry');
     for(const k of poly){
      if(k.some(v=>v< -1e-8)||Math.abs(k.reduce((s,v)=>s+v,0)-1)>1e-8)
       throw Error('Invalid region vertex');
      if(Math.abs(.5*k[1]+k[2]-z.m)>z.epsilon+1e-8)throw Error('Region outside response band');
      if(second&&Math.abs(k[2]-z.t)>1e-8)throw Error('Region violates second probe');
     }
     count++;
    }
   return count;
  });
  await configure(.5,.5,.05,false);
  await page.screenshot({path:path.join(qa,'desktop-ru.png'),fullPage:true});
  await page.locator('#lang').click();
  assert.equal(await page.locator('html').getAttribute('lang'),'en');
  assert.match(await page.locator('#title').textContent(),/experiment/);
  await page.screenshot({path:path.join(qa,'desktop-en.png'),fullPage:true});
  await page.locator('#m').focus();await page.keyboard.press('Home');
  assert.equal((await page.evaluate(()=>window.wrehModel.getModel())).m,0);
  await page.keyboard.press('End');
  assert.equal((await page.evaluate(()=>window.wrehModel.getModel())).m,1);
  await configure(.5,.5,.02,true);
  await page.setViewportSize({width:390,height:844});
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  await page.screenshot({path:path.join(qa,'mobile-en.png'),fullPage:true});
  await page.locator('#lang').click();
  await page.screenshot({path:path.join(qa,'mobile-ru.png'),fullPage:true});
  assert.deepEqual(errors,[]);assert.deepEqual(external,[]);
  const report={status:'PASS',geometry_cases:geometryCases,languages:['ru','en'],
   viewport_checks:['desktop 1360px','mobile 390px'],keyboard:'PASS',
   javascript_errors:errors,external_page_requests:external,
   browser:await browser.version(),visual_review:'PENDING'};
  fs.writeFileSync(path.join(root,'demo-verification.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify({...report,qa_directory:qa},null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
