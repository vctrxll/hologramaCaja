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


audio_path = "../AUDIOS/2025/8.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue = {
    0: "OLLA MINIATURA.",
    3: "Esta es la segunda Olla Miniatura,",
    6: "una representación de un cántaro con borde recto divergente,",
    8: "elaborada con barro oscuro y un acabado liso.",
    11: "Aunque carece de un fragmento en su borde debido al paso del tiempo,",
    16: "su diseño refleja la destreza de los artesanos de la época.",
    20: "Las piezas miniatura eran comunes en la época prehispánica,",
    25: "y encontramos todo tipo de formas, como platos, cuencos, jarras,",
    28: "ollas y cántaros, así como vasijas rituales como sahumadores e incensarios.",
    34: "Durante mucho tiempo se pensó que estas piezas eran juguetes,",
    39: "pero estudios recientes han revelado",
    42: "que algunas de estas vasijas contenían residuos de sangre.",
    45: "Esto sugiere que se usaban como recipientes rituales",
    50: "para ofrendar sangre a deidades",
    52: "o durante celebraciones en los calendarios ceremoniales."
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