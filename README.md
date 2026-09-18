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

Two names are involved, and they are not the same: the **repository** is called `universal-decision-council`, but the **skill** is called `decision-council`. Your agent needs a folder named exactly `decision-council` (it must match the `name:` line in `SKILL.md`). The three ways below differ only in how much renaming you have to do.

**Where the folder goes:** inside your agent's skills directory, so the final path ends in `.../skills/decision-council/SKILL.md`. For Claude Code that is `~/.claude/skills/decision-council/` (all your projects) or `.claude/skills/decision-council/` (one project). For other Agent Skills tools, check that tool's documentation for its skills directory; the skill itself has no Claude-specific parts.

### 1. Recommended: the release ZIP (no renaming)

1. Download [decision-council.zip](https://github.com/forwork255-cmyk/universal-decision-council/releases/latest/download/decision-council.zip) (all releases: [Releases page](https://github.com/forwork255-cmyk/universal-decision-council/releases)).
2. Unzip it. You get one folder, already named `decision-council/`.
3. Move that folder into your skills directory (see above).

### 2. Cloning the repository

Clone straight into a correctly named folder, then remove the git data:

```bash
git clone https://github.com/forwork255-cmyk/universal-decision-council.git decision-council
rm -rf decision-council/.git
```

(PowerShell: `Remove-Item -Recurse -Force decision-council\.git`.) Then move `decision-council/` into your skills directory. If you cloned without the trailing `decision-council` name, rename the folder yourself first.

### 3. GitHub's "Code → Download ZIP" button (needs a rename)

This unpacks into `universal-decision-council-master/`. GitHub always names that folder after the repository and branch, never the skill, so it will not match. Rename the extracted folder to `decision-council` before moving it into your skills directory. It also contains a few repo-only files (such as `ROADMAP.md`); they are harmless.

### Why the name matters

The [Agent Skills spec](https://agentskills.io/specification) requires the `name:` field in `SKILL.md` (`decision-council`) to match its containing folder. A folder called `universal-decision-council` or `universal-decision-council-master` does not match, and some tools will refuse to load the skill. Option 1 avoids this entirely.

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
