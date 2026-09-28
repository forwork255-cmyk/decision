# Registered verified-mode test cases (registered BEFORE any generation, 2026-09-28)

Three new representative cases, none overlapping the six exposed production-lightfix cases
(L1-L3, N1-N3) or the earlier EASY/MEDIUM/HARD set. One generation call per case (3 total),
no retries, no rerun after seeing outcomes.

**Known, disclosed scope limitation (not being tested here, stated up front):** the ratio
checker derives one complement per polarity-pair label per source text; a source describing
two different entities under the same polarity wording (e.g. two vendors both framed as
"on time") would only check the first entity found. All three cases below are single-entity
by design, to stay within tested scope -- this limitation is reported as-is, not hidden.

## V1 -- LIGHT case
> "I keep forgetting my black umbrella by the door because it blends into the wall and I
> walk right past it. A $5 bright-orange stand insert would make it visible; I can buy one
> this weekend, it needs no installation, and it's returnable within 30 days if it doesn't
> help. Should I get the colored insert or keep the umbrella where it is?"

**Pass criterion (registered in advance):** the verifier's LIGHT-form output must be
factually accurate against manual inspection of the actual response -- VERIFIED only if
there is truly no forbidden heading, the response is truly under 400 words, and all 7
ONE NEXT MOVE fields are truly present; NEEDS REVIEW only if at least one of those is truly
violated, with the stated reason matching the real violation.

## V2 -- ratio/complement case (single entity, on-time/late pattern)
> "Our on-call plumbing vendor was on time for 7 of the last 10 emergency callouts we
> logged. Their new contract would raise the base fee from $300/month to $420/month, with
> the same callout terms otherwise. We expect about 10 callouts over the next quarter.
> Should we accept the new contract or look for a different vendor?"

**Pass criterion (registered in advance):** if the response states any count of late/missed
callouts, VERIFIED requires that count to truly equal 3 (10-7); NEEDS REVIEW is correct only
if the response's stated count truly does not equal 3, or the response makes no checkable
late/missed-count claim at all (in which case VERIFIED is correct, since there is nothing to
contradict).

## V3 -- arithmetic case
> "A community garden is choosing between Compost Service A ($45/month flat, handles up to
> 200kg) and Service B ($30/month plus $0.10/kg for anything over an included 150kg). We
> expect about 180kg/month. Which service is cheaper at our expected volume, and how many kg
> would it take to change the answer?"

**Pass criterion (registered in advance):** if the response writes out an explicit
"<expr> = <result>" arithmetic statement, VERIFIED requires every such statement to truly
compute correctly (checked independently by hand: B's monthly cost at 180kg is
30 + 0.10x30 = $33; breakeven is 30 + 0.10(x-150) = 45 -> x = 300kg); NEEDS REVIEW is correct
only if at least one written-out statement truly miscomputes, or an expression could not be
safely evaluated.

## Overall
Each case's real outcome is reported as-is after the single generation call, including
whether the registered pass criterion was actually met -- not adjusted afterward.
