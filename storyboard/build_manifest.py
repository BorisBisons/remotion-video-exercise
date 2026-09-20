#!/usr/bin/env python3
"""Build manifest.csv and download.sh, naming every panel after its timestamp."""
import csv, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_index import BEATS  # noqa: E402


def slug(t):
    """'0:01-0:06' -> '00-01' (zero padded MM-SS of the beat start)."""
    start = t.split("-")[0]
    m, s = start.split(":")
    return f"{int(m):02d}-{int(s):02d}"


def main():
    urls = {}
    with open(os.path.join(HERE, "urls.tsv")) as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                continue
            key, url = line.split("\t", 1)
            urls[key] = url

    rows = []
    if "anchor" in urls:
        rows.append({
            "filename": "character-sheet.png",
            "timestamp": "",
            "beat": "",
            "panel": "",
            "emotion": "",
            "angle": "",
            "shot": "Character and style anchor sheet",
            "line": "",
            "url": urls["anchor"],
        })

    missing = []
    for num, time, line, emotion, angle, shots in BEATS:
        for i, shot in enumerate(shots, start=1):
            key = f"{num}{i:02d}"
            url = urls.get(key)
            if not url:
                missing.append(key)
                continue
            rows.append({
                "filename": f"{slug(time)}_p{i}.png",
                "timestamp": time,
                "beat": f"{num:02d}",
                "panel": str(i),
                "emotion": emotion,
                "angle": angle,
                "shot": shot,
                "line": line,
                "url": url,
            })

    names = [r["filename"] for r in rows]
    dupes = {n for n in names if names.count(n) > 1}
    if dupes:
        raise SystemExit(f"duplicate filenames: {sorted(dupes)}")

    fields = ["filename", "timestamp", "beat", "panel",
              "emotion", "angle", "shot", "line", "url"]
    with open(os.path.join(HERE, "manifest.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    script = [
        "#!/usr/bin/env bash",
        "# Downloads every storyboard panel and names it after its timestamp.",
        "# Usage:  bash download.sh [output-directory]",
        "# Default output directory: ./panels",
        "set -euo pipefail",
        '',
        'OUT="${1:-panels}"',
        'mkdir -p "$OUT"',
        f'TOTAL={len(rows)}',
        'ok=0',
        'fail=0',
        '',
        'fetch() {',
        '  local name="$1" url="$2"',
        '  if [ -s "$OUT/$name" ]; then',
        '    echo "skip  $name (already present)"',
        '    ok=$((ok+1)); return',
        '  fi',
        '  if curl -fsSL --retry 3 --retry-delay 2 --max-time 120 -o "$OUT/$name.part" "$url"; then',
        '    mv "$OUT/$name.part" "$OUT/$name"',
        '    echo "ok    $name"',
        '    ok=$((ok+1))',
        '  else',
        '    rm -f "$OUT/$name.part"',
        '    echo "FAIL  $name" >&2',
        '    fail=$((fail+1))',
        '  fi',
        '}',
        '',
    ]
    for r in rows:
        script.append(f"fetch {r['filename']} '{r['url']}'")
    script += [
        '',
        'echo',
        'echo "downloaded $ok of $TOTAL into $OUT ($fail failed)"',
        '[ "$fail" -eq 0 ]',
    ]

    path = os.path.join(HERE, "download.sh")
    with open(path, "w") as fh:
        fh.write("\n".join(script) + "\n")
    os.chmod(path, 0o755)

    print(f"manifest.csv rows: {len(rows)}")
    print(f"download.sh fetches: {len(rows)}")
    if missing:
        print("missing panels:", ", ".join(missing))


if __name__ == "__main__":
    main()
