from funciones_logicas import *

# Inicia el juego de Preguntadas y respuestas

def jugar_preguntados():
    print_bienvenida()
    config = cargar_configuracion("C:\\Users\\aleca\\OneDrive\\Escritorio\\Alejandro Fernández - Terminal\\config.json")
    aciertos, errores, tiempos_respuesta, vidas, puntaje, monedas, cantidad_preguntas, path_json, costo_vida = retornar_configuraciones(config)

    nombres_de_usuarios = cargar_nombre_usuarios(path_json)

    categorias = cargar_preguntas_csv("C:\\Users\\aleca\\OneDrive\\Escritorio\\Alejandro Fernández - Terminal\\preguntas.csv")

    categoria_seleccionada, preguntas = seleccionar_categoria(categorias)
    preguntas = preguntas[:cantidad_preguntas]

    nombre_usuario = crear_usuario_final(nombres_de_usuarios)
    for orden_pregunta, pregunta_categoria in enumerate(preguntas):
        print_enunciado(categoria_seleccionada, pregunta_categoria, orden_pregunta)
        tiempo_inicio = iniciar_tiempo()

        eleccion_respuesta = elegir_respuesta()
        vidas, puntaje, monedas = validacion_respuesta(eleccion_respuesta, pregunta_categoria, vidas, puntaje, monedas)

        tiempo_fin = finalizar_tiempo()
        calcular_tiempo_promedio(tiempo_fin,tiempo_inicio, tiempos_respuesta)
        aciertos, errores = calcular_si_fue_correcta(pregunta_categoria, eleccion_respuesta, aciertos, errores)

        monedas, vidas = tienda_de_vidas(monedas, vidas, costo_vida)
        if verificacion_vidas(vidas, puntaje):
            proceso_final_del_juego(puntaje, nombre_usuario, monedas, vidas, aciertos, errores, tiempos_respuesta, path_json)
            break
    else:
        print_juego_ganado(puntaje)
        proceso_final_del_juego(puntaje, nombre_usuario, monedas, vidas, aciertos, errores, tiempos_respuesta, path_json)
