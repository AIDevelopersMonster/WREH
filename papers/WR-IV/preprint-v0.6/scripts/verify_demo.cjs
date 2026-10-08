/* MIT License; Copyright (c) 2026 A. A. Malachevsky.
 * Browser QA for the offline bilingual demonstration. Requires Playwright.
 * Set WRIV_BROWSER to a compatible Chromium executable if needed.
 */
'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
const playwright=require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES
  ?path.join(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES,'playwright'):'playwright');
let launchedBrowser;
(async()=>{
  const root=path.resolve(__dirname,'..');
  const qa=path.join(root,'qa');fs.mkdirSync(qa,{recursive:true});
  const browser=await playwright.chromium.launch({headless:true,
    ...(process.env.WRIV_BROWSER?{executablePath:process.env.WRIV_BROWSER}:{}),args:['--no-sandbox']});
  launchedBrowser=browser;
  const page=await browser.newPage({viewport:{width:1400,height:1100}});
  const errors=[],external=[];
  page.on('pageerror',e=>errors.push(e.message));
  page.on('request',r=>{if(/^https?:/.test(r.url()))external.push(r.url());});
  await page.goto(pathToFileURL(path.join(root,'WREH_WR-IV_Demo_v0.6_EN-RU.html')).href);
  assert.equal(await page.locator('#postVar').textContent(),'0.24');
  assert.equal(await page.locator('#postMean').textContent(),'1.5');
  const core=await page.evaluate(()=>{
    const exact=WRIV.marginal(0,.5,1,.6,2.5,0),noisy=WRIV.marginal(0,.5,1,.6,2.5,.5);
    const bridges=WRIV.paths(0,.5,1,2.5,0,20261008,20,20);
    const rows=WRIV.paths(0,.5,1,2.5,.5,20261008,25000,20);
    const states=rows.map(r=>r[12]),mean=states.reduce((a,b)=>a+b,0)/states.length;
    const variance=states.reduce((a,b)=>a+(b-mean)**2,0)/states.length;
    return {exact,noisy,endpoints:bridges.map(r=>r.at(-1)),mean,variance,
      branches:WRIV.branchChains(.3,5,'01').length,
      zero:WRIV.marginal(0,.5,1,0,2.5,0).variance,
      terminal:WRIV.marginal(0,.5,1,1,2.5,0).variance};
  });
  assert(Math.abs(core.exact.variance-.24)<1e-12);
  assert(Math.abs(core.noisy.variance-.36)<1e-12);
  assert(Math.abs(core.noisy.mean-1)<1e-12);
  assert(core.endpoints.every(v=>Math.abs(v-2.5)<1e-12));
  assert(Math.abs(core.mean-1)<.02&&Math.abs(core.variance-.36)<.02);
  assert.equal(core.branches,8);assert.equal(core.zero,0);assert.equal(core.terminal,0);
  await page.screenshot({path:path.join(qa,'demo-en-exact.png'),fullPage:true});
  await page.locator('#mode').selectOption('noisy');
  assert.equal(await page.locator('#postVar').textContent(),'0.36');
  await page.locator('#language').click();
  assert.equal(await page.locator('html').getAttribute('lang'),'ru');
  await page.screenshot({path:path.join(qa,'demo-ru-noisy.png'),fullPage:true});
  for(const panel of ['doubling','gate','walls']){
    await page.locator('#tab-'+panel).click();
    assert(await page.locator('#'+panel).isVisible());
    if(panel==='doubling')assert((await page.locator('#branchCount').textContent()).startsWith('8 '));
    if(panel==='walls'){
      await page.locator('#endpoint').click();
      assert((await page.locator('#wallStatus').textContent()).includes('стена'));
      await page.locator('#interior').click();
      assert((await page.locator('#wallStatus').textContent()).includes('окружность'));
    }
    await page.screenshot({path:path.join(qa,'demo-ru-'+panel+'.png'),fullPage:true});
  }
  await page.locator('#tab-diffusion').click();
  await page.locator('#tab-diffusion').focus();await page.keyboard.press('ArrowRight');
  assert.equal(await page.locator('#tab-doubling').getAttribute('aria-selected'),'true');
  await page.setViewportSize({width:390,height:844});
  await page.locator('#tab-diffusion').click();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
  await page.screenshot({path:path.join(qa,'demo-mobile-ru.png'),fullPage:true});
  const translations=await page.evaluate(()=>[...document.querySelectorAll('[data-i]')].map(e=>e.textContent));
  assert(translations.every(t=>t.trim().length));
  assert.deepEqual(errors,[]);assert.deepEqual(external,[]);
  const result={result:'passed',runtime_errors:errors,external_page_requests:external,
    viewport_checks:['1400x1100','390x844'],languages:['en','ru'],core_check:core,
    sampled_law_check:'Seeded marginal mean and variance within specified tolerances; illustration only'};
  fs.writeFileSync(path.join(root,'demo-verification.json'),JSON.stringify(result,null,2)+'\n');
  console.log(JSON.stringify({result:result.result,runtime_errors:errors.length,external_requests:external.length,
    sampled_mean:core.mean,sampled_variance:core.variance,compatible_depth5_chains:core.branches}));
  await browser.close();
})().catch(async e=>{if(launchedBrowser)await launchedBrowser.close();console.error(e);process.exitCode=1;});
