#!/usr/bin/env python3
"""Report real product-media coverage from showroom-products.json.

A metadata label or a product-page URL is not proof that a screenshot or MP4
exists. Media counts require an explicit repository-relative path that resolves
to an existing file inside the repository. External URLs are reported as routes,
not independently fetched or verified.
"""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "showroom-products.json"
MEDIA_FIELDS = {
    "screenshot": "screenshot_path",
    "mp4_demo": "demo_video_path",
    "passport": "passport_path",
}


def repository_file(value):
    """Return a safe existing repository file for a relative path, else None."""
    if not isinstance(value, str) or not value.strip():
        return None
    value = value.strip()
    parsed = urlparse(value)
    if parsed.scheme or parsed.netloc or value.startswith("//"):
        return None
    target = (ROOT / value.lstrip("/")).resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        return None
    return target if target.is_file() else None


def coverage(products):
    total = len(products)
    report = {
        "catalogue_records": total,
        "concrete_artifacts": 0,
        "screenshot": 0,
        "mp4_demo": 0,
        "passport": 0,
        "usage_guide": 0,
        "demo_route_present": 0,
        "missing": {},
    }
    for metric in (*MEDIA_FIELDS, "concrete_artifact", "usage_guide", "demo_route"):
        report["missing"][metric] = []

    for product in products:
        pid = str(product.get("id") or "UNKNOWN")
        artifact = product.get("artifact_url") or product.get("store_url")
        if repository_file(artifact):
            report["concrete_artifacts"] += 1
        else:
            report["missing"]["concrete_artifact"].append(pid)

        for metric, field in MEDIA_FIELDS.items():
            if repository_file(product.get(field)):
                report[metric] += 1
            else:
                report["missing"][metric].append(pid)

        guide = product.get("usage_guide")
        if isinstance(guide, str) and guide.strip():
            report["usage_guide"] += 1
        else:
            report["missing"]["usage_guide"].append(pid)

        route = product.get("demo_url")
        if isinstance(route, str) and route.strip():
            parsed = urlparse(route.strip())
            if parsed.scheme in ("http", "https") or repository_file(route):
                report["demo_route_present"] += 1
            else:
                report["missing"]["demo_route"].append(pid)
        else:
            report["missing"]["demo_route"].append(pid)

    return report


def percent(numerator, denominator):
    return "n/a" if denominator == 0 else f"{100 * numerator / denominator:.1f}%"


def render_markdown(report):
    total = report["catalogue_records"]
    rows = [
        "# Product Media Coverage",
        "",
        f"- Catalogue denominator: **{total}** records",
        f"- Concrete artifact files present: **{report['concrete_artifacts']}/{total}** ({percent(report['concrete_artifacts'], total)})",
        "",
        "| Measure | Present | Coverage |",
        "|---|---:|---:|",
    ]
    for metric, label in (
        ("screenshot", "Product-specific screenshot file"),
        ("mp4_demo", "Product-specific MP4 demo file"),
        ("passport", "Product passport file"),
        ("usage_guide", "Non-empty usage guide"),
        ("demo_route_present", "Demo/test-drive route recorded"),
    ):
        value = report[metric]
        rows.append(f"| {label} | {value}/{total} | {percent(value, total)} |")

    rows += [
        "",
        "## Missing evidence",
        "",
        "Missing items below are not counted as completed assets. Only the first 20 IDs per measure are shown.",
        "",
    ]
    for metric in ("concrete_artifact", "screenshot", "mp4_demo", "passport", "usage_guide", "demo_route"):
        missing = report["missing"][metric]
        rows.append(f"- **{metric}** ({len(missing)} missing): " + (", ".join(missing[:20]) if missing else "none"))
    rows += [
        "",
        "## Interpretation",
        "",
        "- Screenshot, MP4 and passport coverage count only explicit repository-relative paths that resolve to existing files.",
        "- A demo URL is counted as a recorded route, not proof that the destination is reachable or functional.",
        "- External URLs are not fetched by this report. Run browser/manual QC separately before marking a product ready for dispatch.",
        "- A green report is a coverage measurement, not independent verification, a sale, or proof of revenue.",
        "",
    ]
    return "\n".join(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    parser.add_argument("--output", help="also write the report to this repository-relative path")
    args = parser.parse_args()

    if not REGISTRY.is_file():
        raise SystemExit(f"missing catalogue registry: {REGISTRY}")
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"cannot read showroom-products.json: {exc}")
    products = data.get("products")
    if not isinstance(products, list):
        raise SystemExit("showroom-products.json: 'products' must be a list")

    report = coverage(products)
    output = json.dumps(report, indent=2, ensure_ascii=False) if args.json else render_markdown(report)
    print(output)
    if args.output:
        destination = (ROOT / args.output).resolve()
        try:
            destination.relative_to(ROOT.resolve())
        except ValueError:
            raise SystemExit("--output must stay inside the repository")
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(output + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
