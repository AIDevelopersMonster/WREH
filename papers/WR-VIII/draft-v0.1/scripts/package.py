#!/usr/bin/env python3
"""Fixed-membership bilingual WR-VIII review archive; no VIII publication assertion."""
from pathlib import Path
import argparse,hashlib,json,zipfile
ROOT=Path(__file__).resolve().parents[1];REPO=ROOT.parents[2]
DRAFT='papers/WR-VIII/draft-v0.1/';PREFIX='WREH_WR-VIII_v0.1_review/'
FILES=[DRAFT+n for n in [
 'README.md','THEOREM_MAP.md','CITATION.cff','zenodo_metadata.json','PREPRINT_DEPOSIT.md',
 'WREH_WR-VIII_Draft_v0.1_EN.pdf','WREH_WR-VIII_Draft_v0.1_RU.pdf',
 'WREH_WR-VIII_Draft_v0.1_EN.tex','WREH_WR-VIII_Draft_v0.1_RU.tex','wrviii-preamble.tex','wrviii-body.tex',
 'WREH_WR-VIII_Demo_v0.1_EN-RU.html','figures/distance-fibre.pdf','figures/distance-fibre.png',
 'figures/refinement-lifts.pdf','figures/refinement-lifts.png','LICENSE-CONTENT.md','LICENSE-CODE.txt','LICENSES.md',
 'scripts/build.py','scripts/reproduce.py','scripts/figure.py','scripts/verify_demo.cjs','scripts/package.py',
 'verification.json','build-verification.json','demo-verification.json','architecture-verification.json']]+[
 'reviews/WR-VIII/WREH_WR-VIII_Source_Preflight_v0.1.md',
 'reviews/WR-VIII/WREH_WR-VIII_Technical_Audit_v0.1_RU.md','reviews/WR-VIII/REVIEW_REQUEST_v0.1.md',
 'reviews/WR-VII/WREH_WR-VII_Post_Publication_Check_2026-10-09.md',
 'papers/WR-VII/publication/publication-verification-2026-10-09.json']
MANIFEST=DRAFT+'SHA256SUMS'
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=ROOT/'WREH_WR-VIII_Review_Package_v0.1_EN-RU.zip');args=ap.parse_args()
 assert len(FILES)==len(set(FILES)) and MANIFEST not in FILES
 payload={n:(REPO/n).read_bytes() for n in FILES};sums={n:hashlib.sha256(b).hexdigest() for n,b in payload.items()}
 manifest=''.join(f'{sums[n]}  {n}\n' for n in FILES).encode();(REPO/MANIFEST).write_bytes(manifest);payload[MANIFEST]=manifest
 output=args.output.resolve();output.parent.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for n,b in payload.items():
   info=zipfile.ZipInfo(PREFIX+n,(2026,10,9,0,0,0));info.create_system=3;info.external_attr=0o100644<<16;info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,b,compresslevel=9)
 with zipfile.ZipFile(output) as z:
  assert z.testzip() is None and z.namelist()==[PREFIX+n for n in payload]
  for n,digest in sums.items():assert hashlib.sha256(z.read(PREFIX+n)).hexdigest()==digest
 print(json.dumps({'status':'PASS','files':len(payload),'content_files':len(sums),'archive':str(output),'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'scope':'WR-VIII REVIEWABLE_DRAFT; no VIII DOI or deposit; VII publication author-reported, direct check pending'},indent=2))
if __name__=='__main__':main()
