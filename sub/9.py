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


audio_path = "../AUDIOS/2025/9.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue = {
    0: "COPA DE SILUETA COMPUESTA CON BASE DE PEDESTAL",
    3: "Por último, presento la Copa de Silueta Compuesta con Base de Pedestal,",
    8: "una vasija de paredes delgadas,",
    10: "elaborada en arcilla gris oscura con acabado pulido.",
    14: "Sus dimensiones sugieren que es una pieza miniatura.",
    17: "Se asemeja a la pieza número 8 de esta vitrina;",
    22: "sin embargo, aunque se clasifica en la vajilla gris de la región oaxaqueña,",
    26: "su color y acabado remiten al grupo mixteco.",
    30: "Es un bien de prestigio, con alto valor comercial,",
    33: "registrado en la cuenca del Papaloapan desde los años 30 del siglo pasado",
    38: "como 'cerámica negra pulida'.",
    40: "La singular horadación en su base, similar a la cola de una serpiente de fuego,",
    45: "se relaciona con imágenes de códices antiguos.",
    49: "Esta pieza es exponente de la artesanía prehispánica",
    52: "que une tradiciones mixtecas y oaxaqueñas."
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