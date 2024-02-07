#!/bin/python3


# def lp_f(n):
#     lp = 2
#     while n % 2 == 0:
#         n //= 2
#     if n == 1:
#         return lp
#     p = 3
#     while p * p <= n:
#         if n % p == 0:
#             n //= p
#             lp = p
#         else:
#             p += 2

#     return n if n > lp else lp


def isP(n):
    if n < 2 or (n % 2 == 0 and n != 2):
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    lp = n
    p = 0
    while not isP(n):
        p += 2
        while n % p == 0:
            n = n // p
            if p > lp:
                lp = p

    print(lp)
