"""
Funcion que recibe un texto y decide que responder
implementa Programacion Estructurada pura
"""

def procesar_pregunta(mensasje_usuario):
   
#1.Normalizacion (Paso fundamental en IA)
    mensaje = mensaje_usuario.lower().strip()
   
#2.Base de conocimiento (Diccionario)
conocimiento = {
      #Concepto de Estructura de Control
        "if": "La sentencia 'if' es una condicional. Permite que el programa"
        'tome ' 
#Tipos de datos
    "int": "Representa numeros enteros (ej. 5,-10,0).No tiene parte decimal",
#Funciones y Modularidad
    "def": "Es lapalabra reservada para definir una funcion en Python"
#Operadores sintaxis
    "print": "Funcion que muestra informacion en la consola o salida estandar.",
#Conceptos de Programacion Estructurada
    "algoritmo":"Es una serie de pasos ordenados""y finitos para resolver un problema.",
    #3.Logica de busqueda
    for clave in conocimiento:
        if clave in mensaje:
        return conocimiento[clave]

    return "Lo siento, aun no se que es eso. ¡Preguntame sobre variables"

def main():
    print("¡Hola! Soy tu asistente de programacion. Preguntame sobre variables")
    while True:
        user_input = input("Alumno -> ")
        if user_input.lower() == "salir": break

        respuesta = procesar_pregunta(user_input)
        print(f"Bot -> {respuesta}")
   
   # Prueba local (Offline)
if _name_ == "_main_":
    main()