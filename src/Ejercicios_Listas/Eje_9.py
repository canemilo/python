from Eje_8 import personajes_frieren

print('Magos de Primera Clase')
for personaje in personajes_frieren:
    if "Magos de Primera Clase" in personaje["afiliacion"]:
        print(personaje.get("nombre"), personaje.get("raza"))
        # Al quitar el break, el bucle continuará con el siguiente personaje
