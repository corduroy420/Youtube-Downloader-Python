# Enjoy this but if your going to skid leave some credit
# Corduroy.wtf | corduroy#1001
# :)

import tkinter
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

os.system('title [YouTube Downloader] By Corduroy ^| Menu')

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        pass

#donwload video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.get_highest_resolution()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            pass


    #download function
    select.download(Folder_Name)
    complete()

def deletec():
    complete.destroy()

def complete():
  choice = ytdchoices.get()
  url = ytdEntry.get()
  yt = YouTube(url)
  global complete
  complete = Toplevel(root)
  complete.title("Success")
  complete.geometry("500x60+1200+400")
  complete.iconbitmap(r'./img/favicon.ico')
  Label(complete, text = f"Download Complete!\n{yt.title}").pack()
  Button(complete, text="cool!",bg="red",fg="white",command=deletec).pack()



root = tkinter.Tk()
root.title("YouTube Downloader Corduroy")
root.geometry("350x250+1200+400") #set window
root.columnconfigure(0,weight=1) #set all content in center.
root.iconbitmap(r'./img/favicon.ico')
root.configure(bg="#2a2f38")


#Ytd Link Label
ytdLabel = Label(root,text="Youtube Video URL",bg="#2a2f38",font=("jsot",15),fg="white")
ytdLabel.grid()

# Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#Asking save file label
saveLabel = Label(root,text="Location of file",bg="#2a2f38",font=("jsot",15),fg="white")
saveLabel.grid()

#btn of save file
saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

#Download Quality
ytdQuality = Label(root,text="Select Quality",bg="#2a2f38",font=("jsot",15),fg="white")
ytdQuality.grid()

#Error Msg location
locationError = Label(root,text="",font=("jost",10),bg="#2a2f38",fg="white")
locationError.grid()

#combobox
choices = ["1080p","720p","mp3"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid(pady=3)

#donwload btn
downloadbtn = Button(root,text="Donwload",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

def deleteabout():
    about.destroy()

def about():
  global about
  about = Toplevel(root)
  about.title("About")
  about.geometry("233x90+1260+500")
  about.iconbitmap(r'./img/favicon.ico')
  Label(about, text = f'Just a cool little youtube\n downloader made with tkinter\n By Corduroy#1001').pack()
  ok = ttk.Button(about, text='oke dokie',command=deleteabout).pack()

def deletetips():
    tips.destroy()

def tips():
  global tips
  tips = Toplevel(root)
  tips.title("tips")
  tips.geometry("250x100+1260+500")
  tips.iconbitmap(r'./img/favicon.ico')
  Label(tips, text = f'When selection to download as an mp3\n it will download as an mp4 with\n no audio. Just rename the file\n extension to mp3').pack()
  ok = ttk.Button(tips, text='lol alr',command=deletetips).pack()

# help menu
menubar = tkinter.Menu(root)
root['menu'] = menubar
change_menu = tkinter.Menu(menubar)
menubar.add_cascade(menu=change_menu, label='Info')
change_menu.add_command(label='About',command=about)
change_menu.add_command(label='Tips',command=tips)


if __name__ == "__main__":
    root.mainloop()
