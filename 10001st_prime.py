#!/bin/python3

import sys

def is_primo(n):
    count=0
    for i in range(n):
       if n%i==0:
           count+=1
    if count==2:
        print('es primo')


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
