import random
from funciones_prints import *
from funciones_archivos import *
import datetime


# 𝗦𝗣𝗥𝗜𝗡𝗧 𝟭
# Funcion donde crea el usuario

def crear_usuario_final(usuarios_existentes):
    indice_actual = 0
    while True:
        nombre_usuario = input("​​​​​Ingrese su nombre de usuario 👤: ").strip()
        if not nombre_usuario: # Agregamos validación para nombre vacío
            imprimir_mensaje_nombre_usuario_vacio()
            continue
        usuario_ya_existe = recorrido_usuarios_existentes_recursivo(nombre_usuario, usuarios_existentes, indice_actual)
        if usuario_ya_existe:
            continue
        confirmado = confirmar_usuario(nombre_usuario)
        if confirmado:
            imprimir_mensaje_usuario_creado(nombre_usuario)
            return nombre_usuario
        # Si no está confirmado, el bucle continúa para pedir un nuevo nombre

def recorrido_usuarios_existentes_recursivo(nombre_usuario, usuarios_existentes, indice_actual):
    # Caso base: la lista está vacía, el usuario no existe.
    if indice_actual >= len(usuarios_existentes):
        return False
    
    # Caso base: el primer usuario de la lista coincide.
    if nombre_usuario == usuarios_existentes[indice_actual]:
        imprimir_mensaje_usuario_ya_existe()
        return True
    
    # Paso recursivo: busca en el resto de la lista (excepto el del indice).
    recursion = recorrido_usuarios_existentes_recursivo(nombre_usuario, usuarios_existentes, indice_actual + 1)
    return recursion

def confirmar_usuario(nombre_usuario):
    confirmacion = input(f"​​​​​🪪 ​¿Está seguro que '{nombre_usuario}' será su nombre de usuario? (si/no): ").lower()
    if confirmacion in {"si", "sí", "s"}:
        return True
    elif confirmacion in {"no", "n"}:
        imprimir_mensaje_usuario_cancelado() # Llama a la nueva función
        return False
    else:
        imprimir_mensaje_respuesta_no_valida_confirmacion() # Llama a la nueva función
        return False


# Selecciona una categoria aleatoriamente
def seleccionar_categoria(categorias):
    categoria_seleccionada = random.choice(list(categorias.keys())) #Elige entre 7, una sola categoria aleatoriamente
    preguntas = categorias[categoria_seleccionada][:] #Copia las preguntas de la categoria seleccionada
    random.shuffle(preguntas) #Mezcla las preguntas de la categoria seleccionada
    return categoria_seleccionada, preguntas

# El usuario va a elegir una respuesta
def elegir_respuesta():
    while True:
        eleccion_respuesta = input("Elegí una opción: ").strip()
        if eleccion_respuesta == "":
            print_eleccion_respuesta_valida()
            continue
        if not eleccion_respuesta.isdigit():
            print_eleccion_respuesta_invalida()
            continue
        eleccion_respuesta = int(eleccion_respuesta)
        return eleccion_respuesta

# Valida si la respuesta es correcta o no
def validacion_respuesta(eleccion_respuesta, pregunta_categoria, vidas, puntaje, monedas):
    eleccion_respuesta = eleccion_respuesta - 1

    if 0 <= eleccion_respuesta < len(pregunta_categoria["opciones"]):
        if pregunta_categoria["opciones"][eleccion_respuesta] == pregunta_categoria["respuesta_correcta"]:
            respuesta_correcta()
            puntaje = sistema_puntuacion(puntaje, pregunta_categoria)
            monedas = sumar_monedas(monedas)
            limpiar_pantalla()    
        else:
            vidas = vidas_restar(vidas)
            respuesta_incorrecta(vidas)
            limpiar_pantalla()
    else:
        vidas = vidas_restar(vidas)
        respuesta_fuera_de_rango(vidas)
        limpiar_pantalla()
    return vidas, puntaje, monedas

# Resta una vida al usuario si la respuesta es incorrecta
def vidas_restar(vidas):
    vidas -= 1
    return vidas

# Verifica si el usuario se quedo sin vidas
def verificacion_vidas(vidas, puntaje):
    if vidas == 0:
        print_fin_juego(puntaje)
        return True
    return False

# Suma el puntaje de la pregunta respondida correctamente
def sistema_puntuacion(puntaje, pregunta_categoria):
    puntaje += pregunta_categoria["puntaje"]
    return puntaje

# Por cada pregunta respondida correctamente ganas 1 moneda
def sumar_monedas(monedas):
    monedas += 1
    return monedas

# Tienda / Monedas # En esta funcion se usan los requirimientos de Sets

# Funcion principal de la tienda
def tienda_de_vidas(monedas, vidas, costo_vida):
    mensaje = (f"¿Desea comprar más vidas o intentar ganarla? Sus monedas {monedas} (si/no) 🛒: ").strip()
    if solicitar_confirmacion(mensaje):
        mostrar_mensaje_tienda(monedas) # Muestra el menú de la tienda
        while True:
            opcion_tienda = input("Elige una opción (1 o 2): ").strip()
            if opcion_tienda == 's':
                monedas, vidas = realizar_compra_vida(monedas, vidas, costo_vida)
                break
            else:
                mostrar_opcion_invalida()
    else:
        mostrar_regreso_juego()
    return monedas, vidas

def solicitar_confirmacion(pregunta): 
    respuestas_si = {"si", "s", "yes", "sí", "SI", "Si"} 
    respuestas_no = {"no", "n", "noo","NO","No"}
    while True:
        confirmacion = input(pregunta).strip()
        if confirmacion in respuestas_si:
            return True
        elif confirmacion in respuestas_no:
            return False
        else:
            mostrar_respuesta_no_valida()
            continue


def realizar_compra_vida(monedas, vidas, costo_vida):
    confirmar_usuario = input(f"¿Confirma la compra de una vida por {costo_vida} monedas? (si/no) 🛒: ")
    if solicitar_confirmacion(confirmar_usuario):
        if monedas >= costo_vida:
            vidas += 1
            monedas -= costo_vida
            mostrar_compra_exitosa(vidas, monedas)
        else:
            mostrar_monedas_insuficientes()
    else:
        mostrar_compra_cancelada()
    return monedas, vidas


# Calcula el tiempo promedio del tiempo por respuesta
def calcular_tiempo_promedio(tiempo_inicio, tiempo_fin, tiempos_respuesta):
    duracion = (tiempo_fin - tiempo_inicio).total_seconds()
    tiempos_respuesta.append(duracion) # Agrega la duración a la lista


def calcular_tiempo_promedio_recursivo(tiempos_respuesta, indice_actual=0, suma_total=0, contador=0):
    # Caso base: si el índice actual es igual o mayor que la longitud de la lista,
    if indice_actual >= len(tiempos_respuesta):
        if contador > 0:
            return suma_total / contador
        else:
            return 0
    # Paso recursivo: toma el tiempo en el índice actual, lo suma y llama a la función con el siguiente índice.
    tiempo_actual = tiempos_respuesta[indice_actual]
    # La llamada recursiva avanza el índice y actualiza la suma y el contador
    recursion = calcular_tiempo_promedio_recursivo(tiempos_respuesta, indice_actual + 1, suma_total + tiempo_actual, contador + 1)
    return recursion

# Calcula la cantidad de veces que fue acertada o errado
def calcular_si_fue_correcta(pregunta_categoria, eleccion_respuesta, aciertos, errores):
    eleccion_respuesta_index = eleccion_respuesta - 1 
    if pregunta_categoria["opciones"][eleccion_respuesta_index] == pregunta_categoria["respuesta_correcta"]:
        aciertos += 1
    else:
        errores += 1
    return aciertos, errores

# para calcular el tiempo
def iniciar_tiempo():
    return datetime.datetime.now()
def finalizar_tiempo():
    return datetime.datetime.now()

def retornar_configuraciones(config):
    aciertos = config.get("aciertos")
    errores = config.get("errores")
    tiempos_respuesta = config.get("tiempos_respuesta")
    vidas = config.get("vidas_iniciales")
    puntaje = config.get("puntaje_inicial")
    monedas = config.get("monedas_iniciales")
    cantidad_preguntas = config.get("cantidad_preguntas")
    path_json = config.get("path_json")
    COSTO_VIDA = config.get("costo_vida")
    return aciertos, errores, tiempos_respuesta, vidas, puntaje, monedas, cantidad_preguntas, path_json, COSTO_VIDA


def proceso_final_del_juego(puntaje, nombre_usuario, monedas, vidas, aciertos, errores, tiempos_respuesta, path_json):
    promedio_tiempo = calcular_tiempo_promedio_recursivo(tiempos_respuesta)
    mostrar_estadisticas_individual (nombre_usuario, puntaje, monedas, vidas, aciertos, errores, promedio_tiempo)
    guardar_estadisticas_json(nombre_usuario, puntaje, monedas, vidas, aciertos, errores, tiempos_respuesta, path_json) # Guardar estadísticas
    matriz = convertir_json_a_matriz(path_json)
    matriz_ordenada = ordenar_burbuja_por_puntaje(matriz)
    mostrar_matriz(matriz_ordenada)

# Requirimientos para promocion 1er parcial
def ordenar_burbuja_por_puntaje(matriz: list) -> list:
    encabezados = matriz[0]
    datos = matriz[1:]
    n = len(datos)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            puntaje_actual = int(datos[j][1])
            puntaje_siguiente = int(datos[j + 1][1])
            if puntaje_actual < puntaje_siguiente:
                
                auxiliar = datos[j]
                datos[j] = datos[j + 1]
                datos[j + 1] = auxiliar
    return [encabezados] + datos
