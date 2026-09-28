#!/usr/bin/env python3
"""Prospective, separate 'verified mode' path for production Decision Council. NOT the ordinary
prompt-only skill, NOT enforced by any other host -- this is a standalone, explicitly
tool-backed wrapper the user runs themselves:

    python verified_mode.py "<the decision request>"

It installs the pinned production skill byte-exact from git, makes ONE fresh isolated model
call (no retries), then runs the deterministic code-only checker (verifier.py) against the
(source, response) pair BEFORE printing anything, and prints either:

  - "STATUS: VERIFIED" followed by the report, when every checkable claim in it (the limited
    ratio/complement and arithmetic patterns verifier.py supports, plus LIGHT structural form)
    checks out against source text and arithmetic actually recomputed in code; or
  - "STATUS: NEEDS REVIEW" followed by the specific reason(s) and then the report anyway (never
    withheld -- the user still sees what was generated, just not represented as checked).

What the verifier cannot check (any numerical or factual claim outside its two registered
patterns) is never silently counted as passing: it simply isn't mentioned, and VERIFIED means
"every claim this verifier is able to check, checked out" -- not "everything in this report is
correct." That scope limit is real and is not hidden from the user in the printed output.
"""
import os, shutil, subprocess, sys, tempfile
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import verifier

TRAINING = r"C:\Users\forwo\Projects\new skill\training"
sys.path.insert(0, os.path.join(TRAINING, "batch-reviews", "21-support", "harness"))
import run_call as rc

PRODUCTION_REPO = r"C:\Users\forwo\Projects\new skill\decision-council"
PRODUCTION_COMMIT = "dc6684126b8883311a9bcd85a5cf0e914cb4ba83"
BASE_ARGS = ["-p", "--model", "sonnet", "--effort", "medium", "--no-session-persistence", "--strict-mcp-config",
             "--setting-sources", "project", "--system-prompt", "You are a helpful assistant.",
             "--output-format", "stream-json", "--verbose", "--tools", "Read"]


def install(cwd):
    names = ["SKILL.md"] + subprocess.check_output(
        ["git", "-C", PRODUCTION_REPO, "-c", "core.autocrlf=false", "ls-tree", "-r", "--name-only",
         PRODUCTION_COMMIT, "references"]).decode().split()
    dest = os.path.join(cwd, ".claude", "skills", "decision-council")
    os.makedirs(os.path.join(dest, "references"))
    for n in names:
        b = subprocess.check_output(["git", "-C", PRODUCTION_REPO, "-c", "core.autocrlf=false", "show",
                                      PRODUCTION_COMMIT + ":" + n])
        with open(os.path.join(dest, n), "wb") as f:
            f.write(b)


def run_verified(request_text, run_id, out_dir):
    prompt = ("/decision-council " + request_text).encode("utf-8")
    env, removed = rc.clean_env()
    cwd = tempfile.mkdtemp(prefix="vm_")
    try:
        install(cwd)
        meta, paths = rc.run(run_id, prompt, out_dir, [shutil.which("claude")] + BASE_ARGS, env, cwd)
    finally:
        shutil.rmtree(cwd, ignore_errors=True)
    if meta.get("status") != "OK":
        return {"call_status": meta.get("status"), "meta": meta}
    response = open(paths["response"], encoding="utf-8").read()
    result = verifier.verify(request_text, response)
    return {"call_status": "OK", "meta": meta, "response": response, "result": result}


def render(outcome):
    if outcome["call_status"] != "OK":
        return "STATUS: NEEDS REVIEW\nReason: generation call did not complete (status=%s); nothing to check.\n" % outcome["call_status"]
    r = outcome["result"]
    lines = ["STATUS: %s" % r["status"]]
    if r["reasons"]:
        lines.append("Reason(s) this was not verified:")
        lines.extend("  - " + x for x in r["reasons"])
    lines.append("")
    lines.append("Note: VERIFIED means every claim this checker's limited patterns (LIGHT form/length, "
                  "one on-time/late-style ratio complement per source, and any explicit '<expr> = <result>' "
                  "arithmetic) could check, checked out -- not that every claim in the report is correct.")
    lines.append("")
    lines.append(outcome.get("response", ""))
    return "\n".join(lines)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 3:
        sys.exit("usage: verified_mode.py <run_id> <out_dir> < request_text_on_stdin")
    run_id, out_dir = sys.argv[1], sys.argv[2]
    text = sys.stdin.read()
    outcome = run_verified(text, run_id, out_dir)
    print(render(outcome))
