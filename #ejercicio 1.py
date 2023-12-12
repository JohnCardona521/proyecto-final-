#ejercicio 1
from re import A

import random
N=1000
A=[]
for i in range (N):
    Val=random.randint(0,255)
    A.append(Val)
tension_minima = (min(A) / 255) *12
tension_maxima = (max(A) / 255) *12
tension_promedio = (sum(A) / len(A) / 255) *12

print(f"tension minima medida: {tension_minima} V")
print(f"tension maxima medida: {tension_maxima} V")
print(f"tension promedio: {tension_promedio} V")