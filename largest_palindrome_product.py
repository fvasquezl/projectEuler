#!/bin/python3

import sys
import time

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    BP = 0
    tiempo_inicio = time.time()
    for i in range(700, 1000):
        for j in range(140, i + 1):
            p = i * j
            if 101101 <= p < n:
                if str(p) == str(p)[::-1]:
                    if p > BP:
                        BP = p

    tiempo_fin = time.time()  # Registra el tiempo de finalización
    tiempo_total = tiempo_fin - tiempo_inicio
    print(BP, tiempo_total)
