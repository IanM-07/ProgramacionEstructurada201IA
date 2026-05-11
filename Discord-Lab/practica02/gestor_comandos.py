import datetime

def analizar_comando(entrada_usuario):
    """
    Segunda fase del Agente: Procesamiento de comandos y logica dinamica.
    Aqui el alumno aprende a separar la 'accion' de los 'datos'.
    """
    mensaje = entrada_usuario.lower().strip()
    
    # Simulacion de comandos prefijados (como se usan en Discord: !ayuda, !ejemplo)
    if mensaje.startswith("!"):
        partes = mensaje.split(" ", 1)
        comando = partes[0]
        argumento = partes[1] if len(partes) > 1 else None

        # Lógica de Comandos
        if comando == "!definir":
            return buscar_en_diccionario(argumento)
        
        elif comando == "!validar":
            return validar_variable(argumento)
        
        elif comando == "!hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f"🕛 La hora actual del servidor es: {ahora}"
        
        elif comando == "!ayuda":
            return ("**Comandos disponibles**\n"
                    "1. '!definir <termino>' - Busca conceptos de Python.\n"
                    "2. '!validar <nombre>' - Revisa si un nombre de variable es valido.\n"
                    "3. '!hora - Muestra la hora del sistema.")
def buscar_en_diccionario(termino):
    if not termino:
        return "Debes escribir que termino quieres definir. Ej: '!definir list'"
    
# Base de datos simplificada (puedes reutilizar la de la practica anterior)
    conocimiento = {
        "variable": "Un espacio en memoria para almacenar datos",
        "lista": "Coleccion mutable de elementos",
        "tupla": "Coleccion inmutable de elementos(no se puede cambiar)."
    }
    return conocimiento.get(termino, f"No encontre '{termino}'en mi base de datos")


def validar_variable(nombre):
    """
    Logica pedagógica: Enseña a los alumnos reglas de nombrado en Python.
    """
    if not nombre:
        return "Indica el nombre a validar. Ej: '!validar mi_variable'"
    
    #Reglas básicas de Python
    if nombre[0].isdigit():
        return f" '{nombre}' no es válido: ¡No se puede empezar con un numero!"
    if " " in nombre:
        return f" '{nombre}' no es válido: ¡No se puede contener espacios!"
    if not nombre.isidentifier():
        return f" '{nombre}' contiene caracteres no permitidos (solo letras, números y_)."
    
    return f" '{nombre}' es un nombre de variable valido en python"

# ---Simulacion de ejecucion ---
if __name__ == "__main__":
    print("---Agente de Lógica: Fase de Comandos ---")
    print("Prueba comandos como: !validar 123hola o !definir lista\n")
 
    while True:
        user_input = input("Alumno >> ")
        if user_input.lower() in ["salir", "exit"]: break
 
        respuesta = analizar_comando(user_input)
        print(f"Bot >> {respuesta}\n")