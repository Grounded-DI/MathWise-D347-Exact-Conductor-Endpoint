# Exact Conductor Endpoint Check for D={3,4,7}, k=1

## Theorem statement

Let

```text
B = {3^a : a >= 1} union {4^b : b >= 1} union {7^c : c >= 1}.
```

The finite endpoint check proves:

```text
581 not in SubSum(B).
```

Therefore, combined with the previously certified fixed-case tail result

```text
[582, infinity) subset SubSum(B),
```

the exact conductor for the fixed case is

```text
C = 582.
```

## Scope

This endpoint package proves only endpoint sharpness for the fixed case:

```text
D = {3,4,7}, k = 1.
```

It does not claim:
- a general BEGL theorem,
- any result for other generating sets,
- any result for k != 1,
- endpoint optimality for any other case,
- independent verification of the prior [582, infinity) tail certificate.

## Finite reduction

For any n < 582, no summand >= 582 can occur in a positive subset-sum representation. Therefore only these basis elements are relevant:

```text
[3, 4, 7, 9, 16, 27, 49, 64, 81, 243, 256, 343]
```

There are 12 elements and 2^12 = 4096 possible subsets.

## Computed status

```text
representable integers in [0,581]: 545
positive non-representable integers in [1,581]: 37
largest positive non-representable integer below 582: 581
conditional exact conductor: 582
```

## Non-representable positive integers below 582

```text
[1, 2, 5, 6, 8, 15, 17, 18, 21, 22, 24, 33, 42, 44, 45, 48, 51, 70, 82, 178, 190, 209, 212, 215, 216, 218, 227, 236, 238, 239, 242, 245, 258, 261, 264, 521, 581]
```

## Verification command

```bash
python3 verify_exact_conductor_d347_k1.py
```

Expected output begins with:

```text
EXACT CONDUCTOR ENDPOINT CHECK: PASS
```

## Public claim language

A safe public description is:

> MathWise DI² endpoint verifier shows that 581 is not representable as a subset sum of distinct powers of 3, 4, and 7. Combined with the existing replayable certificate for [582, infinity), this gives an exact fixed-case conductor C = 582 for D={3,4,7}, k=1. No general BEGL result is claimed.
