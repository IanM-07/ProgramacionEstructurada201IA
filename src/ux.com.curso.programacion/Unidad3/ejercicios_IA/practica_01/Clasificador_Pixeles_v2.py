#Limpiieza de datos, normalizacion
"""
UMBRAL_ALTO = 0.7
UMBRAL_BAJO = 0.3

def clasificador_pixeles(intensidad):

   #Si la intensidad es menor a 0.0 o mayor a 1.0 es un valor invalido
    if intensidad < 0.0 or intensidad > 1.0:
        return None
    
    if 0.0 <= intensidad < UMBRAL_BAJO:
        return "Clasificacion (Fondo Oscuro)"
        
    
    if UMBRAL_BAJO < intensidad < UMBRAL_ALTO:
        return "Clasificacion (Fondo Gris)"

    if intensidad >= UMBRAL_ALTO:
        return "Clasificacion (Objeto Brillante)"
    
import os

def cargar_y_procesar(nombre_archivo):
    datos_limpios = []
    ruido_detectado = 0
    fondo_oscuro = 0
    gris_ruido = 0
    objeto_brillante = 0

    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_script, nombre_archivo)

    try:
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                valor_crudo = float(linea.strip())
                clasificacion = clasificador_pixeles(valor_crudo)
                if clasificacion is None:
                    ruido_detectado += 1
                else: 
                    datos_limpios.append(clasificacion)
                    if clasificacion == "Clasificacion (Fondo Oscuro)":
                        fondo_oscuro += 1
                    elif clasificacion == "Clasificacion (Fondo Gris)":
                        gris_ruido += 1
                    elif clasificacion == "Clasificacion (Objeto Brillante)":
                        objeto_brillante += 1
                    
        print("Resultados de clasificacion:")
        print(f"Fondo Oscuro: {fondo_oscuro}")
        print(f"Fondo Gris: {gris_ruido}")
        print(f"Objeto Brillante: {objeto_brillante}")
        print(f"Ruido Detectado: {ruido_detectado}")
    except FileNotFoundError:
        print(f"ERROR: El archivo '{nombre_archivo}' no se encontró.")

def main():
    cargar_y_procesar("lecturas_sensores.txt")

if __name__ == "__main__":  
    main()
"""
UMBRAL_BAJO = 0.3
UMBRAL_ALTO = 0.7

def clasificar(valor):
    if valor < 0.0 or valor > 1.0:
        return None
    if valor <= UMBRAL_BAJO:
        return "Oscuro"
    elif valor < UMBRAL_ALTO:
        return "Gris"
    else:
        return "Brillante"

def analizar_archivo(nombre):
    oscuro = 0
    gris = 0
    brillante = 0
    ruido = 0

    try:
        archivo = open(nombre, "r")
        for linea in archivo:
            try:
                numero = float(linea.strip())
                tipo = clasificar(numero)
            except ValueError:
                tipo = None

            if tipo is None:
                ruido += 1
            elif tipo == "Oscuro":
                oscuro += 1
            elif tipo == "Gris":
                gris += 1
            elif tipo == "Brillante":
                brillante += 1
        archivo.close()

        print("Resultados:")
        print("Oscuro:", oscuro)
        print("Gris:", gris)
        print("Brillante:", brillante)
        print("Ruido:", ruido)

    except FileNotFoundError:
        print("No encontré el archivo:", nombre)

def main():
    analizar_archivo("C:/Users/Nail_/Documents/ProgramacionEstructurada201IA/src/ux.com.curso.programacion/Unidad3/ejercicios_IA/practica_01/lecturas_sensores.txt")

if __name__ == "__main__":
    main()