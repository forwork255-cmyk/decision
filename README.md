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

There are three ways to get this skill. If you're not sure which to use, use the first one.

**1. Recommended — download the release package.** Go to [Releases](https://github.com/forwork255-cmyk/universal-decision-council/releases), download `decision-council.zip` from the latest release, and unzip it. You'll get a folder already named exactly `decision-council/` — copy that whole folder into your agent platform's skills directory (e.g. `.claude/skills/`, so the final path is `.claude/skills/decision-council/`). No renaming needed.

**2. Cloning this repository.** `git clone` puts the skill files directly in the folder you cloned into — but that folder is named `universal-decision-council` (this repo's name), not `decision-council`. Rename it to `decision-council` before copying it into your skills directory.

**3. GitHub's "Code → Download ZIP" button.** This unpacks into a folder named `universal-decision-council-master/` — GitHub always names it after the repository and branch, never the skill. Rename the extracted folder to `decision-council` before installing it.

Why the renaming matters for options 2 and 3: the [Agent Skills spec](https://agentskills.io/specification) requires a skill's `SKILL.md` `name:` field (here, `decision-council`) to exactly match its containing folder name. A folder named `universal-decision-council` or `universal-decision-council-master` won't match, and some hosts will refuse to load it. Option 1 sidesteps this entirely, which is why it's recommended for anyone who isn't already comfortable with this rule.

Any host that implements the [Agent Skills open standard](https://agentskills.io/) can load this skill — it has no Claude-specific dependencies.

## Files

- `SKILL.md` — the workflow the agent follows (loaded when the skill activates).
- `references/council-method.md` — detail on the five perspectives, independence, and adversarial review.
- `references/research-method.md` — source-quality tiers, evidence labeling, fabrication rules, and the prompt-injection defense rule.
- `references/injection-test-fixture.md` — a repeatable test case for checking the prompt-injection defense rule still holds.
- `SECURITY.md` — this skill's attack surface and the one real risk to watch for.
- `CONTRIBUTING.md` — guidelines for changing this skill.
- `CHANGELOG.md` — release history and what's actually been validated.
- `LICENSE` — MIT.

## Scope

This is a decision-analysis skill, not a general research, coding, or code-review skill. It activates on real decisions with genuine uncertainty and multiple paths — not on routine coding tasks, formatting, or simple factual questions.

## License

MIT — see [LICENSE](LICENSE).
