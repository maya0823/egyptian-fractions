#!/usr/bin/env python3
"""
Convert a positive fraction to an Egyptian fraction expansion
using the greedy algorithm.
"""

import sys
from math import gcd


def to_egyptian(numerator: int, denominator: int) -> list[int]:
    """Return the denominators of the unit fractions that sum to num/den."""
    if numerator <= 0 or denominator <= 0:
        raise ValueError("numerator and denominator must be positive integers")

    unit_denoms = []
    num, den = numerator, denominator

    while num > 0:
        # Smallest integer k such that 1/k <= num/den
        # i.e. k >= den/num, so k = ceil(den / num)
        k = (den + num - 1) // num
        unit_denoms.append(k)

        # Subtract 1/k from the remaining fraction
        num = num * k - den
        den = den * k

        # Reduce the fraction
        g = gcd(num, den)
        if g:
            num //= g
            den //= g

    return unit_denoms


def format_egyptian(denoms: list[int]) -> str:
    return " + ".join(f"1/{d}" for d in denoms)


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python egyptian.py <numerator> <denominator>")
        print("Example: python egyptian.py 4 13")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        den = int(sys.argv[2])
    except ValueError:
        print("Both arguments must be integers")
        sys.exit(1)

    try:
        denoms = to_egyptian(num, den)
    except ValueError as e:
        print(e)
        sys.exit(1)

    print(f"{num}/{den} = {format_egyptian(denoms)}")


if __name__ == "__main__":
    main()
