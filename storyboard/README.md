# Storyboard — "King of Leaves"

109 illustrations: 108 storyboard panels (four per timestamp across 27 beats,
0:01–4:20) plus one character anchor sheet.

## Get the images locally

The images are hosted on the generation service. This repository stores their
addresses rather than the binaries, so the folder stays small and the panels
can be re-fetched at full 2k resolution at any time.

```bash
bash storyboard/download.sh                # writes into ./panels
bash storyboard/download.sh ~/Desktop/king-of-leaves   # or anywhere you like
```

The script skips anything already downloaded, retries transient failures, and
prints a count at the end. On Windows, run it from Git Bash or WSL.

## File naming

Every file is named after the timestamp it illustrates, zero padded so the
folder sorts in script order:

```
00-01_p1.png   0:01, panel 1
00-01_p2.png   0:01, panel 2
00-01_p3.png   0:01, panel 3
00-01_p4.png   0:01, panel 4
00-06_p1.png   0:06, panel 1
...
04-11_p4.png   4:11, panel 4
character-sheet.png
```

`MM-SS` is the beat's start time. The four panels sharing a timestamp are the
four shots cut within that beat, in screen order.

## Files here

| File | What it is |
|---|---|
| `manifest.csv` | One row per image: filename, timestamp, beat, panel, emotion, angle, shot, line, URL |
| `download.sh` | Fetches all 109 images and applies the timestamp names |
| `panels.md` | Every panel inline, grouped by beat |
| `storyboard.md` | The 27-beat table with emotion and camera angle |
| `characters.md` | Character and style bible |
| `urls.tsv` | Panel id to image URL |
| `jobs.tsv` | Panel id to generation job id |
| `build_index.py` | Regenerates `panels.md` from `urls.tsv` |
| `build_manifest.py` | Regenerates `manifest.csv` and `download.sh` |

## Importing into Remotion

`manifest.csv` is the edit list. Each row carries the timestamp, the shot
description and the camera angle, so a sequence can be built straight from it
without re-reading the script.
