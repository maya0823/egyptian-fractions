# Egyptian Fractions

The greedy Egyptian fraction method turns any positive fraction into a sum of distinct unit fractions (fractions with numerator 1). This small program does exactly that.

You give it a numerator and a denominator. It repeatedly picks the largest unit fraction that does not exceed the remaining amount, subtracts it, and continues until nothing is left. The result is an expression such as 4/13 = 1/4 + 1/18 + 1/468.

## What you can learn

- How the greedy algorithm for Egyptian fractions works and why it always terminates.
- Integer arithmetic tricks for computing ceilings and reducing fractions with gcd.
- Writing a short, self-contained command-line tool that handles basic input validation.

## Learning from mistakes

- Forgetting to reduce the fraction after each subtraction quickly produces huge intermediate numbers. Always divide by the gcd.
- The greedy choice is not always the shortest possible expansion. Some fractions have shorter representations that the algorithm misses.

## How to run / usage

Requires Python 3. No external packages.

```
python egyptian.py 4 13
```

```
python egyptian.py 5 121
```

```
python egyptian.py 3 7
```

## Notes

The algorithm works for any positive integers, including improper fractions. The expansion uses distinct denominators by construction.

## License

MIT
