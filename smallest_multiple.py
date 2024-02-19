
#!/bin/python3

import sys
import time


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    SM = 0
    c = 0

    tiempo_inicio = time.time()
    while SM==0:
        c +=1
        for j in range(1,n+1):
            r = c/j
            if r%1 == 0 :
                SM=c
                continue
            else:
                SM=0
                break
        
    tiempo_fin = time.time()  # Registra el tiempo de finalización
    tiempo_total = tiempo_fin - tiempo_inicio
    print(SM, tiempo_total)