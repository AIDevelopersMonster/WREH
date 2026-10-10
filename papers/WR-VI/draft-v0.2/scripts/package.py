#!/usr/bin/env python3
"""Fixed-membership WR-VI review archive; no Zenodo publication claim."""
from pathlib import Path
import argparse,hashlib,json,zipfile

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[2]
DRAFT='papers/WR-VI/draft-v0.2/'
PREFIX='WREH_WR-VI_v0.2_review/'
FILES=[DRAFT+n for n in [
 'README.md','THEOREM_MAP.md','WREH_WR-VI_Draft_v0.2_EN.pdf',
 'WREH_WR-VI_Draft_v0.2_RU.pdf','WREH_WR-VI_Draft_v0.2_EN.tex',
 'WREH_WR-VI_Draft_v0.2_RU.tex','wrvi-preamble.tex','wrvi-body.tex',
 'WREH_WR-VI_Demo_v0.2_EN-RU.html','LICENSE-CONTENT.md','LICENSE-CODE.txt',
 'LICENSES.md','scripts/build.py','scripts/reproduce.py','scripts/verify_demo.cjs',
 'scripts/package.py','verification.json','build-verification.json',
 'demo-verification.json','architecture-verification.json']]+[
 'reviews/WR-VI/WREH_WR-VI_Prior_Art_Preflight_v0.1.md',
 'reviews/WR-VI/WREH_WR-VI_Technical_Audit_v0.2_RU.md',
 'reviews/WR-VI/REVIEW_REQUEST_v0.2.md',
 'reviews/WR-VI/WREH_WR-VI_Response_to_Review_v0.2_RU.md']
MANIFEST=DRAFT+'SHA256SUMS'

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--output',type=Path,default=ROOT/'WREH_WR-VI_Review_Package_v0.2_EN-RU.zip')
 args=ap.parse_args()
 payload={n:(REPO/n).read_bytes() for n in FILES}
 sums={n:hashlib.sha256(b).hexdigest() for n,b in payload.items()}
 manifest=''.join(f'{sums[n]}  {n}\n' for n in FILES).encode()
 (REPO/MANIFEST).write_bytes(manifest);payload[MANIFEST]=manifest
 output=args.output.resolve();output.parent.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as a:
  for n,b in payload.items():
   info=zipfile.ZipInfo(PREFIX+n,date_time=(2026,10,9,0,0,0))
   info.create_system=3;info.external_attr=0o100644<<16;info.compress_type=zipfile.ZIP_DEFLATED
   a.writestr(info,b,compresslevel=9)
 with zipfile.ZipFile(output) as a:
  assert a.testzip() is None and a.namelist()==[PREFIX+n for n in payload]
  for n,digest in sums.items(): assert hashlib.sha256(a.read(PREFIX+n)).hexdigest()==digest
 print(json.dumps({'status':'PASS','files':len(payload),'archive':str(output),
  'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'scope':'review draft; not publication ready'},indent=2))

if __name__=='__main__': main()
