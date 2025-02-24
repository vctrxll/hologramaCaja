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


audio_path = "../../AUDIOS/ESPANOL/PEDANTE FENICIO DE CRISTAL.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue = {
    0: "Aquí tenemos un pedante fenicio de cristal en forma de cabeza barbuda...",
    5: "... originario de Cartago y datado en los siglos IV a III a.C.",
    10: "Actualmente, esta pieza está expuesta en el Museo Nacional del Bardo en Túnez...",
    15: "... y es un ejemplo exquisito de la maestría en el trabajo del vidrio de los fenicios.",
    20: "Una técnica que alcanzaron con gran perfección...",
    25: "... y que refleja la sofisticación de su cultura.",
    30: "La representación de la barba puede indicar sabiduría o autoridad...",
    35: "... rasgos valorados en muchas culturas antiguas.",
    40: "Este colgante no solo demuestra la habilidad artesanal fenicia...",
    45: "... sino que también ofrece una ventana a las prácticas espirituales y la vida cotidiana en la antigua Cartago.",
    50: "Revela la importancia de los amuletos y la simbología religiosa en esta civilización marítima avanzada...",
    55: "... sirviendo como un puente entre el pasado remoto y el presente."
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