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


audio_path = "../AUDIOS/2025/4.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue = {
    0: "CAJETE TRÍPODE DE FONDO SELLADO.",
    3: "Esta pieza aquí es un cajete trípode de fondo sellado,",
    9: "una pieza típica de los habitantes de la cuenca del Papaloapan.",
    13: "Se caracteriza por su forma hemisférica",
    15: "y por un fondo que fue sellado con moldes de barro cocido.",
    20: "Estos sellos, utilizados para crear relieves en la base de la vasija,",
    25: "son la principal distintiva de este tipo de cerámica.",
    28: "Los cajetes cumplían dos funciones importantes:",
    32: "servían para preparar alimentos, de manera similar al molcajete,",
    36: "y también formaban parte de ofrendas mortuorias,",
    40: "ya que no muestran desgaste en su fondo sellado,",
    44: "lo que sugiere que se usaban exclusivamente con fines ceremoniales.",
    48: "Este tipo de cerámica refleja la habilidad",
    51: "y el simbolismo de los pueblos antiguos de la región."
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