def decimal_a_romano(N):
    if N < 1 or N > 3000:
        print ("Numero invalido")
        return None
    
    romano = ""

    valores = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    
    for valor, simbolo in valores:
        while N >= valor:
            romano = romano + simbolo
            N = N - valor
    
    print("Número romano:", romano)
    return romano


def main():
    numero = int(input("Ingresa un número entero positivo (≤ 3000): "))
    decimal_a_romano(numero)

if __name__ == "__main__":
    main()