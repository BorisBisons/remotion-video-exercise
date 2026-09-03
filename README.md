# Koboyi Manager

Prompt package for **Koboyi Manager**, the orchestrator that runs the YouTube channel
**Koboyi Studio** (Kinyarwanda animated comedy for Rwandans aged 18–28, home and diaspora)
the way a manager runs an artist: goal, brief, deadline, numbers, next action.

## Files

| File | What it is | Who reads it |
|---|---|---|
| `orchestrator.md` | The system prompt (v2). Paste it as the system prompt of the manager session. | the runtime |
| `agents.md` | Prompts for the six specialists the orchestrator spawns (Analyst, Script Writer, Script Critic, Producer, Experiment Designer, Scout), the Brief format, and the rejection checklist. | the orchestrator, per §5 |
| `templates.md` | Exact schemas for the nine state files and the output cards (Concept, Script Pack, Diagnosis, Prediction, 7-Day Grade, Milestone Table, Next Actions, Weekly review). | orchestrator and specialists |
| `state_seed/` | Header-only CSVs for `01_ledger.csv` and `02_script_index.csv`, copied exactly from `templates.md`. Copy into the Drive folder on First Run. | First Run |
| `tasks/` | Repo work log: `todo.md` (plan and review), `lessons.md` (rules added after corrections). | maintainers |

## How it runs

1. Start a session with `orchestrator.md` as the system prompt. Make `agents.md` and
   `templates.md` readable to it (Drive, or paste on request).
2. State lives in the Google Drive folder `Koboyi Manager/` as the nine files listed in
   `orchestrator.md` §3. The orchestrator reads them at session start and writes them back at
   session end. Memory does not persist otherwise.
3. If `00_goal.md` is absent the orchestrator runs First Run (§12): one message asking for
   subscriber count, video list, scripts, hours, next publish date, timezone, and credit budget,
   then builds the first ledger, voice bible, goal, and Milestone Table.
4. Every video: Concept Cards → Brief → Writer → Critic → lock → Producer → Prediction Card →
   publish → 7-Day Grade → Experiment Designer. The Critic pass and the two cards are never skipped.

## Status

- `templates.md` in this repo mirrors the Google Doc of the same name in Drive (converted to
  plain markdown, content unchanged).
- `agents.md` was written here first and uploaded to Drive beside `templates.md`.
- No `Koboyi Manager/` Drive folder or state files exist yet, so the next manager session is a
  First Run.

## Editing rules

- `orchestrator.md`, `agents.md`, and `templates.md` are one system. A new required output in
  `orchestrator.md` §5 needs a format in `templates.md` or `agents.md` in the same commit.
- CSV headers in `state_seed/` must stay byte-identical to `templates.md` §2 and §3.
- Version bumps go in the `orchestrator.md` title line (v2 → v3) and a dated line in
  `tasks/todo.md`.
