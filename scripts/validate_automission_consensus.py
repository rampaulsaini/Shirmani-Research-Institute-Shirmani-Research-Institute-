import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONSENSUS = ROOT / "benchmarks/automission/consensus_predictions.jsonl"
FIXTURE = ROOT / "benchmarks/automission/sample_predictions.jsonl"
CONTRACT = ROOT / "docs/yatharth-governance/supreme-automission-contract.json"
OUT = ROOT / "automission-consensus-audit.json"


def load_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    minimum_agents = int(contract["accuracy"]["minimum_independent_agents"])
    unknown = contract["accuracy"]["unresolved_disagreement_output"]

    rows = load_jsonl(CONSENSUS)
    fixture = load_jsonl(FIXTURE)
    assert rows, "consensus fixture is empty"

    expected_cases = {r["case_id"] for r in fixture}
    groups = defaultdict(list)
    for row in rows:
        for field in ("case_id", "expected", "agent_id", "predicted", "confidence", "evidence_ids"):
            assert field in row, f"{row.get('case_id', '?')}: missing {field}"
        assert isinstance(row["evidence_ids"], list)
        assert 0.0 <= float(row["confidence"]) <= 1.0
        groups[row["case_id"]].append(row)

    assert set(groups) == expected_cases, "consensus coverage differs from benchmark fixture"

    decisions = {}
    for case_id, members in sorted(groups.items()):
        agents = [m["agent_id"] for m in members]
        assert len(set(agents)) == len(agents), f"{case_id}: duplicate agent identity"
        assert len(agents) >= minimum_agents, f"{case_id}: insufficient independent agents"

        expected_values = {m["expected"] for m in members}
        assert len(expected_values) == 1, f"{case_id}: inconsistent expected label"

        counts = Counter(m["predicted"] for m in members)
        ranked = counts.most_common()
        if len(ranked) > 1 and ranked[0][1] == ranked[1][1]:
            consensus = unknown
        else:
            consensus = ranked[0][0]

        evidence_union = sorted({e for m in members for e in m["evidence_ids"]})
        if consensus != unknown and not evidence_union:
            consensus = unknown

        agreement = counts[consensus] / len(members) if consensus != unknown else 0.0
        confidence_values = [float(m["confidence"]) for m in members if m["predicted"] == consensus]
        consensus_confidence = min(confidence_values) if confidence_values else 0.0

        decisions[case_id] = {
            "consensus": consensus,
            "agreement": round(agreement, 6),
            "consensus_confidence_floor": round(consensus_confidence, 6),
            "evidence_count": len(evidence_union),
            "agents": sorted(agents),
        }

    unresolved = sum(v["consensus"] == unknown for v in decisions.values())
    report = {
        "schema_version": "1.0.0",
        "status": "PASS",
        "policy": {
            "minimum_independent_agents": minimum_agents,
            "unresolved_disagreement_output": unknown,
            "evidence_required_for_known_consensus": True,
        },
        "counts": {
            "cases": len(decisions),
            "unresolved": unresolved,
            "known_consensus": len(decisions) - unresolved,
        },
        "decisions": decisions,
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    print("Automission consensus integrity: PASS")


if __name__ == "__main__":
    main()
