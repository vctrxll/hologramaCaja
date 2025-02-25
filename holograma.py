from math import sqrt
import cv2
import mediapipe as mp  # Importa 'mediapipe' para la detección y el seguimiento de manos.
import open3d as o3d  # Importa la biblioteca 'open3d' para trabajar con modelos 3D.
import os
import platform
import time
import subprocess
import pygame
import pygetwindow as gw
import tkinter as tk
from tkinter import messagebox

pygame.init()

root = tk.Tk()
root.withdraw()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, 'render_options.json')
PIEZAS_PATH = os.path.join(BASE_DIR, "source")
AUDIOS_PATH = os.path.join(BASE_DIR, "AUDIOS", "2025")
INICIO_PATH = os.path.join(BASE_DIR, "INICIO")



archivos = {

    0: os.path.join(PIEZAS_PATH, "patas", "tripie.obj"), #CAJETE GRIS TRÍPODE CON SOPORTES DE SERPIENTE
    1: os.path.join(PIEZAS_PATH, "PIEZA2exhibicion2025", "PIEZA8.obj"), #CAJETE GRIS DE SILUETA COMPUESTA TRÍPODE.
    2: os.path.join(PIEZAS_PATH, "PIEZA42025", "PIEZA1.obj"),#JARRA DE CUERPO ELIPSOIDAL
    3: os.path.join(PIEZAS_PATH, "5", "5.obj"),#VASO POLÍCROMO TRÍPODE
    4: os.path.join(PIEZAS_PATH, "pieza10", "PIEZA10.obj"), #CAJETE TRÍPODE DE FONDO SELLADO
    5: os.path.join(PIEZAS_PATH, "pieza6", "PIEZA6.obj"), #OLLA BAJA POLICROMA TRÍPODE
    6: os.path.join(PIEZAS_PATH, "ondo", "sss.obj"),#COPA DE SILUETA COMPUESTA CON BASE DE PEDESTAL
    7: os.path.join(PIEZAS_PATH, "Pieza9exhibicion2025", "eee.obj"),#OLLA MINIATURA
    8: os.path.join(PIEZAS_PATH, "jarrita", "jarra.obj"),#OLLA MINIATURA
    9: os.path.join(PIEZAS_PATH, "PIEZA16", "PIEZA16.obj"),#COPA DE SILUETA COMPUESTA CON BASE DE PEDESTAL
}

# Diccionario de archivos de audio
audios = {
    0: os.path.join(AUDIOS_PATH, "0.mp3"),
    1: os.path.join(AUDIOS_PATH, "1.mp3"),
    2: os.path.join(AUDIOS_PATH, "2.mp3"),
    3: os.path.join(AUDIOS_PATH, "3.mp3"),
    4: os.path.join(AUDIOS_PATH, "4.mp3"),
    5: os.path.join(AUDIOS_PATH, "5.mp3"),
    6: os.path.join(AUDIOS_PATH, "6.mp3"),
    7: os.path.join(AUDIOS_PATH, "7.mp3"),
    8: os.path.join(AUDIOS_PATH, "8.mp3"),
    9: os.path.join(AUDIOS_PATH, "9.mp3"),
}


audios_cargados = {k: pygame.mixer.Sound(v) for k, v in audios.items()}
# Inicialización de variables y configuración
tiempoPieza = 0
hand_detection_counter = 0  # Contador para el número de frames sin detección de manos.
objectreadfile = os.path.join(INICIO_PATH, "Green_Circle_0915213601.obj")


isoptimized = "SI"  # Cadena que indica si la optimización está habilitada.
makeoptimize = isoptimized == "SI"  # Convierte la cadena en una variable booleana.


cap_width = 640
cap_height = 360
logo = True  # Bandera para indicar si se está mostrando el logo.
isFullscreen = True


# Cargar el modelo 3D
mesh = o3d.io.read_triangle_mesh(objectreadfile, True)  # Lee el modelo 3D desde el archivo.
# Crear la ventana de visualización del modelo 3D
vis = o3d.visualization.Visualizer()  # Crea un visualizador de Open3D.
vis.create_window(window_name="Open3D", width=960, height=540)
vis.add_geometry(mesh)  # Añade el modelo 3D a la ventana de visualización.
vis.get_render_option().load_from_json(json_path)  # Carga las opciones de renderización desde un archivo JSON.
vis.get_view_control().set_zoom(0.7)  # Establece el nivel de zoom de la vista.
#vis.get_view_control().rotate(300, 1000, xo=0.0, yo=0.0)  # Rota la vista del modelo 3D.
#vis.get_view_control().rotate(1000, 0, xo=0.0, yo=0.0)  # Rota la vista del modelo 3D.
vis.poll_events()  # Procesa los eventos de la ventana.
vis.update_renderer()  # Actualiza el renderizador.

if platform.system() == "Linux":
    # Cámaras
    cap = cv2.VideoCapture(0)  # Abre la cámara con optimización (modo DirectShow).

    if isFullscreen:
        # Busca la ventana con título "Open3D"
        window_id = os.popen("wmctrl -l | grep 'Open3D' | awk '{print $1}'").read().strip()
        # Cambia la ventana a pantalla completa
        os.system(f"wmctrl -ir {window_id} -b add,fullscreen")
    print("Se está ejecutando en Linux")

elif platform.system() == "Windows":
    if makeoptimize:  # Verifica si se debe optimizar la captura de video.
        cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)  # Abre la cámara con optimización (modo DirectShow).
    else:
        cap = cv2.VideoCapture(0)  # Abre la cámara sin optimización.

    if isFullscreen:
        import win32gui
        import win32con
        import win32api

        hwnd = win32gui.FindWindow(None, 'Open3D')
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, win32con.WS_POPUP | win32con.WS_VISIBLE)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1),
                              win32con.SWP_FRAMECHANGED)
    print("Se está ejecutando en Windows")
else:
    print("Se está ejecutando en otro sistema operativo")

print("Ejecutando...")  # Imprime un mensaje indicando que el programa está en ejecución.
mp_drawing = mp.solutions.drawing_utils  # Inicializa las utilidades de dibujo de MediaPipe.
mp_hands = mp.solutions.hands  # Inicializa el módulo de detección de manos de MediaPipe.

# Inicialización de variables para el seguimiento de gestos y el control de la cámara.
moveX = 0  # Movimiento actual en X.
moveY = 0  # Movimiento actual en Y.
moveZ = 0  # Movimiento actual en Z.
newZ = True  # Bandera para indicar si el movimiento en Z es nuevo.
refZ = 0  # Referencia de posición en Z.
absZ = 0  # Posición absoluta en Z.


def calc_distance(p1, p2):
    return sqrt(
        (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)  # Calcula la distancia euclidiana entre dos puntos p1 y p2.

def cambiarObj(vis, modelo_viejo, objectreadfile):
    directorio = os.path.join(os.getcwd(), 'sub')
    print(directorio)

    if objectreadfile in archivos.values():
        current_index = list(archivos.values()).index(objectreadfile)
        next_index = (current_index + 1) % len(archivos)
        if current_index == 0:
            pygame.mixer.music.stop()
        audios_cargados[current_index].stop()

        subtitulos = gw.getWindowsWithTitle("pygame window")
        if subtitulos:
            pygame_window = subtitulos[0]  # Si hay múltiples ventanas, tomamos la primera
            pygame_window.close()
        else:
            print("No se encontró una ventana llamada 'pygame window'.")
        # -------------------
        script = f"{next_index}.py"
        # Ejecutar el archivo .py con Popen
        proces = subprocess.Popen(['python', script], cwd=directorio)

        audios_cargados[next_index].play()
        objectreadfile = list(archivos.values())[next_index]
        audioreadfile = list(archivos.values())[next_index]
    else:
        objectreadfile = list(archivos.values())[0]
        audios_cargados[0].play()
        proces = subprocess.Popen(['python', "0.py"], cwd=directorio)

    meshNew = o3d.io.read_triangle_mesh(objectreadfile, True)
    vis.remove_geometry(modelo_viejo)
    vis.add_geometry(meshNew)
    vis.get_view_control().set_zoom(1)
    # vis.get_view_control().rotate(300, 1200, xo=0.0, yo=0.0)  # Rota la vista del modelo 3D.
    # vis.get_view_control().rotate(1000, 0, xo=0.0, yo=0.0)  # Rota la vista del modelo 3D.
    vis.poll_events()  # Procesa los eventos de la ventana.
    vis.update_renderer()  # Actualiza el renderizador.
    print(f" Pieza cambiada a '{objectreadfile}'")
    # print(f" audio en reproduccion '{audioreadfile}'")
    return objectreadfile, meshNew

def detect_finger_down(hand_landmarks):
    print("-----------------------------")
    finger_down = False
    x_base1 = int(hand_landmarks.landmark[0].x * cap_width)
    y_base1 = int(hand_landmarks.landmark[0].y * cap_height)

    x_base2 = int(hand_landmarks.landmark[17].x * cap_width)
    y_base2 = int(hand_landmarks.landmark[17].y * cap_height)

    x_pinky = int(hand_landmarks.landmark[20].x * cap_width)
    y_pinky = int(hand_landmarks.landmark[20].y * cap_height)

    x_anular = int(hand_landmarks.landmark[16].x * cap_width)
    y_anular = int(hand_landmarks.landmark[16].y * cap_height)

    x_medio = int(hand_landmarks.landmark[12].x * cap_width)
    y_medio = int(hand_landmarks.landmark[12].y * cap_height)

    p1 = (x_base1, y_base1)
    p5 = (x_base2, y_base2)
    p2 = (x_pinky, y_pinky)
    p3 = (x_anular, y_anular)
    p4 = (x_medio, y_medio)
    d_base_base = calc_distance(p1, p5)
    d_base_pinky = calc_distance(p1, p2)
    d_base_anular = calc_distance(p1, p3)
    d_base_medio = calc_distance(p1, p4)
    print(d_base_base)
    print("------------------------------------")
    print("Pinky ", d_base_pinky)
    print("Anular ", d_base_anular)
    print("Medio ", d_base_medio)
    if d_base_anular < 30 and d_base_medio < 30 and d_base_pinky < 30:
        finger_down = True
    print("---------------------")
    return finger_down

with mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.9, min_tracking_confidence=0.88) as hands:
    # Inicia el contexto del modelo de manos de MediaPipe con una confianza mínima de detección de 0.8 y una confianza mínima de seguimiento de 0.5.

    while cap.isOpened():
        # Bucle que se ejecuta mientras la cámara esté abierta.

        ret, frame = cap.read()
        # Lee un frame de la cámara.

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convierte el frame de BGR a RGB.

        frameWidth = image.shape[1]
        frameHeight = image.shape[0]
        # Obtiene el ancho y la altura del frame.

        image = cv2.flip(image, 1)
        # Invierte la imagen horizontalmente.

        image.flags.writeable = False
        # Marca la imagen como no escribible para mejorar el rendimiento de procesamiento.

        results = hands.process(image)
        # Procesa la imagen para detectar manos.

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # Marca la imagen como escribible nuevamente y convierte de RGB a BGR.

        pos = (0, 0)
        # Dibuja un rectángulo negro que cubre toda la imagen.

        totalHands = 0

        # Inicializa el contador de manos detectadas.

        if results.multi_handedness:

            hand_detection_counter = 0
            tiempoPieza += 1

            totalHands = len(results.multi_handedness)
            # Si se detectaron manos, actualiza el contador.

            if totalHands == 2:
                if results.multi_handedness[0].classification[0].label == results.multi_handedness[1].classification[0].label:
                    totalHands = 1
                # Si se detectan dos manos pero ambas son del mismo tipo (izquierda o derecha), las cuenta como una.

        if results.multi_hand_landmarks:
            if logo:
                logo = False
                objectreadfile, meshNew = cambiarObj(vis=vis, modelo_viejo=mesh, objectreadfile=objectreadfile)
                mesh = meshNew
                print("BIENVENIDO")

            for hand_landmarks in results.multi_hand_landmarks:
                if tiempoPieza >= 25:
                    if detect_finger_down(hand_landmarks):
                        objectreadfile, meshNew = cambiarObj(vis=vis, modelo_viejo=mesh, objectreadfile=objectreadfile)
                        mesh = meshNew
                        tiempoPieza = 0




            if totalHands == 1:
                for num, hand in enumerate(results.multi_hand_landmarks):
                    indexTip = results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    indexTipXY = mp_drawing._normalized_to_pixel_coordinates(indexTip.x, indexTip.y, frameWidth,
                                                                             frameHeight)
                    thumbTip = results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.THUMB_TIP]
                    thumbTipXY = mp_drawing._normalized_to_pixel_coordinates(thumbTip.x, thumbTip.y, frameWidth,
                                                                             frameHeight)

                    mp_drawing.draw_landmarks(
                        image,
                        hand,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                        mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                    )
                    # Normaliza las coordenadas de los puntos de la mano a las coordenadas del píxel en la imagen.



                    if indexTipXY and thumbTipXY is not None:
                        indexXY = (indexTipXY[0], indexTipXY[1])
                        thumbXY = (thumbTipXY[0], thumbTipXY[1])
                        dist = calc_distance(indexXY, thumbXY)
                        # Dibuja círculos en la punta del índice y el pulgar y calcula la distancia entre ellos.

                        #Movimiento de la piezas con las manos
                        if dist < 20:
                            netX = round((indexTipXY[0] + thumbTipXY[0]) / 2)
                            netY = round((indexTipXY[1] + thumbTipXY[1]) / 2)

                            deltaX = moveX - netX
                            moveX = netX
                            deltaY = moveY - netY
                            moveY = netY
                            if abs(deltaX) > 40 or abs(deltaY) > 40:
                                print("Max reached: " + str(deltaX) + "," + str(deltaY))
                            else:
                                #print(str(deltaX) + "," + str(deltaY))
                                vis.get_view_control().rotate(-deltaX * 8, -deltaY * 8, xo=0.0, yo=0.0)
                                vis.poll_events()
                                vis.update_renderer()
                            # Si la distancia es menor que 50, mueve la vista del modelo 3D de acuerdo con los movimientos detectados.
                        #No hacer movimiento
                        else:
                            moveX = 0
                            moveY = 0
                            # Si la distancia es mayor que 50, reinicia los movimientos.
            elif totalHands == 2:
                handX = [0, 0]
                handY = [0, 0]
                isHands = [False, False]
                # Inicializa las posiciones de las manos y las banderas para la detección.

                for num, hand in enumerate(results.multi_hand_landmarks):
                    indexTip = results.multi_hand_landmarks[num].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    indexTipXY = mp_drawing._normalized_to_pixel_coordinates(indexTip.x, indexTip.y, frameWidth,
                                                                             frameHeight)
                    thumbTip = results.multi_hand_landmarks[num].landmark[mp_hands.HandLandmark.THUMB_TIP]
                    thumbTipXY = mp_drawing._normalized_to_pixel_coordinates(thumbTip.x, thumbTip.y, frameWidth,
                                                                             frameHeight)
                    # Normaliza las coordenadas de los puntos de la mano a las coordenadas del píxel en la imagen.

                    if indexTip and indexTipXY and thumbTipXY is not None:
                        indexXY = (indexTipXY[0], indexTipXY[1])
                        thumbXY = (thumbTipXY[0], thumbTipXY[1])
                        dist = calc_distance(indexXY, thumbXY)
                        # Dibuja círculos en la punta del índice y el pulgar y calcula la distancia entre ellos.

                        if dist < 50:
                            netX = round((indexTipXY[0] + thumbTipXY[0]) / 2)
                            netY = round((indexTipXY[1] + thumbTipXY[1]) / 2)
                            handX[num] = netX
                            handY[num] = netY
                            isHands[num] = True
                            # Si la distancia es menor que 50, guarda las posiciones promedio de los puntos detectados.

                    #print(isHands[0], ",", isHands[1])
                    if isHands[0] and isHands[1]:
                        distpar = calc_distance((handX[0], handY[0]), (handX[1], handY[1]))
                        if newZ:
                            newZ = False
                            moveZ = distpar
                            refZ = distpar

                        netX = round((handX[0] + handX[1]) / 2)
                        netY = round((handY[0] + handY[1]) / 2)
                        deltaZ = (distpar - moveZ) / refZ
                        if deltaZ < abs(1):
                            absZ = absZ - deltaZ
                            if absZ > 2.0:
                                absZ = 2.0
                            elif absZ < 0.6:
                                absZ = 0.6
                            moveZ = distpar
                            print(absZ)
                            vis.get_view_control().set_zoom(absZ)
                            vis.poll_events()
                            vis.update_renderer()
                        # Si se detectan ambas manos, calcula la distancia entre ellas y ajusta el zoom del modelo 3D en función de esa distancia.

                    elif not isHands[0] and not isHands[1]:
                        newZ = True

        else:
            if not logo:
                hand_detection_counter += 1
                tiempoPieza = 0

                if hand_detection_counter >= 1000:
                    for key in audios:
                        pygame.mixer.music.stop()
                        audios_cargados[key].stop()
                    vis.remove_geometry(mesh)
                    objectreadfile = os.path.join(INICIO_PATH, "Green_Circle_0915213601.obj")
                    mesh = o3d.io.read_triangle_mesh(objectreadfile, True)
                    mesh.compute_vertex_normals()
                    vis.add_geometry(mesh)
                    #vis.get_view_control().rotate(300, 1000, xo=0.0, yo=0.0)  # Rota la vista del modelo 3D.
                    #vis.get_view_control().rotate(1000, 0, xo=0.0, yo=0.0)
                    vis.get_view_control().set_zoom(0.7)
                    vis.poll_events()  # Procesa los eventos de la ventana.
                    vis.update_renderer()  # Actualiza el renderizador.
                    hand_detection_counter = 0
                    logo = True
                    print("Regresar inicio")

            ctrl = vis.get_view_control()
            ctrl.rotate(3, 0, xo=0.0, yo=0.0)
            vis.poll_events()
            vis.update_renderer()
            # Si no se detectan manos, rota el modelo 3D ligeramente.
        if not isFullscreen:
            cv2.imshow('MANO', image)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            print("Programa cerrado por el usuario.")
            break
    messagebox.showinfo("Información", "Esto es un mensaje informativo.")

cap.release()
cv2.destroyAllWindows()