const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:process.env.CHROME_PATH||'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 for(const file of ['mermail-pitch-deck.html','arc/index.html','ds2s/index.html','colosseum/index.html','rtc/index.html','suss2026/index.html','uii-sip-share/index.html']){
  const page=await browser.newPage({viewport:{width:1440,height:900},reducedMotion:'reduce'});
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.route('https://**/*',route=>route.abort());
  await page.goto(pathToFileURL(path.resolve(__dirname,'..',file)).href);
  const native=/^(rtc|suss2026|uii)/.test(file);
  const index=()=>page.evaluate(()=>typeof cur!=='undefined'?cur:typeof current!=='undefined'?current:Array.from(document.querySelectorAll('.slide')).reduce((found,s,i)=>s.offsetTop<=scrollY+innerHeight*.35?i:found,0));
  await page.locator('.slide').first().click({position:{x:20,y:120}});
  await page.waitForTimeout(150);
  assert.equal(await index(),1,`${file}: body click`);
  if(!native) await page.mouse.wheel(0,100);await page.waitForTimeout(100);
  if(!native){assert.equal(await index(),2,`${file}: wheel next`);await page.evaluate(()=>{for(let i=0;i<4;i++)document.body.dispatchEvent(new WheelEvent('wheel',{deltaY:80,bubbles:true,cancelable:true}));});assert.equal(await index(),2,`${file}: inertia`);await page.waitForTimeout(700);await page.mouse.wheel(0,-100);await page.waitForTimeout(100);assert.equal(await index(),1,`${file}: wheel previous`);}
  await page.evaluate(()=>{const s=document.querySelector('.slide.active')||document.querySelectorAll('.slide')[1];const a=document.createElement('button');a.id='test-control';a.textContent='control';s.prepend(a)});
  const before=await index();await page.locator('#test-control').click();assert.equal(await index(),before,`${file}: control click`);
  await page.setViewportSize({width:390,height:844});
  await page.locator('#test-control').evaluate(el=>el.remove());
  await page.evaluate(()=>{const s=document.querySelector('.slide.active')||document.querySelectorAll('.slide')[1];s.dispatchEvent(new TouchEvent('touchstart',{touches:[new Touch({identifier:1,target:s,clientX:300,clientY:200})],bubbles:true}));s.dispatchEvent(new TouchEvent('touchend',{changedTouches:[new Touch({identifier:1,target:s,clientX:100,clientY:200})],bubbles:true}));});
  await page.waitForTimeout(150);
  assert.equal(await index(),before+1,`${file}: mobile swipe`);
  assert.deepEqual(errors,[],file);console.log('PASS '+file);await page.close();
 }
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
