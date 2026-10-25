from pathlib import Path
from urllib.parse import quote
import html
import json
import os
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
CAT = ROOT / "generated/1000-digital-products.json"
OUT = ROOT / "products/live"
MAN = ROOT / "generated/product-surface-manifest.json"
CONTACT_EMAIL = "sainirampaul60@gmail.com"
WHATSAPP_NUMBER = "918082935186"


def e(value):
    return html.escape(str(value or ""), quote=True)


def slug_for(product_id):
    return re.sub(r"[^a-zA-Z0-9._-]", "-", str(product_id)).lower()


def relative_href(target, page_dir):
    """Build a repository-local href from the real nested product-page directory."""
    return Path(os.path.relpath(target, start=page_dir)).as_posix()


def page(product, root=ROOT):
    pid = str(product["id"])
    slug = slug_for(pid)
    name = product.get("name") or pid
    family = product.get("family") or product.get("category") or "Digital Product"
    engine = product.get("engine") or "package"
    description = product.get("short_description") or product.get("description") or "Customer-facing digital product."
    price = product.get("offer_price_inr", product.get("price_inr", ""))

    # These pages are emitted at products/live/<slug>/index.html. Resolve each
    # local link from that actual directory rather than maintaining fragile ../ counts.
    page_dir = root / "products/live" / slug
    passport_href = f"{relative_href(root / 'product-passport.html', page_dir)}?id={quote(pid, safe='')}"
    showroom_href = relative_href(root / "showroom-public.html", page_dir)
    vip_disk_rel = f"products/demos/vip/{slug}.svg"
    video_name = str(engine) + ".mp4"
    video_disk_rel = f"products/demos/{video_name}"
    vip_exists = (root / vip_disk_rel).is_file()
    video_exists = Path(video_name).name == video_name and (root / video_disk_rel).is_file()

    vip_href = quote(relative_href(root / vip_disk_rel, page_dir), safe="/")
    video_href = quote(relative_href(root / video_disk_rel, page_dir), safe="/")
    media_links = []
    if vip_exists:
        media_links.append(f'<a href="{e(vip_href)}">Open product screenshot</a>')
    if video_exists:
        media_links.append(f'<a href="{e(video_href)}">Watch {e(engine)} demo video</a>')
    media_html = "".join(media_links) if media_links else (
        '<p class="notice">Demo media is not published for this product yet. '
        'This page is a catalogue listing, not proof of a runnable product demo.</p>'
    )

    enquiry_text = f"Hello Shirmani Research Institute, I want to enquire about {name} (Product ID: {pid}). Please confirm the actual demo, deliverables, price, delivery time, support and payment terms before I place an order."
    whatsapp_href = "https://wa.me/" + WHATSAPP_NUMBER + "?text=" + quote(enquiry_text, safe="")
    email_subject = quote(f"Product enquiry: {name} ({pid})", safe="")
    email_body = quote(enquiry_text, safe="")
    email_href = f"mailto:{CONTACT_EMAIL}?subject={email_subject}&body={email_body}"

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{e(name)} — public catalogue listing from Shirmani Research Institute. Confirm demo, scope and terms before purchase.">
<title>{e(name)} · SHIRMANI</title>
<style>
:root{{color-scheme:dark;--bg:#07101b;--panel:#101d2b;--line:#29445d;--gold:#f5d36c;--cyan:#75e5f5;--text:#f5f7fa;--muted:#b5c4d2}}
*{{box-sizing:border-box}}body{{margin:0;background:radial-gradient(ellipse at top,#1b3450,#07101b 62%);color:var(--text);font:16px/1.65 system-ui,sans-serif}}
main{{max-width:1000px;margin:auto;padding:20px 16px 56px}}.card{{border:1px solid var(--line);border-radius:20px;padding:clamp(18px,4vw,34px);background:var(--panel);margin:14px 0}}
h1,h2{{color:var(--gold)}}h1{{font-size:clamp(2rem,5vw,3.5rem);line-height:1.12}}.tag{{color:var(--cyan);font-weight:800}}.price{{color:#72e6aa;font-size:2rem;font-weight:900}}p{{color:var(--muted)}}
a{{display:inline-block;padding:11px 14px;margin:5px 5px 5px 0;border:1px solid #41617b;border-radius:10px;color:var(--text);text-decoration:none}}a.primary{{background:var(--gold);color:#111827;border-color:var(--gold);font-weight:850}}.notice{{border-left:4px solid var(--cyan);padding:12px 14px;background:#0a1724}}
</style>
</head>
<body><main>
<p><a href="{e(showroom_href)}">← Public showroom</a></p>
<section class="card">
<div class="tag">SHIRMANI RESEARCH INSTITUTE · PUBLIC CATALOGUE</div>
<h1>{e(name)}</h1>
<p class="tag">{e(pid)} · {e(family)} · {e(engine)}</p>
<p>{e(description)}</p>
<p class="price">{"₹" + e(price) if str(price) else "Price to be confirmed"}</p>
<p class="notice">Catalogue listing only. Confirm that the demo works, what is delivered, the final price, delivery date, support and payment terms before ordering. A listed price or generated page is not evidence of a sale or successful delivery.</p>
<h2>Demo and product evidence</h2>
{media_html}
<p><a href="{e(passport_href)}">Product passport / details</a></p>
<h2>Ask about this product</h2>
<p>Use either contact option to request a working demo and a written scope. Nothing is sent automatically from this page.</p>
<a class="primary" href="{e(whatsapp_href)}" target="_blank" rel="noopener noreferrer">Enquire on WhatsApp</a>
<a href="{e(email_href)}">Prepare email enquiry</a>
</section>
<footer><a href="{e(showroom_href)}">Browse public showroom</a> · SHIRMANI Research Institute</footer>
</main></body></html>
"""


def main():
    data = json.loads(CAT.read_text(encoding="utf-8"))
    rows = [product for product in data.get("products", []) if str(product.get("id", "")).strip()]
    batch = max(1, min(100, int(os.getenv("PRODUCT_SURFACE_BATCH", "25"))))
    OUT.mkdir(parents=True, exist_ok=True)

    existing = {path.parent.name for path in OUT.glob("*/index.html")}
    selected = [product for product in rows if slug_for(product["id"]) not in existing][:batch]
    for product in selected:
        (OUT / slug_for(product["id"])).mkdir(parents=True, exist_ok=True)

    # Refresh all existing surfaces as well as adding the next batch. This ensures
    # fixed navigation, contact CTAs, and honest demo availability reach old pages.
    published = 0
    for product in rows:
        destination = OUT / slug_for(product["id"]) / "index.html"
        if destination.parent.exists() or product in selected:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(page(product), encoding="utf-8")
            published += 1

    payload = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "catalog_count": len(rows),
        "public_surface_count": published,
        "remaining_public_surfaces": len(rows) - published,
        "created_this_cycle": len(selected),
        "batch_size": batch,
        "state": "OPERATIONAL_SURFACE",
        "truth_boundary": "A catalogue page is not evidence of a working demo, sale, payment, delivery, scientific validation, or independent human review."
    }
    MAN.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False))


if __name__ == "__main__":
    main()
