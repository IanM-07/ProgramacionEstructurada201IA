def imprimir_identificadores():
    # identificadores validos
    nombre_usuario="Alumno" # Inicia con letra y tiene guion bajo
    sensor="Temperatura" # Inicia con letra
    _id_interno12 =12 # Puede contener guion bajo y numeros

    print(nombre_usuario)
    print(sensor)
    print(_id_interno12)

# Nombre correcto de funciones
def calcular_area():
    print("Calculamos el área...")

def main():
        imprimir_identificadores()
        calcular_area()

if __name__ == "__main__":
    main()
