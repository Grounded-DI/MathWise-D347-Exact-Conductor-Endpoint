# MathWise Exact Conductor Endpoint Check: D={3,4,7}, k=1

This mini-package checks endpoint sharpness below 582 for the fixed-case subset-sum basis

```text
B = {3^a : a >= 1} union {4^b : b >= 1} union {7^c : c >= 1}.
```

The verifier proves that 581 is not representable. Combined with a separate certified proof of
`[582, infinity) subset SubSum(B)`, this establishes the exact fixed-case conductor `C = 582`.

## Run

```bash
python3 verify_exact_conductor_d347_k1.py
```

## Scope limitations

No general BEGL result is claimed. No result for other D or k is claimed. This package only checks the finite endpoint below 582.
