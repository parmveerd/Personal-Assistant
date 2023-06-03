import time
from pytube import YouTube
import os

# import link variable the was inputted by user
from personalassistant import link


# download the video
yt = YouTube(str(link))
title = yt.title
video = yt.streams.filter(only_audio=True).first()
video.download()

# make the file an mp3
og_file = video.default_filename
new_file = og_file.replace('.mp4', '.mp3')
os.rename(og_file, new_file)