const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(const f of ['053-editorial','056-canvas','001-sheet']){await p.goto('file://'+process.cwd()+'/'+f+'.html');await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:f+'.png'})}await b.close()})()
