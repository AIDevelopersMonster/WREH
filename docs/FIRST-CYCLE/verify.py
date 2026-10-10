#!/usr/bin/env python3
"""Verify first-cycle integration and frozen content; no scientific peer-review claim."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

REPO=Path(__file__).resolve().parents[2]
ROOT=Path(__file__).resolve().parent
BASELINE='63e2888dc732f558ded2ea058cccc7dc2a691097'

def git(*args):
    return subprocess.check_output(['git',*args],cwd=REPO)

def frozen(path):
    parts=Path(path).parts
    if parts[0]=='demos':return True
    if parts[:2]==('docs','WREH-00'):return True
    if parts[0]!='papers':return False
    if len(parts)==3:return Path(path).suffix in {'.tex','.pdf'}
    return len(parts)>3 and (parts[2].startswith(('draft-','preprint-')) or parts[2] in {'demo','figures'})

def main():
    paths=[p for p in git('ls-tree','-r','--name-only',BASELINE).decode().splitlines() if frozen(p)]
    unchanged=[]
    for p in paths:
        assert (REPO/p).read_bytes()==git('show',BASELINE+':'+p),'Frozen content changed: '+p
        unchanged.append(p)
    entries=[]
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        sha,p=line.split('  ',1)
        assert p in paths,'Unexpected manifest member: '+p
        assert hashlib.sha256((REPO/p).read_bytes()).hexdigest()==sha,'Hash mismatch: '+p
        entries.append(p)
    assert set(entries)==set(paths) and len(entries)==len(paths)
    manifests=[]
    for m in sorted(REPO.glob('papers/**/SHA256SUM*')):
        original=git('log','-1','--format=%H',BASELINE,'--',str(m.relative_to(REPO))).decode().strip()
        local=historical=0
        for line in m.read_text().splitlines():
            fields=line.split(maxsplit=1)
            if len(fields)!=2 or not re.fullmatch(r'[0-9a-f]{64}',fields[0]):continue
            expected,p=fields[0],fields[1].lstrip('*')
            target=m.parent/p
            if not target.exists():target=REPO/p
            rel=str(target.relative_to(REPO))
            within=target.is_relative_to(m.parent)
            if within:
                assert hashlib.sha256(target.read_bytes()).hexdigest()==expected,'Frozen version mismatch: '+rel
                local+=1
            else:
                assert hashlib.sha256(git('show',original+':'+rel)).hexdigest()==expected,'Historical manifest mismatch: '+rel
                historical+=1
        manifests.append({'path':str(m.relative_to(REPO)),'original_commit':original,'version_local_checks':local,'historical_snapshot_checks':historical,'status':'PASS'})
    refs=[r for r in git('for-each-ref','--format=%(refname)','refs/remotes/origin').decode().splitlines() if not r.endswith('/HEAD')]
    branch_status=[]
    for ref in refs:
        ahead=int(git('rev-list','--count','HEAD..'+ref).decode())
        assert ahead==0,'Unmerged remote branch: '+ref
        branch_status.append({'branch':ref.removeprefix('refs/remotes/'),'head':git('rev-parse',ref).decode().strip(),'commits_outside_main':ahead})
    docs=[REPO/'README.md',REPO/'registry/PROGRAMME_REGISTER.md',ROOT/'README.md',*sorted(REPO.glob('papers/WR-*/README.md'))]
    count=0
    for p in docs:
        for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
            if link.startswith(('http:','https:','mailto:','#')):continue
            target=link.split('#',1)[0]
            if target:
                assert (p.parent/target).exists(),f'Broken link: {p.relative_to(REPO)} -> {target}'
                count+=1
    registry=json.loads((REPO/'registry/FIRST_CYCLE_PUBLICATIONS.json').read_text())
    assert len(registry['articles'])==9
    for article in registry['articles']:
        assert article['status']=='PUBLISHED_FROZEN'
        cff=(REPO/'papers'/article['code']/'CITATION.cff').read_text()
        assert article['doi'] in cff,'Missing DOI citation: '+article['code']
    report={'status':'PASS','baseline':BASELINE,'frozen_files_identical':len(unchanged),'integration_manifest_entries':len(entries),'historical_manifests':manifests,'branches':branch_status,'relative_links_checked':count,'publication_entries':9,'proofs_changed':False,'review_type':'Repository integration and publication identity checks; not independent external scientific peer review'}
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
