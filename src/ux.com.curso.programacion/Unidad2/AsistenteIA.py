UMBRAL_ALTO = 80.0
UMBRAL_MINIMO = 40.0

instruccion = input("Instrucción recibida: ")
confianza = float(input("Nivel de confianza calculado (%): "))

if confianza >= UMBRAL_ALTO:
    print(f"Ejecutando la acción: {instruccion}... (Éxito)")
    
    if confianza > 95.0:
        print("Aviso: El modelo ha sido reforzado con éxito debido a la alta precisión.")

elif confianza >= UMBRAL_MINIMO:
    print(f"Confianza insuficiente. ¿Se refiere a: {instruccion}? Por favor confirme.")

else:
    print("Error 404: No pude entender la instrucción. Intente hablar más claro.")

print("Sesión de procesamiento finalizada.")
