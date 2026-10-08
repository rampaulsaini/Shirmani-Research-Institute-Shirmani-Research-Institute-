# SHIRMANI Product 5,000 / Catalogue 150,000 Scale Plan

## Production objective

Move from the existing Product-First and Product-Specific Media Factory toward:

- 5,000 concrete products with product-specific identity
- visual asset
- QR
- product passport
- demo MP4
- usage guide
- customer review/rating intake
- quality-improvement loop

Then support a 150,000-record catalogue using deterministic shards.

## Shard model

`catalogue/{shard:03}/{product_id}.json`

Recommended deterministic partition:

`shard = numeric(product_id) mod 1000`

This gives 1,000 stable shards with an average capacity of 150 records at 150,000 total records.

## Reality gate

A product is not counted as delivery-ready merely because a JSON record exists.

Required states:

SOURCE_ASSET -> PRODUCT_RECORD -> PACKAGING -> PRODUCT_PAGE -> DEMO -> USAGE_GUIDE -> EVIDENCE -> VERIFICATION

Customer reviews are improvement inputs, not scientific verification.

## Scale controller

Each automation cycle should:

1. read the strongest non-empty production catalogue
2. count concrete product records
3. count real product-specific MP4s
4. count passport/visual/demo/usage assets
5. calculate remaining work to 5,000
6. calculate catalogue headroom to 150,000
7. publish a machine-readable scale report

No cycle should claim 5,000 completed products unless the corresponding evidence exists.

## Outreach rule

Official-link mapping may be automated. Actual outbound contact is reported only after a real authorized channel confirms success.
