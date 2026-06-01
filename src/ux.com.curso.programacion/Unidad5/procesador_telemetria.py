# ==========================================
# IMPORTACIÓN DE BIBLIOTECAS
# ==========================================

import sys


# ==========================================
# FUNCIONES
# ==========================================

def limpiar_lecturas(lista_datos):
    """
    Recibe una lista de lecturas del sensor LIDAR y devuelve
    una nueva lista solo con los valores válidos entre 0.0 y 100.0.
    """
    lista_filtrada = []

    for dato in lista_datos:
        if dato >= 0.0 and dato <= 100.0:
            lista_filtrada.append(dato)

    return lista_filtrada


def calcular_alertas(lista_filtrada, umbral_critico):
    """
    Recibe una lista de lecturas limpias y un umbral crítico.
    Cuenta cuántas lecturas están por debajo del umbral.
    """
    total_alertas = 0

    for lectura in lista_filtrada:
        if lectura < umbral_critico:
            total_alertas = total_alertas + 1

    return total_alertas


def generar_log_sistema(total_alertas):
    """
    Recibe el número total de alertas y genera un mensaje
    con el sistema operativo, el total de alertas y la acción.
    """
    sistema = sys.platform

    if total_alertas > 3:
        accion = "ABORTAR"
    else:
        accion = "PERMITIDA"

    log = "[SISTEMA " + sistema + "] Alertas críticas encontradas: " + str(total_alertas) + ". Acción: " + accion

    return log


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

if __name__ == "__main__":

    lecturas_raw = [12.5, -5.0, 88.2, 120.1, 1.2, 0.0, 45.6, 2.5]
    UMBRAL = 3.0

    print("=== SISTEMA DE TELEMETRÍA DE AGENTE AUTÓNOMO ===\n")

    lecturas_limpias = limpiar_lecturas(lecturas_raw)

    total_alertas = calcular_alertas(lecturas_limpias, UMBRAL)

    log_final = generar_log_sistema(total_alertas)

    print(log_final)


"""
EVIDENCIAS DE CONTROL DE CALIDAD

1. PROMPT UTILIZADO

Actúa como un programador experto en Python Estructurado. Escribe el código de una función llamada limpiar_lecturas. Recibe como parámetro una lista de números flotantes que representan distancias detectadas por el LIDAR de un robot y debe retornar una nueva lista con solo los valores válidos entre 0.0 y 100.0. Restricciones estrictas:
1. No utilices programación orientada a objetos.
2. No utilices manejo de excepciones, nada de bloques try-except.
3. Usa condicionales if/else tradicionales.
4. Incluye un docstring descriptivo.

También se usó el mismo formato para las funciones calcular_alertas y generar_log_sistema.


2. TABLA DE PRUEBAS DE ESCRITORIO MANUAL

Caso de prueba diferente:

lecturas_raw = [-10.0, 150.0, 2.0, 1.5, 80.0, 101.0]
UMBRAL = 3.0

Paso 1:
La función limpiar_lecturas revisa cada dato.

-10.0 no se acepta porque es menor que 0.0.
150.0 no se acepta porque es mayor que 100.0.
2.0 sí se acepta.
1.5 sí se acepta.
80.0 sí se acepta.
101.0 no se acepta porque es mayor que 100.0.

Resultado:
lecturas_limpias = [2.0, 1.5, 80.0]

Paso 2:
La función calcular_alertas revisa cuáles lecturas son menores que 3.0.

2.0 es menor que 3.0, entonces cuenta como alerta.
1.5 es menor que 3.0, entonces cuenta como alerta.
80.0 no es menor que 3.0, entonces no cuenta.

Resultado:
total_alertas = 2

Paso 3:
La función generar_log_sistema recibe total_alertas = 2.

Como 2 no es mayor que 3, la acción es PERMITIDA.

Resultado esperado:
[SISTEMA win32] Alertas críticas encontradas: 2. Acción: PERMITIDA

Nota:
El sistema puede cambiar dependiendo de la computadora. En Windows normalmente aparece win32.


3. AUDITORÍA DE CÓDIGO

La IA podía intentar usar comprensión de listas o sintaxis más avanzada para limpiar los datos, por ejemplo:

lista_filtrada = [dato for dato in lista_datos if dato >= 0.0 and dato <= 100.0]

Sin embargo, para mantener el código más básico y estructurado, se usó un ciclo for normal con condicional if.

También se evitó usar try-except porque la práctica pedía no utilizar manejo de excepciones. El programa solo trabaja con los datos simulados que ya están en la lista.

No se usaron bibliotecas externas. Solamente se usó la biblioteca estándar de Python mediante import sys, como solicitaba la práctica.
"""