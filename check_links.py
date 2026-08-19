import re
from pathlib import Path
from typing import List, Tuple

_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def find_broken_links(files: List[Path]) -> List[Tuple[Path, str]]:
    """Return local markdown links that point to missing files.

    The checker intentionally ignores external URLs, anchors, and Pelican-specific
    links such as {filename}... because those are not ordinary filesystem paths.
    """

    broken_links: List[Tuple[Path, str]] = []

    for file_path in files:
        text = file_path.read_text(encoding="utf-8")
        for raw_target in _LINK_PATTERN.findall(text):
            target = raw_target.strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "tel:", "#")):
                continue
            if target.startswith("{") or target.startswith("/"):
                continue

            resolved_path = (file_path.parent / target).resolve()
            if not resolved_path.exists():
                broken_links.append((file_path, target))

    return broken_links


if __name__ == "__main__":
    import sys

    paths = [Path(arg) for arg in sys.argv[1:]]
    if not paths:
        paths = [Path("content")]

    if paths and paths[0].is_dir():
        markdown_files = sorted(paths[0].rglob("*.md"))
    else:
        markdown_files = paths

    broken = find_broken_links(markdown_files)
    if broken:
        for file_path, target in broken:
            print(f"{file_path}: {target}")
        raise SystemExit(1)

    print("All local markdown links resolve.")
