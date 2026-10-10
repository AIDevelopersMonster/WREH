#!/usr/bin/env python3
"""Build parallel PDFs; keep TeX intermediates outside the repository."""
from pathlib import Path
import argparse, json, re, shutil, subprocess, tempfile
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--build-dir')
    args = ap.parse_args()
    build = Path(args.build_dir or tempfile.mkdtemp(prefix='wreh-wrv-build-')).resolve()
    build.mkdir(parents=True, exist_ok=True)
    reports, keys, citations = {}, {}, {}
    for lang in ['EN', 'RU']:
        stem = f'WREH_WR-V_Draft_v0.1_{lang}'
        out = build/lang; out.mkdir(exist_ok=True)
        for _ in range(3):
            result = subprocess.run(['xelatex', '-interaction=nonstopmode',
                '-halt-on-error', '-file-line-error', '-output-directory', str(out),
                stem+'.tex'], cwd=ROOT, capture_output=True, text=True)
            if result.returncode:
                raise RuntimeError(result.stdout[-6000:] + result.stderr)
        log = (out/(stem+'.log')).read_text()
        warnings = [s for s in log.splitlines() if any(x in s for x in
            ['Warning:', 'Overfull', 'Underfull', 'Missing character:'])]
        if warnings:
            raise RuntimeError('\n'.join(warnings))
        aux = (out/(stem+'.aux')).read_text()
        keys[lang] = re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}', aux)
        citations[lang] = re.findall(r'\\bibcite\{([^}]+)\}\{([^}]+)\}', aux)
        pdf = out/(stem+'.pdf')
        reader = PdfReader(pdf)
        if '??' in '\n'.join(p.extract_text() or '' for p in reader.pages):
            raise RuntimeError('Unresolved extracted text in '+lang)
        shutil.copy2(pdf, ROOT/pdf.name)
        reports[lang] = {'pages':len(reader.pages),'bytes':pdf.stat().st_size,
            'warnings':warnings,'numbered_labels':len(keys[lang]),
            'numbered_equations':sum(k.startswith('eq:') for k, _ in keys[lang]),
            'bibliographic_entries':len(citations[lang])}
    if keys['EN'] != keys['RU']:
        raise RuntimeError('Parallel language numbering differs')
    if citations['EN'] != citations['RU'] or len(citations['EN']) != 8:
        raise RuntimeError('Parallel bibliography differs')
    reports['parallel_numbering'] = 'PASS'
    reports['visual_review'] = 'PENDING'
    (ROOT/'build-verification.json').write_text(json.dumps(reports,indent=2)+'\n')
    print(json.dumps(reports,indent=2))

if __name__ == '__main__':
    main()
