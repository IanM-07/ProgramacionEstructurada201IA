def division_entera(dividendo, divisor):
    cociente = 0
    residuo = dividendo
    
    while residuo >= divisor:
        residuo = residuo - divisor
        cociente = cociente + 1
    
    print("Cociente:", cociente, "Residuo:", residuo)
    return cociente, residuo


def main():
    dividendo = int(input("Ingresa el dividendo: "))
    divisor = int(input("Ingresa el divisor: "))
    
    division_entera(dividendo, divisor)

if __name__ == "__main__":
    main()
