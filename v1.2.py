from pytube import Playlist
import pytube as pt
import sys
import keyboard
import yt_dlp
import time as t
##import youtube_dl
number_default = 0

class Khongphainhen():
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
    
    
    #download videos as mp3 or mp4
    def Download_Playlist(meow, number, number_default, total_time, choice):
        for links in meow:
            start_time = t.time()
            
            getdownload = pt.YouTube(links)
            thisdidntwork = getdownload.streams.filter(only_audio=False).first()
            
            #this is a temp folder, nothing will be store here. Crate a new folder and put the path
            thisdidntwork.download(output_path = "D:\Administrator\Downloads\Test")# <------------- here
            
            if choice == 'mp3':
                ydl = yt_dlp.YoutubeDL({
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                    }],
                    'outtmpl': 'audio/%(title)s.%(ext)s',
                })
                
            elif choice == 'mp4':
                ydl = yt_dlp.YoutubeDL({
                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                    'outtmpl': 'video/%(title)s.%(ext)s',
                })
                
            print(f'\nStarting download {thisdidntwork.default_filename}')

            ydl.download([links])
            number_default = number_default + 1
            print(f'Finished {number_default}/{number} songs in ', round(t.time()-float(start_time),2),'s')

            t.time()
            if number_default == number:
                
                print('\nfinished download in', round(t.time()-float(total_time),2),'s')
                print('\nPress Enter to countinue')
                while True:
                    try:
                        if keyboard.is_pressed('Enter'):
                            sys.exit(0)
                    except:
                        break
                    
    
    #download video as mp3 or mp4
    def Download_Video(URL_VIDEO, choice):
        getdownload = pt.YouTube(URL_VIDEO)
        video_name = getdownload.streams.filter(only_audio=False).first()
        
        #this is a temp folder, nothing will be store here. Crate a new folder and put the path
        video_name.download(output_path='D:\Administrator\Downloads\Test')#<------------------- here
    
        if choice == 'mp3':
            ydl = yt_dlp.YoutubeDL({
                'format': 'bestaudio/best',
                'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }],
                'outtmpl': 'audio/%(title)s.%(ext)s',
            })
            
        elif choice == 'mp4':
            ydl = yt_dlp.YoutubeDL({
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': 'video/%(title)s.%(ext)s',
            })
            
        print(f'\nStarting download {video_name.default_filename}')
        
        start_time = t.time()
        ydl.download([URL_VIDEO])
        
        print('\nFinished download in', round(t.time()-float(start_time),2),'s')
        t.time() 
        print('\nPress Enter to continue')
        while True:
            try:
                if keyboard.is_pressed('Enter'):
                    sys.exit(0)
            except:
                break
        


while True:
    print("""\nHello tysm for using this little silly script that i made <3,
feels free to send any feedback to my github to help me improve this thing <3
also i couldn't make the next line to print so this is like a decoy message for now""")
    
    
    total_time = t.time()
    playlist_or_video = input("\nYou want to download a playlist or a video? ").upper()
    
    if playlist_or_video == 'VIDEO':
        choice = input('Mp3 or Mp4: ').lower()
        ##URL_VIDEO = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        URL_VIDEO = input("\nEnter a video's URL: ")
        Khongphainhen.Download_Video(URL_VIDEO, choice)
          
          
    elif playlist_or_video == 'PLAYLIST':
        choice = input('Mp3 or Mp4: ').lower()
        ##URL_PLAYLIST = "https://www.youtube.com/playlist?list=PL4RWBwVliOGn4K7XjkQNZP-s8XtCKuIsQ"
        URL_PLAYLIST = input("\nEnter a playlist's URL: ")    
        playlist = Playlist(URL_PLAYLIST)
        number = len(playlist.video_urls)
        meow = Khongphainhen.Get_Url(URL_PLAYLIST)
        Khongphainhen.Download_Playlist(meow, number, number_default, total_time, choice)
        
    elif keyboard.is_pressed('Enter'):
        print('maow')
        
    else:
        print('Invalid input')
