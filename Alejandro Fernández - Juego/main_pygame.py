import pygame
import sys
import random
from funciones_archivos import cargar_preguntas_csv 
# ^ Reusamos tu función de archivos tal cual la tenés. 
# Asegurate de que funciones_archivos.py esté en la misma carpeta.

# --- CONFIGURACIÓN INICIAL ---
pygame.init()

# Colores (R, G, B)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)
AZUL = (50, 150, 250)
VERDE = (50, 200, 50)
ROJO = (200, 50, 50)

# Pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Preguntados - Versión Pygame")

# Fuentes (Tipografías)
FUENTE_TITULO = pygame.font.SysFont("Arial", 40, bold=True)
FUENTE_TEXTO = pygame.font.SysFont("Arial", 24)
FUENTE_BOTON = pygame.font.SysFont("Arial", 20, bold=True)

# Estados del Juego
ESTADO_MENU = "MENU"
ESTADO_JUGANDO = "JUGANDO"
ESTADO_GAMEOVER = "GAMEOVER"

# --- CLASES ---

class Boton:
    def __init__(self, x, y, ancho, alto, texto, color_base, accion=None):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.color_base = color_base
        self.color_hover = (min(color_base[0]+30, 255), min(color_base[1]+30, 255), min(color_base[2]+30, 255))
        self.accion = accion # Qué valor devuelve este botón si lo tocan

    def dibujar(self, superficie):
        pos_mouse = pygame.mouse.get_pos()
        # Cambiar color si el mouse está encima
        color = self.color_hover if self.rect.collidepoint(pos_mouse) else self.color_base
        
        pygame.draw.rect(superficie, color, self.rect, border_radius=10)
        pygame.draw.rect(superficie, NEGRO, self.rect, 2, border_radius=10) # Borde
        
        # Renderizar texto centrado
        texto_surf = FUENTE_BOTON.render(self.texto, True, NEGRO)
        texto_rect = texto_surf.get_rect(center=self.rect.center)
        superficie.blit(texto_surf, texto_rect)

    def clic(self, evento):
        # Detectar si hicieron clic en el botón
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                return True
        return False

# --- VARIABLES GLOBALES DEL JUEGO ---
estado_actual = ESTADO_MENU
datos_juego = {
    "vidas": 3,
    "puntaje": 0,
    "monedas": 0,
    "pregunta_actual": None,
    "botones_opciones": [],
    "mensaje_resultado": "" # Para mostrar "Correcto!" o "Incorrecto"
}
lista_preguntas = []

# --- FUNCIONES ---

def iniciar_partida():
    global datos_juego, lista_preguntas
    
    # Reiniciar stats
    datos_juego["vidas"] = 3
    datos_juego["puntaje"] = 0
    datos_juego["monedas"] = 0
    datos_juego["mensaje_resultado"] = ""
    
    # Cargar preguntas usando TU archivo y función existente
    # OJO: Chequeá que la ruta sea correcta o poné solo "preguntas.csv" si está al lado.
    categorias = cargar_preguntas_csv("preguntas.csv") 
    
    # Aplanamos las categorías en una sola lista para hacerlo simple por ahora
    lista_preguntas = []
    for cat, preguntas in categorias.items():
        lista_preguntas.extend(preguntas)
    
    random.shuffle(lista_preguntas)
    cargar_nueva_pregunta()

def cargar_nueva_pregunta():
    global datos_juego
    if not lista_preguntas:
        datos_juego["pregunta_actual"] = None # No hay más preguntas
        return

    pregunta = lista_preguntas.pop(0)
    datos_juego["pregunta_actual"] = pregunta
    
    # Crear botones para las opciones (posiciones fijas)
    opciones = pregunta["opciones"]
    # random.shuffle(opciones) # Si querés mezclar el orden de los botones
    
    botones = []
    # Creamos 4 botones, 2 arriba y 2 abajo
    coords = [(50, 250), (450, 250), (50, 400), (450, 400)]
    
    for i, texto_opcion in enumerate(opciones):
        x, y = coords[i]
        # El botón guarda el texto de la opción como su 'accion'
        botones.append(Boton(x, y, 300, 80, texto_opcion, AZUL, accion=texto_opcion))
    
    datos_juego["botones_opciones"] = botones
    datos_juego["mensaje_resultado"] = ""

def verificar_respuesta(texto_elegido):
    global estado_actual
    pregunta = datos_juego["pregunta_actual"]
    
    if texto_elegido == pregunta["respuesta_correcta"]:
        datos_juego["puntaje"] += pregunta["puntaje"]
        datos_juego["monedas"] += 1
        datos_juego["mensaje_resultado"] = "¡CORRECTO! +1 Moneda"
        # Pequeña pausa o efecto podría ir acá, por ahora pasamos directo
        pygame.time.delay(500) # Espera medio segundo
        cargar_nueva_pregunta()
    else:
        datos_juego["vidas"] -= 1
        datos_juego["mensaje_resultado"] = "¡INCORRECTO! -1 Vida"
        pygame.time.delay(500)
        
        if datos_juego["vidas"] <= 0:
            estado_actual = ESTADO_GAMEOVER
        else:
            cargar_nueva_pregunta()
            
    # Si se acabaron las preguntas, terminamos
    if datos_juego["pregunta_actual"] is None and datos_juego["vidas"] > 0:
         datos_juego["mensaje_resultado"] = "¡GANASTE! No hay más preguntas."
         estado_actual = ESTADO_GAMEOVER

# --- BUCLE PRINCIPAL ---
boton_jugar = Boton(300, 300, 200, 80, "JUGAR", VERDE)
boton_salir = Boton(300, 450, 200, 60, "SALIR", ROJO)
boton_reiniciar = Boton(300, 400, 200, 80, "VOLVER AL MENU", AZUL)

reloj = pygame.time.Clock()

while True:
    # 1. Manejo de Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if estado_actual == ESTADO_MENU:
            if boton_jugar.clic(evento):
                iniciar_partida()
                estado_actual = ESTADO_JUGANDO
            if boton_salir.clic(evento):
                pygame.quit()
                sys.exit()
                
        elif estado_actual == ESTADO_JUGANDO:
            # Revisar clics en las opciones
            if datos_juego["pregunta_actual"]:
                for boton in datos_juego["botones_opciones"]:
                    if boton.clic(evento):
                        verificar_respuesta(boton.accion)
                        
        elif estado_actual == ESTADO_GAMEOVER:
            if boton_reiniciar.clic(evento):
                estado_actual = ESTADO_MENU

    # 2. Dibujar Pantalla
    pantalla.fill(BLANCO) # Limpiar fondo

    if estado_actual == ESTADO_MENU:
        # Título
        texto = FUENTE_TITULO.render("PREGUNTADOS: EDICIÓN PYGAME", True, NEGRO)
        pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 100))
        
        # Botones
        boton_jugar.dibujar(pantalla)
        boton_salir.dibujar(pantalla)

    elif estado_actual == ESTADO_JUGANDO:
        # Barra superior (Vidas, Puntaje)
        info = f"Vidas: {datos_juego['vidas']} | Puntaje: {datos_juego['puntaje']} | Monedas: {datos_juego['monedas']}"
        texto_info = FUENTE_TEXTO.render(info, True, NEGRO)
        pantalla.blit(texto_info, (20, 20))
        
        if datos_juego["pregunta_actual"]:
            # Dibujar pregunta (con ajuste de línea básico si es muy larga)
            enunciado = datos_juego["pregunta_actual"]["enunciado"]
            texto_preg = FUENTE_TITULO.render(enunciado, True, NEGRO)
            # Centrar pregunta
            rect_preg = texto_preg.get_rect(center=(ANCHO//2, 150))
            pantalla.blit(texto_preg, rect_preg)
            
            # Dibujar botones de opciones
            for boton in datos_juego["botones_opciones"]:
                boton.dibujar(pantalla)
                
            # Mostrar dificultad
            dif = datos_juego["pregunta_actual"]["dificultad"]
            texto_dif = FUENTE_TEXTO.render(f"Dificultad: {dif}", True, GRIS)
            pantalla.blit(texto_dif, (ANCHO - 150, 20))
            
    elif estado_actual == ESTADO_GAMEOVER:
        titulo = "¡JUEGO TERMINADO!"
        if datos_juego["vidas"] > 0:
             titulo = "¡GANASTE!"
             
        texto_go = FUENTE_TITULO.render(titulo, True, ROJO)
        pantalla.blit(texto_go, (ANCHO//2 - texto_go.get_width()//2, 150))
        
        texto_puntaje = FUENTE_TEXTO.render(f"Puntaje Final: {datos_juego['puntaje']}", True, NEGRO)
        pantalla.blit(texto_puntaje, (ANCHO//2 - texto_puntaje.get_width()//2, 250))
        
        boton_reiniciar.dibujar(pantalla)

    # 3. Actualizar Frame
    pygame.display.flip()
    reloj.tick(60)