from pytube import Playlist
import pytube as pt
##import youtube_dl
import sys
import keyboard
import yt_dlp
import time as t
number_default = 0

class Nguvaicalon():
    #get all video urls in a playlist
    def Get_Url(URL_PLAYLIST):

        playlist = Playlist(URL_PLAYLIST)
        print('Number Of Videos In playlist: %s' % len(playlist.video_urls))

        urls = []
        for url in playlist:
            urls.append(url)
            
        for links in urls:
            print(links)
            
        return urls
    
    #download videos as mp3
    def Download(meow, number, number_default, tolal_time):
        for links in meow:
            start_time = t.time()
            
            getdownload = pt.YouTube(links)
            thisdidntwork = getdownload.streams.filter(only_audio=True).first()
            
            #this is a temp folder, nothing will be store here. Crate a new folder and put the path
            thisdidntwork.download(output_path = "D:\Administrator\Downloads\Test")# <------------- here
            
            #change quality to 192 if seeing issues
            ydl = yt_dlp.YoutubeDL({
                'format': 'bestaudio/best',
                'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }],
                'outtmpl': 'audio/%(title)s.%(ext)s',
            })
            
            print(f'\nStarting download {thisdidntwork.default_filename}')

            ydl.download([links])
            number_default = number_default + 1
            print(f'Finished {number_default}/{number} songs in ', round(t.time()-float(start_time),2),'s')

            t.time()
            if number_default == number:
                
                print('\nfinished download in', round(t.time()-float(tolal_time),2),'s')
                print('\nPress Esc or Enter to escape')
                while True:
                    try:
                        if keyboard.is_pressed('Esc') or keyboard.is_pressed('Enter'):
                            sys.exit(0)
                    except:
                        break
            


if True:
    ##URL_PLAYLIST = "https://www.youtube.com/playlist?list=PL4RWBwVliOGn4K7XjkQNZP-s8XtCKuIsQ"
    URL_PLAYLIST = input("Enter a playlist's URL: ")
    
    tolal_time = t.time()
    playlist = Playlist(URL_PLAYLIST)
    number = len(playlist.video_urls)
    
    meow = Nguvaicalon.Get_Url(URL_PLAYLIST)
    
    Nguvaicalon.Download(meow, number, number_default, tolal_time)
