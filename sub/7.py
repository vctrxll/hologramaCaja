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


audio_path = "../AUDIOS/2025/7.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue = {
    0: "OLLA MINIATURA.",
    1: "Hoy les presento la Olla Miniatura,",
    5: "una representación de una olla de cuello curvo con aditamento de asas.",
    10: "Esta pieza está elaborada en barro burdo de tonalidades claras;",
    15: "el color blanco del exterior proviene de residuos adheridos por el paso del tiempo.",
    20: "Durante la época prehispánica, las representaciones en miniatura",
    25: "eran parte cotidiana de la vida,",
    27: "hallándose formas como platos, cuecos, jarras, ollas, cántaros",
    32: "e incluso vasijas rituales tales como sahumadores o incensarios.",
    37: "Por largo tiempo se interpretaron como juguetes,",
    40: "similar a lo que ocurre hoy en día.",
    43: "Sin embargo, estudios de residuos químicos en algunas vasijas del centro de México",
    48: "han permitido proponer su uso como recipientes rituales,",
    53: "en los que se depositaba el líquido precioso de la sangre",
    55: "para ofrendas a deidades."
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