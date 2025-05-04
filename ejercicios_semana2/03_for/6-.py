'''
6. **Contar letras "a"**:  
   Pide al usuario una palabra y usa un `for` con un condicional para contar cuántas veces aparece la letra "a".
'''

### Se inicializa un contador en 0.
contador = 0

### Se le pide al usuario ingresar una palabra.
palabraIngresada = input("Ingrese una palabra: ")

### Ciclo for para recorrer la palabra, sumando +1 al contador por cada letra "a".
for letra in palabraIngresada:
    if letra == "a":
        contador += 1

### Se imprime el total almacenado en el contador.
print(contador)





