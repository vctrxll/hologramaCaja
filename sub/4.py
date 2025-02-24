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


audio_path = "../../AUDIOS/ESPANOL/ESCUDO ANTIGUO DE TRES DISCOS.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue = {
        0: "Aquí presentamos un escudo antiguo de tres discos...",
        5: "... encontrado en un cementerio púnico en 1909 cerca de la ciudad de Ksour Essef, en la gobernación de Mahdia, Túnez.",
        10: "Esta pieza, que data generalmente del siglo III a.C., es de origen italiano...",
        15: "... y proviene del sur de Italia.",
        20: "Su hallazgo en Túnez llevó a los investigadores a asociarlo con las expediciones de la Segunda Guerra Púnica...",
        25: "... lideradas por el general cartaginés Aníbal en Italia entre los años 211 y 203 a.C.",
        30: "Actualmente, el escudo se encuentra en el Museo Nacional del Bardo en Túnez...",
        35: "... junto con el material arqueológico encontrado en la misma tumba.",
        40: "Un siglo después de su descubrimiento, sigue siendo una de las piezas simbólicas más destacadas...",
        45: "... de la sección antigua a la que pertenece."
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