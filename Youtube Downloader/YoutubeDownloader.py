# Creating GUI for the Downloader

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

# Global Variable
folder_name = ""


# Path location function
def openpath():
    global folder_name
    folder_name = filedialog.askdirectory()  # ask user to for file path
    if (len(folder_name)) > 1:
        patherror.config(text=folder_name, fg="green")
    else:
        patherror.config(text=folder_name, fg="red")


# download video function
def download_vid():
    choice = ytchoices.get()
    url = youtube_entry.get()

    if (len(url)) > 1:
        yterror.config(text="")
        yt = YouTube(url)

        if choice == choices[0]:
            select = yt.streams.get_highest_resolution()  # fetch the highest resolution of video

        elif choice == choices[1]:
            select = yt.streams.filter(progressive=True, file_extension='mp4').first()

        elif choice == choices[2]:
            select = yt.streams.filter(only_audio=True).first()
        else:
            yterror.config(text="Paste Link Again...", fg="red")

    # Download Message alert
    select.download(folder_name)  # download method
    yterror.config(text="Download Completed")


# Creating Window
root = Tk()
root.title("Youtube Video and Audio Downloader")
root.geometry("400x500")
root.config(bg="gray3")
root.resizable(False, False)
root.columnconfigure(0, weight=1)  # set all content in centre.

# Youtube Link Label
youtube_link = Label(root, text="Paste the URL of the Video", bg="gray3", fg="orange", font=("jost", 15))
youtube_link.grid()

# Youtube link label entry box
youtube_entryvar = StringVar()
youtube_entry = Entry(root, width=50, textvariable=youtube_entryvar)
youtube_entry.grid()

# URL Error Message
yterror = Label(root, text=" To paste URL above use CTRL+V", bg="gray3", fg="red", font=("jost", 10))
yterror.grid()

# Path Location Label
pathlabel = Label(root, text="Choose location to save video", bg="gray3", fg="orange", font=("jost", 15, "bold"))
pathlabel.grid()

# Path Button 
pathbtn = Button(root, text="Choose Path", width=10, bg="red", fg="white", command=openpath)
pathbtn.grid()

# Path Error
patherror = Label(root, text=" Please Choose Correct path", bg="gray3", fg="red", font=("jost", 10))
patherror.grid()

# Download Quality
ytquality = Label(root, text="Select Quality", bg="gray3", fg="orange", font=("jost", 15))
ytquality.grid()

# combobox for the quality choices
choices = ["High", "Low", "Audio"]
ytchoices = ttk.Combobox(root, values=choices)
ytchoices.grid()

# Download Button
download_button = Button(root, text="Download", width=10, bg="red", fg="white", command=download_vid)
download_button.grid()

# Designer Label
my_name = Label(root, text="  Made by Puneet Rajput  ", bg="gray3", fg="orange", font=("jost", 15))
my_name.grid()

root.mainloop()
