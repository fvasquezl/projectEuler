#!/bin/python3
import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    r=-1
    f=False
    for k in range(5, n//2):
        for j in range(3, n//2):
            for i in range(1, n//2):
                if i<j<k and i+j+k == n and i**2+j**2 ==k**2:
                    m = i*j*k
                    if m > r:
                        r = m
                   
                    
    print(r)

    # 1,2,3,4,5,6,7,8,9,10,11,12



    # for i in range(1,n//2):
    #     for j in range(2, n//2):
    #         for k in range(3, n//2):
    #             if i<j<k: 
    #                 if i+j+k == n:
    #                     if i**2+j**2 ==k**2:
    #                         m = i*j*k
    #                         if m > r:
    #                             r = m
                   
    # print(r)

