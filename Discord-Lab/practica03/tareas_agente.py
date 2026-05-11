import datetime

def agregar_tareas(lista_tareas, descripcion):
    """
    Agregar una tarea a la lista si sumple con los requisitos
    """
    if len(descripcion) < 3:
        return "Error: Longitud no valida"
    
    # Crear formato para tarea 

    fecha = datetime.datetime.now().strftime("%H:%M")

    nueva_tarea = f"{descripcion} - {fecha}"
    lista_tareas.append(nueva_tarea)
    return f"Tarea agregada con exito"

def listar_tareas(lista_tareas):
    """
    Formatea la lista de tareas para su visualizacion
    """
    if not lista_tareas:
        return "No hay tareas"
    
    #agrega un avariable llamada resultado

    resultado = "Listado de tareas: \n"

    #Iterar la lista de tareas y formatear la salida
     
    for i, tarea in enumerate(lista_tareas, start=1):
        resultado += f"{i}, {tarea}\n"
    return resultado

def eliminar_tarea (lista_tareas, indice):
    """
    Eliminar una tarea por su numero de indice
    """
    if not indice.isdigit():
        return "Error: El indice debe ser un numero"
    
    indice = int(indice)-1
    
    #Agregamos la logica al preguntar
    #Si el elemento esta en la lista y eliminarlo

    if 0 <= indice < len(lista_tareas):
        tarea_eliminada = lista_tareas.pop(indice)
    else:
        return "Error: No existe la tarea"
    return f"Tarea eliminada: {tarea_eliminada}"

def main():
    tareas = []
    PREFIJO ="!"

    print("Bienvenido al geestor de tareas")
    activa = True
    while activa:
        entrada = input(">>>").strip()
        continue

    #Procesamiento de la entrada
    cuerpo = entrada [len(PREFIJO):].split(maxsplit=1)
    comando = cuerpo[0].lower()
    argumento = cuerpo[1] if len(cuerpo) > 1 else ""

    #Seleccion de accion
    if comando=="add"
        resultado = agregar_tareas(tarea, argumento)
        