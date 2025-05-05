### Se inicializan las listas.
nombres = []
edades = []
enfermo = []

### Se definen las funciones.

### Función agregar con parametros nombre, edad, enfermo.
def agregar(nombreAnimal,edadAnimal,enfermoAnimal):
    nombres.append(nombreAnimal)
    edades.append(edadAnimal)
    enfermo.append(enfermoAnimal)

### Función eliminar con parametro el índice del animal a eliminar.
def eliminar(indiceEliminar):
    nombres.pop(indiceEliminar)
    edades.pop(indiceEliminar)
    enfermo.pop(indiceEliminar)

### Inicio de menú.

### Ciclo para verificar que la opción ingresada sea válida.
while True: 
    try:
        opcion = int(input("Bienvenido al menú veterinaria, digite la opción que desea realizar.\n1. Agregar\n2. Eliminar\n3. Listar todos los animales registrados. \n4. Salir\n"))
        if 1 <= opcion <= 4:
            break
        else:
            print("Ingrese una opción válida.")

    except ValueError:
        opcion = int(input("Debe ingresar un número.\n1. Agregar\n2. Eliminar\n3. Listar todos los animales registrados. \n4. Salir\n"))

while 1 <= opcion <= 3:

    ### Agregar animal.
    if opcion == 1:
        print("Opción 1. Agregar")

        ### Se le pide al usuario todos los datos del animal.
        nombreIngresado = input("Ingrese el nombre del animal: ")
        edadIngresado = input("Ingrese la edad del animal: ")
        enfermoIngresado = input("¿El animal está enfermo? (Sí/No): ")

        ### Se llama a la función agregar, dando como argumento los datos ingresados.
        agregar(nombreIngresado, edadIngresado, enfermoIngresado)

    ### Eliminar animal.
    elif opcion == 2:
        print("Opción 2. Eliminar")

        ### Se le pide al usuario el nombre del animal a eliminar: 
        nombreIngresado = input("Ingrese el nombre del animal a eliminar: ")

        ### Condicional para verificar si el nombre ingresado se encuentra en la lista.
        if nombreIngresado in nombres:

            ### Se confirma la eliminación, y se manda a la función eliminar, dando como argumento el índice del animal con el nombre ingresado.
            print("El animal",nombreIngresado, "será eliminado.")
            indiceEliminar = int(nombres.index(nombreIngresado))
            eliminar(indiceEliminar)
        else:
            print("El animal",nombreIngresado,"no se encuentra en la lista.")
    
    ### Listar los animales.
    elif opcion == 3:
        print("Opción 3. Listar todos los animales.")

        ### Se imprime cada índice de cada lista en conjunto.
        for i in range(len(nombres)):
            print(f"{i+1}. {nombres[i]} | {edades[i]} años | {enfermo[i]} está enfermo")

    ### Se le pide al usuario ingresar nuevamente la opcióna realizar.
    opcion = int(input("Bienvenido al menú veterinaria, digite la opción que desea realizar.\n1. Agregar\n2. Eliminar\n3. Listar todos los animales registrados. \n4. Salir"))

print("Ha salido del programa.")
