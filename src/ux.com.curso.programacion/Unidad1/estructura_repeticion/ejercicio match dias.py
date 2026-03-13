# Impletmentacion de Match em Python

def demostracion():
    opcion = input("Ingrese una opcion (1-7):")

    match opcion:
        case "1":
            print("Opcion 1 seleccionada")
            print("Lunes")
        case "2":
            print("Opcion 2 seleccionada")
            print("Martes")
        case "3":
            print("Opcion 3 seleccionada")
            print("Miercoles")
        case "4":
            print("Opcion 3 seleccionada")
            print("Jueves")
        case "5":
            print("Opcion 3 seleccionada")
            print("Viernes")
        case "6":
            print("Opcion 3 seleccionada")
            print("Sabado")
        case "7":
            print("Opcion 3 seleccionada")
            print("Domingo")
        case _:
            print("Opcion no valida0")

def main():
    demostracion()

if __name__ == "__main__":
    main()
