from pytube import Playlist
import sys
import keyboard


# credit to noccoa0 on stackoverflow
URL_PLAYLIST = input("Enter a playlist's URL: ")

playlist = Playlist(URL_PLAYLIST)
print('Number Of Videos In playlist: %s' % len(playlist.video_urls))

urls = []
for url in playlist:
    urls.append(url)
    
print(f'\n{urls}')
#----------------------------------------------------------------


print("Press Esc to exit: ")

while True:
    try:
        if keyboard.is_pressed('Esc'):
            print("\nyou pressed Esc, so exiting...")
            sys.exit(0)
    except:
        break