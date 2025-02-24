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


audio_path = "../../AUDIOS/ESPANOL/JARRO DE ARCILLA PÚNICO.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue = {
        0: "Aquí tenemos un jarro de arcilla púnico...",
        5: "... un artefacto representativo del arte y la utilidad en la antigua civilización cartaginense.",
        10: "Este recipiente, moldeado meticulosamente con arcilla local...",
        15: "... destaca por su diseño robusto y funcional.",
        20: "Típicamente utilizado para el almacenamiento y transporte de alimentos y líquidos...",
        25: "... esencial para el comercio marítimo y la vida cotidiana púnica.",
        30: "El jarro refleja la pericia técnica de los artesanos púnicos en cerámica...",
        35: "... conocidos por su habilidad para crear objetos duraderos y estéticamente agradables.",
        40: "Su forma y material nos ofrecen una ventana al pasado...",
        45: "... revelando detalles sobre las prácticas diarias y económicas de Cartago.",
        50: "Este jarro no solo es un testimonio de la vida diaria...",
        55: "... sino también un vestigio de las rutas comerciales del Mediterráneo antiguo."
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