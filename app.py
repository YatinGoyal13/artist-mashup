from flask import Flask, render_template,request
import youtube_dl
import moviepy.editor as mp
import os
import sys
from youtubesearchpython import VideosSearch
import glob
import zipfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/",methods=['POST'])
def home():
    channel_name=request.form['singername']
    no_of_videos=request.form['no_of_videos']
    trim_time=request.form['timestamp']
    email=request.form['email']
    main(channel_name,no_of_videos,trim_time,email)
    return "<h1><center>Welcome</center></h1>"

def download_audio_from_youtube(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
        ydl.download([url])

def cut_audio_file(audio_file, start, end):
    audio = mp.AudioFileClip("./"+audio_file)
    audio_cut = audio.subclip(start, end)
    audio_cut.write_audiofile(audio_file)


def main(singer,n,audio_duration,email):
    n=int(n)
    audio_duration=int(audio_duration)
    # if n < 10:
    #     print('Number of videos should be greater than 10')
    #     sys.exit(1)

    # if audio_duration < 20:
    #     print('Audio duration should be greater than 20 seconds')
    #     sys.exit(1)

    videosSearch = VideosSearch(singer, limit = n)
    url=[]
    for i in range(0,n):
        url.append(videosSearch.result()["result"][i]["link"])
        download_audio_from_youtube(url[i])
    list_of_mp3s = glob.glob('./*.mp3')
        # Cut the first Y seconds of the audio file
    for i in range(0,n):
        audio_file = list_of_mp3s[i]
        cut_audio_file(audio_file, 0, audio_duration)
    audio_folder='.'

    audio_files = [audio_folder+'/'+img for img in os.listdir(audio_folder) if img.endswith(".mp3")]

    print(audio_files)

    audios = []
    for audio in audio_files :
        audios.append(mp.AudioFileClip(audio))

    audioClips = mp.concatenate_audioclips([audio for audio in audios])
    audioClips.write_audiofile('102003655.mp3')
    zip = zipfile.ZipFile("102003655.zip", "w", zipfile.ZIP_DEFLATED)
    zip.write("./102003655.mp3")
    zip.close()
    fromaddr = "enter email"
    toaddr = email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "DS Assignment-2"
    filename = "102003655.zip"
    attachment = open("./102003655.zip", "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "enter password")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()
    
if __name__=="main_":
    app.run(debug=True)
