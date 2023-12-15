import customtkinter as ctk
from pytube import YouTube
from tkinter import ttk
import os

#setting root window
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#seting title
root.title("Youtube Downloader!")

#setting geometry
root.geometry("720,480")
root.minsize(720, 480)
root.maxsize(1080, 720)

#mainloop
root.mainloop()

# link = input("Kindly enter the link: ")
# yt = YouTube(link)
# video = yt.streams.get_highest_resolution()
# video.download()
# print("All done.")
