import os
from tkinter import *
from pytube import YouTube
from tkinter import messagebox
import ffmpeg
import time
import vlc

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("YouTube Video Downloader")
root.configure(bg="#800020")

Label(root, text = 'YouTube - Video Downloader', font = 'arial 20 bold', fg = 'white', bg = '#800020').pack()
Label(root, text = 'Created by Panos Sakketos', font = 'arial 11 bold', fg = 'gray', bg = '#800020').place(x = 129, y = 35)

link = StringVar()
Label(root, text = 'Paste URL', font = 'arial 14 bold', bg = "#800020", fg = 'white').place(x = 175 , y = 60)
Entry(root, width = 70, textvariable = link).place(x = 35, y = 90)

link1 = StringVar()
Label(root, text = 'File NAME', font = 'arial 14 bold', bg = '#800020', fg = 'white').place(x = 175, y = 130)
Entry(root, width = 70, textvariable = link1).place(x = 35, y = 160)
        #y axis
def Downloader():
    value = os.environ['USERPROFILE']
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    value1 = os.path.join(value, "Desktop")
    try:
        url = YouTube(str(link.get()))
        instance = 1
    except: 
        Label(root, text = 'Invalid URL.', font = 'arial 15', fg = 'white', bg = "#800020").place(x = 182 , y = 240)
    try:
        if instance:
            video = url.streams.filter(res="1080p").first()
            video.download(f'{value1}/YouTube/video', filename = 'video.mp4')
            indicator = 1
    except:
        if instance:
            os.system("mkdir %userprofile%\Desktop\YouTube") 
            path = os.path.join(value1, "YouTube")
            path1 = os.path.join(path, "downloaded")
            url.streams.get_highest_resolution().download(output_path = path1)
            os.system("cd.> file.txt")
    try:        
        if indicator:
            print(value1)
            audio = url.streams.filter(only_audio = True).first()
            audio.download(f'{value1}/YouTube/audio', filename = f'audio.mp3')
    except:
        Label(root, text = None, font = 'arial 14', fg = 'white', bg = "#800020").place(x = 29 , y = 211)


    #audio1 = os.path.join(value1, "YouTube")
    video1 = os.path.join(value1, "YouTube")
    video6 = os.path.join(value1, "video")
    video8 = os.path.join(video6, "video.mp4")
    video2 = os.path.join(video1, "video")
    audio2 = os.path.join(video1, "audio")
    audio54 = os.path.join(audio2, "audio.mp3")
    video_file = f'{video2}/video.mp4'
    audio_file= f'{audio2}/audio.mp3'
    #file_saved = f'{final_path}/{file_name}.mp4'
    #file = open("content.txt", "w+")
    #file.write(f"{url.title}")
    #value3 = os.path.join(video2, "video.mp4")
    #value4 = os.path.join(audio2, "audio.mp3")
    file_named1 = str(link1.get())
    file_named = file_named1.replace(" ", "")
    print(file_named)
    final_file = os.path.join(video1, f"{file_named}.mp4")
    final = f"{file_named}.mp4"
    print(final_file)
    dire = os.listdir(video1)
    print(f"DIR : {dire}")

    #file1 = open("ffmpeg.bat", "w+")
    #file1.write(text)
    #file.write(f"\n{audio_file}")
    #file.write(f"\n{file_saved}")
    def merge(video, audio, file):
        file_video = ffmpeg.input(video)
        file_audio = ffmpeg.input(audio)
        #ffmpeg.concat(file_video, file_audio, v=1, a=1).output(file).run()
        
    #audio and video
        ffmpeg.output(file_video, file_audio, file, acodec='copy', vcodec='copy').run()
    #os.system("cmd /c ffmpeg.bat")
    if os.path.exists("file.txt"):
        Label(root, text = 'Download Successful!', font = 'arial 17', fg = 'white', bg = "#800020").place(x = 129 , y = 241)
        os.remove("file.txt")
        
    else:
        merge(video_file, audio_file, final_file)
        Label(root, text = 'Download Successful!', font = 'arial 17', fg = 'white', bg = "#800020").place(x = 129 , y = 241)
        os.system(f'explorer %userprofile%\Desktop\YouTube\{file_named}.mp4')
    Label(root, text = f'title = {url.title}', font = 'arial 11 bold', fg = 'white', bg = '#800020').place(x = 3 , y = 272)
    #os.system(f"cmd /c {value1}/ffmpeg.bat")
    #os.system(f"ffmpeg -i video.mp4 -i audio.mp3 -c copy function.mp4")
    #os.system('explorer "%userprofile%\Desktop\YouTube"')
btn = Button(root,text = 'Download', font = 'arial 15 bold', bg = "pale violet red", command = Downloader, activebackground = 'white', activeforeground = 'black', cursor = "hand2", padx = 3, pady = 3, border = 2).place(x = 180, y = 189)
root.mainloop()
