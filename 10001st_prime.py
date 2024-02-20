#!/bin/python3

import sys
import time
import math

l1=[2,3]
n=3
while len(l1)<10:
    n+=2
    x=True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
           x=False
           break
    if x:   
        l1.append(n)



t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())

    tiempo_inicio = time.time()
    print(l1)
    print(l1[n-1])
    
        
           

    tiempo_fin = time.time()  # Registra el tiempo de finalización
    tiempo_total = tiempo_fin - tiempo_inicio
    print(tiempo_total)