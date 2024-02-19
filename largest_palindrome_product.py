

import sys
import time

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    BP = 0

    tiempo_inicio = time.time()
    while BP==0:
        n -=1
        if str(n)==str(n)[::-1]:
            for j in range(100, 999):
                r = n/j
                if r%1 == 0 and r < 1000:
                    print(j,r)
                    BP=n
                    break
  
    tiempo_fin = time.time()  # Registra el tiempo de finalización
    tiempo_total = tiempo_fin - tiempo_inicio
    print(BP, tiempo_total)
  