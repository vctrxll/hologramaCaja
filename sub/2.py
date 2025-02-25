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


audio_path = "../AUDIOS/2025/2.mp3"
audio = pygame.mixer.Sound(audio_path)
audio_length = audio.get_length()

# Diccionario con subtítulos sincronizados
dialogue = {
    0: "JARRA DE CUERPO ELIPSOIDAL",
    2: "La tercera pieza en esta vasta exhibición es una jarra de cuerpo elipsoidal.",
    8: "Su elegante cuello alto y su forma ovoide fueron modelados en una pasta gris muy",
    12: "oscura, similar a las que usaban los grupos mixtecos y zapotecos",
    18: "en la última etapa prehispánica de Mesoamérica.",
    22: "Aunque parece una vasija para líquidos,",
    25: "no posee el recubrimiento necesario para contenerlos,",
    29: "lo que indica que fue creada especialmente para integrarse en ofrendas rituales.",
    35: "Este tipo de jarra es común en los Valles Centrales de Oaxaca y la región Mixteca,",
    40: "pero es muy escasa en la región serrana,",
    43: "resaltando su alto valor como objeto de intercambio comercial.",
    47: "Una obra que nos invita a descubrir la espiritualidad",
    53: "y las complejas relaciones culturales del pasado."
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