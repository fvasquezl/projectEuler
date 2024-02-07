#!/bin/python3

import sys
import time

# t = int(input().strip())
t = 1
for a0 in range(t):
    # n = int(input().strip())
    n = 101110
    # n = 999999
    # n = 200000
    # n = 800000
    # n = 499999
    nn = n // 1000
    print(nn)

    start = nn
    end = nn + 150

    print(start, end)
    BP = 0
    tiempo_inicio = time.time()
    for i in range(start, 1000):
        for j in range(100, end):
            p = i * j
            if 101101 <= p < n:
                if str(p) == str(p)[::-1]:
                    if p > BP:
                        BP = p

    tiempo_fin = time.time()  # Registra el tiempo de finalización
    tiempo_total = tiempo_fin - tiempo_inicio
    print(BP, tiempo_total)
