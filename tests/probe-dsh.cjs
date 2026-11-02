const path = require('node:path');
const {createRequire} = require('node:module');
const archive = process.argv[2];
const root = process.argv[3];
if(!archive || !root) throw new Error('Usage: probe-dsh.cjs <DSH app.asar> <skills directory> [output.json]');
const req = createRequire(path.join(archive,'dsh/package.json'));
const fs = require('node:fs');
const output = process.argv[4];
const {FileSystemSkillProvider} = req('@deepseek-ai/dsh-skill-filesystem');
const names=['scxrd-refinement','huangjt-computational-chemistry','huangjt-spectral-structure-analysis','organic-chemistry-reasoning','huangjt-academic-research','huangjt-academic-writing'];
(async()=>{
  const warnings=[];
  const control=new AbortController();
  const ctx={logger:{warn:s=>warnings.push(String(s))},get(){return undefined}};
  const provider=new FileSystemSkillProvider(ctx,{signal:control.signal,invalidate(){}},{includeDefaultRoots:false,customSkillDirs:[root],watch:false});
  try {
    const list=await provider.list({signal:control.signal});
    const candidates=Array.isArray(list)?list:list.candidates;
    const results=[];
    for(const name of names){
      const hits=candidates.filter(x=>x.name===name);
      if(hits.length!==1)throw new Error(`Expected one ${name}, found ${hits.length}`);
      const full=await provider.get(hits[0],{signal:control.signal});
      if(!full?.content || !full.invocation.modelInvocable)throw new Error(`Cannot load ${name}`);
      results.push({name,path:full.path,contentChars:full.content.length,modelInvocable:full.invocation.modelInvocable});
    }
    const result=JSON.stringify({loader:'Installed DSH FileSystemSkillProvider',root,results,warnings},null,2)+'\n';
    if(output) fs.writeFileSync(output,result);
    process.stdout.write(result);
  } finally {control.abort();await provider.dispose();}
})().catch(e=>{if(output)fs.writeFileSync(output,JSON.stringify({error:String(e.stack||e)}));process.stderr.write(String(e.stack||e)+'\n');process.exitCode=1});
