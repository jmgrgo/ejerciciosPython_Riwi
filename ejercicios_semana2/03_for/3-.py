'''
3. **Sumar los primeros 10 números**:  
   Usa un `for` para sumar los números del 1 al 10 e imprime el resultado.
'''

### Se inicializa la suma en 0.
suma = 0

### Bucle para sumar, en cada iteración, la suma agrega el número siguiente a su valor previo.
for i in range(1, 11):
    suma += i
print(suma)

