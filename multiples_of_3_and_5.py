#!/bin/python3

import sys


def sum_m(n, k):
    n = (n - 1) // k
    return k * n * (n + 1) // 2


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_m(n, 3) + sum_m(n, 5) - sum_m(n, 15))
