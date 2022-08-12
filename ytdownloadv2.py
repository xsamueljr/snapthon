from pytube import YouTube

link = input("Paste the link: ")
route = input("Paste the route: ")
ft = input("mp4 or mp3?: ")
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)
if ft == "mp4":
    yd = yt.streams.get_highest_resolution()

    yd.download(route)
    print("Done it! See you later!")
elif ft == "mp3":
    yd = yt.streams.get_audio_only()

    yd.download(route, f"{yt.title}.mp3")
    print("Done it! See you later!")
else:
    print("Invalid format")
