import customtkinter as ctk
from pytube import YouTube
from tkinter import ttk
import os

#setting root window
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

#seting title
root.title("Youtube Downloader!")

#setting geometry
root.geometry("720,480")
root.minsize(720, 480)
root.maxsize(1080, 720)

#create a frame to hold the content
contentFrame = ctk.CTkFrame(root)
contentFrame.pack(fill=ctk.BOTH, expand=True)


#create a lable and the entry widget for the vidoe url
urlLable = ctk.CTkLabel(contentFrame, text="Kindly enter the youtube URL")
entryUrl = ctk.CTkEntry(contentFrame, width=400, height=40)
urlLable.pack(pady=("10p", "5p"))
entryUrl.pack(pady=("10p", "5p"))

#create a download button
downloadBotton = ctk.CTkButton(contentFrame, text="Dowmload")
downloadBotton.pack(pady=("10p", "5p"))

#creats a resolution combo box
resolutions =["720px", "360", "240"]
resolutionVar = ctk.StringVar()
resolutionComboBox = ctk.CTkComboBox(contentFrame, values=resolutions)

#mainloop
root.mainloop()

# link = input("Kindly enter the link: ")
# yt = YouTube(link)
# video = yt.streams.get_highest_resolution()
# video.download()
# print("All done.")
