def activacion_neurona():
    print("Estimación de Activación de Neurona Artificial")
    w = float(input("Ingrese el peso de entrada (w): "))
    x = float(input("Ingrese el dato de entrada (x): "))
    
    Z = w * x
    print(f"El valor de activación (Z) es: {Z}")

if __name__ == "__main__":
    activacion_neurona()