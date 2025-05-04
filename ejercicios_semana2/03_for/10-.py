'''
10. **Simulación de contraseña**:  
    Pide al usuario que ingrese una contraseña e imprime "Acceso permitido" solo si la contraseña es "python123", usando un `for` para simular tres intentos.
'''

### Se define la contraseña.
password = "python123"

### Se le solicita al usuario ingresar la contraseña.
passwordIngresada = input("Ingrese una contraseña: ")

### Ciclo for para validar la contraseña ingresada, con 3 iteraciones para simular 3 intentos.
for i in range(3, 1, -1):

    ### Si la contraseña ingresada es igual a la contraseña definida, se imprime el mensaje de éxito y se rompe el bucle.
    if password == passwordIngresada:
        print("Inicio de sesión con éxito.")
        break

    ### Si la contraseña es incorrecta, se imprime el número de intentos restantes y se pide volver a ingresar la contraseña.
    else:
        print(f"Contraseña incorrecta, intente nuevamente.\nTe quedan {i-1} intentos.")
        passwordIngresada = input("Ingrese una contraseña: ")


### Se imprime un mensaje en caso no queden más intentos posibles.
if password != passwordIngresada:
    print("No te quedan intenos pendientes.")