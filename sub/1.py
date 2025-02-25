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


audio_path = "../AUDIOS/2025/1.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue = {
    0: "CAJETE GRIS DE SILUETA COMPUESTA TRÍPODE:",
    3: "La segunda de la exhibición es el CAJETE GRIS DE SILUETA COMPUESTA TRÍPODE.",
    8: "Aunque carece de soportes, se cree que originalmente se añadían figuras animales",
    14: "como serpientes o venados, en cuyo caso se representaba una pezuña.",
    18: "Esta tradición, propia de los grupos chinantecos y mazatecos, se distingue por la suavidad",
    26: "de su pasta, similar a la textura de un gis.",
    29: "Aunque este tipo de vasija se encuentra en diversas regiones de Oaxaca,",
    33: "su silueta compuesta es particularmente característica en estos grupos.",
    38: "Se usaba tanto como objeto de servicio cotidiano como en rituales mortuorios,",
    44: "ya que se han descubierto en tumbas de la cuenca del Papaloapan.",
    48: "Algunos exploradores del siglo pasado relataron la presencia de ofrendas de pequeños animales,",
    55: "como peces."
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