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


audio_path = "../../AUDIOS/ESPANOL/HERMA CON EL BUSTO DE BACO.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue = {
        0: "Aquí presentamos un herma con el busto de Baco...",
        5: "... esculpida en mármol amarillo de Túnez, conocido como giallo antico.",
        10: "Esta pieza destaca por su barba y una diadema de mirto con flores...",
        15: "... aportando un toque orientalizante a sus facciones.",
        20: "Fue hallada en una habitación de una casa en la parte alta de Baetulo.",
        25: "Este descubrimiento refleja la influencia y la estética romanas...",
        30: "... combinando elementos artísticos orientales y occidentales en una representación única.",
        35: "Baco, el dios del vino y el éxtasis, era venerado por su conexión con la naturaleza y la fertilidad.",
        40: "La herma muestra la habilidad de los artesanos romanos en el manejo del mármol...",
        45: "... e ilustra la integración cultural en la decoración y la religión de la época.",
        50: "Sirve como un testimonio valioso de la historia y el legado artístico de Baetulo."
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