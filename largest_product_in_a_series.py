#!/bin/python3

from functools import reduce
import sys

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    r=0
    i=0
    while i<(n-k):
        x= reduce(lambda x, y: x * y, list(map(int,num[i:i+k])))
        if x > r:
            r=x
        i+=1
    print(r)