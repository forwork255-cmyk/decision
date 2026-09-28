#!/usr/bin/env python3
"""Deterministic, code-only verifier for a prospective "verified mode" of Decision Council.

Scope (deliberately narrow -- this is a limited pattern-matcher, not an NLU system):

1. LIGHT report form/length: structural checks only (forbidden headings at LIGHT depth,
   word-count cap, exactly one Verdict line in the allowed vocabulary, all 7 ONE NEXT MOVE
   fields present). Does NOT police "Done when" content -- a bounded/finite future window
   is an explicitly valid form per the skill and is never flagged here.

2. Numerical claims, in two limited patterns only:
   a) Complementary-ratio claims: "<N1> of <N2> <polarity>" in the SOURCE (e.g. "on time for
      9 of 12", "two of the last three events") implies the opposite-polarity count is
      N2 - N1 (e.g. "late" = 12 - 9 = 3). If the RESPONSE states a count for the opposite
      polarity, it is checked against that derived complement -- not against a keyword
      co-occurring with the digits, against the actual computed number.
   b) Arithmetic expressions written as "<expr> = <result>" using +,-,*,/,x,X (e.g.
      "3 * 80 - 120 = 120"): the expression is evaluated with Python's ast (a whitelisted
      subset: numbers and + - * / operators only, nothing else), never with eval() on raw
      text, and compared to the stated result.

Any numerical claim that does not match one of these two patterns is left alone (neither
confirmed nor rejected) -- it is not this checker's job to adjudicate unsupported reasoning;
that is surfaced as NEEDS REVIEW by the caller, not silently passed as VERIFIED.
"""
import ast
import re

# ---------- number parsing (digits and words) ----------

NUMBER_WORDS = {
    "zero": 0, "one": 1, "a": 1, "an": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19, "twenty": 20,
}
_NUM_WORD_RE = "(?:" + "|".join(sorted(NUMBER_WORDS, key=len, reverse=True)) + ")"
_NUM_RE = r"(?:\d+(?:\.\d+)?|%s)" % _NUM_WORD_RE


def _to_int(raw):
    raw = raw.strip().lower()
    if raw in NUMBER_WORDS:
        return NUMBER_WORDS[raw]
    return int(float(raw))


# ---------- 2a. complementary-ratio checker ----------

# polarity -> its opposite, as a small curated registry (the "limited input patterns" this
# checker actually understands). Each value is a compiled regex matching that polarity's
# vocabulary. Extending coverage means adding a pair here, deliberately, not guessing.
POLARITY_PAIRS = [
    (re.compile(r"\bon[\s-]?time\b", re.I), re.compile(r"\blate\b", re.I), "on-time/late"),
    (re.compile(r"\bdelivered\s+on\s+time\b", re.I), re.compile(r"\b(late|delayed)\b", re.I), "delivered-on-time/late"),
    (re.compile(r"\bsuccessful(?:ly)?\b", re.I), re.compile(r"\b(fail(?:ed|ure)?s?)\b", re.I), "successful/failed"),
]

_RATIO_RE = re.compile(
    r"(?P<n1>%s)\s+of\s+(?:the\s+(?:last\s+)?)?(?P<n2>%s)" % (_NUM_RE, _NUM_RE), re.I)


def find_ratio_claims(text):
    """Returns [{'n1':int,'n2':int,'polarity':label,'span':(start,end),'source_text':str}, ...]
    for every '<N1> of <N2>' whose surrounding +-60 chars contains a registered polarity word."""
    claims = []
    for m in _RATIO_RE.finditer(text):
        window_lo, window_hi = max(0, m.start() - 60), min(len(text), m.end() + 60)
        window = text[window_lo:window_hi]
        for pos_re, neg_re, label in POLARITY_PAIRS:
            if pos_re.search(window):
                claims.append({"n1": _to_int(m.group("n1")), "n2": _to_int(m.group("n2")),
                               "polarity": label, "span": (m.start(), m.end()),
                               "source_text": text[m.start():m.end()], "window": window})
    return claims


def find_opposite_count_claims(text, label):
    """Scan `text` for '<N> <opposite-polarity-word>' or '<opposite-polarity-word> ... <N>'
    claims for the given registered polarity pair label. Returns [{'n':int,'span':...}, ...]."""
    pos_re, neg_re, lbl = next(p for p in POLARITY_PAIRS if p[2] == label)
    out = []
    # "<N> <neg-word...>" e.g. "two late deliveries"
    for m in re.finditer(r"(?P<n>%s)\b[^.\n]{0,25}?%s" % (_NUM_RE, neg_re.pattern), text, re.I):
        out.append({"n": _to_int(m.group("n")), "span": m.span(), "matched_text": m.group(0)})
    # "<neg-word...> <N>" e.g. "late on two occasions"
    for m in re.finditer(r"%s[^.\n]{0,25}?(?P<n>%s)\b" % (neg_re.pattern, _NUM_RE), text, re.I):
        out.append({"n": _to_int(m.group("n")), "span": m.span(), "matched_text": m.group(0)})
    return out


def check_ratio_consistency(source_text, response_text):
    """Returns a list of finding dicts: {'ok':bool,'label':str,'expected':int,'found':int,
    'source_claim':str,'response_claim':str}. Only fires where BOTH a source ratio+polarity
    AND a response opposite-count claim exist -- silent otherwise (no claim to check)."""
    findings = []
    seen_labels = set()
    for claim in find_ratio_claims(source_text):
        label = claim["polarity"]
        if label in seen_labels:
            continue  # one derived complement per polarity pair is enough for this prototype
        seen_labels.add(label)
        complement = claim["n2"] - claim["n1"]
        opp_claims = find_opposite_count_claims(response_text, label)
        for oc in opp_claims:
            findings.append({
                "ok": oc["n"] == complement,
                "label": label,
                "expected": complement,
                "found": oc["n"],
                "source_claim": claim["source_text"] + " (→ window: …%s…)" % claim["window"].strip(),
                "response_claim": oc["matched_text"],
            })
    return findings


# ---------- 2b. arithmetic checker ----------

_ARITH_RE = re.compile(
    r"(?P<expr>\$?-?\d+(?:\.\d+)?(?:\s*[×x\*/÷\+\-−]\s*\$?\d+(?:\.\d+)?)+)\s*=\s*\$?(?P<result>-?\d+(?:\.\d+)?)",
    re.I)


class _SafeArith(ast.NodeVisitor):
    ALLOWED = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
               ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub, ast.UAdd)

    def visit(self, node):
        if not isinstance(node, self.ALLOWED):
            raise ValueError("disallowed expression element: %s" % type(node).__name__)
        if isinstance(node, ast.Constant) and not isinstance(node.value, (int, float)):
            raise ValueError("disallowed constant")
        return super().generic_visit(node)


def _safe_eval(expr):
    node = ast.parse(expr, mode="eval")
    _SafeArith().visit(node)
    return eval(compile(node, "<verifier>", "eval"))  # nosec: whitelisted AST only, no names/calls


def check_arithmetic(text):
    """Returns [{'ok':bool,'expr':str,'stated':float,'computed':float}, ...] for every
    '<expr> = <result>' pattern found, evaluated with a whitelisted AST (numbers and
    + - * / only -- no names, no calls, no attribute access)."""
    findings = []
    for m in _ARITH_RE.finditer(text):
        raw_expr = m.group("expr")
        norm = (raw_expr.replace("$", "").replace("×", "*").replace("x", "*")
                 .replace("X", "*").replace("÷", "/").replace("−", "-"))
        try:
            computed = _safe_eval(norm)
        except Exception as e:
            findings.append({"ok": None, "expr": raw_expr, "stated": float(m.group("result")),
                              "computed": None, "error": str(e)})
            continue
        stated = float(m.group("result"))
        findings.append({"ok": abs(computed - stated) < 0.01, "expr": raw_expr,
                          "stated": stated, "computed": computed})
    return findings


# ---------- LIGHT report form/length ----------

STANDARD_ONLY = ["What We Found", "Strongest Evidence For", "Strongest Evidence Against",
                  "Where the Council Agrees", "Where the Council Disagrees", "Critical Assumptions",
                  "Alternatives Considered", "Required Modification", "Biggest Risk",
                  "What Would Change the Verdict", "Sources"]
NEXT_MOVE_FIELDS = ["Key question", "Result", "Not in scope", "Exercise", "Evidence source", "Target", "Done when"]
MAX_LIGHT_WORDS = 400


def check_light_form(text):
    """Structural-only LIGHT check. Returns list of violation strings (empty = clean).
    Deliberately does NOT inspect 'Done when' content: a bounded/finite window is valid."""
    violations = []
    effort_m = re.search(r"(?im)^\W*Council Effort\W*:?\W*(LIGHT|STANDARD|DEEP|MAX)", text)
    if not effort_m or effort_m.group(1).upper() != "LIGHT":
        return []  # not a (declared) LIGHT report; this checker has nothing to say
    heads = [re.sub(r"[^A-Za-z ]", "", h).strip() for h in re.findall(r"(?m)^#{1,3}\s*(.+)$", text)]
    bad_heads = [h for h in heads if any(h.startswith(s) for s in STANDARD_ONLY)]
    if bad_heads:
        violations.append("STANDARD-only heading(s) in a LIGHT report: %s" % bad_heads)
    words = len(text.split())
    if words > MAX_LIGHT_WORDS:
        violations.append("LIGHT report is %d words, over the %d-word cap" % (words, MAX_LIGHT_WORDS))
    verdict_lines = re.findall(r"(?m)^\W*Verdict\W*:\s*(.+)$", text)
    if len(verdict_lines) != 1:
        violations.append("%d Verdict lines (need exactly 1)" % len(verdict_lines))
    elif verdict_lines[0].strip() not in ("APPROVE", "MODIFY", "WAIT", "REJECT"):
        violations.append("Verdict line is not exactly one of APPROVE/MODIFY/WAIT/REJECT: %r" % verdict_lines[0])
    move = re.search(r"(?is)#\s*ONE NEXT MOVE(.*)$", text)
    move_text = move.group(1) if move else ""
    missing = [f for f in NEXT_MOVE_FIELDS if not re.search(r"(?im)^\W*" + re.escape(f) + r"\W*:", move_text)]
    if missing:
        violations.append("ONE NEXT MOVE missing field(s): %s" % missing)
    return violations


# ---------- top-level verify() ----------

def verify(source_text, response_text):
    """Returns {'status': 'VERIFIED'|'NEEDS REVIEW', 'reasons': [str,...], 'detail': {...}}."""
    reasons = []
    form_violations = check_light_form(response_text)
    reasons.extend("LIGHT form: %s" % v for v in form_violations)

    ratio_findings = check_ratio_consistency(source_text, response_text)
    for f in ratio_findings:
        if not f["ok"]:
            reasons.append(
                "numeric contradiction (%s): source implies %d, response states %d -- source: %r; response: %r"
                % (f["label"], f["expected"], f["found"], f["source_claim"], f["response_claim"]))

    arith_findings = check_arithmetic(response_text)
    for f in arith_findings:
        if f["ok"] is False:
            reasons.append("arithmetic contradiction: %r computes to %s, response states %s"
                            % (f["expr"], f["computed"], f["stated"]))
        elif f["ok"] is None:
            reasons.append("arithmetic expression could not be evaluated safely: %r (%s)" % (f["expr"], f["error"]))

    status = "NEEDS REVIEW" if reasons else "VERIFIED"
    return {"status": status, "reasons": reasons,
            "detail": {"light_form_violations": form_violations, "ratio_findings": ratio_findings,
                       "arithmetic_findings": arith_findings}}
