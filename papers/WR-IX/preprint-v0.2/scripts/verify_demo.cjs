const fs=require('fs'),path=require('path');const {chromium}=require('playwright');
(async()=>{
 const root=path.resolve(__dirname,'..'),errors=[],requests=[];
 const browser=await chromium.launch({executablePath:process.env.WREH_CHROME_PATH||chromium.executablePath(),headless:true,args:['--no-sandbox']});
 const page=await browser.newPage();page.on('pageerror',e=>errors.push(e.message));page.on('request',r=>{if(!r.url().startsWith('file:'))requests.push(r.url())});
 await page.goto('file://'+path.join(root,'WREH_WR-IX_Demo_v0.2_EN-RU.html'));let scenarios=0;
 for(const viewport of [{width:1360,height:1024},{width:390,height:844}]){
  await page.setViewportSize(viewport);
  for(let language=0;language<2;language++){
   for(const x of [.05,.5,.9,1,1.2])for(const u of [0,.69,1,4,8])for(const e of [0,.5,1,2,20]){
    const r=await page.evaluate(({x,u,e})=>{for(const [id,v] of [['period',x],['deadline',u],['energy',e]])document.getElementById(id).value=v;window.WREH.render();return window.WREH.compute(x,u,e)},{x,u,e});
    if(x<1){
     // Simpson integration independently verifies the inverse span at the returned time.
     let sum=0,n=800;for(let j=0;j<=n;j++)sum+=(j===0||j===n?1:j%2?4:2)*Math.exp(-r.time*j/n);
     if(Math.abs(sum*r.time/(3*n)-x)>2e-10)throw Error('span inverse');
     if(Math.abs(e*Math.exp(-r.time)-e/r.need)>1e-10)throw Error('arrival redshift');
     const detectable=u>=r.time&&e*Math.exp(-r.time)>=1;
     if((r.kind==='detected')!==detectable)throw Error('detectability');
    }else if(r.kind!=='causal')throw Error('strict causal cap');
    const ui=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth,text:document.getElementById('verdict').textContent,empty:[...document.querySelectorAll('[data-key]')].some(e=>!e.textContent)}));
    if(ui.overflow||ui.empty||!ui.text||ui.text==='undefined')throw Error('UI content or overflow');scenarios++;
   }
   await page.locator('#language').click();
  }
 }
 const boundary=await page.evaluate(()=>window.WREH.compute(.5,Math.log(2),2));if(boundary.kind!=='detected')throw Error('double equality');scenarios++;
 for(const bad of [[0,1,2],[-1,1,2],[.5,-1,2],[.5,1,-1]]){const rejected=await page.evaluate(v=>{try{window.WREH.compute(...v);return false}catch{return true}},bad);if(!rejected)throw Error('domain not rejected');scenarios++}
 const dest=process.env.WREH_SCREENSHOT_DIR;if(dest)fs.mkdirSync(dest,{recursive:true});
 await page.evaluate(()=>{document.getElementById('period').value=.5;document.getElementById('deadline').value=1;document.getElementById('energy').value=3;window.WREH.render()});
 for(const [width,height,tag] of [[1360,1024,'desktop'],[390,844,'mobile']]){await page.setViewportSize({width,height});if(dest)await page.screenshot({path:path.join(dest,tag+'-ru.png'),fullPage:true});await page.locator('#language').click();if(dest)await page.screenshot({path:path.join(dest,tag+'-en.png'),fullPage:true});await page.locator('#language').click()}
 await browser.close();if(errors.length||requests.length)throw Error(JSON.stringify({errors,requests}));
 const report={status:'PASS',scenarios,languages:['EN','RU'],viewports:['1360x1024','390x844'],page_errors:errors,external_requests:requests,horizontal_overflow:false,independent_span_check:'Simpson integration, 800 intervals',visual_review:'PENDING'};
 fs.writeFileSync(path.join(root,'demo-verification.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report,null,2));
})().catch(e=>{console.error(e);process.exit(1)});
