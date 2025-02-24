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


audio_path = "../../AUDIOS/ESPANOL/6E.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue = {
    0: "Aquí tenemos una olla baja policroma trípode, una pieza excepcionalmente fina y elaborada con destreza.",
    5: "Esta olla, hecha de una arcilla muy fina y con un grosor de sólo 3 mm, no se ha encontrado en ningún otro lugar de Mesoamérica...",
    10: "... lo que la convierte en una forma diagnóstica y única.",
    15: "La decoración de esta olla es especialmente notable por sus temas rituales, asociados a una serpiente fantástica que podría ser una de las deidades más importantes en la mitología mesoamericana.",
    20: "La imagen de la serpiente fantástica sugiere un significado relacionado con el cosmos.",
    25: "En el cuello de la vasija, encontramos una banda solar simplificada.",
    30: "Está compuesta por rayos solares pintados en rojo y espinas de sacrificio, elementos que evocan prácticas y simbolismos rituales.",
    35: "Los rayos solares y las espinas de sacrificio indican la importancia del Sol en las ceremonias religiosas y su relación con el sacrificio...",
    40: "... un tema recurrente en las culturas mesoamericanas.",
    45: "Esta olla es, sino también, un testimonio de sus creencias, ofreciendo una visión fascinante de su mundo espiritual."
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