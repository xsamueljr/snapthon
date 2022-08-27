from pytube import YouTube

link = input("Copia el link: ")
yt = YouTube(link)
route = input("Copia la ruta: ")
ft = input("¿Vídeo o audio?: ")

print(f"Título: {yt.title}")
print(f"Visitas: {yt.views}")

if ft == "Vídeo":
    fm = input("¿Formato?\n(Ponlo en minúscula sin punto)\nFormato recomendado mp4: ")
    yd = yt.streams.get_highest_resolution()

    yd.download(route, f"{yt.title}.{fm}")
    print("¡Hecho! ¡Hasta luego!")
elif ft == "Audio":
    fm = input("¿Formato?\n(Ponlo en minúscula sin punto)\nFormato recomendado mp3: ")
    yd = yt.streams.get_audio_only()

    yd.download(route, f"{yt.title}.{fm}")
    print("¡Hecho! ¡Hasta luego!")
else:
    print("Formato inválido")
