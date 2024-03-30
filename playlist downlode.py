from pytube import Playlist, YouTube
from tkinter import filedialog
import tkinter as t

i = 1
''' this code work proper '''


def download_video(video1):
    global i
    # Create a YouTube object with the video URL
    str1 = YouTube(video1)


    #  this function Get the highest resolution stream available

    # str = str1.streams.get_highest_resolution()
    # str = str1.streams.first()
    str = str1.streams.get_highest_resolution()
    print(f"Video tittle:  {str.title}")
    # a=input("ok")

    print('Downloding...')

    # Download the video to the selected directory
    str.download(output_path=save_path)
    # Update the status label

    print(f"completed:{i} and remaining:{len(py) - i}")
    i += 1


root = t.Tk()
root.withdraw()
save_path = filedialog.askdirectory()
print("your video  are downloading this location :👇👇👇")
print(save_path)
print(50 * "-")

url_input = str(input("Now Enter url  of Playlist:"))


py = Playlist(url_input)

''' download playlist all single click'''
print(f"total video: {len(py)}")

try:
    if len(py)>1:
        print("""                 1.  enter 1  if change video download sequence 
                 2.  enter 2 other wise defoult  download 
                 3.  enter  3 if choose random number video for download\n""")
        number = int(input("enter a number"))
        if number == 1:
            print("enter where start index video:")
            start = int(input(""))
            print("enter where stop index video:")
            stop = int(input(""))
        elif number == 3:
            print("enter video number which download if done ,enter: 405 for downloading start")
            number_list = set()
            while True:
                try:
                    n = int(input('enter video number:'))
                    n -= 1
                    if n == 404:
                        break
                    elif n <= len(py):
                        number_list.add(n)
                    else:
                        print(f"wrong number enter please enter 1 to{len(py)} your video range available")
                except Exception as e:
                    print(f'error{e}')



        elif number == 2:
            start = 0
            stop = len(py)
        else:
            print(" wrong operation  try again please only enter 1 or 2 or 3")
            exit()
    else:
        print('some thing is wrong this link zero video contain  choose other link')
        exit()
except Exception as e:
    print(" wrong operation  try again please only enter 1 or 2 or 3")
    exit()


print('Downloading start..')
if number == 3:
    for video_number in number_list:
        # call download function for one by one download video
        download_video(py[video_number])
    print('Complete all downloade process is done 👍👍')
else:
    for video_number in range(start - 1, stop):
        # call download function for one by one download video
        download_video(py[video_number])
    print('Complete all downloade process is done 👍👍')
