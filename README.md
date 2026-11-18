# MathWise DI² Exact-Conductor Endpoint: `{3,4,7}`, `k=1`

The verifier establishes endpoint sharpness for the fixed basis

```text
B = {3^a : a >= 1} ∪ {4^b : b >= 1} ∪ {7^c : c >= 1}.
```

## Recorded check

Run:

```bash
python3 verify_exact_conductor_d347_k1.py
```

The current verifier returns **PASS**: 545 integers are representable in `[0,581]`, 37 positive integers in `[1,581]` are not, and the largest positive nonrepresentable is `581`.

The endpoint is **581 NOT REPRESENTABLE**. Combined with the separately supplied tail certificate for `[582, infinity)`, this gives the **conditional exact conductor `C=582`** for the fixed case.

## Evidence

`EXACT_CONDUCTOR_ENDPOINT_REPORT.md` states the finite reduction and scope; `REPRESENTABLES_BELOW_582_WITH_WITNESSES.txt` and `NONREPRESENTABLES_BELOW_582.txt` preserve the enumerated results; `SHA256SUMS.txt` records the package bytes.

## Scope

The endpoint verifier covers `D={3,4,7}`, `k=1`. The infinite-tail result rests on the separately supplied certificate.

## How to review

Run the verifier first, then read the endpoint report and inspect the witness/nonrepresentable lists.


## Curated collection

This endpoint record is indexed in [MathWise Deterministic Replay Certificates](https://github.com/Grounded-DI/MathWise-Deterministic-Replay-Certificates/tree/main/d347-k1-exact-conductor-endpoint). This repository remains the canonical source.
