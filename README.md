# Decision Council

A portable [Agent Skill](https://agentskills.io/specification) that helps you decide whether an idea, feature, architecture, pivot, or already-started project is worth pursuing — **before** you spend significant time or money on it.

> Don't build blindly. Investigate first.

## What it does

Point it at a decision — a new app idea, "should I build X or Y", "should I keep going with this project", a feature call, an architecture choice, or "I don't know what to build" — and it:

1. Understands what's actually being decided and for whom.
2. Researches relevant real-world evidence (when the host has web/browser/data access), tagging findings as fact / assumption / uncertain / unverified.
3. Runs five distinct reasoning perspectives (Contrarian, First Principles, Expansionist, Outsider, Executor), independently where the host supports it.
4. Challenges its own council's conclusions (bias, missed alternatives, weak evidence) instead of just counting votes.
5. Compares real alternatives to the proposed approach.
6. Returns one clear verdict: **APPROVE / MODIFY / WAIT / REJECT** — never "it depends."

It adapts effort to the decision (LIGHT / STANDARD / DEEP / MAX) and degrades gracefully when a host lacks a capability (no subagents → sequential reasoning; no web access → says so, doesn't fabricate).

## Install

Copy the `decision-council/` folder into your agent platform's skills directory (e.g. `.claude/skills/` for Claude Code). Any host that implements the [Agent Skills open standard](https://agentskills.io/) can load it — the skill has no Claude-specific dependencies.

## Files

- `SKILL.md` — the workflow the agent follows (loaded when the skill activates).
- `references/council-method.md` — detail on the five perspectives, independence, and adversarial review.
- `references/research-method.md` — source-quality tiers, evidence labeling, fabrication rules.

## Scope

This is a decision-analysis skill, not a general research, coding, or code-review skill. It activates on real decisions with genuine uncertainty and multiple paths — not on routine coding tasks, formatting, or simple factual questions.

## License

MIT — see [LICENSE](LICENSE).
