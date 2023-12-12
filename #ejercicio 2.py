#ejercicio 2
import random
N=1000
A=[]
for i in range(N):
    val=random.randint(0,255)
    A.append(val)
    tension_real= [(val/255)*12 for val in A]
    tension_cuadrado=[t**2 for t in tension_real]
    rms=(sum(tension_cuadrado)/len(tension_real))
    
print(f"valor rms: {rms} V")