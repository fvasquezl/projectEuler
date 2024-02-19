#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x,s=0,0
    for i in range(1,n+1):
        s +=i
        x +=i**2
    print(s**2-x)