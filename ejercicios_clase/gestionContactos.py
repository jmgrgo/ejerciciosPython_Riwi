'''
## Ejercicio: Gestión de Contactos

### Objetivo:
Crear un diccionario para gestionar los contactos, donde la **clave** sea el nombre del contacto y el **valor** sea su número de teléfono. El programa permitirá agregar nuevos contactos.

### Instrucciones:
1. Crea un diccionario llamado `contactos` donde cada **clave** sea el nombre de un contacto y su **valor** sea el número de teléfono.

2. El programa debe permitir al usuario realizar las siguientes operaciones:

   - **Agregar un nuevo contacto** (nombre, número de teléfono).
   - **Mostrar todos los contactos** almacenados.
   - **Buscar un contacto por su nombre**.
'''

contactos = {}

### Ciclo principal
while True:

    ### Try para verificar que la opción ingresada por el usuario sea un número entero.
    try:

        ### Se le pide al usuario ingresar la opción a ejecutar.
        opcion = int(input(f"Ingrese la opción que desea hacer: \n1. Agregar nuevo contacto.\n2. Mostrar todos los contactos.\n3. Buscar un contacto por su nombre.\n4. Salir del programa.\n"))

        ### Condicional para verificar que si se ingresó una opción válida.
        if 0 < opcion <= 4:

            ### Opción 1 Agregar contacto.
            if opcion == 1:
                print("="*50)
                print("Agregar nuevo contacto.")
                
                ### Try para validar que el usuario ingrese un número a la hora de poner el contacto.
                try: 
                    ### Se piden los datos del nuevo contacto y se agregan al diccionario.
                    nombreContacto = input("Ingrese el nombre del contacto: ")
                    numeroContacto = int(input("Ingrese el número del contacto: "))
                    contactos[nombreContacto] = numeroContacto
                    print("¡Contacto Agregado!")
                    print("="*50)
                except ValueError:
                    print("Debe ingresar un número, intente nuevamente.")

            ### Opción 2 Mostrar todos los contactos.
            elif opcion == 2:
                print("="*50)
                print("Mostrar todos los contactos.")
                for nombre,numero in contactos.items():
                    print(f"{nombre}:{numero}")
                print("="*50)
            
            ### Opción 3 Buscar contacto por su nombre.
            elif opcion == 3:

                print("="*50)
                print("Buscar contacto por su nombre: ")
                nombreContacto = input("Ingrese el nombre del contacto: ")

                ### Condicional para verificar que el nombre exista en el diccionario de contactos. 
                if nombreContacto in contactos:
                    print(f"{nombreContacto}:{contactos.get(nombreContacto)}")
               
                else:
                    print(f"El contacto {nombreContacto} no existe.")

                print("="*50)

            ### Opción 4 Eliminar contacto.
            elif opcion == 4:
                print("="*50)
                print("Eliminar contacto: ")
                nombreContacto = input("Ingrese el nombre del contacto: ")

                ### Condicional para validar que el contacto se encuentre en la lista.
                if nombreContacto in contactos:
                    contactos.pop(nombreContacto)
                else:
                    print(f"El contacto {nombreContacto} no existe.")

            ### Opción 4 Salir del bucle.
            elif opcion == 5:
                print("="*50)
                print("Salió del programa.")
                break

    except ValueError:
        print("Debe ingresar un número.")
