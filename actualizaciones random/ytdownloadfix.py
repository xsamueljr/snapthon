from pytube import YouTube

link = input("Paste the link: ")
route = input("Paste the route: ")
ft = input("1 for video, 2 for audio")
titulo = input("Enter the title (+ format): ")
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)
if ft == "1":
    yd = yt.streams.get_highest_resolution()

    yd.download(route)
    print("Done it! See you later!")
elif ft == "2":
    yd = yt.streams.get_audio_only()

    yd.download(route, titulo)
    print("Done it! See you later!")
else:
    print("Invalid format")