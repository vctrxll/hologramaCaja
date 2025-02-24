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


audio_path = "../../AUDIOS/ESPANOL/COLGANTE PUNICO.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue = {
        0: "Aquí tenemos un colgante púnico de vidrio de Cartago...",
        5: "... que representa a Baal, también conocido como Melkart, Herakles y Hércules.",
        10: "Descubierto en una antigua fosa de basura de la ciudad íbera de Alon...",
        15: "... este raro hallazgo es uno de los pocos ejemplares encontrados en la Península Ibérica.",
        20: "El amuleto de 5 cm destaca por sus grandes ojos abiertos...",
        25: "... diseñados para repeler el 'mal de ojo' y subraya la importancia de Baal en el panteón cartaginés.",
        30: "Refleja creencias y prácticas culturales antiguas.",
        35: "Este colgante demuestra la habilidad de los artesanos púnicos en el trabajo del vidrio...",
        40: "... y también representa creencias religiosas y prácticas espirituales de Cartago.",
        45: "Destaca la importancia del simbolismo y la indumentaria en su cultura.",
        50: "Su inesperado descubrimiento es un valioso testimonio...",
        55: "... de la rica historia y del legado cultural de Cartago."
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