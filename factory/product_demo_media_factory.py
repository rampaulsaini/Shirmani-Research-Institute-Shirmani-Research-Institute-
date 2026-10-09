#!/usr/bin/env python3
"""Generate product-labelled orientation MP4s and report demo readiness truthfully."""
from pathlib import Path
from datetime import datetime, timezone
import os, json, subprocess, shutil

ROOT = Path(__file__).resolve().parents[1]
OVL = ROOT / "generated/concrete-production-overlay.json"
OUT = ROOT / "products/demo-video"
MAN = ROOT / "generated/product-specific-demo-video-manifest.json"


def main():
    ffmpeg = shutil.which("ffmpeg")
    data = json.loads(OVL.read_text(encoding="utf-8")) if OVL.exists() else {}
    products = data.get("products", [])
    OUT.mkdir(parents=True, exist_ok=True)
    created = 0
    errors = []
    limit = max(1, min(500, int(os.getenv("MEDIA_BATCH", "25"))))

    if ffmpeg:
        for product in products:
            if created >= limit:
                break
            pid = str(product.get("id", "")).upper()
            if not pid:
                continue
            output = OUT / (pid + ".mp4")
            if output.exists():
                continue

            # These are clearly labelled orientation slates, not screen recordings
            # or evidence that the underlying product has been fully demonstrated.
            title = "SHIRMANI PRODUCT ORIENTATION"
            subtitle = "Read passport  |  Open product  |  Use  |  Review"
            vf = (
                "drawtext=text='" + title + "':fontcolor=0xE8C65B:fontsize=42:"
                "x=(w-text_w)/2:y=170,"
                "drawtext=text='" + pid + "':fontcolor=white:fontsize=48:"
                "x=(w-text_w)/2:y=270,"
                "drawtext=text='" + subtitle + "':fontcolor=white:fontsize=27:"
                "x=(w-text_w)/2:y=370"
            )
            result = subprocess.run(
                [ffmpeg, "-y", "-f", "lavfi", "-i",
                 "color=c=0x08111B:s=1280x720:r=30",
                 "-vf", vf, "-t", "6", "-pix_fmt", "yuv420p",
                 "-movflags", "+faststart", str(output)],
                stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True
            )
            if result.returncode == 0 and output.exists() and output.stat().st_size > 0:
                created += 1
            else:
                errors.append({
                    "product_id": pid,
                    "returncode": result.returncode,
                    "error_tail": (result.stderr or "")[-1200:]
                })
                if output.exists():
                    output.unlink()

    videos = sorted(OUT.glob("SP-*.mp4"))
    # Count an interactive demo only when the product record explicitly names
    # a demo URL/path and that local path actually exists. Do not infer coverage
    # from the number of catalogue rows or orientation videos.
    interactive_count = 0
    for product in products:
        demo_path = product.get("interactive_demo_path")
        if demo_path:
            candidate = (ROOT / str(demo_path)).resolve()
            if candidate.is_relative_to(ROOT.resolve()) and candidate.is_file():
                interactive_count += 1

    manifest = {
        "schema_version": 4,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "catalog_count": len(products),
        "orientation_mp4_count": len(videos),
        "real_product_demo_count": 0,
        "interactive_demo_count": interactive_count,
        "vip_screenshot_count": 0,
        "remaining_full_product_demos": len(products),
        "remaining_vip_screenshots": len(products),
        "created_this_cycle": created,
        "batch_size": limit,
        "mode": "PRODUCT_LABELLED_ORIENTATION_SLATE",
        "artifact_definition": "Six-second title/orientation slate labelled with product ID; not a screen recording or complete product-specific usage demonstration.",
        "truth_boundary": "An MP4 file existing does not prove the product works or that a full demo has been recorded.",
        "errors_this_cycle": errors
    }
    MAN.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "created_orientation_slates": created,
        "orientation_mp4_count": len(videos),
        "real_product_demo_count": 0,
        "interactive_demo_count": interactive_count,
        "errors": len(errors)
    }, ensure_ascii=False))
    if errors:
        print("Some orientation MP4s could not be rendered; details recorded in manifest.")


if __name__ == "__main__":
    main()
