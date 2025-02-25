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


audio_path = "../AUDIOS/2025/0.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue = {
    0: "CAJETE GRIS TRÍPODE CON SOPORTES DE SERPIENTE",
    2: "un cajete elaborado en arcilla gris fina.",
    7: "Su diseño destaca por el uso de moldes para crear relieves de serpientes en los soportes",
    12: "un motivo que simboliza la conexión entre la vida y el más allá. ",
    18: "Esta vasija pertenece a la tradición del Posclásico en Oaxaca",
    22: "y fue confeccionada con una pasta única",
    26: " utilizada por grupos indígenas como los chinantecos y mazatecos",
    30: "Se han encontrado ejemplares similares en importantes centros ceremoniales, ",
    35: "lo que sugiere vínculos culturales con otras civilizaciones prehispánicas.",
    40: "Además, su hallazgo en contextos funerarios resalta su función ritual y espiritual",
    47: "Descubran cómo cada detalle de esta pieza narra historias del pasado",
    51: "y enriquece nuestro conocimiento ancestral",
    54: "Una obra que cautiva e inspira profundamente."
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