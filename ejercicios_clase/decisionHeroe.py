'''
Situación: El Colapso del Tren Aéreo
En una ciudad futurista, un tren aéreo de alta velocidad sufre una falla catastrófica y queda suspendido en el aire, a punto de caer desde una gran altura. Dentro, hay más de 300 pasajeros, incluyendo un diplomático clave para evitar una guerra internacional.

Opción 3: Colaboración con otros héroes o ciudadanos
Convoca o coordina con otros superhéroes o ciudadanos con habilidades útiles (telequinesis, manipulación del metal, etc.) para resolver el problema en equipo. Esta opción promueve el trabajo en conjunto, pero depende de su habilidad de liderazgo.

¿Dividir el grupo o mantenerlo unido?

'''
'''
primeraDecision = int(input("¿Qué elegirá hacer el héroe?"))

if primeraDecision == 3:
    print("El héroe decide reunir a un équipo de héroes antes de actuar. A la escena se presentan 2 héroes más. uno con el poder de la telequinesis, y otro con el poder de controlar el metal.")
    print("Una vez que los aliados llegan, el héroe debe decidir cómo organizar la operación de rescate.")
    segundaDecision = int(input("1. Mantener el grupo unido en una única acción masiva. 2. Dividir tareas para cada uno de los miembros"))
    if segundaDecision == 1:
        print("El héroe decide ejecutar el plan enconjunto. Le ordena a ambos héroes usar sus poderes para estabilizar el tren, mientras intentan bajarlo al suelo, acción la cual resulta muy costosa energéticamente para ambos héroes.")
        print("Una repentina explosión de uno de los motores del tren hace que los héroes pierdan la concentración, desplomandose a caída libre el tren.")
        terceraDecision = int(input("Dada la delicada situación, los héroes deben elegir una opción (1. Intentar desacelerar la caída entre los tres. 2. Abandonar el intento de detener el tren e intentar salvar a cuantos pasajaros sea posible." ))

        if terceraDecision == 1:
            print("Los héroes deciden usar todas sus fuerzas para intentar frenar la caída del tren.")
            print("El tren parece no ceder, y sigue cayendo a toda velocidad. El héroe con poderes magnéticos, decide tomar una complicada decisión. Decide sacrificarse a si mismo, impulsando sus poderes más allá de sus limites. ")
            print("El héroe magnetico, logra una maravillosa azaña, y el tren se reposa sobre el suelo suavemente, salvando a todos los pasajeros.")
            print("Los héroes restantes, devastados, se retiran del lugar.")
            print("Meses después, la esposa del héroe con poderes magnéticos decide quitarse la vida.")

        elif terceraDecision == 2:
            print("Los héroes deciden invertir todos sus esfuerzos en salvar a la mayor cantidad posible de pasajeros, deben decidir si rescatar los vagones de adelante, o los vagones de atrás. Dado el frenesí del momento, los héroes no pueden detallar quien hay en cada vagón.")

            cuartaDecision = int(input("¿Qué deciden hacer los héroes? (1. Salvar los vagones de adelante 2. Salvar los vagones de atrás)"))

            if cuartaDecision == 1:
                print("Los héroes deciden salvar los vagones de adelante, usando sus poderes para crear un colchón mágico espacial, amortiguando la caída de los vagones, dejando daños menores.")
                print("Se escuchan los gritos de un grupo de niños que iban en los vagones de adelante, quienes ahoran están coreando a los héroes y agradeciendoles por salvarlos.")
                print("Los vagones de atrás caen al suelo y explotan en mil pedazos, causando la muerte de un importante diplomatico de la nación del oeste.")
                print("Tras unos largos dialogos de paz entre la nación del este y la nación del oeste, ambas finalmente llegan a un acuerdo, y logran por poco, evitar una gran guerra.")
            
            if cuartaDecision == 2:
                print("Los héroes deciden salvar a los vagones de atrás, usando sus poderes para crear un colchón mágico espacial, amortiguando la caída de los vagones, dejando daños menores.")
                print("Los vagones de adelante caen al suelo, explotando en mil pedazos.")
                print("Desde los vagones de atrás emergen los pasajeros, de entre ellos, los héroes logran distinguir a un importante diplomático de la nación del oeste, quien les promete una gran recompensa por haberlo salvado.")
                print("Los héroes reciben una gran recompensa monetaria por parte de la nación del oeste a modo de agradecimiento por haber salvado a su diplomático.")

    elif segundaDecision == 2:
        print("El héroe decide darle tareas separadas a cada héroe adicional, piensa que uno puede encargarse de sostener el tren mientras que el otro puede bajar a los pasajeros.")
        print("¿Qué heroe debería encargarse de sostener el tren?")

        terceraDecision = int(input("1. El héroe con poderes telepáticos 2. El héroe con poderes magneticos."))
        if terceraDecision == 1:
            print("El héroe con poderes telepaticos usa toda su concentración para mantener el tren a flote, pues nunca ha tenido que sostener tal masa. Mientras esto, el héroe con poderes magneticos se encarga de movilizar los pasajeros usando su habilidad de vuelo.")
            print("Sin embargo, los poderes del héroe telépata ceden, y accidentalmente deja caer al vacío dos vagones en cada extremo del tren.")
            print("Uno de los vagones se encuentra lleno de niños y ancianos, hacían parte de una excursión de una escuela local., el otro vagón, tiene solo 3 personas, 3 hombres de mediana edad, uno de ellos siendo el importante diplomático.")
            cuartaDecision = int(input("El héroe principal, se ve forzado a usar su superfuerza para salvar uno de los vagones, sin embargo, debe tomar una decisión. 1. Salvar el vagon de niños y ancianos. 2. Salvar el vagón del diplomatico."))
            if cuartaDecision == 1:
                print("El héroe logra salvar satisfactoriamente al grupo de ancianos y niños, quienes, agradecidos, empiezan a corear al héroe victorioso. Sin embargo, el otro vagón cae al suelo y explota en mil pedazos.")
                print("El resto de héroes logran terminar de evacuar los pasajeros y liberan el peso del resto del tren en un lugar seguro.")
                print("Meses después, se desata una guerra entre la nación del este y la nación del oeste, ya que esta última culpa a la primera de haber orquestado el incidente con el objetivo de asesinar a su diplomatico.")
            elif cuartaDecision == 2:
                print("El héroe salva el vagón del diplomatico, dejando caer el otro vagón, el cual procede a prenderse en llamas.")
                print("El resto de héroes logran terminar de evacuar los pasajeros y liberan el peso del resto del tren en un lugar seguro. ")
                print("Este evento supone un gran trauma para el héroe, quien adquiere una fuerte adicción al tabaco y al alcohol, lo cual hace que pierda su licencia de héroe.")
        elif terceraDecision == 2:
            print("El héroe con poderes magneticos usa todo su poder para sostener el tren, mientras que el resto de heroes usan sus habilidades para sacar a los pasajeros del tren.")
            print("Todos los héroes logran hacer sus tareas satisfactoriamente, salvando a todos.")
'''










primeraDecision = int(input("¿Qué elegirá hacer el héroe?: "))

if primeraDecision == 3:
    print(f"El héroe decide reunir a un equipo de héroes antes de actuar. A la escena se presentan 2 héroes más. Uno con el poder de la telequinesis, y otro con el poder de controlar el metal.\nUna vez que los aliados llegan, el héroe debe decidir cómo organizar la operación de rescate.")
    
    segundaDecision = int(input(f"1. Mantener el grupo unido en una única acción masiva. \n2. Dividir tareas para cada uno de los miembros\n"))
    
    if segundaDecision == 1:
        print(f"El héroe decide ejecutar el plan en conjunto. Le ordena a ambos héroes usar sus poderes para estabilizar el tren, mientras intentan bajarlo al suelo, acción que resulta muy costosa energéticamente para ambos héroes.\nUna repentina explosión de uno de los motores del tren hace que los héroes pierdan la concentración, desplomándose a caída libre el tren.\nDada la delicada situación, los héroes deben elegir una opción:")
        
        terceraDecision = int(input(f"1. Intentar desacelerar la caída entre los tres.\n2. Abandonar el intento de detener el tren e intentar salvar a cuantos pasajeros sea posible.\n"))
        
        if terceraDecision == 1:
            print(f"Los héroes deciden usar todas sus fuerzas para intentar frenar la caída del tren.\nEl tren parece no ceder, y sigue cayendo a toda velocidad. El héroe con poderes magnéticos, decide tomar una complicada decisión.\nDecide sacrificarse a sí mismo, impulsando sus poderes más allá de sus límites.\nEl héroe magnético logra una maravillosa hazaña, y el tren se reposa sobre el suelo suavemente, salvando a todos los pasajeros.\nLos héroes restantes, devastados, se retiran del lugar.\nMeses después, la esposa del héroe con poderes magnéticos decide quitarse la vida.")

        elif terceraDecision == 2:
            print(f"Los héroes deciden invertir todos sus esfuerzos en salvar a la mayor cantidad posible de pasajeros, deben decidir si rescatar los vagones de adelante, o los vagones de atrás.\nDado el frenesí del momento, los héroes no pueden detallar quién hay en cada vagón.\n ¿Qué deciden hacer los héroes?")
            
            cuartaDecision = int(input(f"1. Salvar los vagones de adelante\n2. Salvar los vagones de atrás.\n"))
            
            if cuartaDecision == 1:
                print(f"Los héroes deciden salvar los vagones de adelante, usando sus poderes para crear un colchón mágico espacial, amortiguando la caída de los vagones, dejando daños menores.\nSe escuchan los gritos de un grupo de niños que iban en los vagones de adelante, quienes ahora están coreando a los héroes y agradeciéndoles por salvarlos.\nLos vagones de atrás caen al suelo y explotan en mil pedazos, causando la muerte de un importante diplomático de la nación del oeste.\nTras unos largos diálogos de paz entre la nación del este y la nación del oeste, ambas finalmente llegan a un acuerdo, y logran por poco, evitar una gran guerra.")
            
            elif cuartaDecision == 2:
                print(f"Los héroes deciden salvar a los vagones de atrás, usando sus poderes para crear un colchón mágico espacial, amortiguando la caída de los vagones, dejando daños menores.\nLos vagones de adelante caen al suelo, explotando en mil pedazos.\nDesde los vagones de atrás emergen los pasajeros, de entre ellos, los héroes logran distinguir a un importante diplomático de la nación del oeste, quien les promete una gran recompensa por haberlo salvado.\nLos héroes reciben una gran recompensa monetaria por parte de la nación del oeste a modo de agradecimiento por haber salvado a su diplomático.")
    
    elif segundaDecision == 2:
        print(f"El héroe decide darle tareas separadas a cada héroe adicional, piensa que uno puede encargarse de sostener el tren mientras que el otro puede bajar a los pasajeros.\n¿Qué héroe debería encargarse de sostener el tren?")
        
        terceraDecision = int(input(f"1. El héroe con poderes telepáticos\n2. El héroe con poderes magnéticos\n"))
        
        if terceraDecision == 1:
            print(f"El héroe con poderes telepáticos usa toda su concentración para mantener el tren a flote, pues nunca ha tenido que sostener tal masa.\nMientras esto, el héroe con poderes magnéticos se encarga de movilizar los pasajeros usando su habilidad de vuelo.\nSin embargo, los poderes del héroe telépata ceden, y accidentalmente deja caer al vacío dos vagones en cada extremo del tren.\nUno de los vagones se encuentra lleno de niños y ancianos, hacían parte de una excursión de una escuela local, el otro vagón, tiene solo 3 personas, 3 hombres de mediana edad, uno de ellos siendo el importante diplomático.\nEl héroe principal, se ve forzado a usar su superfuerza para salvar uno de los vagones, sin embargo, debe tomar una decisión.")
            
            cuartaDecision = int(input(f"1. Salvar el vagón de niños y ancianos.\n2. Salvar el vagón del diplomático.\n"))
            
            if cuartaDecision == 1:
                print(f"El héroe logra salvar satisfactoriamente al grupo de ancianos y niños, quienes, agradecidos, empiezan a corear al héroe victorioso.\nSin embargo, el otro vagón cae al suelo y explota en mil pedazos.\nEl resto de héroes logran terminar de evacuar los pasajeros y liberan el peso del resto del tren en un lugar seguro.\nMeses después, se desata una guerra entre la nación del este y la nación del oeste, ya que esta última culpa a la primera de haber orquestado el incidente con el objetivo de asesinar a su diplomático.")
            
            elif cuartaDecision == 2:
                print(f"El héroe salva el vagón del diplomático, dejando caer el otro vagón, el cual procede a prenderse en llamas.\nEl resto de héroes logran terminar de evacuar los pasajeros y liberan el peso del resto del tren en un lugar seguro.\nEste evento supone un gran trauma para el héroe, quien adquiere una fuerte adicción al tabaco y al alcohol, lo cual hace que pierda su licencia de héroe.")
        
        elif terceraDecision == 2:
            print(f"El héroe con poderes magnéticos usa todo su poder para sostener el tren, mientras que el resto de héroes usan sus habilidades para sacar a los pasajeros del tren.\nTodos los héroes logran hacer sus tareas satisfactoriamente, salvando a todos.")
