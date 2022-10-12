from pytube import Playlist

link = input("Paste the link: ")
route = input("Paste the route: ")
ft = input("mp4 or mp3?: ")
pl = Playlist(link)


if ft == "mp3":
    for video in pl.videos:
        title = video.title
        fixedtitle = title.replace("/", "-")
        try:
            video.streams.filter(only_audio=True)
            yd = video.streams.get_audio_only()
            yd.download(route, f"{fixedtitle}.mp3")
            print("Done it! See you later!")
        except:
            print("Skipped video. Unknown error")


else:
    print("Invalid format")
