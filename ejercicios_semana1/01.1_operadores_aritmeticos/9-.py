'''
### 9. Conversor de minutos a días y horas
Pide una cantidad de minutos y muestra a cuántos días, horas y minutos equivale.
'''
'''
segundos = int(input("Ingrese los segundos totales: "))
horas = segundos / 3600
minutos = (segundos / 60) - (round(horas) * 60)
segundosFinal = segundos - (round(minutos) * 60) - 3600

print("Horas: ", round(horas))
print("Minutos: ", round(minutos))
print("Segundos: ", round(segundosFinal))
'''

import math

minutos = int(input("Ingrese los minutos totales: "))
dias = minutos / 1440
horas = (minutos / 60) - (round(dias)*24)
minutosFinal = minutos - (round(horas)*24) - 1440


print("Días: ",math.floor(dias))
print("Horas: ",horas)
print("Minutos: ",minutosFinal)