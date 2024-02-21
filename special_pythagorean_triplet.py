#!/bin/python3

from functools import reduce
import sys
from itertools import permutations,product



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    res=-1
    listn = list(permutations([x for x in range(1,n)],3))
    listp = list(product([x for x in range(1,n)],repeat=3))
    # print(listp)
    for r in listp:
        xs =reduce(lambda x, y: x + y, r)
        xm =reduce(lambda x, y: x * y, r)
        xss = [x for x in r if x[0]<x[1]<x[2] ]
        print(xss)
    #     if xs == n:
    #         print(r)
    #         if xm >res:
    #             res=xm        
    # print(res)

