
# MINI PROJECTS - 04 : -

# Project Name : Youtube MP3 Downloder

# from pytube import YouTube

# url = input("Enter the Url of the Video : ")
# yt = YouTube(url)

# #Filter audio streams and download the first one -
# audio_stream = yt.streams.filter(only_audio=True).first()
# audio_stream.download()  # Didnot work

# Trying a different Package name 'pytubefix' -

from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input("Enter the YouTube video URL: ")
yt = YouTube(url, on_progress_callback = on_progress)

# Display video information -
print(f"Title : {yt.title}")

# Filter audio streams and download the first one -
audio_stream = yt.streams.filter(only_audio=True).first()
audio_stream.download() 





