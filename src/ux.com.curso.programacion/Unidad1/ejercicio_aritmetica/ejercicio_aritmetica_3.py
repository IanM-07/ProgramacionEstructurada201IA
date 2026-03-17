import math

# Demostracion del uso de funciones de math

def mostrar_funciones_math(numero):
    # Crear una variable

    sen_x = math.sin(numero)
    conse_x = math.cos(numero)

    print("El seno de", numero, "es:", sen_x)
    print("El coseno de", numero, "es:", conse_x)

    resultado = sen_x ** 2 + conse_x ** 2

    print("El resultado de sen*2(x) + cos*2(x) es:", resultado)

def mostrar_funciones_math_tan(numero):
    tan_x = math.tan(numero)

    print("La tangente de ", numero, "es:", tan_x)

def main():
    numero = float(input("Ingrese un numero: "))
    mostrar_funciones_math(numero)
    mostrar_funciones_math_tan(numero)

if __name__ == "__main__":
    main()
