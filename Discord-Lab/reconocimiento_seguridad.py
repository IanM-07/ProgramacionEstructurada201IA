patron_maestro = [1, 0, 1, 1, 0]

lectura_sensor = []

print("--- ESCÁNER BIOMÉTRICO DE IA ---\n")

for i in range(5):
    bit = int(input(f"Ingrese bit {i + 1}: "))
    lectura_sensor.append(bit)

print("\n> Comparando lectura con base de datos...\n")

coincidencias = 0

for i in range(5):
    if lectura_sensor[i] == patron_maestro[i]:
        coincidencias += 1

similitud = (coincidencias / 5) * 100

print("> Coincidencias encontradas:", coincidencias)
print("> Porcentaje de Similitud:", similitud, "%")

if similitud == 100:
    print("\nESTADO: ACCESO TOTAL: Identidad Verificada.")
elif similitud >= 60:
    print("\nESTADO: ADVERTENCIA: Similitud parcial. Se requiere verificación manual.")
else:
    print("\nESTADO: ALERTA: Intruso detectado. Sistema bloqueado.")

print("\n--- DETALLE DE COMPARACIÓN ---")
print("Patrón Maestro :", patron_maestro)
print("Lectura Sensor :", lectura_sensor)