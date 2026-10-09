#!/usr/bin/env python3
"""Check bilingual mathematical alignment and release metadata, not proof validity."""
from pathlib import Path
import re,json
ROOT=Path(__file__).resolve().parents[1]
def group(s,i):
    assert s[i]=='{';depth=1;j=i+1
    while depth:
        if s[j]=='{' and s[j-1]!='\\':depth+=1
        elif s[j]=='}' and s[j-1]!='\\':depth-=1
        j+=1
    return s[i+1:j-1],j
def select(s,lang):
    out='';i=0
    while i<len(s):
        if s.startswith('\\Lang',i):
            j=i+5
            while s[j].isspace():j+=1
            a,j=group(s,j)
            while s[j].isspace():j+=1
            b,j=group(s,j);out+=select(a if lang=='en' else b,lang);i=j
        else:out+=s[i];i+=1
    return out
def main():
    body=(ROOT/'wrix-body.tex').read_text();texts={l:select(body,l) for l in ['en','ru']}
    inline={l:re.findall(r'\$(.*?)\$',v,re.S) for l,v in texts.items()}
    assert inline['en']==inline['ru'],'Parallel inline mathematics differs'
    assert body.count('\\begin{proof}')==body.count('\\end{proof}')==8
    assert body.count('\\begin{equation}')==12
    labels=re.findall(r'\\label\{([^}]+)\}',body);assert len(labels)==len(set(labels))==32
    meta=json.loads((ROOT/'zenodo_metadata.json').read_text());assert meta['version']=='0.1' and 'doi' not in meta
    assert meta['creators'][0]['orcid']=='0009-0008-6009-3196'
    provenance=json.loads((ROOT/'SOURCE_PROVENANCE.json').read_text());assert provenance['source_base_commit']=='3963c3b71f464b7de85750fd4a51d680943d5162'
    report={'status':'PASS','proof_blocks':8,'numbered_equations':12,'source_labels':32,'inline_math_expressions':len(inline['en']),'parallel_inline_math':'IDENTICAL','claim_ceiling':'declared observer protocols; ideal kinematics and detector','upstream_snapshot':provenance['source_base_commit'],'frozen_upstream_preservation':'Verified separately by Git tree comparison before commit','wr_ix_doi':None}
    (ROOT/'architecture-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
