"""Install this checkout into an empty project and verify the bundle."""

import os
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = {
    "execute": "execution-handoff.md",
    "independent-review": "result-axes.md",
    "plan": "topic-and-tasks.md",
    "problem": "problem-brief.md",
    "review": "axes-and-report.md",
}


def heading_ids(document):
    ids = set()
    for heading in re.findall(r"^#{1,6} +(.+)$", document.read_text(), re.MULTILINE):
        slug = re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-")
        anchor = slug
        number = 0
        while anchor in ids:
            number += 1
            anchor = f"{slug}-{number}"
        ids.add(anchor)
    return ids


def check_links(document):
    for link in re.findall(r"\]\(([^)\n]+)\)", document.read_text()):
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = document.parent / unquote(url.path) if url.path else document
        if not target.exists():
            raise SystemExit(f"{document}: missing target {link}")
        if url.fragment and target.suffix == ".md" and unquote(url.fragment) not in heading_ids(target):
            raise SystemExit(f"{document}: missing heading {link}")


def check_install(project):
    subprocess.run(["git", "init", "--quiet"], cwd=project, check=True)
    subprocess.run(
        ["npx", "--yes", "skills@1.9.0", "add", str(ROOT), "--agent", "universal", "--skill", "*", "-y"],
        cwd=project,
        env={**os.environ, "DO_NOT_TRACK": "1"},
        check=True,
    )
    installed = project / ".agents" / "skills"
    names = {p.name for p in installed.iterdir() if p.is_dir()} if installed.is_dir() else set()
    if names != set(TEMPLATES):
        raise SystemExit(f"Expected {sorted(TEMPLATES)}, found {sorted(names)}")
    for name, template in TEMPLATES.items():
        skill = installed / name
        for required in (skill / "SKILL.md", skill / "references" / template):
            if not required.is_file():
                raise SystemExit(f"Missing installed file: {required}")
        subprocess.run(["diff", "-qr", str(ROOT / "skills" / name), str(skill)], check=True)
        for document in skill.rglob("*.md"):
            check_links(document)


def main():
    files = subprocess.check_output(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", "*.md"],
        cwd=ROOT,
    )
    for path in files.split(b"\0"):
        if path:
            check_links(ROOT / os.fsdecode(path))
    work = ROOT / ".work"
    work.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(dir=work, prefix="check-install-") as temp:
        check_install(Path(temp))
    print("Verified all five installed skills, their templates, and local Markdown links.")


if __name__ == "__main__":
    main()
