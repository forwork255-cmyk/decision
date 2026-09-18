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

The skill is one folder named **`decision-council`**. Any of these three ways gives you exactly that folder:

**1. Easiest: GitHub's green Code button → Download ZIP.** Extract it. You get one folder, already named `decision-council`, containing `SKILL.md`. Move that folder into your agent's skills directory (below). No renaming.

**2. The release ZIP.** Same result and same contents, from the [Releases page](https://github.com/forwork255-cmyk/decision/releases) ([direct download](https://github.com/forwork255-cmyk/decision/releases/latest/download/decision-council.zip)).

**3. `git clone`.** Give the clone the skill's name, then drop the git data:

```bash
git clone https://github.com/forwork255-cmyk/decision.git decision-council
rm -rf decision-council/.git
```

(PowerShell: `Remove-Item -Recurse -Force decision-council\.git`.) The trailing `decision-council` matters: without it git names the folder `decision`.

**Where the folder goes:** inside your agent's skills directory, so the path ends in `.../skills/decision-council/SKILL.md`. For Claude Code that is `~/.claude/skills/decision-council/` (all projects) or `.claude/skills/decision-council/` (one project). For other Agent Skills tools, check that tool's documentation; the skill has no Claude-specific parts.

**One common trap (mainly Windows "Extract All"):** the tool may wrap the ZIP in an extra outer folder, giving `decision-council\decision-council\SKILL.md`. Move the inner folder, the one that directly contains `SKILL.md`. If you move the outer one, the skill will not be found.

**Check it worked:** start a new session in your agent; the skill should be listed as `decision-council`.

**Why the repository is called `decision` and its default branch `council`:** GitHub names the Download-ZIP folder `<repository>-<branch>`, so this pair produces exactly `decision-council`. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before renaming either. Tools such as Claude Code name a skill after its folder, and the [Agent Skills spec](https://agentskills.io/specification) requires the folder to match the `name:` in `SKILL.md`, which is why the folder name matters.

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
