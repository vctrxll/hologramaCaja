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


audio_path = "../AUDIOS/2025/6.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue = {
    0: "COPA DE SILUETA COMPUESTA CON BASE DE PEDESTAL.",
    3: "Esta copa de silueta compuesta con base de pedestal",
    6: "es una pieza de pasta negra muy fina,",
    10: "con un acabado pulido que demuestra un gran trabajo en su modelado.",
    14: "Aunque su forma es similar a otras piezas de esta vitrina,",
    18: "el color gris, lo delgada de la pieza y su acabado fino",
    22: "la vinculan con el grupo mixteco.",
    25: "Aunque no tiene un soporte visible,",
    28: "se asemeja a una vasija que se exhibe aquí,",
    31: "lo que sugiere que originalmente tuvo una base de pedestal alto.",
    35: "Esta copa fue colocada boca abajo,",
    38: "lo cual es común en piezas funerarias de contextos como las cuevas,",
    42: "donde este tipo de postura tiene un significado ritual.",
    47: "Es un ejemplo claro de la sofisticación de la cerámica mixteca."
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