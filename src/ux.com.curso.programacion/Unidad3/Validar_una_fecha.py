def validar_fecha(dia, mes, año):
    if mes < 1 or mes > 12:
        print("Fecha inválida")
        return False
    
    if mes == 2:  # Febrero
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            max_dias = 29
        else:
            max_dias = 28
    elif mes in [4, 6, 9, 11]:
        max_dias = 30
    else:
        max_dias = 31
    
    if dia < 1 or dia > max_dias:
        print("Fecha inválida")
        return False
    else:
        print("Fecha válida")
        return True


def main():
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    año = int(input("Ingresa el año: "))
    
    validar_fecha(dia, mes, año)

if __name__ == "__main__":
    main()
    