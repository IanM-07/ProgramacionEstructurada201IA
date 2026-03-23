def sincronizacion_frecuencia():
    print("Sincronización de Frecuencia en Agentes")
    freqA = int(input("Ingrese frecuencia del Agente A (Hz): "))
    freqB = int(input("Ingrese frecuencia del Agente B (Hz): "))
    
    if freqA % freqB == 0 or freqB % freqA == 0:
        print(" Existe una relación de sincronización perfecta.")
    else:
        print(" No hay sincronización de ciclos.")

if __name__ == "__main__":
    sincronizacion_frecuencia()