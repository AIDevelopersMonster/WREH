#!/usr/bin/env python3
"""Package the fixed release file set. MIT; (c) 2026 A. A. Malachevsky."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = 'WREH_WR-IV_Zenodo_Package_v0.6_EN-RU.zip'
FILES = [
    'WREH_WR-IV_Preprint_v0.6_EN.pdf', 'WREH_WR-IV_Preprint_v0.6_RU.pdf',
    'WREH_WR-IV_Preprint_v0.6_EN.tex', 'WREH_WR-IV_Preprint_v0.6_RU.tex',
    'wriv-preamble.tex', 'wriv-body.tex', 'WREH_WR-IV_Demo_v0.6_EN-RU.html',
    'README.md', 'AUDIT_RU.md', 'SOURCE_MAP.md', 'ZENODO_DEPOSIT.md',
    'LICENSE-CONTENT.md', 'LICENSE-CODE.txt', 'LICENSES.md',
    'CITATION.cff', 'CITATION.bib', 'metadata/zenodo-deposit.json',
    'metadata/description_EN.txt', 'metadata/description_RU.txt',
    'verification.json', 'demo-verification.json', 'build-verification.json',
    'scripts/reproduce.py', 'scripts/build.py', 'scripts/package.py', 'scripts/verify_demo.cjs',
] + [f'figures/{name}_{lang}.{extension}'
     for name in ('variance', 'densities') for lang in ('en', 'ru') for extension in ('pdf', 'png')]


def main():
    for name in ('verification.json', 'demo-verification.json', 'build-verification.json'):
        assert json.loads((ROOT / name).read_text())['result'] == 'passed', name
    for name in FILES:
        if not (ROOT / name).is_file():
            raise FileNotFoundError(name)
    (ROOT / 'SHA256SUMS.txt').write_text(''.join(
        f'{hashlib.sha256((ROOT / name).read_bytes()).hexdigest()}  {name}\n'
        for name in sorted(FILES)), encoding='utf-8')
    with zipfile.ZipFile(ROOT / ARCHIVE, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(FILES + ['SHA256SUMS.txt']):
            entry = zipfile.ZipInfo(name, date_time=(2026, 10, 8, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, (ROOT / name).read_bytes())
    with zipfile.ZipFile(ROOT / ARCHIVE) as archive:
        assert archive.testzip() is None
        assert sorted(archive.namelist()) == sorted(FILES + ['SHA256SUMS.txt'])
    print(json.dumps({'archive': ARCHIVE, 'files': len(FILES) + 1,
                      'bytes': (ROOT / ARCHIVE).stat().st_size,
                      'sha256': hashlib.sha256((ROOT / ARCHIVE).read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
