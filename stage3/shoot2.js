const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+process.cwd()+'/sketch.html');await p.evaluate(()=>document.fonts.ready);
for(let i=1;i<=7;i++){await (await p.$('#f'+i)).screenshot({path:'frame'+i+'.png'})}await b.close()})()
