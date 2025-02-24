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


audio_path = "../../AUDIOS/ESPANOL/8E.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue =  {
        0: "Aquí presentamos una fascinante vasija efigie antropomorfa...",
        5: "... representando a un personaje asociado a un chinanteco Pichinche.",
        10: "Un antiguo poblador de lo que se conocía como la Chinantla Pichinche...",
        15: "... cercano al actual pueblo de Yolox.",
        20: "Podemos identificar esta particularidad gracias al peinado del personaje...",
        25: "... una especie de trenzado que recorre toda su cabeza.",
        30: "El personaje representado parece estar muerto, con los ojos entrecerrados...",
        35: "... simbolizando la última imagen del mundo terrenal.",
        40: "Su boca abierta sugiere que su espíritu se está escapando...",
        45: "... reflejando la visión y las creencias sobre la muerte y el más allá en la cultura chinanteca."
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