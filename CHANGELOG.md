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
