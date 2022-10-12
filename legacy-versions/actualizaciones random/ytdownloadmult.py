from pytube import YouTube

playlist = []
route = input("Paste the route: ")
ft = input("mp4 or mp3?: ")
videos = int(input("How many videos?: "))
i = 0
while i < videos:
    yes = input("Paste a link: ")
    playlist.append(yes)
    i += 1

i = 0
while i < videos:
    yt = YouTube(playlist[i])
    fixedtitle = yt.title.replace("/", "-")
    i += 1
    if ft == "mp4":
        yd = yt.streams.get_highest_resolution()

        yd.download(route, f"{fixedtitle}.mp4")
        print("Done it! See you later!")
    elif ft == "mp3":
        yd = yt.streams.get_audio_only()

        yd.download(route, f"{fixedtitle}.mp3")
        print("Done it! See you later!")
    else:
        print("Invalid format")
