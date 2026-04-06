def n_impar():
    N = int(input("Ingresa la cantidad de números impares: "))
    contador = 0
    numero = 1

    while contador < N:
        print(numero)
        numero = numero + 2
        contador = contador + 1

def main():
    n_impar()

if __name__ == "__main__":
    main()