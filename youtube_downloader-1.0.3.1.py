import os
from tkinter import *
from pytube import YouTube
import ffmpeg
import requests
import shutil
import subprocess
import gdown
import pathlib


root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("YouTube Video Downloader")
root.configure(bg="#282828")
curr_dir = os.path.dirname(os.path.realpath(__file__))

Label(root, text = 'YouTube - Video Downloader', font = 'arial 20 bold', fg = 'white', bg = '#282828').pack()
Label(root, text = 'Created by Panos-Jr', font = 'arial 11 bold', fg = 'gray', bg = '#282828').place(x = 129, y = 35)

link = StringVar()
Label(root, text = 'Paste URL', font = 'arial 14 bold', bg = "#282828", fg = 'white').place(x = 175 , y = 60)
Entry(root, width = 70, textvariable = link).place(x = 35, y = 90)

link1 = StringVar()
Label(root, text = 'File NAME', font = 'arial 14 bold', bg = '#282828', fg = 'white').place(x = 175, y = 130)
Entry(root, width = 70, textvariable = link1).place(x = 35, y = 160)
        #y axis

def return_code(code):
    if not code:
        print(f'[stdout] ==> {code.stdout.decode()}')
        return code
    else:
        return f'return code ==> {code} [stdout] = {code.stdout.decode()}'

def exception(e, locale='NOT specified'):
    print(f'\n[exception] ==> {e}. [From] = {locale}')


def process(task):
    run = subprocess.run(f'exlorer "{curr_dir}\youtube_downloader {ver_rqst}\youtube_downloader-{ver_rqst}.exe"')
    output = subprocess.run(f'taskkill /f /im {task}', shell=True, capture_output=True)
    function = return_code(output.returncode)
    print(function)

def archive(file, file_name):
    if not os.path.exists(file):
        print(f'{file_name} doesn\'t exist')
        return file
    else:
        try:
            exc_file = 'youtube_downloader-1.0.2.7'
            print(f'IN ARCHIVE {file} and {file_name}')
            shutil.unpack_archive(file, file_name)
            task = f'youtube_downloader-{version}.exe'
            process(task)
        except Exception as rep:
            exception(rep, 'archive()')
        print('ARCHIVE extracted!')

def update():
    try:
        upd_url = 'https://raw.githubusercontent.com/Panos-Jr/YouTube_Downloader/main/google-drive.txt'
        upd_val = requests.get(upd_url)
        get_lnk = upd_val.text
        print(f'URL ==> {upd_val}')
        file_acq = f'{curr_dir}/youtube_downloader-{ver_rqst}.zip'
        ARCHIVED = f'{curr_dir}/youtube_downloader-{ver_rqst}'
        print(f'file_acq ==> {file_acq}')
        print(f'UPDATE FUNCTION ==> {ver_rqst}\n')
        gdown.download(get_lnk, file_acq, quiet = False)
    except Exception as e:
        exception(e, 'update()')
    archived = archive(file_acq, ARCHIVED)
    
try:
    version = '1.0.3.1'
    Label(root, text=f'Version : {version}', font = 'Arial 13 bold', fg = 'white', bg = '#282828').place(x = 299, y = 35)
    num =  version.replace('.', '')
    ver_url = 'https://raw.githubusercontent.com/Panos-Jr/YouTube_Downloader/main/version.txt'                                                                     
    url_req = requests.get(ver_url)
    ver_sc = url_req.status_code
    if ver_sc == 200:
        rqst_ver = url_req.text
        ver_rqst = rqst_ver.strip()
        number = ver_rqst.replace('.', '')
        if version == ver_rqst or num > number: #[num > number] if someone is BETA testing.
            print("NO updates available.")
        else:
            update = Button(root, text = 'Update', font = 'arial 15 bold', bg = '#808080', command = update, activebackground = 'white', activeforeground = 'black', cursor = 'hand2', padx = 2, pady = 2, border = 2).place(x = 190, y = 250)
    else:
        print(f'Status ==> {ver_sc}')
except Exception as e:
    exception(e, 'version-validate')


def Downloader():
    value = os.environ['USERPROFILE']
    global curr_dir
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    value1 = os.path.join(value, "Desktop")
    try:
        url = YouTube(str(link.get()))
        instance = 1
    except: 
        Label(root, text = 'Invalid URL.', font = 'arial 15', fg = 'white', bg = "#282828").place(x = 182 , y = 240)
    try:
        if instance:
            video = url.streams.filter(res="1080p").first()
            video.download(f'{value1}/YouTube/video', filename = 'video.mp4')
            indicator = 1
    except:
        path = os.path.join(value1, "YouTube")
        path1 = os.path.join(path, "downloaded")
        url.streams.get_highest_resolution().download(output_path = path1)
        file = open('file.txt', 'a')
        file.write('file')
    try:        
        if indicator:
            audio = url.streams.filter(only_audio = True).first()
            audio.download(f'{value1}/YouTube/audio', filename = f'audio.mp3')
    except:
        print("Complete.")

    #configure PATH to YouTube [DIRECTORY]
    YOUTUBE = os.path.join(value1, "YouTube")
    video = os.path.join(YOUTUBE, 'video')
    audio = os.path.join(YOUTUBE, 'audio')
    video_file = f'{video}/video.mp4'
    audio_file = f'{audio}/audio.mp3'
    file_named1 = str(link1.get())
    file_named = file_named1.replace(" ", "")
    print(file_named)
    final_file = os.path.join(YOUTUBE, f"{file_named}.mp4")
    final = f"{file_named}.mp4"
    print(final_file)
    dire = os.listdir(YOUTUBE)
    print(f"DIR : {dire}")

    def merge(video, audio, file):
        file_video = ffmpeg.input(video)
        file_audio = ffmpeg.input(audio)
        #ffmpeg.concat(file_video, file_audio, v=1, a=1).output(file).run()
        
    #audio and video
        ffmpeg.output(file_video, file_audio, file, acodec='copy', vcodec='copy').run()

    if os.path.exists(f"{value1}/file.txt"):
        Label(root, text = 'Download Successful!', font = 'arial 17', fg = 'white', bg = "#282828").place(x = 129 , y = 241)
        file_rem = pathlib.Path(f'{value1}/file.txt')
        file_rem.unlink()
        print('exists')
        subprocess.run(f'explorer "%userprofile%\Desktop\YouTube\downloaded\{url.title}.mp4"', shell=True)

    else:
        merge(video_file, audio_file, final_file)
        Label(root, text = 'Download Successful!', font = 'arial 17', fg = 'white', bg = "#282828").place(x = 129 , y = 241)
        subprocess.run(f'explorer "%userprofile%\Desktop\YouTube\{file_named}.mp4"', shell=True)
    Label(root, text = f'title = {url.title}', font = 'arial 11 bold', fg = 'white', bg = "#282828").place(x = 3 , y = 272)    
btn = Button(root,text = 'Download', font = 'arial 15 bold', bg = "pale violet red", command = Downloader, activebackground = 'white', activeforeground = 'black', cursor = "hand2", padx = 3, pady = 3, border = 2).place(x = 180, y = 189)
root.mainloop()
