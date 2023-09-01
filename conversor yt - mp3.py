#haz un programa para descargar videos de youtube y guardarlos en el escritorio

import re
from pytube import YouTube
import os
import moviepy.editor as mp

link = input("Introduce el link del video: ")
yt = YouTube(link)

ys = yt.streams.get_highest_resolution()

print("Descargando...")

ys.download("C:\Program Files\Soundpad\sounds")

#convertir el video a mp3 y borrar el archivo mp4

for file in os.listdir("C:\Program Files\Soundpad\sounds"):
    if re.search('mp4', file):
        mp4_path = os.path.join("C:\Program Files\Soundpad\sounds", file)
        mp3_path = os.path.join("C:\Program Files\Soundpad\sounds", os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)

print("Descarga completa!!")



















