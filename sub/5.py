import pygame
import time
import os

# Inicializar pygame y cargar un audio de prueba
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Arial", 40)


# Configuración inicial de la pantalla sin bordes
def create_subtitle_window():
    text_surface = font.render("Cargando...", True, (255, 255, 255))
    text_width, text_height = text_surface.get_size()
    return pygame.display.set_mode((text_width + 1200, text_height + 20), pygame.NOFRAME)


os.environ['SDL_VIDEO_WINDOW_POS'] = "50,770"  # Ajusta las coordenadas según necesidad
screen = create_subtitle_window()


audio_path = "../AUDIOS/2025/5.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue = {
    0: "OLLA BAJA POLICROMA TRÍPODE",
    3: "Esta es la séptima parada de nuestro recorrido.",
    10: "Aquí destacamos la Olla Baja Policroma Trípode,",
    13: "una vasija fina elaborada en arcilla de tonalidad crema y de grosor delicado.",
    15: "Sus características, en la pasta, forma y decoración,",
    20: "la convierten en una pieza diagnóstica de la región chinanteca.",
    24: "Su ornamentación está vinculada a rituales ancestrales y simbolismos profundos.",
    30: "La presencia de una serpiente fantástica invita a relacionarla con Quetzalcóatl,",
    38: "importante divinidad mesoamericana, que simboliza fertilidad, creación y el orden del cosmos.",
    44: "En el borde, se aprecia una banda solar simplificada",
    48: "con representaciones de rayos y espinas de sacrificio en tonalidades rojas y negras.",
    54: "Cada detalle revela un mensaje sagrado",
    56: "y la profunda espiritualidad de culturas antiguas,",
    59: "invitándonos a reflexionar sobre el misticismo y la historia de estos pueblos.",
    65: "Esta pieza enriquece nuestra colección",
    69: "y conecta nuestro presente con el eco de tiempos sagrados."
}

start_time = time.time()
running = True
while running:
    elapsed_time = int(time.time() - start_time)

    # Buscar el subtítulo correspondiente al tiempo transcurrido
    subtitle = ""
    for timestamp in sorted(dialogue.keys()):
        if elapsed_time >= timestamp:
            subtitle = dialogue[timestamp]
        else:
            break

    # Renderizar subtítulo y actualizar pantalla
    if subtitle:
        screen.fill((0, 0, 0))  # Fondo negro
        text_surface = font.render(subtitle, True, (255, 255, 255))
        text_width, text_height = text_surface.get_size()
        screen.blit(text_surface, (20, 10))

    pygame.display.update()

    # Manejo de eventos para salir
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            running = False

    # Detener cuando termine el audio
    if elapsed_time >= audio_length:
        running = False

pygame.quit()