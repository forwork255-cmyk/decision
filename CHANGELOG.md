# Changelog

## 1.0 — 2026-09-18

Initial release.

- Core workflow: activation gate, adaptive depth (LIGHT/STANDARD/DEEP/MAX), decision framing, research step, five-perspective council, adversarial review, alternatives comparison, discovery mode, mid-project mode, final verdict report.
- `references/council-method.md` — perspective definitions, independence/anchoring rules, adversarial review, evidence-conflict handling.
- `references/research-method.md` — source-quality tiers, fact/assumption/uncertain/unverified labeling, anti-fabrication rules, capability degradation.
- `SECURITY.md` — no executable code, minimal attack surface, states prompt-injection-via-research as the relevant risk to watch for.
- Scenario coverage designed for 10 target cases (new app idea, continue-vs-pivot, technical architecture, feature decision, several named competing options, discovery mode, weak evidence, conflicting evidence, live web research, and a trivial request that should not activate the skill); reviewed by design-walkthrough against each case, but not yet independently validated end-to-end with real invocation transcripts.
- Fixes from that review: mid-project verdicts (CONTINUE/MODIFY/PIVOT/PAUSE/STOP) now explicitly map onto the report's APPROVE/MODIFY/WAIT/REJECT line; clarified how the verdict works when choosing among several named options; clarified that low evidence quality should lean the verdict toward WAIT when cheap validation is available, rather than forcing a confident call.
