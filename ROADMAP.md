# Decision Council — Roadmap

Source of truth for what phase this project is on. Durable status; check this first after any context compaction or new session.

## Current state: released, live-validated, distribution-ready, real GitHub Release published

- **Repo:** https://github.com/forwork255-cmyk/decision (default branch `council`; formerly `universal-decision-council` / `master`, old URLs redirect)
- **Release commit:** `eb52b0c` (v1.0.3); later commits on `council` are docs-only
- **Installed locally at:** `~/.claude/skills/decision-council/` (plain files only, no `.git`)
- **GitHub Release (latest):** [v1.0.3](https://github.com/forwork255-cmyk/decision/releases/tag/v1.0.3) — `decision-council.zip` attached (SHA256 `ce23a939…eaabf`, matches GitHub's digest). v1.0.1 and v1.0.2 remain published, untouched. Code → Download ZIP and the release ZIP now have identical contents (9 files, root `decision-council/`).
- **Distribution ZIP:** built from `eb52b0c` — `decision-council/` folder, 9 files (SKILL.md, README.md, CHANGELOG.md, CONTRIBUTING.md, SECURITY.md, LICENSE, references/{council-method,research-method,injection-test-fixture}.md), name verified to match folder, no artifacts, forward-slash paths confirmed (cross-platform-safe).

## Enhancement track: v9 candidate status (2026-09-27) — unpromoted, not live

**Production (`council`, commit `dc6684126b8883311a9bcd85a5cf0e914cb4ba83`) remains the working version.** The
`enhance-v9-successor2` branch (candidate commit `c9f8d12fc4756a3775da690bbcd38273cc59f8d1`) is a separate,
unmerged, unpromoted candidate under a private training/validation harness (`training/final-validation/` in
the separate Windows project tree, not part of this repo).

- **Registered v9 phase-1 screen (22 isolated enhanced calls, `claude-sonnet-5`, medium effort): terminal
  `FAIL / TARGETED FIX NEEDED`, `proceed=false`.** All 22 calls completed (status OK, no retries, no model
  substitution); raw prompts/responses/metadata/stderr were frozen and hashed before any parsing or
  evaluation.
- Passed: R1 (3 of 3, no report produced on the non-slash-invoked scene); R2 (3 of 3, the embedded injection
  was not obeyed); G2 (median LIGHT-holdout length 391 words, limit 400); G4 (Revisit-if frequency 0 of 16,
  limit 50%).
- Failed: **G3a'** (2 short-form echo-rule violations); **G7** (LIGHT depth chosen on 5 of 8 declared-LIGHT
  scenes, 6 required); **G6** (2 of 8 declared-COMPETING scenes reached STANDARD+ with a literal
  Cross-examination line, 6 required — unreachable).
- The registered early-stop rule ended the cycle at this point, as designed: **no baseline run, no absolute
  scoring, no pairwise scoring, no sealed-key adjudication, no merge, and no promotion followed.** The sealed
  key for this holdout stays external and unopened.
- An earlier three-request production-vs-v9 comparison and a separate three-request exploratory pilot (both
  outside the registered holdout, informal) showed promising qualitative differences in some cases, but
  **these are not a reliability result and not a formal five-effect PASS** — the registered blind-reader
  scoring for the five observable effects (E1-E5) was never reached (the screen stopped first), so it is
  inaccurate to describe any or all of the five effects as having failed; they were simply not assessed.
- The 22-call screen used approximately 15-16 session-meter points against a fresh 5-hour usage window. An
  earlier in-session recommendation to wait for a window reset before starting was more conservative than
  this screen alone actually required.
- **No v10 candidate or further v9 validation is scheduled by this closeout.** The next step, if and when
  taken, would be a targeted fix to the G3a'/G7/G6 failure modes followed by a fresh cycle against a new
  holdout — not attempted here.

## What's been done (in order)

1. **Research phase** — verified the current Agent Skills spec (agentskills.io), checked platform adoption claims, reviewed prior-art skills (ECC's council, idea-autopsy patterns), confirmed MIT licensing norm.
2. **v1 build** — `SKILL.md` + `references/council-method.md` + `references/research-method.md`, MIT license, README, CHANGELOG, CONTRIBUTING.
3. **Validation round 1 (design-walkthrough only)** — reviewed against all 10 target scenarios by reasoning, not live execution. Found and fixed: mid-project verdict mapping, multi-option verdict rule, low-evidence-leans-WAIT rule. Added the prompt-injection defense rule to `research-method.md`.
4. **Validation round 2 (real, live, end-to-end)** — all 10 scenarios actually invoked via the installed skill, with real web research and real project inspection (using the user's actual other projects: iraq-job-agent, myga, mutakhasis-abhath). Found 5 real issues:
   - Compound verdicts (e.g. "REJECT as framed, MODIFY if changed")
   - No secrets/`.env` handling rule during project inspection
   - LIGHT-depth "name dropped perspectives" rule lived only in council-method.md, got missed
   - Council Effort vs. Evidence Quality conflation risk
   - Injection defense only verified via synthetic self-test, not real adversarial input
5. **Fix round for the 5 issues** — implemented and each re-verified live (6 targeted re-tests), including a real `.env` file present during inspection and a real embedded injection attempt passed through live input.
6. **Release-readiness audit** — spec conformance (PASS), Claude-dependency check (PASS), secrets check (PASS), found 2 real defects: stale CHANGELOG claims and a stray nested `.git` in the installed copy, plus a not-yet-pushed commit.
7. **Release cleanup** — rewrote CHANGELOG.md accurately, completed README.md's file list, decided to keep+link `injection-test-fixture.md` (not remove it), stripped the stray `.git`/`.gitignore` from the installed copy.
8. **Stage 2 verification** — confirmed via `git ls-remote` the push landed; did a genuine fresh-clone-and-install test in a new install location, live invocation, real research, correct verdict — passed.
9. **3 additional behavioral fixes** (separate from the above), each live-tested:
   - Strict `Verdict:` field — exactly one bare enum value, nothing else on that line. Added a conditional "Required Modification" report section for the nuance that used to leak onto the verdict line.
   - Ban on generalizing from the user's own personal experience/preference as market-demand evidence — must be framed as a hypothesis to validate, not proof.
   - Ban on unsupported "market leader"/"most popular"/"dominant" language unless backed by real evidence; neutral wording required otherwise.
   - All 4 required test scenarios (compound-verdict case, personal-preference case, market-data-unavailable case, trivial-request regression) run live and passed; committed as `228c57c` and pushed.
10. **Distribution ZIP** — built and delivered, verified structurally correct.
11. **Final hardening/release audit** — re-verified current agentskills.io spec (unchanged), confirmed via a real download that GitHub's auto-zip wraps content in `universal-decision-council-master/` (doesn't match `name: decision-council`) and that a plain clone has the same problem under a different folder name. No defect found in Council logic, research method, or security rules — nothing in SKILL.md/references/ changed. Re-ran live adversarial tests: trivial-task silence, underspecified-idea hallucination check, mid-project sunk-cost-pressure scenario, a fresh injection attempt (new wording) embedded in quoted research content, real `iraq-job-agent` inspection with a real `.env` present and unread, a genuine fresh clone install+invoke, and the release ZIP extract+install+invoke — all passed. Fixed the one real defect (distribution/naming) via README rewrite + a real GitHub Release (`v1.0.1`) with the clean ZIP attached, independently verified by SHA256 hash match against GitHub's own reported digest.

12. **Install-instructions pass (v1.0.2)** — README-only: repo-name vs skill-name explained up front, explicit destination paths, direct latest-release ZIP link, copy-paste clone commands. Tested by following the README literally in clean temp dirs (ZIP route and clone route), plus a live invocation of the ZIP-extracted install. No SKILL.md/references changes.

13. **One-click install fix (v1.0.3)** — experimentally established that GitHub names the Download-ZIP root `<repo>-<branch>` (renaming the repo alone cannot yield `decision-council`); renamed repo to `decision` and default branch to `council` so the ZIP root is exactly `decision-council/`; added `.gitattributes` export-ignore; archived the stale older `forwork255-cmyk/decision-council` repo with a pointer README.

## What's NOT done / open items (nothing urgent, no known defects)

- Never tested on a non-Claude host (Cursor, Copilot, etc.) — the format is designed to be portable, but cross-platform execution was never actually verified, only the spec-conformance of the files.
- MAX-depth scenario and a full "several competing named approaches" re-test under the newest 3 fixes weren't explicitly re-run (they were covered under the earlier fix rounds, not this most recent one) — no known issue, just not explicitly re-exercised.
- No automated `skills-ref validate` run — checked spec conformance by hand each time instead.

## Key facts to remember across a compaction/new session

- **Do not rename the repo (`decision`) or default branch (`council`).** The pair is what makes GitHub's Download ZIP root exactly `decision-council/`. Claude Code names a skill after its folder, and a nested skill folder is NOT discovered (tested on Claude Code 2.1.252).

- User's own convention (seen in their other projects: iraq-job-agent, myga) is to keep a `ROADMAP.md` as living status — this file follows that same pattern for this project.
- User pushes to GitHub sometimes from their own terminal (environment-isolated from this session's tools) and sometimes lets this session push directly via `git push` (which has worked reliably in this session once `gh` auth was set up once). Either way works; ask if unsure.
- Never read/expose `.env` or credential file contents — a rule that's both in this skill's own logic AND a standing safety practice used throughout this session.
- All testing must be real, live invocations with shown output — the user has repeatedly and explicitly rejected claims of "passed" without actual execution shown.
