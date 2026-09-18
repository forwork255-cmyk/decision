# Council Method

Detail behind the "run the council" step in `SKILL.md`. Read this when actually running a STANDARD+ depth council.

## Core perspectives

Use all five for STANDARD/DEEP/MAX. For LIGHT depth, 2-3 of the most relevant are enough — say which ones you dropped and why.

1. **Contrarian** — "How could this fail?" Look for fatal assumptions, weak or unproven demand, competitive risk, bad incentives, likely failure modes.
2. **First Principles** — "Are we solving the right problem?" Strip away the proposed solution and examine the underlying problem and mechanism directly. Sometimes the right answer is a different problem entirely.
3. **Expansionist** — "What upside are we missing?" Adjacent markets, a stronger version of the same idea, alternative use cases, alternative business models, second-order opportunities.
4. **Outsider** — "What would someone without our assumptions see?" Normal-user perception, obvious flaws insiders stop noticing, confusing value propositions.
5. **Executor** — "Can this actually be built, launched, and maintained?" Engineering complexity, time, cost, operational burden, dependencies, realistic constraints for *this* user's resources.

Keep these genuinely distinct. Don't force artificial disagreement, but don't let four of them collapse into restating the same point either.

## Adding specialists

Only add a specialist perspective (Data Analyst, Market Researcher, Competitive Intel, Security, Financial, Legal/Compliance, UX, AI/ML, Infrastructure, domain expert) when it would materially change the answer. Use the smallest council that can responsibly answer the question — more voices is not more rigor.

## Independent execution

- **Subagents available:** launch the core perspectives independently and in parallel, without letting later ones see earlier answers — this avoids anchoring. State your own tentative read of the decision *before* dispatching them, and don't let it leak into their prompts.
- **Subagents unavailable:** perform each perspective as a distinct, sequential reasoning pass. Keep them analytically separate (each should reach its own conclusion from its own angle) but never claim they ran as independent agents — say plainly that they were reasoned through sequentially.

## Adversarial review

After the five perspectives produce their views, turn on the council itself:

- Weak reasoning, unsupported claims, confirmation/survivorship/selection bias, circular reasoning
- Hidden assumptions and contradictory evidence
- Overlooked alternatives and opportunity cost
- Technical and business risks nobody flagged

Ask explicitly: **"what did the entire council miss?"**

Do not resolve this by counting votes. A 4-1 or 5-0 split is not itself evidence — trace *why* the outlier (or everyone) reached their conclusion and judge the argument.

## Evidence conflicts vs. reasoning disagreement

- **Reasoning disagreement** (same facts, different interpretation): present both readings, explain the interpretive difference, let the verdict weigh which reading the evidence better supports.
- **Evidence conflict** (credible sources disagree about what's factually true): try to verify the underlying claim directly rather than picking a side by preference or majority.

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
