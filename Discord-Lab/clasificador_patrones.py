puntajes_sentimiento = [0, 0, 0]

print("--- ANALIZADOR DE SENTIMIENTOS IA ---\n")

for i in range(5):
    clasificacion = int(input(f"Palabra {i + 1} - Clasificación (0: Positivo, 1: Neutral, 2: Negativo): "))

    puntajes_sentimiento[clasificacion] += 1

print("\nEstado final del vector de características:", puntajes_sentimiento)

mayor = puntajes_sentimiento[0]
indice_mayor = 0

for i in range(1, 3):
    if puntajes_sentimiento[i] > mayor:
        mayor = puntajes_sentimiento[i]
        indice_mayor = i

if indice_mayor == 0:
    print("Resultado de IA: La frase es Positiva (Predominancia en índice 0)")
elif indice_mayor == 1:
    print("Resultado de IA: La frase es Neutral (Predominancia en índice 1)")
else:
    print("Resultado de IA: La frase es Negativa (Predominancia en índice 2)")