# SHIRMANI Production Layer

Production chain:

ENGINE → MODULE → BUILD → QC → RELEASE GATE → QC CODE → GATE NO → DISPATCH NO → QR PAYLOAD → PUBLIC PRODUCT

## Batch numbering

100200 is a production capacity/batch target, not a verification count. Individual sequence starts at .001:

- 100200.001
- 100200.002
- 100200.003

## Product truth

Catalog entry ≠ finished independent product.  
Shared engine configuration ≠ independent codebase.  
Workflow run ≠ product.  
QC pass ≠ sale.  
Release-ready ≠ dispatched.  
Dispatch ≠ sold.

Every release record must carry Product ID, engine/module, version, batch number, QC code, gate number, dispatch number, QR payload, status and timestamp.
