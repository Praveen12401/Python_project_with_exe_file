from pytube import YouTube
from tkinter import filedialog


# Function to download the video
def download_video():
    save_path = filedialog.askdirectory()
    print("your video  are downloading this location :👇👇👇")
    print(save_path)
    print(50 * "-")
    url_input = input("enter url:")

    # Create a YouTube object with the video URL

    yt = YouTube(url_input)




    # Get the highest resolution stream available
    if yt.age_restricted:
        print('yes age')
        yt.bypass_age_gate()
        str = yt.streams.get_lowest_resolution()
        str.download(output_path=save_path)

    str = yt.streams.get_highest_resolution()


    title = yt.title

    print(f"video title: {title}")
    print('Downloding...')
    # Download the video to the selected directory

    str.download(output_path=save_path)
    # Update the status label
    print("Download Completed")


download_video()
