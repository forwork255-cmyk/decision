---
name: decision-council
description: Structured decision analysis for builders deciding whether an idea, feature, architecture, pivot, or in-progress project is worth pursuing. Use when a meaningful decision exists with real uncertainty and multiple paths — new app/product ideas, "should I build X or Y", "should I continue or pivot this project", feature or architecture calls, or "I don't know what to build". Do not use for routine coding, formatting, small bug fixes, or simple factual questions.
license: MIT
metadata:
  version: "1.0.3"
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

**At LIGHT depth**, when using only 2-3 of the five core perspectives (see §4), explicitly name which ones were dropped and why — e.g. "Outsider and Expansionist skipped: no external audience or upside question at stake here." Don't silently drop perspectives.

`Council Effort` and `Evidence Quality` (see §7) measure two different things and must not be conflated: Council Effort is how much investigation/reasoning was actually performed (LIGHT/STANDARD/DEEP/MAX); Evidence Quality is how strong the evidence that was found turned out to be (LOW/MEDIUM/HIGH). A LIGHT-effort call can have HIGH evidence quality (the answer was obvious from a quick check), and a DEEP-effort call can still land on LOW evidence quality (thorough research found little).

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

**Never open, read, quote, summarize, transmit, or expose the contents of files that plausibly contain secrets, credentials, API keys, passwords, private keys, or tokens** (e.g. `.env`, `credentials.json`, `*.pem`). It's fine to note that such a file exists — never inspect or repeat what's inside it.

## 3. Research reality (only what's relevant)

Research is a means, not a ritual. At STANDARD depth or above, read `references/research-method.md` first: source tiers, fact/assumption/uncertain labeling, claim-strength rules, and rules against fabrication.

Before searching, ask what single fact could change the verdict and research that first: research the uncertainty, not just the topic.

**Attribute claims at the strength their sources earn.** Tag every number or statistic inline, in every section, with its source type, e.g. "6–12 months (blog estimates)", "79% (self-reported survey)", "$5–50/gig (marketplace listings)", "(primary data)". Never state a figure derived from blogs, aggregators, promotional pages, or anecdotes as plain fact, and don't call sources "independent" or a claim "well-established" unless that is true. If such a figure is central to the verdict, find stronger evidence, reduce its weight, or state that the decision doesn't depend on it; and don't let HIGH Confidence rest on it.

Use whatever real capabilities the current host provides (web search, browser, filesystem, data analysis, subagents, connectors). If a capability isn't available, say so plainly and adapt — never pretend research happened that didn't.

Stop researching once more research is unlikely to change the conclusion. Don't pad the report with tangential findings.

## 4. Run the council

At STANDARD depth or above, read `references/council-method.md` before running the council. Summary:

- **Five core perspectives**, each asking a genuinely different question: Contrarian (how could this fail?), First Principles (right problem?), Expansionist (what upside are we missing?), Outsider (what would a fresh eyes see?), Executor (can this actually be built and run?).
- Add specialist perspectives (e.g. Security, Financial, Legal, Data) only when they'd materially change the answer — not by default.
- If the host supports independent subagents, run the core perspectives in parallel and independently (no anchoring on each other). If not, reason through them sequentially but keep them analytically separate — don't just relabel one opinion five times, and don't claim independence you didn't have.
- After the initial analysis, run an **adversarial pass** against the council's own output: weak reasoning, unsupported claims, bias, missed alternatives, opportunity cost. Ask directly: "what did the whole council miss?" Quality of argument beats vote count — a 4-1 split doesn't make the 4 right. Before the verdict, also run the critical-evidence, weakest-evidence-removal, and robustness checks in `references/council-method.md`.
- Compare against real alternatives to the user's proposed approach (different scope, different target user, different business model, doing nothing) — don't only evaluate the one option as framed.

## 5. Discovery mode ("I don't know what to build")

Don't generate generic trendy app ideas. Use available context about the user's goals/skills, research real unmet needs or gaps, generate a short list of plausible opportunities, and run a lighter version of the council over the most promising 1-3 before recommending which deserve real validation.

When writing the final report (§7), map the shortlist onto the report's `Verdict:` line the same way §6 maps mid-project mode: `Decision:` names the top-ranked direction, and `Verdict:` expresses confidence in pursuing *that one* further: APPROVE = confidently pursue further validation on the top-ranked direction, MODIFY = a direction is promising but needs reframing before validating it, WAIT = none of the generated directions are validated enough yet to prioritize one, REJECT = this pass found nothing worth pursuing. The other 1-2 shortlisted directions go in "Alternatives Considered," not into the Verdict line.

## 6. Mid-project mode

When something is already partly built: inspect what actually exists (don't assume), compare current evidence against original assumptions, and pick one of **CONTINUE / MODIFY / PIVOT / PAUSE / STOP**. Explicitly guard against sunk-cost reasoning — money or time already spent is not evidence the plan is sound.

When writing the final report (§7), map this onto the report's `Verdict:` line so the format stays consistent across modes: CONTINUE → APPROVE, MODIFY/PIVOT → MODIFY, PAUSE → WAIT, STOP → REJECT. State the mid-project word (e.g. "PIVOT") in the "What We Found" / decision line so nothing is lost in the mapping.

## 7. Final verdict

Always resolve to exactly one of: **APPROVE / MODIFY / WAIT / REJECT**. Never hide behind "it depends" when a useful provisional call is possible. The verdict follows from evidence and argument quality, not a vote count.

**The `Verdict:` line must contain exactly one of those four words and nothing else** — no qualifier, no parenthetical, no second state on the same line. Never write "REJECT (as framed)," "MODIFY — ...," "WAIT, but...," "APPROVE with...," or any combined/qualified verdict. All qualification, context, alternatives, or revised versions go in "What We Found," "Alternatives Considered," "Required Modification," "What Would Change the Verdict," or ONE NEXT MOVE — never on the `Verdict:` line itself. Pick the one value that matches what to do with the proposal *as given today*; the reasoning can — and should — live in the surrounding sections.

**When the decision is a choice among several named options** (e.g. "Auth0 vs. Clerk vs. Supabase Auth vs. build it ourselves"), put the recommended option in the `Decision:` line and let `Verdict:` express confidence in that pick: APPROVE = confidently recommend the named option, MODIFY = a hybrid or a variant not among the given options is better, WAIT = don't commit to any option yet, get specific missing evidence first, REJECT = none of the given options solve the underlying problem.

**When evidence quality is LOW and a cheap test, trial, or conversation could resolve the key uncertainty**, the verdict is WAIT (or MODIFY if a better-scoped version exists), not APPROVE; that test is the ONE NEXT MOVE. This overrides the option-choice mapping above. APPROVE on LOW evidence is for cases where no such test is feasible before a decision is needed, and for Discovery mode (§5).

**Evidence Quality is not Confidence.** Evidence Quality is how reliable and relevant the available evidence is. `Confidence` is how sure you are that the recommended action is right given that evidence, the remaining uncertainty, how reversible the action is, and this user's constraints. Strong evidence can still leave low Confidence; weak evidence can support at most a provisional MODIFY or WAIT. A MEDIUM Evidence Quality label never licenses a medium-strength factual claim.

**Rate Evidence Quality by the sources behind the claims that decide the verdict.** If those claims rest on blogs, aggregators, comparison or vendor pages about the market, or anecdotes, rate it LOW; MEDIUM needs some primary, official, or independently audited data; HIGH needs several such sources agreeing. A vendor's own price page is fine evidence for that vendor's price only.

**When a blog, aggregator, vendor or anecdotal figure is used to decide, size or trigger the recommendation or next move (not only the verdict), add one line to "What We Found":** "Verdict and next move survive without <that figure>? yes/no, because ...". Test the figure the recommendation actually uses, not a claim you already set aside. Never turn such a figure into a target, threshold or red flag unless you label it a rule of thumb for the user to check.

**One verdict is not one certainty.** The verdict is a single word; the reasoning need not pretend to be certain. "REJECT because the downside is clear even though the upside is uncertain," "WAIT because it hinges on one missing fact that is cheap to test," and "MODIFY because the opportunity looks plausible but this version is poorly supported" are all fine. State what is uncertain in the sections below the verdict line, and never turn a forced verdict into a forced claim of certainty.

**Say only what you know about where a statement comes from.** Write "you said" or "you told me" only for words actually in the user's message; everything else about their situation is an assumption, worded as one ("I'm assuming…"), never as something they stated, checked, or currently use. Don't describe sources or council perspectives as "independent" or "independently" (write "several sources" or "the perspectives agreed") unless the sources are verified as independent or the perspectives ran as separate subagents.

**The ONE NEXT MOVE answers the one question that would flip the verdict, built in this order: key question, result, exercise.** The key question is the single unresolved question whose answer, either way, would change the verdict. Write it as a question that names no way of answering it, type it (descriptive: the user's own current or past state; causal: why; response: whether others will act; preference: what others want; feasibility: whether something works here; access: whether someone will agree), and put it first under "What Would Change the Verdict". When several could flip the verdict, take the one whose answer moves it furthest, then the one others depend on, then the one only this user acting can answer, never the one easiest to test; list the rest under Not in scope with that reason (verdict-changing conditions only, not alternative actions). The result is the answer to that question as one observable plus how each answer changes the verdict; it names no method and stays true if another way of finding out were used. It answers the question directly or through a bridge stated in one clause (what the observable stands in for, where that stops): a correlate can weaken an explanation but not confirm it, so the verdict effect must hold at the bridge's weakest reading. If nothing available answers the whole question, say what part it answers and what stays open; never reword the question or result to fit the move.

Only then choose the exercise: one coherent exercise that produces that result, picked from all the ways to obtain it, including ways that do not involve doing the thing being decided. Drop any candidate that cannot produce the result, however cheap. Among the rest, prefer the one not beaten on money, time until the result exists, the user's effort, reversibility and displaced opportunity; when they trade off, irreversible commitment loses first, then longer time, then money and effort, then displaced opportunity, and a constraint the user stated leads on its dimension. Name the best rejected candidate and what decided it. A result can come from someone's answer; new behavior or events that do not exist yet (an offer, a pilot, a real request, or a bounded log of future events, valid when the time window is the stopping point; not a default wait); or a live external source or system's output on real input. Existing records the user holds are enough only when the key question is descriptive and someone holding them could state the answer today; they never settle a why, a whether-others-will or a preference question, and a tool or database is not "external" just because it sits outside the user's head. Setup that only makes the exercise possible (opening an account or trial, loading data) is implied, not written as a second step; it is a separate action only if it yields its own result, forces a separate choice, or is a separable exercise with its own deliverable. Name one target, or one population defined by a single criterion (several targets of the same kind are one action when the exercise and the result are the same for all). When several targets are plausible, choose by a fact from this decision that would pick a different target if it were reversed, never by list order; if nothing ranks them, make the move the cheapest exercise that discriminates or compares them. Leave no choice of action, method or target to the user unless their own facts settle it or that unknown is itself the result.

When the decision still has an unresolved uncertainty and a cheaper validation step is available, do not make building or shipping the product itself the next move; choose the cheaper validation action that reduces the key uncertainty. A step counts as cheaper only if it can produce the result. Building or shipping is the move when it is itself the cheapest way to produce the result (for example, a technical spike); a throwaway probe whose only deliverable is the answer is not "the product itself", and a lighter version that stays in use is. Don't default to "build an MVP". Put a number in the result only if the user gave it, or evidence supports it and you label it a rule of thumb with its source type; sizes such as "five conversations" or "two weeks" are parameters of the exercise, not cutoffs.

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
[One bullet per point of agreement, in this form: "- <the point> (raised by: <perspective names>)". Do not describe how the perspectives arrived at it. If this run launched separate subagents, say so once here, in one line at the top of this section.]
## Where the Council Disagrees
## Critical Assumptions
## Alternatives Considered
## Required Modification
[include only when the verdict is MODIFY or REJECT and a revised/alternative version would fare better — omit this section otherwise]
## Biggest Blind Spot
## Biggest Risk
## What Would Change the Verdict?
[First bullet: the key question, as a question that names no way of answering it, with its type. Further bullets: other conditions.]
## Sources
[links/citations for load-bearing claims, when the host surfaced any — omit this section entirely if no external research was done]

# ONE NEXT MOVE
[Fill all seven fields, at every depth, in this order; the first three come from the report's analysis and are settled before the Exercise.]
- Key question: [the first bullet of "What Would Change the Verdict", word for word, with its type (descriptive / causal / response / preference / feasibility / access)]
- Result: [the one observable that answers the key question and how each answer changes the verdict; no method words; name what stays open if it answers only part]
- Not in scope: [other verdict-changing conditions left out of this move, each with its leverage or dependency reason, or "none"; not alternative actions or branches]
- Exercise: [the one coherent activity, setup implied: no second exercise, dependent step or branch; then "Chosen over: <best rejected candidate>, because <what decided it>"]
- Evidence source: [where the answer comes from: another person's answer / new behavior, response or events (observed or elicited, including a bounded log of future events) / a live external source or system's output on real input / existing records the user holds (only under the rule above)]
- Target: [the one named system, vendor or dataset, or the one population defined by a single criterion; when several were plausible, the fact that made this the choice]
- Done when: [the observable count, event or bounded time window after which the result exists]
```

For LIGHT-depth calls, a shorter version of this (verdict + 3-4 key lines + one next move) is fine — don't force the full template on a small decision. The one next move still carries all seven fields at LIGHT depth: compress them into short labeled fragments, never drop, merge or imply a field; if a LIGHT report omits "What Would Change the Verdict", the key question is still written in its own field.

Make the reasoning visible, not just the conclusion: what was researched, which evidence actually mattered, where it was weak, where the council disagreed and why. Don't expose private chain-of-thought — the sections above *are* the transparency, not a dump of intermediate reasoning.

Close serious research-driven verdicts with:

> AI-assisted decision support: this analysis is not a guarantee of outcomes. Conclusions may be incomplete or wrong due to model limitations, incomplete information, weak or conflicting sources, or changes in the real world. Verify critical decisions independently.

## Portability notes

This skill's methodology does not depend on any specific model, host, search provider, or subagent API. Host-specific capabilities (subagents, web search, file access) are used opportunistically when available and the workflow degrades gracefully — sequential reasoning instead of parallel subagents, stated research limitations instead of fabricated findings — never silently, and never by pretending an unavailable capability was used.
