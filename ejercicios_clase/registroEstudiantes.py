'''
## Ejercicio 1: Registro de Estudiantes

### Objetivo:
Crear un diccionario para almacenar información sobre estudiantes y realizar algunas operaciones básicas como agregar, modificar y mostrar datos.

### Instrucciones:

1. Crea un diccionario llamado `estudiantes`, donde las **claves** sean los **nombres de los estudiantes** y los **valores** sean otro diccionario con las claves `edad` y `calificacion`.

2. El programa debe permitir al usuario realizar las siguientes operaciones:

   - **Agregar un nuevo estudiante** (nombre, edad, calificación).
   - **Modificar la calificación** de un estudiante.
   - **Mostrar la información de todos los estudiantes**.
   - **Eliminar un estudiante por su nombre**.
'''

### Se inicializa el diccionario estudiantes.
estudiantes = {}

### Ciclo while para verificar la interacción con el menú.
while True:

    ### Try para verificar que el usuario ingrese un número.
    try:
        opcion = int(input(f"Ingrese la opción que desea realizar: \n1. Agregar nuevo estudiante.\n2. Modificar la calificacion de un estudiante.\n3. Mostrar la información de todos los estudiantes.\n4. Eliminar a un estudiante por su nombre. 5. Salir del menú.\n"))

        ### Condicional para verificar que la opción ingresada esté dentro del rango.
        if 1 <= opcion <= 5:

            ### Opción 1 "Agregar estudiante"
            if opcion == 1:

                print(f"="*50,"\nSeleccionaste la opción 1.\nAgregar estudiante.")

                ### Se piden los datos del estudiante.
                nombre = input("Ingrese el nombre del estudiante: ")
                edad = int(input("Ingrese la edad del estudiante: "))
                calificacion = float(input("Ingrese la calificación del estudiante: "))

                ### Se agregan los datos previamente solicitados al diccionario "estudiantes".
                estudiantes[nombre] = {"edad":edad,"calificacion":calificacion}

                ### Opción 2 "Modificar calificación"

            elif opcion == 2:
                nombre = input("Ingrese el nombre del estudiante: ")
                print("Opción 2 Modificar la calificacion.")
                calificacion = float(input("Ingrese la nueva calificación del estudiante: "))

                estudiantes[nombre] = {"calificacion":calificacion}

            ### Opción 3 "Listar todos los estudiantes."
            elif opcion == 3:

                print("Listar todos los estudiantes")
                for clave, valor in estudiantes.items():
                    print(f"{clave}: {valor}")

            ### Opción 4 "Eliminar un estudiante."
            elif opcion == 4:

                print("Eliminar a un estudiante por su nombre.")
                nombre = input("Ingrese el nombre del estudiante: ")

                ### Condicional para verificar que el nombre ingresado exista dentro de el diccionario de estudiantes.
                if nombre in estudiantes:
                    estudiantes.pop(nombre)
                else:
                    print("El nombre ingresado no existe en la lista.")

            elif opcion == 5:
                print("Salió del menú.")
                break
        else:
            print("Ingrese un número dentro del rango.")

    except ValueError:
            opcion = int(input(f"Debe ingresar un número.\n1. Agregar nuevo estudiante.\n2. Modificar la calificacion de un estudiante.\n3. Mostrar la información de todos los estudiantes.\n4. Eliminar a un estudiante por su nombre.\n5. Salir del menú."))

