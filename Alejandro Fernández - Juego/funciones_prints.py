import os 
import funciones_logicas

# Funcion para limpiar la pantalla de la consola
# (Esta funcion se utiliza para que el usuario pueda ver mejor las preguntas y respuestas)
def limpiar_pantalla():
    """Limpia la consola para una mejor experiencia de usuario."""
    input ("Aprete Enter para continuar.. ")
    os.system('cls' if os.name == 'nt' else 'clear')

#Muestra la bienvenida del juego al usuario por consola
def print_bienvenida():
    print("")
    print("Bienvenido al juego​​​​​🕹️​​ de preguntas y respuestas")
    print("Se harán preguntas dependiendo de la temática elegida al azar​​💬​")
    print("Solo tienes 3 vidas")
    print("")
    print("¡Responde correctamente para acumular el máximo de puntos!")
    print("Cada pregunta, tiene una dificultad que influye en el puntaje ganado, de la siguiente manera:")
    print("")
    print("Facil: 3️⃣")
    print("Medio: 6️⃣")
    print("Dificil: 9️⃣")

    limpiar_pantalla()

# Muestra el enunciado de la pregunta y las opciones de respuesta
def print_enunciado(categoria_seleccionada, pregunta_categoria, orden_pregunta):
    print(f"La temática elegida fue: {categoria_seleccionada}")
    print(f"Pregunta {orden_pregunta + 1}: {pregunta_categoria['enunciado']}")
    print("")
    for i, opcion in enumerate(pregunta_categoria['opciones'], 1):
        print(f"{i}. {opcion}")
    print("")
    print(f"Dificultad: {pregunta_categoria["dificultad"]}")
    print(f"Puntaje: {pregunta_categoria["puntaje"]} 📊​")
    print("")

# Muestra los mensajes de las validaciones de las respuestas del usuario
def respuesta_correcta():
    print("")
    print("Respuesta correcta ✔️")
    print("Te ganaste 1 moneda 💰​")
    print("")
def respuesta_incorrecta(vidas):
    print("Respuesta incorrecta ❌")
    print(f"Se ha perdido 1 vida 💖​, te quedan {vidas} 💖")
    print("")
def respuesta_fuera_de_rango(vidas):
    print("Respuesta fuera de rango, se restara una vida")
    print(f"Se ha perdido 1 vida 💖​, te quedan {vidas} 💖")

# Muestra el mensaje de fin del juego
def print_fin_juego(puntaje):
    print("Fin del juego 😥​")
    print("Te quedaste sin vidas 💔 ")
    print(f"Tu puntaje final es: {puntaje} 📊​")
    limpiar_pantalla()

def print_juego_ganado(puntaje):
    print("¡Felicidades! Has llegado al fin del juego 🎉")
    print(f"Tu puntaje final es: {puntaje} 📊​")
    limpiar_pantalla()

# Mensajes que se van a usar durante la tienda
def elementos_disponibles():
    print("Vidas = $3")

# Muestra basicamente la matriz ordenada
def mostrar_matriz(matriz):
    print("\n📊 Estadísticas acumuladas globales:\n")
    for fila in matriz:
        print(" | ".join(col.ljust(20) for col in fila))

# Mensaje para mostrar el menu de la tienda
def mensaje_para_tienda(monedas):
    """Muestra el menú de opciones de la tienda."""
    print("\n")
    print(f"Usted tiene {monedas} monedas")
    print("🛒 Elementos disponibles en la tienda:")
    print("1. + 1 vida extra = 3 monedas")
    print("2. Jugar minijuego por 1 vida (gratis, pero arriesgado)")

def imprimir_mensaje_usuario_ya_existe():
    """Imprime el mensaje cuando un nombre de usuario ya está en uso."""
    print("Este nombre de usuario ya existe. Por favor elige otro.")

def imprimir_mensaje_usuario_creado(nombre_usuario):
    """Imprime el mensaje de confirmación de creación de usuario."""
    print(f"¡Excelente! '{nombre_usuario}' ha sido creado.")
    print("")

def imprimir_mensaje_usuario_cancelado():
    """Imprime el mensaje cuando el usuario cancela la creación del nombre."""
    print("Ok, ingrese un nuevo nombre de usuario.")

def imprimir_mensaje_respuesta_no_valida_confirmacion():
    """Imprime el mensaje de error para respuestas inválidas en la confirmación."""
    print("Respuesta no válida. Por favor, responde 'si' o 'no'. Intenta de nuevo con un nombre de usuario.")

def imprimir_mensaje_nombre_usuario_vacio():
    """Imprime el mensaje si el nombre de usuario es vacío."""
    print("El nombre de usuario no puede estar vacío. Por favor, ingresa un nombre.")


def print_eleccion_respuesta_valida():
    print("Por favor, ingresá una opción válida.")

def print_eleccion_respuesta_invalida():
    print("Por favor, ingresá un número válido.")


def mostrar_mensaje_tienda(monedas):
    """Muestra el menú de la tienda."""
    print(f"\n--- Tienda de Vidas ---")
    print(f"Monedas actuales: {monedas} 💰")
    print("$3. ¿Desea Comprar una vida?")
    print("-----------------------")

def mostrar_opcion_invalida():
    """Muestra un mensaje cuando la opción ingresada no es válida."""
    print("Opción no válida. Por favor, elige '1' o '2'.")

def mostrar_regreso_juego():
    """Muestra un mensaje al volver al juego."""
    print("Volviendo al juego..")

def mostrar_respuesta_no_valida():
    """Muestra un mensaje cuando la respuesta de confirmación no es válida."""
    print("Respuesta no válida. Por favor, responde 'si' o 'no'.")

def mostrar_compra_exitosa(vidas, monedas):
    """Muestra un mensaje de compra de vida exitosa."""
    print(f"✅ Compra exitosa. Ahora tenés {vidas} vidas y {monedas} monedas 💰.")

def mostrar_monedas_insuficientes():
    """Muestra un mensaje cuando no hay suficientes monedas."""
    print("❌ No tenés monedas suficientes.")

def mostrar_compra_cancelada():
    """Muestra un mensaje cuando la compra es cancelada."""
    print("🛑 Compra cancelada.")

def mostrar_inicio_minijuego():
    """Muestra un mensaje al iniciar el minijuego."""
    print("\n¡Vamos a jugar el minijuego para ganar una vida!")

def mostrar_vida_ganada(vidas):
    """Muestra un mensaje de vida ganada en el minijuego."""
    print(f"🎉 ¡Felicidades! Has ganado una vida. Ahora tenés {vidas} vidas.")

def mostrar_vida_no_ganada():
    """Muestra un mensaje cuando no se logra ganar la vida en el minijuego."""
    print("😔 Lo siento, no lograste ganar la vida en el minijuego.")


def mostrar_estadisticas_individual(nombre_usuario, puntaje, monedas, vidas, aciertos, errores, promedio_tiempo):
    print("\n--- Estadísticas Individuales ---")
    
    print(f"\nEstadísticas de {nombre_usuario}:")
    print(f"Puntaje final: {puntaje}")
    print(f"Monedas restantes: {monedas}")
    print(f"Vidas restantes: {vidas}")
    print(f"Respuestas correctas: {aciertos}")
    print(f"Respuestas incorrectas: {errores}")
    print(f"Tiempo promedio por respuesta: {promedio_tiempo:.2f} segundos") # Muestra el promedio
