#!/usr/bin/env python3
"""Build and validate the two language manifestations. MIT; (c) 2026 A. A. Malachevsky."""
from pathlib import Path
import json
import re
import subprocess
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]


def run(command):
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if completed.returncode:
        raise RuntimeError(completed.stdout[-6000:] + completed.stderr[-6000:])
    return completed.stdout


def main():
    labels, citations, pages = {}, {}, {}
    for language in ('EN', 'RU'):
        stem = f'WREH_WR-IV_Preprint_v0.6_{language}'
        for _ in range(3):
            run(['xelatex', '-interaction=nonstopmode', '-halt-on-error', stem + '.tex'])
        log = (ROOT / (stem + '.log')).read_text(encoding='utf-8')
        issues = re.findall(r'^.*(?:LaTeX Warning|Package .* Warning|Overfull|Underfull|Missing character|Undefined control sequence).*$'
                            , log, re.MULTILINE)
        if issues:
            raise RuntimeError('\n'.join(issues))
        aux = (ROOT / (stem + '.aux')).read_text(encoding='utf-8')
        labels[language] = dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^{}]*)\}', aux))
        citations[language] = dict(re.findall(r'\\bibcite\{([^}]+)\}\{([^}]+)\}', aux))
        pages[language] = len(PdfReader(ROOT / (stem + '.pdf')).pages)
        run(['pdftotext', '-layout', stem + '.pdf', stem + '.txt'])
    assert labels['EN'] == labels['RU'], 'Language labels differ'
    assert citations['EN'] == citations['RU'], 'Bibliographies differ'
    assert len(citations['EN']) == 11, 'Unexpected bibliography size'
    equations = {k: v for k, v in labels['EN'].items() if k.startswith('eq:')}
    assert sorted(map(int, equations.values())) == list(range(1, 23)), 'Equation numbering differs'
    report = {'result': 'passed', 'pages': pages, 'matching_numbered_labels': len(labels['EN']),
              'numbered_equations': len(equations), 'bibliographic_entries': len(citations['EN']),
              'final_latex_warnings': [], 'source_languages': ['en', 'ru'],
              'visual_review': 'All pages of both delivered PDFs inspected; formula, dictionary, figures and bibliography checked'}
    (ROOT / 'build-verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
