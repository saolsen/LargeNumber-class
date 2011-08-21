#!/usr/bin/env python
# Prime tester
# Stephen Olsen
# SE Final project

from largeNumber import LargeNumber

def main():
    n = raw_input("Enter a number to test (n): ")
    k = raw_input("Enter a number of repetitions (k): ")
    n = LargeNumber(n)
    k = LargeNumber(k)
    print check_primality(n,k)

def check_primality(n,k):
    for i in range(k):
        one = LargeNumber("1")
        a = LargeNumber.Random(one,n)
        if not (modular_pow(a, (n - one), n) == one):
            return "composite"
    return "probably-prime"

def modular_pow(base, exponent, modulus):
    one = LargeNumber("1")
    result = one
    while exponent > LargeNumber("0"):
        if (exponent & one) == one:
            result = (result * base) % modulus
        exponent = exponent >> one
        base = (base * base) % modulus
    return result

if __name__ == '__main__':
    main()
