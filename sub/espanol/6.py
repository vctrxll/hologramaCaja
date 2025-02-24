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


audio_path = "../../AUDIOS/ESPANOL/10E.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue = {
        0: "Hoy les presento un cajete gris trípode de pasta fina...",
        5: "... elaborado por los grupos culturales chinantecos y mazatecos durante el Posclásico Tardío.",
        10: "Este tipo de vasija es especialmente notable por su diseño y uso ceremonial...",
        15: "... distinguiéndose por su forma trípode, que le da estabilidad y eleva la vasija del suelo.",
        20: "Lo que realmente destaca en esta pieza es el motivo decorativo en su fondo...",
        25: "... realizado cuando la vasija aún estaba fresca.",
        30: "Este motivo es una cruz que divide la vasija en los cuatro puntos cardinales...",
        35: "... un diseño que refleja la importancia simbólica de la orientación y el cosmos en la cultura de estos pueblos.",
        40: "El hecho de que este tipo de vasijas se haya encontrado exclusivamente en recintos funerarios...",
        45: "... sugiere que tenían un uso ritual específico.",
        50: "Estas vasijas no eran simples objetos cotidianos...",
        55: "... sino que desempeñaban un papel en los rituales relacionados con la muerte y el más allá."
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