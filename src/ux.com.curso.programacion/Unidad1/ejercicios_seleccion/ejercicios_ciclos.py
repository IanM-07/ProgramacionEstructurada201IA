# Ejemplo de repeticion

def ejemplo_for():
    print("Estructura FOR")

    frutas = ["manzana", "banana", "naranja"]

    # For para iterar lista
    for fruta in frutas:
        print(fruta)

        # For para iterar rangos
        for i in  range(1,5):
            print(i)

        # For para iterar rangos con paso
        for i in range(1, 10, 2):
            print(i)

# Ejemplo de While
def ejemplo_while():
    print("Estructura WHILE")

    contador = 0

    while contador < 5:
        print(contador)
        contador +=1

# Simulacion de Do While
def ejemplo_do_while():
    print("Estructura de dO While")

    secreto = "python12"
    intentos =0
    
    while True:
        intentos_usuario = "python12" # Simulamos la entrada del usuario
        intentos += 1

        if intentos_usuario == secreto:
            print("Acceso concedido")
            break
        else:
            print("¡Acceso denegado! Intentalo de nuevo.")
            break
        print("\n")

def main():
    ejemplo_for()
    ejemplo_while()
    ejemplo_do_while()

if __name__ == "__main__":
    main()