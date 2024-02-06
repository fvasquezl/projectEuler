#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    s = [1, 1]
    r = 0
    for i in range(3, n + 2):
        if i >= 3 and s[i - 2] + s[i - 3] <= n:
            s.append(s[i - 2] + s[i - 3])
            if i % 3 == 0:
                r += s[i - 1]
        else:
            break

    print(r)
