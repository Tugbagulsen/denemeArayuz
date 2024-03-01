from tkinter import *
from tkinter import messagebox
from  tkcalendar import DateEntry

master = Tk()


canvas = Canvas(master, width=1000, height=450)
canvas.pack()

panel_genislik = 150
panel_yukseklik = 250
panel_aralik = 10
ust_bosluk = 20

frameVeriPanel = Frame(master, width=panel_genislik, height=panel_yukseklik, highlightbackground='Black', highlightthickness=1)
frameVeriPanel.place(relx=0.04, rely=ust_bosluk / 450, relwidth=0.5, relheight=0.65)
#relx = Panelin pencerenin sol üst köşesinden yatay olarak ne kadar uzak olacağını belirtir
#rely = Panelin pencerenin sol üst köşesinden dikey olarak ne kadar uzaklıkta olacağını belirtir
#relwidth = Panelin genişliğinin pencerenin genişliğine oranıdır
#reheight = Panelin yüksekliğinin pencerenin yüksekliğine oranıdır

frameAracPanel = Frame(master, width=panel_genislik, height=panel_yukseklik, highlightbackground='Black', highlightthickness=1)
frameAracPanel.place(relx=0.6, rely=0.04, relwidth=0.34, relheight=0.1)

frameSonucPanel = Frame(master, width=panel_genislik, height=panel_yukseklik, highlightbackground='Black', highlightthickness=1)
frameSonucPanel.place(relx=0.04, rely=ust_bosluk / 28, relwidth=0.9, relheight=0.2)

frameFonksiyonlarPanel = Frame(master, width=panel_genislik, height=panel_yukseklik, highlightbackground='Black', highlightthickness=1)
frameFonksiyonlarPanel.place(relx=0.6, rely=0.2, relwidth=0.34, relheight=0.5)



master.mainloop()