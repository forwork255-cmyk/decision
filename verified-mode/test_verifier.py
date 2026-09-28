#!/usr/bin/env python3
"""No-model tests for verifier.py. Every case is a synthetic source+response snippet, not a
real generation. Run: python test_verifier.py"""
import sys
sys.dont_write_bytecode = True
import verifier as v

tests, fails = [], []


def check(name, cond, detail=""):
    tests.append(name)
    if not cond:
        fails.append((name, detail))


# ---------- the known regression: must be caught, digit-word and both directions ----------

SRC_DIGITS = "Supplier A offers 45 meals for $135 and delivered on time for two of the last three events I know about."
BAD_DIGITS = "Call Supplier A and ask what caused the two prior late deliveries."
r = v.verify(SRC_DIGITS, BAD_DIGITS)
check("regression (word source, word 'two' response): NOT VERIFIED", r["status"] == "NEEDS REVIEW")
check("regression: contradiction reason present",
      any("numeric contradiction" in x for x in r["reasons"]), r["reasons"])
check("regression: expected=1, found=2 recorded",
      any(f["expected"] == 1 and f["found"] == 2 for f in r["detail"]["ratio_findings"]))

SRC_D2 = "Supplier A was on time for 2 of the last 3 events."
BAD_D2 = "Ask about the 2 prior late deliveries from Supplier A."
r2 = v.verify(SRC_D2, BAD_D2)
check("regression (digit source, digit response): NOT VERIFIED", r2["status"] == "NEEDS REVIEW")

# ---------- correct statements must be accepted (not falsely flagged) ----------

GOOD_WORDS = "Ask what caused the one prior late delivery from Supplier A."
rg = v.verify(SRC_DIGITS, GOOD_WORDS)
check("correct statement (words): VERIFIED", rg["status"] == "VERIFIED", rg["reasons"])

GOOD_DIGITS = "Ask about the 1 late delivery."
rg2 = v.verify(SRC_D2, GOOD_DIGITS)
check("correct statement (digits): VERIFIED", rg2["status"] == "VERIFIED", rg2["reasons"])

# ---------- must NOT be a bare "digits 2 and 3 occur somewhere" regex ----------

DISTRACTOR = "We have 2 apples and 3 oranges on the table, plus one late delivery from Supplier A."
rd = v.verify(SRC_DIGITS, DISTRACTOR)
check("distractor digits (2, 3) elsewhere don't cause a false contradiction", rd["status"] == "VERIFIED", rd["reasons"])
# same distractor but WITH the wrong claim too -- must still catch it despite the noise
DISTRACTOR_BAD = "We have 2 apples and 3 oranges on the table. Ask about the two late deliveries."
rdb = v.verify(SRC_DIGITS, DISTRACTOR_BAD)
check("distractor digits don't mask a real contradiction", rdb["status"] == "NEEDS REVIEW")

# ---------- other-polarity registry pair ----------

SRC_SUCC = "The campaign was successful for 9 of the 12 attempts we tracked."
BAD_SUCC = "There were 2 failed attempts to investigate."
rs = v.verify(SRC_SUCC, BAD_SUCC)
check("success/failed pair: catches wrong complement (expected 3, got 2)", rs["status"] == "NEEDS REVIEW")
GOOD_SUCC = "There were 3 failed attempts to investigate."
rs2 = v.verify(SRC_SUCC, GOOD_SUCC)
check("success/failed pair: accepts correct complement", rs2["status"] == "VERIFIED", rs2["reasons"])

# ---------- unmatched pattern -> no claim to check (not falsely VERIFIED, not falsely rejected) ----------

SRC_NOPAIR = "The warehouse holds 9 of 12 pallet slots."  # no registered polarity keyword nearby
UNMATCHED = "The remaining 3 slots are empty."
ru = v.verify(SRC_NOPAIR, UNMATCHED)
check("no registered polarity pair -> no ratio finding recorded, VERIFIED (nothing checkable here)",
      ru["status"] == "VERIFIED" and ru["detail"]["ratio_findings"] == [], ru)

# ---------- arithmetic checker ----------

GOOD_ARITH = "Net profit: 3 x $80 - $120 = $120."
ra = v.verify("irrelevant source text", GOOD_ARITH)
check("correct arithmetic: VERIFIED", ra["status"] == "VERIFIED", ra["reasons"])

BAD_ARITH = "Net profit: 3 x $80 - $120 = $200."
rb = v.verify("irrelevant source text", BAD_ARITH)
check("incorrect arithmetic: NOT VERIFIED", rb["status"] == "NEEDS REVIEW")
check("incorrect arithmetic: reason names the contradiction",
      any("arithmetic contradiction" in x for x in rb["reasons"]), rb["reasons"])

DIV_ARITH = "Breakeven: 120 / 6 = 20 sessions."
rdv = v.verify("irrelevant", DIV_ARITH)
check("division arithmetic: VERIFIED", rdv["status"] == "VERIFIED", rdv["reasons"])

DIV_ARITH_WRONG = "Breakeven: 120 / 6 = 15 sessions."
rdvw = v.verify("irrelevant", DIV_ARITH_WRONG)
check("wrong division: NOT VERIFIED", rdvw["status"] == "NEEDS REVIEW")

# ---------- LIGHT form checker ----------

LIGHT_CLEAN = """# COUNCIL VERDICT

Decision: Attach the clip tonight.
Verdict: APPROVE
Confidence: HIGH
Evidence Quality: HIGH
Council Effort: LIGHT

Key reasons here, short.

# ONE NEXT MOVE
- Key question: will it hold? (feasibility)
- Result: it stays attached or it doesn't.
- Not in scope: none.
- Exercise: attach it tonight.
- Evidence source: new behavior observed.
- Target: the clip.
- Done when: checked once tomorrow morning.
"""
check("clean LIGHT report: no form violations", v.check_light_form(LIGHT_CLEAN) == [])

LIGHT_WITH_HEADING = LIGHT_CLEAN.replace("Key reasons here, short.", "## What We Found\nKey reasons here.")
viol = v.check_light_form(LIGHT_WITH_HEADING)
check("LIGHT report with a STANDARD-only heading: flagged", any("STANDARD-only heading" in x for x in viol), viol)

LIGHT_LONG = LIGHT_CLEAN.replace("Key reasons here, short.", "word " * 450)
viol2 = v.check_light_form(LIGHT_LONG)
check("LIGHT report over 400 words: flagged", any("word cap" in x for x in viol2), viol2)

LIGHT_BOUNDED_WINDOW = LIGHT_CLEAN.replace(
    "Done when: checked once tomorrow morning.",
    "Done when: two weeks have passed, or the item has been used at least 3 times, whichever comes first.")
check("bounded-window Done-when is NOT flagged (explicitly preserved as valid)",
      v.check_light_form(LIGHT_BOUNDED_WINDOW) == [])

LIGHT_MISSING_FIELD = LIGHT_CLEAN.replace("- Target: the clip.\n", "")
viol3 = v.check_light_form(LIGHT_MISSING_FIELD)
check("missing ONE NEXT MOVE field: flagged", any("missing field" in x for x in viol3), viol3)

STANDARD_REPORT = LIGHT_CLEAN.replace("Council Effort: LIGHT", "Council Effort: STANDARD")
check("STANDARD-depth report: this checker has nothing to say (not its scope)",
      v.check_light_form(STANDARD_REPORT) == [])

# ---------- end-to-end: full LIGHT report carrying the known regression ----------

FULL_BAD = LIGHT_CLEAN.replace(
    "Key reasons here, short.",
    "Contrarian: with " + SRC_DIGITS.split("Supplier A ")[1] + " ask about the two prior late deliveries.")
rfull = v.verify(SRC_DIGITS, FULL_BAD)
check("full LIGHT report carrying the regression: NOT VERIFIED", rfull["status"] == "NEEDS REVIEW")

print("%d/%d tests passed" % (len(tests) - len(fails), len(tests)))
if fails:
    for name, detail in fails:
        print("  FAIL:", name, "--", detail)
    sys.exit(1)
print("ALL PASS")
