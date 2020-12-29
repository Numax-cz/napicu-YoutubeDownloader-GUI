from tkinter import *
import pytube
from tkinter import filedialog
from pytube import YouTube
import os
import time
import tkinter as tk
font = ('calibri', 16)

class Obrazovka(Tk):
    def __init__(self):
        super().__init__()
        # Šířka a Výška okna
        self.geometry('500x800')
        # Název okan
        self.title('NaPicu-YouTubeDownloader')
    def YouTubeUrlLabel(self):
        global lb
        # Yt url get
        lb = tk.Label(text='Zadej URL z YouTube', font=font)
        lb.place(relwidth=1, relheight=0.1)
    def YouTubeUrl(self):
        global url
        url = tk.Entry(font = font)
        url.place(relx=0.5, rely=0.1, relwidth= 0.45, relheight=0.03, anchor='n')  
    def ButtonCommand(self):
        global u
        # Get url
        u = url.get()
        # Když neni UrlPlace prazdná
        if u != '':
            url.destroy()
            lb.destroy()
            btn.destroy()
            try:
                global video
                video = pytube.YouTube(u)
            except:
                # Program se vypne --- někdy opravit!!
                self.tk.quit()
            global lb2
            global btn2
            lb2 = tk.Label(text=video.title, font=font)
            lb2.place(relwidth=1, relheight=0.1)
            # Button Stáhnout?
            btn2 = tk.Button(text='Stáhnout?', font=font, borderwidth=0, bg='#2ecc71', activebackground='#27ae60', command=self.VybratSlozku)
            btn2.place(relx=0.5, rely=0.1, relwidth= 0.45, relheight=0.03, anchor='n')
    def VybratSlozku(self):
        global soubor
        global lb3
        # Cesta k souboru
        soubor = filedialog.askdirectory(initialdir="/", title='Vybrat',)
        btn2.destroy()
        lb2.destroy()
        lb3 = tk.Label(text='Video bylo staženo!', font=font)
        lb3.place(relwidth=1, relheight=0.1)
        try:
            # Video rozliseni - tag
            VideoTag = video.streams.get_highest_resolution()
            # Stazeni videa soubor = filedirectory
            VideoTag.download(soubor)
        except:
            # Program se vypne --- někdy opravit!!
            self.tk.quit()
    def YouTubeButton(self):
        global btn
        # Button načíst
        btn = tk.Button(text='Načíst', font=font, borderwidth=0, bg='#2ecc71', activebackground='#27ae60', command=self.ButtonCommand)
        btn.place(relx=0.5, rely=0.15, relwidth= 0.45, relheight=0.03, anchor='n')
if __name__ == '__main__':
    window = Obrazovka()
    window.YouTubeUrlLabel()
    window.YouTubeUrl()
    window.YouTubeButton()
    window.mainloop()