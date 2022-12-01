# pip install ffmpeg moviepy

import moviepy.editor as mp

video = mp.VideoFileClip(r"video.mov")

video.audio.write_audiofile(r"audio-extraido.mp3")


