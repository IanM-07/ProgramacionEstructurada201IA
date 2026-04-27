""" 
Funcion que recibe un texto y decide que responder. 
Implementa Programacion Estructurada.
"""

def procesar_pregunta(mensaje_usuario):
    # 1. Normalización
    mensaje = mensaje_usuario.lower().strip()

    # 2. Base de conocimiento
    conocimiento = {
        # Estructuras de control
        "if": "La sentencia 'if' permite tomar decisiones basadas en una condición.",
        "while": "El ciclo 'while' repite un bloque de código mientras una condición sea verdadera.",
        "for": "El ciclo 'for' permite recorrer elementos de una lista o rango.",

        # Tipos de datos
        "int": "Tipo de dato entero (ej. 1, 5, -10).",
        "float": "Número con decimales (ej. 3.14).",
        "string": "Cadena de texto (ej. 'Hola').",

        # Funciones y modularidad
        "def": "Es la palabra reservada para definir una función en Python.",
        "funcion": "Una función es un bloque de código reutilizable.",
        "return": "Permite que una función devuelva un resultado.",

        # Operadores y sintaxis
        "print": "Muestra información en pantalla.",
        "==": "Operador de comparación (igualdad).",
        "+": "Operador de suma.",

        # Programación estructurada
        "algoritmo": "Conjunto de pasos ordenados y finitos para resolver un problema.",
        "secuencia": "Ejecución de instrucciones en orden.",
        "seleccion": "Permite tomar decisiones usando condiciones (if, else).",
    }

    # 3. Búsqueda
    for clave in conocimiento:
        if clave in mensaje:
            return conocimiento[clave]

    return "No entiendo eso todavía. Pregunta sobre if, while, funciones o tipos de datos."


def main():
    print("Hola! Soy tu asistente de programación.")
    print("Escribe 'salir' para terminar.\n")

    while True:
        user_input = input("Alumno -> ")

        if user_input.lower() == "salir":
            print("Bot -> ¡Hasta luego!")
            break

        respuesta = procesar_pregunta(user_input)
        print(f"Bot -> {respuesta}")


# Ejecución del programa
if __name__ == "__main__":
    main()