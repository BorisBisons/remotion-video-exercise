# Koboyi Manager — State Schemas and Output Templates

Reference file. The orchestrator and specialists copy these formats exactly. Deviations are rejected and re-run.

---

## 1. 00_goal.md

```
# Primary goal
Goal: <number> <metric> by <YYYY-MM-DD>
Set on: <date> · Status: on track / at risk / behind (as of <date>)
Math: current rate <x/week> [L:...] → required rate <y/week> → gap <z> → lever: <one line>
Active plan: <3 lines max>
Cadence: <1 upload / 2 weeks> · Weekly review day: <day>
Boris: timezone <TZ> · hours/week <n> on <days> · tool credit budget <n>/month
Streak: <n> milestones hit in a row (last miss: <date or none>)
Previous goals: <goal → hit/missed on date → one-line post-mortem>
```

## 2. 01_ledger.csv — one row per video

Header (copy exactly; one line, shown wrapped here):

```
video_id,title,population,format,series,characters,topic,hook_type,script_id,script_version,
publish_date,publish_time_local,publish_time_cat,runtime_sec,
views_24h,views_72h,views_7d,views_28d,impressions,ctr_pct,avd_sec,avg_pct_viewed,
ret_0m30,ret_1m00,ret_50pct,likes,comments,shares,subs_gained,
top_traffic_source,geo_rw_pct,geo_diaspora_pct,age_gender_note,
shorts_shown_in_feed,shorts_viewed_vs_swiped_pct,
pred_views_7d_low,pred_views_7d_high,pred_ctr_low,pred_ctr_high,pred_pct_viewed_low,pred_pct_viewed_high,pred_break_risk,
grade_notes,data_as_of,source_tag
```

- population = long or short. format = 3D / 2D / narrated. hook_type = cold-open-joke / character-intro / conflict-first / narrated-setup.
- Long-form metric set: impressions, ctr_pct, avd_sec, avg_pct_viewed, ret_*, views_*.
- Shorts metric set: shorts_shown_in_feed, shorts_viewed_vs_swiped_pct, avd_sec, views_*, subs_gained. Impressions/CTR cells for Shorts are n/a, not MISSING.
- Empty cells are never blank: ?, n/a, or MISSING — <tab> > <metric>.

## 3. 02_script_index.csv

```
script_id,title_kin,title_gloss,version,status,series,characters,setting,theme,joke_style,hook_type,target_runtime_sec,est_runtime_sec,shipped_as_video_id,file_path,locked_on
```

- status = idea / draft / critic-fail / locked / shipped / shelved.
- joke_style = one or more of situational / wordplay / character / social-commentary.
- Script files live at scripts/<script_id>_v<version>.md.

## 4. 03_insights.md entry

```
- <YYYY-MM-DD> · <Observation in one sentence>
  Evidence: [L:V003] [L:V005] [L:V007] · Confidence: low / med / high
  Action: <what changes in the next brief or schedule>
  (Retired <date>: <what contradicted it>)
```

## 5. 04_experiments.md — Experiment Spec

```
### EXP-<nn> · <name> · status: open / closed
Hypothesis: <if X then metric Y moves by Z>
Variable: <one> · Control: <current default> · Arms: <A> vs <B>
Minimum n per arm: <2 long / 3 short> · Primary metric: <one> · Held fixed: <list>
Decision rule (written before data): adopt if <numeric>, drop if <numeric>, else retest
Assignment: V012→A, V013→B, V014→A ...
Duration: <dates> · Confounds to watch: <list>
Result: <rows used> → <numbers> → Decision: adopt / drop / retest (<date>)
```

## 6. 06_production_costs.md

```
| Format | Hours per finished minute | Basis | Last updated |
|---|---|---|---|
| 3D episode | <n> | [B:date] V009 actuals: <hours> for <runtime> | <date> |
| 2D short | <n> | ... | |
| Narrated | <n> | ... | |

Fixed costs per video (any format): script <h>, voice <h>, edit <h>, thumbnail <h>  [B:date]
```

No default numbers. Until Boris reports an actual, the row reads [A] <Boris's estimate>.

## 7. 07_lessons.md entry

```
- <YYYY-MM-DD> · What went wrong: <one line> · Rule: <one line, testable> · (Retired <date>: <reason>)
```

## 8. 08_session_log.md entry

```
## <YYYY-MM-DD>
Decisions: <bullets>
Predictions written: <video IDs> · Grades filed: <video IDs>
Files changed: <list>
```

---

## 9. Concept Card (orchestrator → Boris, three per selection round)

```
### #<rank> — <Kinyarwanda title> (<English gloss>)
Premise: <one line>
Runtime target: <m:ss> · Population: long / short · Format: 3D / 2D / narrated
Cast / setting: <existing characters and assets first>
Hook type: <one of four>
Why: <evidence [L:...] or cold-start reasoning [A]>
Predicted vs <median | previous video>: 7d views <low–high> · CTR <low–high>% · % viewed <low–high>
Cost: ~<n> hours [from 06] · Risk: <one line>
```

## 10. Script Pack (Writer → Critic → orchestrator)

```
# <script_id> v<n> — <Kinyarwanda title> (<gloss>)
Target runtime <m:ss> · Estimated <m:ss> (<words> ÷ <wpm> [source]) · Jokes: <n> (<n> per 30s)

## Hook (0:00–0:15)
<dialogue/action> — Trap avoided: <e.g. "character intro before conflict">

## Beat sheet
| Time | Beat | On screen | Joke / turn |
|---|---|---|---|

## Dialogue
<full Kinyarwanda, character-labelled, [VOICE?] where unsure>

## Ending / callback
<line + what it makes the viewer do: comment / wait for next episode>

## Publishing pack
Titles: 1. <kin> (<gloss>) 2. ... 3. ...
Thumbnails: A. text "<...>" · expression <...> · composition <...>  B. ...
Description: <2–3 lines with keywords>
Pinned comment: <question>

## Production notes
Expensive shots: 1. <shot> → cheaper: <alt>  2. ...  3. ...
Assets reused: <list> · New assets: <list>

## Flags
[VOICE?]: <lines> · [GUARDRAIL?]: <lines or none>
```

## 11. Diagnosis Card (Analyst → orchestrator)

```
### <video_id> · data as of <date>
Problem type: impressions (topic/title/thumb) / click (CTR) / hold (0–30s) / watch-through (mid drop)
Evidence: <metric vs median or previous, rows cited>
Largest drop: <timestamp> · on screen: <beat from script, if available>
Biggest lever (one): <what to change next time>
Prediction gap: views 7d <inside/outside range by n%> · CTR <...> · % viewed <...>
```

## 12. Prediction Card (orchestrator, before publish)

```
### Prediction · <video_id> · publish <date time local> (<time> CAT)
7d views: <low–high> · basis: <rows / reasoning>
CTR: <low–high>% · basis: <...>            (Shorts: viewed-vs-swiped <low–high>%)
Avg % viewed: <low–high> · basis: <...>
Most likely to break it: <one line>
Experiment arm: <EXP-nn / A or B / none>
```

## 13. 7-Day Grade (orchestrator, day 7)

```
### Grade · <video_id>
| Metric | Predicted | Actual | Gap | Inside range? |
|---|---|---|---|---|
Cause of the largest gap: <one line>
Model change: <one line, or "none">
Lesson filed: yes (07_lessons) / no
```

## 14. Milestone Table (Producer) and definitions of done

```
| Milestone | Date | Hours | Done when |
|---|---|---|---|
| Script locked | | | Critic PASS · runtime est. within ±15% · Boris read it, no open vetoes · saved as scripts/<id>_v<n>.md |
| Voice recorded | | | every line in the beat sheet recorded and filed · no re-record notes open · actual duration logged |
| Animation / blocking done | | | every beat-sheet shot exists on the Blender timeline · playblast reviewed by Boris · no missing assets |
| Edit locked | | | Resolve timeline complete · final runtime logged · thumbnail exported · no open notes |
| Published | | | live or scheduled at the experiment slot · title/thumb/description/pinned comment match the Script Pack · ledger row + Prediction Card written |

FIT: YES / NO · Hours available <n> · Hours scheduled <n> (≤80%) · Slack <n>
```

## 15. Next Actions (every session, last block before "Files changed")

```
| # | Action | Owner | Due | Done when |
|---|---|---|---|---|
```

3–5 rows. Owner is Boris or Manager. Dates, not "this week".

## 16. Weekly review

```
## Weekly review · <date>
Numbers: <ledger deltas since last review, tagged>
What we learned: <insights added / retired>
Goal status: <on track / at risk / behind> · math: <current → required → gap>
Experiments: <open spec status · closures>
This week's plan: <milestones due, hours>
Next Actions: <table>
Files changed: <list>
```
