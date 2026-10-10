#!/usr/bin/env python3
"""Create a fixed-membership review archive and check every contained SHA-256."""
from pathlib import Path
import argparse,hashlib,json,zipfile,shutil
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[2]
PREFIX='WREH_WR-IX_v0.2_publication/'
def included_files():
    entries=[]
    for p in sorted(ROOT.rglob('*')):
        if p.is_file() and '__pycache__' not in p.parts and p.name!='SHA256SUMS':
            assert p.suffix in {'.md','.tex','.pdf','.png','.py','.cjs','.json','.txt','.cff','.html'},p
            entries.append(p)
    extras=[ROOT.parent/'README.md',ROOT.parent/'THEOREM_MAP.md',REPO/'reviews/WR-IX/WREH_WR-IX_Technical_Audit_v0.2_EN-RU.md',REPO/'reviews/WR-IX/REVIEW_REQUEST.md',REPO/'reviews/WR-IX/WREH_WR-IX_Reviewer_Response_v0.2_EN-RU.md',REPO/'reviews/WR-VIII/WREH_WR-VIII_Post_Publication_Check_v0.2.md',REPO/'reviews/WR-VIII/publication-verification-v0.2.json',REPO/'reviews/WR-V/WREH_WR-V_Post_Publication_Check_v0.3_2026-10-10.md',REPO/'reviews/WR-V/publication-verification-v0.3-2026-10-10.json',REPO/'reviews/WR-VII/WREH_WR-VII_Post_Publication_Check_v0.2_2026-10-10.md',REPO/'reviews/WR-VII/publication-verification-v0.2-2026-10-10.json']
    return entries+extras
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',required=True);args=ap.parse_args()
    dest=Path(args.output_dir).resolve();dest.mkdir(parents=True,exist_ok=True)
    for n in ['verification.json','adversarial-verification.json','architecture-verification.json','demo-verification.json']:
        assert json.loads((ROOT/n).read_text())['status']=='PASS',n
    for n in ['build-verification.json','demo-verification.json']:
        assert json.loads((ROOT/n).read_text())['visual_review']=='PASS',n
    paths=included_files();payload={str(p.relative_to(REPO)):p.read_bytes() for p in paths};assert len(payload)==len(paths)
    sums=''.join(hashlib.sha256(b).hexdigest()+'  '+n+'\n' for n,b in sorted(payload.items()))
    (ROOT/'SHA256SUMS').write_text(sums);payload[str((ROOT/'SHA256SUMS').relative_to(REPO))]=sums.encode()
    archive=dest/'WREH_WR-IX_Publication_Package_v0.2_EN-RU.zip'
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for n,b in sorted(payload.items()):
            info=zipfile.ZipInfo(PREFIX+n,date_time=(2026,10,10,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16;z.writestr(info,b)
    with zipfile.ZipFile(archive) as z:
        assert set(z.namelist())=={PREFIX+n for n in payload}
        for n,b in payload.items():assert z.read(PREFIX+n)==b
        for line in sums.splitlines():
            sha,n=line.split('  ',1);assert hashlib.sha256(z.read(PREFIX+n)).hexdigest()==sha
    for n in ['WREH_WR-IX_Preprint_v0.2_RU.pdf','WREH_WR-IX_Preprint_v0.2_EN.pdf','WREH_WR-IX_Demo_v0.2_EN-RU.html']:shutil.copy2(ROOT/n,dest/n)
    report={'status':'PASS','archive':archive.name,'files':len(payload),'sha256_entries':len(payload)-1,'exact_membership':True,'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'archive_bytes':archive.stat().st_size}
    (dest/'package-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
