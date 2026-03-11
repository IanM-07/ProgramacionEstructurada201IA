# Calificaciones en python
def calificaciones():
    calificacion = int (input("Ingresa la calificacion:"))

    if calificacion >= 90:
        print ("Grado A")
    elif calificacion >=80:
        print ("Grado B")
    elif calificacion >=70:
        print ("Grado C")
    elif calificacion >=69:
        print ("Grado D")
    else:
        print(" Grado F")

def main():
    calificaciones()

if __name__ == "__main__":
    main()