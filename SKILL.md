---
name: decision-council
description: Structured decision analysis for builders deciding whether an idea, feature, architecture, pivot, or in-progress project is worth pursuing. Use when a meaningful decision exists with real uncertainty and multiple paths — new app/product ideas, "should I build X or Y", "should I continue or pivot this project", feature or architecture calls, or "I don't know what to build". Do not use for routine coding, formatting, small bug fixes, or simple factual questions.
license: MIT
metadata:
  version: "1.0"
  category: decision-analysis
---

# Decision Council

Purpose: **don't build blindly — investigate first.** Help the user decide whether something is worth pursuing (or continuing) *before* they spend significant time or money on it. This is a decision-analysis skill, not a general research, coding, or code-review skill — don't take over tasks that belong to other skills.

## 0. Should the Council even run?

Skip this skill for trivial requests: routine coding changes, formatting, small bug fixes, simple factual lookups, or anything with no real uncertainty or alternative path. When uncertain, default to **not** activating — answer directly instead.

Run it when the user is facing a real decision: a new idea, a build-vs-alternative choice, a continue/pivot/stop call on existing work, a feature or architecture decision, or "I don't know what to build" (Discovery Mode, §5 below).

## 1. Pick a depth

Match effort to the decision's importance. Say which depth you're using and why.

| Depth | When | Roughly |
|---|---|---|
| LIGHT | Small, low-stakes, easily reversible | Skip formal research; 2-3 perspectives; short verdict |
| STANDARD | Normal product/feature/technical decisions | Targeted research; full 5-perspective council; adversarial pass |
| DEEP | Significant time/money at stake, real uncertainty | Broader research; full council; explicit alternatives comparison |
| MAX | User asks for it, or stakes are unusually large | Everything in DEEP plus wider source coverage and more rigorous conflict-checking |

Default to the smallest depth that can responsibly answer the question. Don't run MAX-depth analysis on a light decision.

## 2. Understand the decision

Before researching anything, pin down:
- what the user actually wants to accomplish, and for whom
- what problem is being solved
- what is being proposed (the actual decision, not a vague topic)
- what alternatives already exist in the user's own framing
- what assumptions are being made
- what evidence would actually change the answer

Make reasonable assumptions rather than interrogating the user with unnecessary questions. Label important assumptions explicitly instead of asking about everything.

If project files, code, or prior context are available and relevant (mid-project decisions), inspect them before concluding anything about current state, architecture, or technical debt. Never claim to have inspected something you didn't.

## 3. Research reality (only what's relevant)

Research is a means, not a ritual — see `references/research-method.md` for source tiers, fact/assumption/uncertain labeling, and rules against fabrication.

Use whatever real capabilities the current host provides (web search, browser, filesystem, data analysis, subagents, connectors). If a capability isn't available, say so plainly and adapt — never pretend research happened that didn't.

Stop researching once more research is unlikely to change the conclusion. Don't pad the report with tangential findings.

## 4. Run the council

See `references/council-method.md` for full detail. Summary:

- **Five core perspectives**, each asking a genuinely different question: Contrarian (how could this fail?), First Principles (right problem?), Expansionist (what upside are we missing?), Outsider (what would a fresh eyes see?), Executor (can this actually be built and run?).
- Add specialist perspectives (e.g. Security, Financial, Legal, Data) only when they'd materially change the answer — not by default.
- If the host supports independent subagents, run the core perspectives in parallel and independently (no anchoring on each other). If not, reason through them sequentially but keep them analytically separate — don't just relabel one opinion five times, and don't claim independence you didn't have.
- After the initial analysis, run an **adversarial pass** against the council's own output: weak reasoning, unsupported claims, bias, missed alternatives, opportunity cost. Ask directly: "what did the whole council miss?" Quality of argument beats vote count — a 4-1 split doesn't make the 4 right.
- Compare against real alternatives to the user's proposed approach (different scope, different target user, different business model, doing nothing) — don't only evaluate the one option as framed.

## 5. Discovery mode ("I don't know what to build")

Don't generate generic trendy app ideas. Use available context about the user's goals/skills, research real unmet needs or gaps, generate a short list of plausible opportunities, and run a lighter version of the council over the most promising 1-3 before recommending which deserve real validation.

## 6. Mid-project mode

When something is already partly built: inspect what actually exists (don't assume), compare current evidence against original assumptions, and pick one of **CONTINUE / MODIFY / PIVOT / PAUSE / STOP**. Explicitly guard against sunk-cost reasoning — money or time already spent is not evidence the plan is sound.

When writing the final report (§7), map this onto the report's `Verdict:` line so the format stays consistent across modes: CONTINUE → APPROVE, MODIFY/PIVOT → MODIFY, PAUSE → WAIT, STOP → REJECT. State the mid-project word (e.g. "PIVOT") in the "What We Found" / decision line so nothing is lost in the mapping.

## 7. Final verdict

Always resolve to exactly one of: **APPROVE / MODIFY / WAIT / REJECT**. Never hide behind "it depends" when a useful provisional call is possible. The verdict follows from evidence and argument quality, not a vote count.

Report using this structure:

```
# 🏛️ COUNCIL VERDICT

Decision: [one sentence]
Verdict: APPROVE / MODIFY / WAIT / REJECT
Confidence: LOW / MEDIUM / HIGH
Evidence Quality: LOW / MEDIUM / HIGH
Council Effort: LIGHT / STANDARD / DEEP / MAX

## What We Found
## Strongest Evidence For
## Strongest Evidence Against
## Where the Council Agrees
## Where the Council Disagrees
## Critical Assumptions
## Alternatives Considered
## Biggest Blind Spot
## Biggest Risk
## What Would Change the Verdict?

# ONE NEXT MOVE
[the single most useful next action — not a task list]
```

For LIGHT-depth calls, a shorter version of this (verdict + 3-4 key lines + one next move) is fine — don't force the full template on a small decision.

Close serious research-driven verdicts with:

> AI-assisted decision support: this analysis is not a guarantee of outcomes. Conclusions may be incomplete or wrong due to model limitations, incomplete information, weak or conflicting sources, or changes in the real world. Verify critical decisions independently.

## Portability notes

This skill's methodology does not depend on any specific model, host, search provider, or subagent API. Host-specific capabilities (subagents, web search, file access) are used opportunistically when available and the workflow degrades gracefully — sequential reasoning instead of parallel subagents, stated research limitations instead of fabricated findings — never silently, and never by pretending an unavailable capability was used.
