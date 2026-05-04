#!/usr/bin/env python3

import difflib
from pathlib import Path
import re
import subprocess
import sys

SKIP = [
    re.compile(r'andika', re.IGNORECASE),
    re.compile(r'^\.'),
    re.compile(r'\.(svg|css|lua)$', re.IGNORECASE),
    re.compile(r'^(requirements\.txt|andika|replace-o-matic\.py)$', re.IGNORECASE),
    re.compile(r'^outline\d+.md$', re.IGNORECASE), # old outline
]

COURSE='33421'
SCHEDULE='1sgbyxsapiHyxuBmkHtWGN_PgZbbLnfFiqsUIGSlHyBk'
HELPFORM='1FAIpQLScSdeLbxEUUWzRlhSPZzaVoxlVtSNwpriZ5MSnuatMVYqp1iA'
ZOOMLINK='https://ualberta-ca.zoom.us/j/95893996808'
SYLLABUS='https://ualberta.simplesyllabusca.com/doc/28xys85it/Spring-2026-CMPUT-402A-C1-%2831507%29-SOFTWARE-QUALITY?mode=view'

ZOOMLINK_RE=re.compile(r'https?://[\w\./:\[\]@-]+zoom[\w\./:\[\]@-]+/j/\d+', re.IGNORECASE)

WARNINGS = [
    (re.compile(r'courses/\d+', re.IGNORECASE), re.compile(f'courses/{COURSE}')),
    (re.compile(r'spreadsheets/d/[\w-]+/', re.IGNORECASE), re.compile(re.escape(SCHEDULE))),
    (re.compile(r'forms/\w+/\w+/[\w-]+', re.IGNORECASE), re.compile(re.escape(HELPFORM))),
    (ZOOMLINK_RE, re.compile(re.escape(ZOOMLINK))),
    (re.compile(r'[^\n]*https?://ualberta.simplesyllabusca.com/doc/[\w/()%\./?=-]+', re.IGNORECASE), re.compile(re.escape(SYLLABUS) + r'|class="[^"]*old')),
]

REPLACEMENTS = [
    (re.compile(r'courses/\d+/discussion_topics/\d+', re.IGNORECASE), f'courses/{COURSE}/discussion_topics/276049'),
    (re.compile(r'courses/\d+/(grades|assignments|pages/[\w_-]+|announcements|external_tools/\d+)', re.IGNORECASE), f'courses/{COURSE}/\\1'),
    (re.compile(r'courses/\d+([^/\w-])', re.IGNORECASE), f'courses/{COURSE}\\1'),
    (re.compile(r'spreadsheets/d/[\w-]+/', re.IGNORECASE), f'spreadsheets/d/{SCHEDULE}/'),
    (re.compile(r'forms/d/e/[\w-]+/', re.IGNORECASE), f'forms/d/e/{HELPFORM}/'),
    (ZOOMLINK_RE, ZOOMLINK),
]

COMMIT = len(sys.argv) > 1 and sys.argv[1] == 'commit'

def should_skip(something):
    something = str(something)
    for r in SKIP:
        if r.search(something):
            return True
    return False

root = Path(".")
for (dirpath, dirnames, filenames) in root.walk():
    if dirpath != '.' and len([folder for folder in dirpath.parts if should_skip(folder)]) > 0:
        continue
    # print(dirpath, dirnames, filenames)
    for filename in filenames:
        if should_skip(filename):
            continue
        filepath = dirpath / filename
        temppath = dirpath / (filename + '.tmp')
        assert len(str(temppath)) > len(str(filepath))
        binary = subprocess.run(["git", "check-attr", "-z", "binary", str(filepath)], capture_output=True, stderr=None).stdout.split(b'\0')[2]
        if binary == b'set':
            continue
        # print(filepath)
        try:
            slurp = filepath.read_text(encoding='utf8', errors='strict')
        except UnicodeDecodeError:
            with filepath.open('rb') as f:
                line_nr = 1
                for line in f:
                    print("line", line_nr, file=sys.stderr)
                    try:
                        line.decode(encoding='utf8', errors='strict')
                    except UnicodeDecodeError:
                        print("unicode error on", filepath, "line", line_nr, file=sys.stderr)
                        raise
                    line_nr += 1
            raise
        processed = str(slurp)
        for replacement_re, replacement_with in REPLACEMENTS:
            (processed, n) = replacement_re.subn(replacement_with, processed)
            if n > 0 and False:
                print(filepath, replacement_re, replacement_with, n, file=sys.stderr)
        for warning, but_ok in WARNINGS:
            for m in warning.finditer(processed):
                if (
                    m is not None
                    and but_ok.search(m.group(0)) is None
                ):
                    print("Warning: found", m.group(0), "in", filepath, file=sys.stderr)
                    ln = 1
                    for l in processed.splitlines():
                        lm = warning.search(l)
                        if lm is not None and but_ok.search(lm.group(0)) is None:
                            print("Warning: found", m.group(0), "in", filepath, "line", ln, file=sys.stderr)
                            print(l, file=sys.stderr)
                        ln += 1
        changed = False
        for line in difflib.unified_diff(slurp.splitlines(keepends=True), processed.splitlines(keepends=True), fromfile=str(filepath), tofile=str(temppath)):
            changed = True
            sys.stdout.buffer.write(line.encode('utf8'))
        if COMMIT and changed:
            resp=input("Write y/n? ")
            if resp.lower().startswith('y'):
                assert not temppath.exists()
                assert filepath.exists()
                with temppath.open('wt', encoding='utf8') as f:
                    f.write(processed)
                assert temppath.exists()
                temppath.replace(filepath)
                assert not temppath.exists()
                assert filepath.exists()


        



