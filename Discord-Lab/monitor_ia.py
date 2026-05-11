print("--- TELEMETRÍA DE CLUSTER IA ---\n")

temperatura = float(input("Temperatura actual (°C): "))
memoria_vram = int(input("Uso de Memoria VRAM (%): "))
enfriamiento = input("¿Enfriamiento activo? (si/no): ").lower()

print()

if memoria_vram < 0 or memoria_vram > 100:
    print("Error: Lectura de memoria fuera de rango (0-100%).")

elif temperatura > 90 or memoria_vram == 100:
    print("> Diagnóstico: ¡ALERTA CRÍTICA! Apagando servidores para evitar daños físicos.")

elif temperatura >= 75 and temperatura <= 90:

    if enfriamiento == "no":
        print("> Diagnóstico: Peligro: Temperatura alta y enfriamiento desactivado. Pausando entrenamiento.")
    
    elif enfriamiento == "si":
        print("> Diagnóstico: Temperatura elevada. Reduciendo velocidad de procesamiento (Throttling).")

elif temperatura < 75 and memoria_vram < 80:
    print("> Diagnóstico: Sistema Estable: Entrenamiento en curso a máxima capacidad.")

    memoria_libre = 100 - memoria_vram
    print("> Memoria VRAM disponible:", memoria_libre, "%")

else:
    print("> Diagnóstico: Sistema funcionando con carga moderada.")