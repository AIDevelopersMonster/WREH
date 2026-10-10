#!/usr/bin/env python3
"""Fixed-membership review ZIP and SHA-256 manifest; not a Zenodo release."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
PREFIX = 'WREH_WR-V_v0.2_review/'
DRAFT = 'papers/WR-V/draft-v0.2/'
FILES = [
    DRAFT+'THEOREM_MAP.md',
    DRAFT+'REVISION_NOTES.md',
    DRAFT+'README.md',
    DRAFT+'WREH_WR-V_Draft_v0.2_EN.pdf',
    DRAFT+'WREH_WR-V_Draft_v0.2_RU.pdf',
    DRAFT+'WREH_WR-V_Draft_v0.2_EN.tex',
    DRAFT+'WREH_WR-V_Draft_v0.2_RU.tex',
    DRAFT+'wrv-preamble.tex',
    DRAFT+'wrv-body.tex',
    DRAFT+'WREH_WR-V_Demo_v0.2_EN-RU.html',
    DRAFT+'LICENSE-CONTENT.md',
    DRAFT+'LICENSE-CODE.txt',
    DRAFT+'LICENSES.md',
    DRAFT+'scripts/reproduce.py',
    DRAFT+'scripts/build.py',
    DRAFT+'scripts/verify_demo.cjs',
    DRAFT+'scripts/package.py',
    DRAFT+'verification.json',
    DRAFT+'build-verification.json',
    DRAFT+'demo-verification.json',
    DRAFT+'revision-verification.json',
    'reviews/WR-V/WREH_WR-V_Prior_Art_Preflight_v0.1.md',
    'reviews/WR-V/WREH_WR-V_Revision_Audit_v0.2_RU.md',
    'reviews/WR-V/REVIEW_REQUEST_v0.2.md',
    'reviews/WR-V/WREH_WR-V_Review_Response_v0.2_RU.md',
    'reviews/WR-IV/WREH_WR-IV_Post_Publication_Check_v0.6.md',
]
MANIFEST = DRAFT+'SHA256SUMS'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
        default=ROOT/'WREH_WR-V_Review_Package_v0.2_EN-RU.zip')
    args = parser.parse_args()
    payloads = {name:(REPO/name).read_bytes() for name in FILES}
    sums = {name:hashlib.sha256(data).hexdigest() for name,data in payloads.items()}
    manifest = ''.join(f'{sums[name]}  {name}\n' for name in FILES).encode()
    (REPO/MANIFEST).write_bytes(manifest)
    payloads[MANIFEST] = manifest
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED,
                         compresslevel=9) as archive:
        for name,data in payloads.items():
            info = zipfile.ZipInfo(PREFIX+name, date_time=(2026,10,9,0,0,0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info,data,compresslevel=9)
    with zipfile.ZipFile(output) as archive:
        assert archive.testzip() is None
        assert archive.namelist() == [PREFIX+name for name in payloads]
        for name,digest in sums.items():
            assert hashlib.sha256(archive.read(PREFIX+name)).hexdigest() == digest
    print(json.dumps({'status':'PASS','archive':str(output),
        'files':len(payloads),'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),
        'scope':'review draft; not publication ready'},indent=2))

if __name__ == '__main__':
    main()
