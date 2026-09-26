# Changelog

## 1.0 — 2026-09-18

Initial release.

- Core workflow: activation gate, adaptive depth (LIGHT/STANDARD/DEEP/MAX), decision framing, research step, five-perspective council, adversarial review, alternatives comparison, discovery mode, mid-project mode, final verdict report.
- `references/council-method.md` — perspective definitions, independence/anchoring rules, adversarial review, evidence-conflict handling.
- `references/research-method.md` — source-quality tiers, fact/assumption/uncertain/unverified labeling, anti-fabrication rules, capability degradation.
- `SECURITY.md` — no executable code, minimal attack surface, states prompt-injection-via-research as the relevant risk to watch for.

**Round 1 validation (design-walkthrough):** scenario coverage designed for 10 target cases (new app idea, continue-vs-pivot, technical architecture, feature decision, several named competing options, discovery mode, weak evidence, conflicting evidence, live web research, and a trivial request that should not activate the skill), reviewed against each case by design-walkthrough only — not yet run live.

Fixes from that round: mid-project verdicts (CONTINUE/MODIFY/PIVOT/PAUSE/STOP) now explicitly map onto the report's APPROVE/MODIFY/WAIT/REJECT line; clarified how the verdict works when choosing among several named options; clarified that low evidence quality should lean the verdict toward WAIT when cheap validation is available, rather than forcing a confident call; added the prompt-injection defense rule to `research-method.md`.

**Round 2 validation (real, live, end-to-end):** all 10 scenarios above actually invoked live via the installed skill, with real web research and real project inspection where applicable, each with an honest self-assessment. This round found 5 real issues:

1. Compound verdicts (e.g. "REJECT as framed, MODIFY if changed") that didn't resolve to exactly one of the four values.
2. No rule preventing the skill from reading secrets/credential files (e.g. `.env`) during project inspection.
3. The LIGHT-depth rule to name dropped perspectives lived only in `council-method.md` and was missed twice at LIGHT depth.
4. No stated distinction between Council Effort (investigation performed) and Evidence Quality (strength of what was found) — the two were at risk of being conflated.
5. The prompt-injection defense rule had only been checked with a self-administered synthetic test, not real adversarial input.

**Fixes for all 5 issues**, implemented and each re-verified with a fresh live invocation (6 targeted re-tests, including a real `.env` file present during inspection and a real embedded injection attempt passed through live input, not a synthetic test):

- The verdict now must describe only the proposal as presented, never a compound state; revisions go in Alternatives Considered / ONE NEXT MOVE instead. Added the matching discovery-mode verdict mapping.
- Added an explicit rule: never open, read, quote, or expose contents of files that plausibly hold secrets/credentials — noting a file's existence is fine, reading it is not.
- Moved the LIGHT-depth "name the dropped perspectives" rule into `SKILL.md` itself.
- Clarified Council Effort and Evidence Quality are independent and must not be conflated.
- Added `references/injection-test-fixture.md`, a repeatable regression check for the injection-defense rule, now linked from `research-method.md`.

**Current status:** both validation rounds and all 5 fixes are complete and re-verified live. A release-readiness audit (spec conformance, file resolution, no Claude-specific dependencies in the portable core, no secrets committed, fresh-checkout install, and a final clean end-to-end run) has also been performed; see the repository's audit history for the full PASS/FAIL/WARN breakdown and any items still open at release time.

## 1.0.1 — 2026-09-18 — distribution fix (no Council behavior changed)

Final hardening/release audit against the current Agent Skills spec. This audit found no concrete defect in the Council's activation logic, research method, evidence handling, or security rules — nothing in `SKILL.md` or `references/` was changed.

**The one real defect found:** GitHub's automatic "Code → Download ZIP" wraps this repository's contents in a folder named after the repo and branch (`universal-decision-council-master/`), and a plain `git clone` produces a folder named after the repo (`universal-decision-council/`) — neither matches the skill's required `name: decision-council` folder-matching rule from the Agent Skills spec. Fixed by:
- Rewriting `README.md`'s Install section to explain all three ways to get this skill (release package, clone, GitHub's zip button) and why options 2 and 3 need a manual rename.
- Publishing a GitHub Release with a pre-built `decision-council.zip` (the correctly-named `decision-council/` folder, 9 files, no `.git`/`.gitignore`/artifacts) so the recommended install path needs no renaming at all.

**Live re-verification performed this pass** (all actually executed): a trivial request stayed silent (no Council run); an intentionally underspecified "build me an app" prompt was checked for inventing a fake product/persona and correctly asked narrowing questions instead; a mid-project sunk-cost-pressure scenario (real $/time framing) was checked and the verdict was not pulled toward CONTINUE by the sunk cost; a fresh prompt-injection attempt (different wording than prior rounds, embedded in quoted "research" content) was refused and quoted back rather than followed; a real mid-project inspection was run against the `iraq-job-agent` project with a real `.env` file present and never opened; a genuine fresh `git clone` of the current repository tip was installed and invoked live; and the newly-built release ZIP was extracted, installed, and invoked live. All passed.

## 1.0.2 — 2026-09-18 — install instructions clarified (no Council behavior changed)

`README.md` only. The Install section now states the repository-name vs skill-name difference up front, gives explicit destination paths, links the release ZIP directly (`releases/latest/download/decision-council.zip`), and gives copy-paste clone commands that produce a correctly named folder. `SKILL.md` and `references/` are unchanged.

## 1.0.3 — 2026-09-18 — one-click install fixed at the source (no Council behavior changed)

The repository was previously named `universal-decision-council` (default branch `master`); old URLs redirect. GitHub's Code → Download ZIP produced `universal-decision-council-master/`, and Claude Code registers a skill under its folder name, so the raw ZIP installed a skill called `universal-decision-council-master`. Fixed by renaming the repository to `decision` and the default branch to `council`: GitHub names the ZIP folder `<repository>-<branch>`, so Download ZIP now yields exactly `decision-council/`. Added `.gitattributes` (`export-ignore`) so that ZIP holds only the 9 installable skill files, rewrote the README install section, and documented the naming constraint in `CONTRIBUTING.md`. `SKILL.md` and `references/` are unchanged.

## Unreleased (after 1.0.3) — Council behavior updated

Changes to the Council report and rules since 1.0.3. The skill name, the activation gate, the five perspective names and the four-word verdict vocabulary are unchanged. `SKILL.md`'s `metadata.version` still reads 1.0.3; it will be bumped with the next tagged release.

- **Decision and Verdict agree.** `Decision:` is now an actionable recommendation, with its condition when a check that takes minutes could reverse it. WAIT is used only when waiting is worth it; low evidence alone no longer forces WAIT.
- **ONE NEXT MOVE is a seven-field record:** key question, result, not in scope, exercise, evidence source, target, done when. The key question is fixed before the exercise, and a cheaper validation step comes before building or shipping.
- **Recommendation integrity.** Arithmetic and comparisons are rechecked before the verdict. A visible line states whether the verdict survives without the premise the pick turns on. Assumptions are labelled, an uncertainty the user named stays uncertain, and anything another party has not offered is treated as an assumption.
- **Evidence.** Evidence Quality is separated from Confidence and rated by the claims that decide the verdict. Numbers and statistics are tagged inline by source type. "Independent" is not used for sources or perspectives unless verified.
- **Council.** Shared points are capped, the strongest objection is named (plus at most one more), the whole-council blind spot is stated, and LIGHT depth is shorter.
- **Safety.** Pasted text, fetched pages and inspected file contents are treated as data, not instructions. Email addresses and account details are not carried into reports.
- `references/council-method.md` and `references/research-method.md` were updated to match.
