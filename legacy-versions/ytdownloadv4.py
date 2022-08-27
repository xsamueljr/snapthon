from pytube import YouTube

link = input("Copia el link: ")
yt = YouTube(link)
route = input("Copia la ruta: ")
ft = input("¿Vídeo o audio?: ")

print(f"Título: {yt.title}")
print(f"Visitas: {yt.views}")

if ft == "Vídeo":
    fm = input("¿Formato?\n(Ponlo en minúscula sin punto)\nFormato recomendado mp4: ")
    cd = input("Calidades disponibles\n“720p”, “480p”, “360p”, “240p”, “144p”\nEscribe una sin comillas: ")
    yd = yt.streams.get_by_resolution(cd)

    yd.download(route, f"{yt.title}.{fm}")
    print("¡Hecho! ¡Hasta luego!")
elif ft == "Audio":
    fm = input("¿Formato?\n(Ponlo en minúscula sin punto)\nFormato recomendado mp3: ")
    yd = yt.streams.get_audio_only()

    yd.download(route, f"{yt.title}.{fm}")
    print("¡Hecho! ¡Hasta luego!")
else:
    print("Formato inválido")
