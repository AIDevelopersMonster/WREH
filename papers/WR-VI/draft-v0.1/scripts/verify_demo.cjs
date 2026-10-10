/* MIT License; Copyright (c) 2026 A. A. Malachevsky. */
'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),os=require('node:os');
const {pathToFileURL}=require('node:url');
const playwright=require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES?path.join(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES,'playwright'):'playwright');
(async()=>{
 const root=path.resolve(__dirname,'..');
 const qa=process.env.WRVI_QA_DIR||fs.mkdtempSync(path.join(os.tmpdir(),'wreh-wrvi-qa-'));
 fs.mkdirSync(qa,{recursive:true});
 const browser=await playwright.chromium.launch({headless:true,args:['--no-sandbox'],...(process.env.WRVI_BROWSER?{executablePath:process.env.WRVI_BROWSER}:{})});
 try{
  const page=await browser.newPage({viewport:{width:1360,height:1100}});
  const errors=[],requests=[];page.on('pageerror',e=>errors.push(e.message));page.on('request',r=>{if(/^https?:/.test(r.url()))requests.push(r.url());});
  await page.goto(pathToFileURL(path.join(root,'WREH_WR-VI_Demo_v0.1_EN-RU.html')).href);
  const cases=await page.evaluate(()=>{
   let count=0;
   for(const units of [0,90,99,100,101,150,400,600])for(const delta of [0,1,20,60])for(const strict of [false,true])for(const pos of [0,500,1000]){
    document.getElementById('cap').value=units;document.getElementById('delta').value=delta;
    document.getElementById('irreducible').checked=strict;document.getElementById('position').value=pos;WRVI.update();
    const cap=units/600,minus=Math.max(0,cap-delta/600),plus=cap+delta/600;
    const all=WRVI.interval(minus,strict),some=WRVI.interval(plus,strict);
    const expected=v=>v<1/6-1e-12||(strict&&v<=1/6+1e-12)?'empty':Math.abs(v-1/6)<1e-12?'one':'many';
    if(all.kind!==expected(minus)||some.kind!==expected(plus))throw Error('Wrong cardinality');
    if(!some.empty){
     const displayed=Array.from(document.querySelectorAll('#matrix span'),el=>Number(el.textContent));
     if(displayed.length!==9||displayed.some(v=>v< -1e-4))throw Error('Invalid matrix');
     for(let i=0;i<3;i++){
      if(Math.abs(displayed.slice(3*i,3*i+3).reduce((a,b)=>a+b,0)-1)>0.0002)throw Error('Row sum');
      const q=displayed[3*i+1]/2+displayed[3*i+2];
      if(Math.abs(q-[.25,.5,.75][i])>0.0002)throw Error('Wrong response');
     }
     for(let i=0;i<3;i++)for(let j=0;j<3;j++)if(displayed[3*i+j]!==displayed[3*j+i])throw Error('Asymmetric');
     const alpha=(displayed[1]+displayed[2]+displayed[3]+displayed[5]+displayed[6]+displayed[7])/3;
     if(alpha>plus+0.0002)throw Error('Cap violated');
    }else if(document.querySelectorAll('#matrix span').length)throw Error('Candidate in empty class');
    count++;
   }
   return count;
  });
  const set=async(cap,delta,strict)=>page.evaluate(args=>{
   document.getElementById('cap').value=args.cap;document.getElementById('delta').value=args.delta;
   document.getElementById('irreducible').checked=args.strict;document.getElementById('position').value=500;WRVI.update();
  },{cap,delta,strict});
  await set(100,20,false);await page.screenshot({path:path.join(qa,'desktop-ru.png'),fullPage:true});
  await page.locator('#language').click();assert.equal(await page.locator('html').getAttribute('lang'),'en');
  await page.screenshot({path:path.join(qa,'desktop-en.png'),fullPage:true});
  await page.locator('#cap').focus();await page.keyboard.press('Home');assert.equal((await page.evaluate(()=>WRVI.getState())).cap,0);
  await page.keyboard.press('End');assert.equal((await page.evaluate(()=>WRVI.getState())).cap,1);
  await set(100,0,false);await page.locator('button[data-cap="100"]').click();assert.match(await page.locator('#classText').textContent(),/one matrix/);
  await set(150,0,true);await page.setViewportSize({width:390,height:844});
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  await page.screenshot({path:path.join(qa,'mobile-en.png'),fullPage:true});await page.locator('#language').click();
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  await page.screenshot({path:path.join(qa,'mobile-ru.png'),fullPage:true});
  assert.deepEqual(errors,[]);assert.deepEqual(requests,[]);
  const report={status:'PASS',constraint_cases:cases,languages:['ru','en'],viewport_checks:['desktop 1360px','mobile 390px'],keyboard:'PASS',javascript_errors:errors,external_page_requests:requests,browser:await browser.version(),visual_review:'PENDING'};
  fs.writeFileSync(path.join(root,'demo-verification.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify({...report,qa_directory:qa},null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
