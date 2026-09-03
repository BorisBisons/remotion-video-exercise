# Koboyi Manager — repo bootstrap plan

Goal: turn the pasted "Koboyi Manager (Orchestrator) v2" system prompt into a complete, version-controlled
package: orchestrator prompt + the two companion files it references (`agents.md`, `templates.md`) + seeds
for the state files it expects in Drive.

Findings before starting:
- Repo held only a LICENSE. Branch `claude/koboyi-manager-orchestrator-edwr5t` was empty.
- Google Drive: `templates.md` exists (Google Doc, 2026-09-02). `agents.md` does not exist anywhere.
  No `Koboyi Manager/` folder, no `00_goal.md` or other state files → runtime is in First Run state.

## Plan
- [x] Write this plan; scaffold `tasks/lessons.md`
- [x] `orchestrator.md` — system prompt v2, verbatim
- [x] `templates.md` — Drive doc converted to clean markdown, content unchanged
- [x] `agents.md` — six specialist prompts (Analyst, Script Writer, Script Critic, Producer,
      Experiment Designer, Scout) matching orchestrator §5 and templates.md section numbers
- [x] `README.md` — what this is, how to run it, file map, Drive layout
- [x] `state_seed/` — exact CSV headers for `01_ledger.csv` and `02_script_index.csv`
- [x] Consistency check: every "you require back" item in orchestrator §5 has a defined format;
      every template section referenced by agents.md exists; CSV headers match templates.md
- [x] Commit + push
- [x] Upload `agents.md` to Drive beside `templates.md` so the runtime companion set is complete

## Review
See the final commit message and README "Status" section.
