#!/usr/bin/env python3
"""
verify_exact_conductor_d347_k1.py

Endpoint verifier for the fixed case:
B = {3^a : a >= 1} union {4^b : b >= 1} union {7^c : c >= 1}.

This script checks the finite claim below 582:
- all subset sums below 582 use only powers < 582,
- 581 is not representable as a subset sum of distinct elements of B,
- the largest positive non-representable integer below 582 is 581.

Combined with the separately certified theorem [582, infinity) subset SubSum(B),
this proves that 582 is the least possible conductor for that fixed case.

No general BEGL result is claimed.
No result for any other D or k is claimed.
"""

from itertools import combinations

LIMIT = 582
BASES = (3, 4, 7)

def finite_basis(limit=LIMIT):
    """All basis elements from B that can occur in a representation of n < limit."""
    vals = set()
    for base in BASES:
        x = base
        while x < limit:
            vals.add(x)
            x *= base
    return sorted(vals)

def representation_map(limit=LIMIT):
    """
    Dynamic-programming subset-sum map.

    Returns dict:
        sum -> tuple of distinct basis elements producing sum

    The empty tuple represents 0.
    """
    basis = finite_basis(limit)
    reps = {0: ()}
    for x in basis:
        for s, tup in list(reps.items()):
            ns = s + x
            if ns < limit and ns not in reps:
                reps[ns] = tup + (x,)
    return basis, reps

def main():
    basis, reps = representation_map(LIMIT)

    nonrepresentable = [n for n in range(1, LIMIT) if n not in reps]
    representable = [n for n in range(0, LIMIT) if n in reps]

    assert basis == [3, 4, 7, 9, 16, 27, 49, 64, 81, 243, 256, 343]
    assert 581 in nonrepresentable
    assert max(nonrepresentable) == 581
    assert len(nonrepresentable) == 37
    assert len(representable) == 545

    # Internal consistency check: every stored representation is valid.
    for n, tup in reps.items():
        assert sum(tup) == n
        assert len(tup) == len(set(tup))
        assert all(x in basis for x in tup)

    print("EXACT CONDUCTOR ENDPOINT CHECK: PASS")
    print(f"basis={basis}")
    print(f"representable_count_below_{LIMIT}={len(representable)}")
    print(f"nonrepresentable_count_1_to_{LIMIT-1}={len(nonrepresentable)}")
    print(f"largest_nonrepresentable_below_{LIMIT}={max(nonrepresentable)}")
    print(f"conditional_exact_conductor_given_prior_tail_certificate={max(nonrepresentable)+1}")
    print("scope: fixed case D={3,4,7}, k=1 only")

if __name__ == "__main__":
    main()
