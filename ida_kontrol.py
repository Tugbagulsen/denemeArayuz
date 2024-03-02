import tkinter as tk
from tkinter import LabelFrame

master = tk.Tk()

canvas_genislik = 1000
canvas_yukseklik = 450
panel_genislik = 150
panel_yukseklik = 250
panel_margin = 10
top_margin = 20

canvas = tk.Canvas(master, width=canvas_genislik, height=canvas_yukseklik)
canvas.pack()

def label_frame_olusturma(master, text, relx, rely, relwidth, relheight):
    label_frame = LabelFrame(master, text=text)
    label_frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
    return label_frame

# Veri Paneli Oluşturma Fonksiyonu
label_frame_veri = label_frame_olusturma(master, "Veri", 0.04, top_margin / canvas_yukseklik, 0.5, 0.65)

# Arac Paneli Oluşturma Fonksiyonu
label_frame_arac = label_frame_olusturma(master, "Arac", 0.6, 0.04, 0.34, 0.1)
label_arac = tk.Label(label_frame_arac, text="Jetson Nano    192.168.1.1")
label_arac.pack(padx=15, pady=5, anchor=tk.NW)

# Sonuç Paneli Oluşturma Fonksiyonu
label_frame_sonuc = label_frame_olusturma(master, "Sonuç", 0.04, top_margin / 28, 0.9, 0.2)

# Sonuç Label'larını Dinamik Olarak Yerleştirme Fonksiyonu
def place_labels(veriler):
    for i, veri in enumerate(veriler):
        row = i // 3
        column = i % 3
        label = tk.Label(label_frame_sonuc, text=veri, font=("Arial", 10))
        label.grid(row=row, column=column, padx=35, pady=5, sticky="w")

# Veriler
veriler = [
    "Kırmızı Renk Tespit Edildi: ",
    "Çember Tespit Sayısı: ",
    "Pinger Tespit Edildi:",
    "Araç Konumlanıyor:",
    "Tamamlanan Çember Sayısı:"
]
# Dinamik olarak label yerleştirme işlemini gerçekleştir
place_labels(veriler)

# Fonksiyon Paneli Oluşturma Fonksiyonu
label_frame_fonksiyon = label_frame_olusturma(master, "Fonksiyon", 0.6, 0.2, 0.35, 0.5)

# Butonları Dinamik Olarak Yerleştirme
buton_metinleri = ["Batma", "Çıkma", "Sağ", "Sol", "İleri", "Geri", "Reset", "Kamera", "Arm", "Disarm", "Stabilize", "Auto"]
for i, metin in enumerate(buton_metinleri):
    row = i // 2
    column = i % 2
    buton = tk.Button(label_frame_fonksiyon, text=metin, width=10, height=1, background='White')
    buton.grid(row=row, column=column, padx=40, pady=3)

master.mainloop()
