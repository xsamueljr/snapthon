from pytube import YouTube
from pytube import Playlist

print("¡Hola!\n¿Quieres descargar un vídeo o una playlist?")
print("1 para vídeo, 2 para playlist")
mult = input()
link = input("Pega su enlace: ")
route = input("Pega la ruta: ")
ft = input("1 for video, 2 for audio")
format = input("¿Usar formatos mp4 y mp3? [s/n]: ")
if format == "s":
    if ft == "1":
        format2 = "mp4"
    elif ft == "2":
        format2 = "mp3"
elif format == "n":
    format2 = input("Entonces introduce el formato que quieras, en minúscula y sin punto: ")

if mult == "1":
    yt = YouTube(link)
    fixedtitle = yt.title.replace("/", "-")

    if ft == "1":
        yd = yt.streams.get_highest_resolution()

        yd.download(route, f"{fixedtitle}.{format2}")
        print("¡Vídeo descargado! Hasta luego :D")
    elif ft == "2":
        yd = yt.streams.get_audio_only()

        yd.download(route, f"{fixedtitle}.{format2}")
        print("¡Vídeo descargado! Hasta luego :D")
elif mult == "2":
    pl = Playlist(link)
    if ft == "1":
        for video in pl.videos:
            title = video.title
            fixedtitle = title.replace("/", "-")
            try:
                yd = video.streams.get_highest_resolution()
                yd.download(route, f"{fixedtitle}.{format2}")
                print("+1 vídeo en tu carpeta")
            except:
                print("No se puede acceder a los datos de este vídeo. Saltamos al siguiente")
    elif ft == "2":
        for video in pl.videos:
            title = video.title
            fixedtitle = title.replace("/", "-")
            try:
                video.streams.filter(only_audio=True)
                yd = video.streams.get_audio_only()
                yd.download(route, f"{fixedtitle}.{format2}")
                print("+1 vídeo en tu carpeta")
            except:
                print("No se puede acceder a los datos de este vídeo. Saltamos al siguiente")

print("Tarea completada. Muchas gracias por usar este programa, me hace ilusión :D")