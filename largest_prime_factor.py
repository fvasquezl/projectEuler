#!/bin/python3


def lp_f(n):
    lp = 2
    while n % 2 == 0:
        n //= 2
    if n == 1:
        return lp
    p = 3
    while p * p <= n:
        if n % p == 0:
            n //= p
            lp = p
        else:
            p += 2

    return n if n > lp else lp


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(lp_f(n))
