import datetime

nombre_asistente = "IA-UX"

print(f"Hola, bienvenido, soy {nombre_asistente}. ¿En qué puedo ayudarte?")

frase = input("¿En qué puedo ayudarte hoy?: ").lower()

if "hola" in frase or "buenos días" in frase:
    print("¡Hola! Soy tu asistente. Es un gusto saludarte.")

elif "clima" in frase or "temperatura" in frase:
    print("Consultando el servicio meteorológico... Hoy en Xalapa tendremos un día nublado.")

elif "hora" in frase or "tiempo" in frase:
    hora_actual = datetime.datetime.now().strftime("%I:%M %p")
    print(f"La hora actual del sistema es: {hora_actual}")

else:
    print("Lo siento, todavía no entiendo ese comando. ¿Podrías intentar con otra palabra?")

print(f"Proceso finalizado. Gracias por usar {nombre_asistente}.")
