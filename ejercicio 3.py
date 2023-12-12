
import math
N=1000
A=[]
amplitud_pico=float(input("ingrese la amplitud pico de la onda sinusoidal en voltios:"))


for i in range(N):
    val=amplitud_pico * math.sin(i)
    A.append(val)
    
rms_calculado=((sum(val/255*amplitud_pico for val in A)/len(A))**0.5)
rms_secundario=amplitud_pico/ (2**0.5)
porcentaje_de_error=rms_calculado/rms_secundario/rms_calculado*100

print(f"Valor rms calculado: {rms_calculado:2f}V")
print(f"valor rms_secundario:{rms_secundario:2f}V")
print(f"porcentaje_de_error:{porcentaje_de_error}V")