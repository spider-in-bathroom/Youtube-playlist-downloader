from pytube import Playlist
import pytube as pt
import sys
import keyboard
import yt_dlp
import time as t
from colorama import init as colorama_init
from colorama import Fore, Style
##import youtube_dl
number_default = 0

colorama_init()

print(f"""\n{Fore.CYAN}Hello tysm for using this little silly script that i made <3,
feels free to send any feedback to my github to help me improve this thing <3
also i couldn't make the next line to print so this is like a decoy message for now{Style.RESET_ALL}""")

class Khongphainhen():
    
    #get all video urls in a playlist
    def Get_Url(URL_PLAYLIST):

        playlist = Playlist(URL_PLAYLIST)
        print('Number Of Videos In playlist: %s' % len(playlist.video_urls))
        print(f'{Fore.RED}If the playlist is big (like 800 songs big) this will take a while to load everything{Style.RESET_ALL}')

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
            
            yt = pt.YouTube(links)
            video_title = yt.title
            
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
                
            print(f'\nStarting download{Fore.GREEN} {video_title}{Style.RESET_ALL}')

            ydl.download([links])
            number_default = number_default + 1
            print(f'Finished {number_default}/{number} songs in ', round(t.time()-float(start_time),2),'s')

            t.time()
            if number_default == number:
                        
                print(f'\n{Fore.GREEN}Finished download in{Style.RESET_ALL}', round(t.time()-float(total_time),2),f'{Fore.GREEN}s{Style.RESET_ALL}')
                t.time() 
                print(f'\n{Fore.YELLOW}Press Enter to continue{Style.RESET_ALL}')
                while True:
                    try:
                        if keyboard.is_pressed('Enter'):
                            sys.exit(0)
                    except:
                        break
                    
    
    #download video as mp3 or mp4
    def Download_Video(URL_VIDEO, choice):   
        yt = pt.YouTube(URL_VIDEO)
        video_title = yt.title
    
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
                'outtmpl': 'audio/%(title)s.%(ext)s',
            })
            
        print(f'\nStarting download{Fore.GREEN} {video_title}{Style.RESET_ALL}')
        
        start_time = t.time()
        ydl.download([URL_VIDEO])
        
        print(f'\n{Fore.GREEN}Finished download in{Style.RESET_ALL}', round(t.time()-float(start_time),2),f'{Fore.GREEN}s{Style.RESET_ALL}')
        t.time() 
        print(f'\n{Fore.YELLOW}Press Enter to continue{Style.RESET_ALL}')
        while True:
            try:
                if keyboard.is_pressed('Enter'):
                    sys.exit(0)
            except:
                break
        


while True:    
    total_time = t.time()
    
    playlist_or_video = input(f"""\nYou want to download a {Fore.GREEN}(P)laylist{Style.RESET_ALL} or a {Fore.GREEN}(V)ideo{Style.RESET_ALL}? 
> """).upper()

    if playlist_or_video == 'VIDEO' or playlist_or_video == 'V':        
        choice = input('Mp3 or Mp4: ').lower() 
        ##URL_VIDEO = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
        URL_VIDEO = input("\nEnter a video's URL: ") 
        Khongphainhen.Download_Video(URL_VIDEO, choice) 
           
           
    elif playlist_or_video == 'PLAYLIST' or playlist_or_video == 'P':
        choice = input('Mp3 or Mp4: ').lower() 
        ##URL_PLAYLIST = "https://www.youtube.com/playlist?list=PL4RWBwVliOGmqjMF2OddNoc4vJ7V8y7Ci"
        URL_PLAYLIST = input("\nEnter a playlist's URL: ")    
        playlist = Playlist(URL_PLAYLIST)
        number = len(playlist.video_urls)
        meow = Khongphainhen.Get_Url(URL_PLAYLIST)
        Khongphainhen.Download_Playlist(meow, number, number_default, total_time, choice)
        
    elif keyboard.is_pressed('Enter'):
        print('maow')
        
    else:
        print('Invalid input')
