# Recibir input del usuario
def obtener_input():
    opciones_objeto = {
        1: "Vídeo",
        2: "Playlist"
    }
    opciones_formato = {
        1: "Vídeo",
        2: "Audio"
    }

    objeto = int(input("¿Quieres descargar un vídeo o una playlist?\n1. Vídeo\n2. Playlist\n"))
    objeto = opciones_objeto.get(objeto)
    if objeto == None:
        exit("INPUT INVÁLIDO")
    
    formato = int(input("Elige:\n1. Vídeo (mp3)\n2. Audio (mp4)\n"))

    purification = input("¿Quieres purificar el audio? [s/n]: ")
    if purification == "s" or "S":
        purification = True
    else:
        purification = False

import os
from pytube import YouTube, Playlist
if purification:
    from pydub import AudioSegment