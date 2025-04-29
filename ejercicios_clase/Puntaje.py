primeraPregunta = input("¿Eres un aventurero? (Sí/No): ")
puntos = 0

if primeraPregunta == "Sí":
    puntos = puntos + 20

    segundaPregunta = input("¿Qué tipo de armadura usas? (Pesada, Ligera, Toga)")


    if segundaPregunta == "Pesada":
        puntos = puntos + 20

        segundaPregunta_1_1 = input("¿Usas escudo? (Sí/No): ")

        if segundaPregunta_1_1 == "Sí)":
            puntos = puntos + 20
        else:
            puntos = puntos - 0

        segundaPregunta_1_2 = input("Qué tanta experiencia en combate tienes? (Mucha, Media, Poca): ")
        if segundaPregunta_1_2 == "Mucha":
            puntos = puntos + 20
        elif segundaPregunta_1_2 == "Media":
            puntos = puntos + 10
        elif segundaPregunta_1_2 == "Poca":
            puntos = puntos + 5
        else:
            puntos = puntos - 10

        segundaPregunta_1_3 = input("¿Sabes usar una lanza? (Sí/No): ")
        if segundaPregunta_1_3 == "Sí":
            puntos = puntos + 20

        print("Tienes un ",puntos,"%"," de probabilidades de vencer al dragón.")

    elif segundaPregunta == "Ligera":
        puntos = puntos + 10
        
        segundaPregunta_2_1 = input("¿Usas arco y flecha? (Sí/No): ")

        if segundaPregunta_2_1 == "Sí":
            puntos = puntos + 20

        print("Tienes un ",puntos,"%"," de probabilidades de vencer al dragón.")


    elif segundaPregunta == "Toga":
        segundaPregunta_3 = input("¿Eres un mago? (Sí/No): ")

        if segundaPregunta_3 == "Sí":
            puntos = puntos + 20

            segundaPregunta_3_1 = input("¿Usas hechizos de fuego o de hielo? (Fuego o Hielo)")
            if segundaPregunta_3_1 == "Fuego":
                puntos = puntos - 20
            elif segundaPregunta_3_1 == "Hielo":
                puntos = puntos + 20

            segundaPregunta_3_2 = input("¿Sabes usar hechizos de curación? (Sí/No): ")
            if segundaPregunta_3_2 == "Sí":
                puntos = puntos + 20
            else: puntos = puntos - 20

            segundaPregunta_3_3 = input("¿Posees Grandes cantidades de maná? (Sí/No): ")
            if segundaPregunta_3_3 == "Sí":
                puntos = puntos + 20
            else: puntos = puntos - 20

        else: puntos = puntos - 20
        
        print("Tienes un ",puntos,"%"," de probabilidades de vencer al dragón.")

else:
    print("No puedes luchar contra el dragón")