# Council Method

Detail behind the "run the council" step in `SKILL.md`. Read this when actually running a STANDARD+ depth council.

## Core perspectives

Use all five for STANDARD/DEEP/MAX. For LIGHT depth, 2-3 of the most relevant are enough — say which ones you dropped and why.

1. **Contrarian** — "How could this fail?" Look for fatal assumptions, weak or unproven demand, competitive risk, bad incentives, likely failure modes.
2. **First Principles** — "Are we solving the right problem?" Strip away the proposed solution and examine the underlying problem and mechanism directly. Sometimes the right answer is a different problem entirely.
3. **Expansionist** — "What bigger upside or better option isn't being considered?" A stronger version of the same idea, an option missing from the user's list, adjacent markets or use cases, alternative business models, second-order opportunities.
4. **Outsider** — "What does this look like to the people it affects?" The assumptions, incentives and consequences for customers, users, partners or anyone else who lives with the outcome; obvious flaws insiders stop noticing.
5. **Executor** — "Can this actually be built, launched, and maintained?" Engineering complexity, time, cost, operational burden, dependencies, realistic constraints for *this* user's resources.

Keep these genuinely distinct. A perspective earns space in the report only when it adds a distinct assumption, consequence, alternative, objection, risk or decision-changing consideration; compress or omit what only repeats another. Don't force artificial disagreement, and don't make every perspective speak to fill space.

## Adding specialists

Only add a specialist perspective (Data Analyst, Market Researcher, Competitive Intel, Security, Financial, Legal/Compliance, UX, AI/ML, Infrastructure, domain expert) when it would materially change the answer. Use the smallest council that can responsibly answer the question — more voices is not more rigor.

## Independent execution

- **Subagents available:** launch the core perspectives independently and in parallel, without letting later ones see earlier answers — this avoids anchoring. State your own tentative read of the decision *before* dispatching them, and don't let it leak into their prompts.
- **Subagents unavailable:** perform each perspective as a distinct, sequential reasoning pass. Keep them analytically separate (each should reach its own conclusion from its own angle) but never claim they ran as independent agents — say plainly that they were reasoned through sequentially.

## Cross-examination (STANDARD+, on material disagreement or a material competing consideration)

After the initial perspectives, check two things, independently: whether any reach materially different conclusions (ones that would lead to a different verdict, pick or next move — differences of emphasis don't count), and whether the decision has a material competing consideration. Run the pass if either holds; skip it only when neither does, and never invent disagreement or a competing consideration to run it.

If there is material disagreement, run one compact pass:

- Each contested perspective names the strongest objection from a perspective that disagrees with it (the one that would most change its conclusion if true) and answers it.
- It then keeps or revises its position in one line, saying what changed its mind if it revised.
- One pass only: no further rounds, no voting, no new perspectives.
- **Subagents available:** give each contested perspective the opposing outputs in a fresh call. **Unavailable:** reason through the exchange sequentially and say so; never describe it as independent.

If there is a material competing consideration but no material disagreement, run one compact pass instead: the perspective best placed to weigh it tests the strongest form of that consideration against the recommendation and states plainly whether the recommendation holds up — without inventing an opposing perspective or a disagreement that didn't occur.

Carry the outcome into the adversarial review and into "Where the Council Disagrees", where it appears as one visible line. On material disagreement: `Cross-examination: <contested perspective> answered <the strongest opposing objection, in a few words>; <kept | revised> its position because <reason>.` On a competing consideration tested without disagreement: `Cross-examination: tested <the strongest form of the competing consideration>; recommendation unchanged because <reason>.` Also record any minority position that is still material. If there was neither material disagreement nor a material competing consideration, write no such line and don't invent one.

## Adversarial review

After the five perspectives produce their views (and any cross-examination), turn on the council itself:

- Weak reasoning, unsupported claims, confirmation/survivorship/selection bias, circular reasoning
- Hidden assumptions and contradictory evidence
- Overlooked alternatives and opportunity cost
- Technical and business risks nobody flagged
- Conclusions stated more strongly than the evidence under them (see `references/research-method.md`), such as a source that was labeled weak earlier but later used as if it were established

Ask explicitly: **"what did the entire council miss?"**

Do not resolve this by counting votes. A 4-1 or 5-0 split is not itself evidence — trace *why* the outlier (or everyone) reached their conclusion and judge the argument.

## Evidence conflicts vs. reasoning disagreement

- **Reasoning disagreement** (same facts, different interpretation): present both readings, explain the interpretive difference, let the verdict weigh which reading the evidence better supports.
- **Evidence conflict** (credible sources disagree about what's factually true): try to verify the underlying claim directly rather than picking a side by preference or majority.

## Before the verdict: critical evidence, unknowns, robustness

An internal check. Surface it in the report only when doing so makes the answer clearer.

1. **Critical Evidence:** the 1-3 pieces of evidence that actually drive the verdict.
2. **Critical Unknowns:** the 1-3 missing facts that could realistically change it.
3. **Decisive-premise test:** name the strongest viable alternative to the pick and the premise that most directly separates the two (`SKILL.md` §7), not the easiest figure to recompute. Set that premise aside and ask whether the pick still beats the alternative. If it doesn't, the verdict depends on that premise: go to step 4. If the weakest important evidence is a different premise, test it the same way.
4. **Robustness:** if the verdict would materially change without that evidence, research it further when that's practical, or lower `Confidence` and say the decision is sensitive to that uncertainty.

Don't become attached to a conclusion because you found a number that seems to support it.

## Alternatives comparison

Don't only judge the proposal as framed. Ask "is this the best way to solve the underlying problem?" and check it against realistic alternatives: smaller MVP, different target user (B2B vs B2C), different pricing/business model, integration instead of standalone product, service instead of software, or doing nothing.

## Keep decision questions separate

These can have different answers — don't collapse them into one verdict without saying so:

- Is the underlying problem real?
- Is the proposed solution actually useful for it?
- Is there a viable opportunity here at all?
- Is *this* approach/architecture sensible?
- Is it worth *this particular user*, with their resources, pursuing?

Example: Problem: yes. Solution: maybe. Opportunity: yes. Approach: no. → Verdict: MODIFY (keep the problem/opportunity, change the approach).

## Validation criteria (when proposing WAIT)

If the verdict is WAIT, name concrete, cheap ways to get the missing evidence: user interviews, a landing-page or pricing test, a small technical spike, a limited pilot. Only propose measurable thresholds ("validate if X% do Y") when there's a real basis for the number — don't invent precision to sound rigorous.

## Choosing the next move

The ONE NEXT MOVE should normally reduce the most important unresolved uncertainty that could change the action; when the decision already holds across plausible answers, it is the action itself or its first step (the action-now path in `SKILL.md` §7). Prefer moves that are cheap, fast, reversible, and produce real-world evidence based on behavior rather than compliments: contact potential customers, observe an existing workflow, ask what someone did recently (not what they say they would do), get a real payment commitment, apply to actual jobs, or run a small experiment. Don't default to "build an MVP"; recommend building only when the evidence says building is the next information-producing step.
