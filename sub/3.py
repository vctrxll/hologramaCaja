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


audio_path = "../AUDIOS/2025/3.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue = {
    0: "VASO POLÍCROMO TRÍPODE.",
    3: "En esta quinta pieza les presento el Vaso Policromo Trípode,",
    8: "una pieza excepcional elaborada con una pasta muy fina",
    12: "y de vibrante coloración naranja.",
    14: "Aunque sus paredes son delgadas, la precisión en sus detalles destaca,",
    19: "en especial los soportes que, pese a no estar presentes,",
    22: "se reconocen por su estilo y decoración.",
    25: "Los estudios identifican estos soportes en una tradición pictórica del Posclásico tardío,",
    32: "caracterizada por colores como el naranja, rojo, blanco, ocre",
    37: "y tonalidades especiales para la cultura de la Chinantla, incluso el rosa.",
    43: "Los motivos simbolizan el poder del sol:",
    46: "un gran círculo central engalanado con pequeñas joyas, alas de águila",
    51: "y una banda en el borde con rayos y turquesa.",
    55: "Esta obra refleja la adoración al astro rey,",
    58: "considerado como joya preciosa."
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