peliculas_accion = ["Mad Max", "John Wick", "Inception"]
peliculas_comedia = ["Toy Story", "Minions", "Free Guy"]
peliculas_terror = ["It", "The Conjuring", "Saw"]

def obtener_recomendacion(genero_elegido, edad_usuario):
    if edad_usuario < 13:
        return peliculas_comedia[0]
    else:
        if genero_elegido == "accion":
            return peliculas_accion[0]
        elif genero_elegido == "comedia":
            return peliculas_comedia[0]
        elif genero_elegido == "terror":
            return peliculas_terror[0]
        else:
            return "Genero no valido"

print("Saludos, Agente IA de Recomendación está activo")

edad = int(input("¿Que edad tienes? "))
genero = input("¿Que genero prefiere(accion/comedia/terror)?: ").strip().lower()

ajuste = False
if edad < 13 and genero == "terror":
    ajuste = True

recomendacion = obtener_recomendacion(genero, edad)

if ajuste:
    print("\nNota: Debido a tu edad, hemos ajustado la recomendación a contenido apto para todo público.\n")

print("Recomendación de la IA:", recomendacion)