"""Price a run from its transcripts: the lead's session plus every subagent, in dollars.

Reads Claude Code's own transcripts, so the numbers are measured, not estimated.
Cache reads, cache writes and output are priced separately, per model.

    cost.py                                  # newest session for this folder
    cost.py --since 2026-10-25T21:12 --json runs/<slug>/agents/cost.json
    cost.py --session ~/.claude/projects/<folder>/<id>.jsonl

Groups: lead, lean (ci-lean), browse (ci-browse), default (any other agent type).
Prices are list prices per million tokens; edit PRICES when they change.
"""
import argparse
import collections
import glob
import json
import os
import re

# $/M tokens: input, cache write (5 min), cache write (1 h), cache read, output
PRICES = {
    "opus-5-5": (4, 5, 8, 0.20, 20),
    "opus-5": (5, 6.25, 10, 0.50, 25),
    "opus-4": (5, 6.25, 10, 0.50, 25),
    "sonnet-5-5": (2, 2.5, 4, 0.20, 10),
    "sonnet-5": (2, 2.5, 4, 0.20, 10),
    "sonnet-4": (3, 3.75, 6, 0.30, 15),
    "haiku-5-5": (0.10, 0.125, 0.20, 0.01, 0.50),
    "haiku-4": (1, 1.25, 2, 0.10, 5),
    "fable": (10, 12.5, 20, 1, 50),
}
ORDER = ["opus-5-5", "sonnet-5-5", "haiku-5-5", "opus-5", "sonnet-5", "opus-4", "sonnet-4", "haiku-4", "fable"]


def price(model):
    for key in ORDER:
        if key in (model or ""):
            return key, PRICES[key]
    return "unknown", PRICES["sonnet-5-5"]


def usage(path, since=None, until=None):
    seen, t, first = set(), collections.Counter(), None
    for line in open(path):
        try:
            r = json.loads(line)
        except ValueError:
            continue
        ts = r.get("timestamp", "")
        if (since and ts and ts < since) or (until and ts and ts > until):
            continue
        m = r.get("message")
        if not isinstance(m, dict) or not m.get("usage") or m.get("id") in seen:
            continue
        seen.add(m.get("id"))
        u, (_, p) = m["usage"], price(m.get("model"))
        cc = u.get("cache_creation") or {}
        w5 = cc.get("ephemeral_5m_input_tokens", u.get("cache_creation_input_tokens", 0)) or 0
        w1 = cc.get("ephemeral_1h_input_tokens", 0) or 0
        row = dict(input=u.get("input_tokens", 0), write=w5 + w1, read=u.get("cache_read_input_tokens", 0),
                   output=u.get("output_tokens", 0))
        if first is None:
            first = row["input"] + row["write"] + row["read"]
        for k, v in row.items():
            t[k] += v
        t["usd"] += (row["input"] * p[0] + w5 * p[1] + w1 * p[2] + row["read"] * p[3] + row["output"] * p[4]) / 1e6
        t["calls"] += 1
    t["starting_context"] = first or 0
    t["usd"] = round(t["usd"], 3)
    return dict(t)


def newest_session():
    folder = os.path.expanduser("~/.claude/projects/" + re.sub(r"[^A-Za-z0-9]", "-", os.getcwd()))
    sessions = glob.glob(folder + "/*.jsonl")
    if not sessions:
        raise SystemExit(f"no transcripts in {folder}; pass --session")
    return max(sessions, key=os.path.getmtime)


def group(agent_type):
    return {"ci-lean": "lean", "ci-browse": "browse"}.get(agent_type, "default")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--session", help="the lead's transcript (.jsonl); default: newest for this folder")
    ap.add_argument("--since", help="ISO timestamp: count only from here (the run's start)")
    ap.add_argument("--until", help="ISO timestamp: count only up to here")
    ap.add_argument("--json", help="also write the full breakdown here")
    a = ap.parse_args()
    session = os.path.expanduser(a.session) if a.session else newest_session()
    lead = usage(session, a.since, a.until)
    agents = []
    for f in sorted(glob.glob(session[:-6] + "/subagents/agent-*.jsonl")):
        meta_path = f[:-6] + ".meta.json"
        meta = json.load(open(meta_path)) if os.path.exists(meta_path) else {}
        u = usage(f, a.since, a.until)
        if u.get("calls"):
            agents.append(dict(role=meta.get("description", ""), agent_type=meta.get("agentType", ""),
                               group=group(meta.get("agentType", "")), **u))
    groups = collections.defaultdict(lambda: dict(agents=0, usd=0.0))
    for x in agents:
        groups[x["group"]]["agents"] += 1
        groups[x["group"]]["usd"] = round(groups[x["group"]]["usd"] + x["usd"], 3)
    total = round(lead.get("usd", 0) + sum(x["usd"] for x in agents), 2)
    out = dict(session=session, since=a.since, until=a.until, total_usd=total, lead=lead, groups=dict(groups),
               agents=agents)
    if a.json:
        json.dump(out, open(a.json, "w"), indent=1)
    print(f"total ${total:.2f}")
    print(f"  lead     ${lead.get('usd', 0):7.2f}  {lead.get('calls', 0)} calls")
    for g, v in sorted(groups.items()):
        print(f"  {g:8} ${v['usd']:7.2f}  {v['agents']} agents")
    for x in sorted(agents, key=lambda x: -x["usd"]):
        print(f"    ${x['usd']:6.2f}  {x['group']:7} start {x['starting_context']:>6}  calls {x['calls']:>3}  {x['role'][:60]}")
