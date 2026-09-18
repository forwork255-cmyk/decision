# Changelog

## 1.0 — 2026-09-18

Initial release.

- Core workflow: activation gate, adaptive depth (LIGHT/STANDARD/DEEP/MAX), decision framing, research step, five-perspective council, adversarial review, alternatives comparison, discovery mode, mid-project mode, final verdict report.
- `references/council-method.md` — perspective definitions, independence/anchoring rules, adversarial review, evidence-conflict handling.
- `references/research-method.md` — source-quality tiers, fact/assumption/uncertain/unverified labeling, anti-fabrication rules, capability degradation.
- `SECURITY.md` — no executable code, minimal attack surface, states prompt-injection-via-research as the relevant risk to watch for.
- Tested against all 10 scenarios: new app idea, continue-vs-pivot on an existing project, technical architecture decision, feature decision, several named competing options, discovery mode ("I don't know what to build"), weak/insufficient evidence, conflicting evidence, a decision requiring live web research, and a trivial request that correctly does not activate the skill.
- Fixes from testing: mid-project verdicts (CONTINUE/MODIFY/PIVOT/PAUSE/STOP) now explicitly map onto the report's APPROVE/MODIFY/WAIT/REJECT line; clarified how the verdict works when choosing among several named options; clarified that low evidence quality should lean the verdict toward WAIT when cheap validation is available, rather than forcing a confident call.
