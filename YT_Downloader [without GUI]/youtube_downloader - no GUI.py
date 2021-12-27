import os
import ffmpeg
from pytube import YouTube

curr_dir = os.path.dirname(os.path.realpath(__file__))
user = os.environ['USERPROFILE']
list_dir = os.listdir(curr_dir)

obj = open("file.txt", "w+")

for file in list_dir:
    obj.write(str(file))
print("CONTENT written.")


link = input("Paste LINK -->  ")
print("Downloading . . .")

def download():
    url = YouTube(link)
    path = os.path.join(curr_dir, "YouTube")
    video = os.path.join(path, "video")
    url.streams.get_highest.resolution().download(output_path = video)

def concat(video, audio, file):
    video_file = ffmepg.input(video)
    audio_file = ffmpeg.input(audio) 
    ffmpeg.output(video_file, audio_file, file, acodec = 'copy', vcodec = 'copy').run()

download()


#while True:
 #   if os.path.exists("run.txt"):
  #      instance = 1
   # else:
    #    concat()
