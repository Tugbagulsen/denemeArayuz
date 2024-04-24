import tkinter as tk
from tkinter import LabelFrame, messagebox
import cv2
from PIL import Image, ImageTk
import threading



master = tk.Tk()
master.geometry("1500x700+5+0")
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
label_frame_veri = label_frame_olusturma(master, "KAMERA", 0.04, top_margin / canvas_yukseklik, 0.4, 0.48)


label_frame_veri_kilitlenme = label_frame_olusturma(master,"KİLİTLENME DURUMU",0.04, 0.5, 0.4, 0.2)

label_kilitlenme_durum = tk.Label(label_frame_veri_kilitlenme,text="Kilitlenme Durum:")
label_kilitlenme_durum.place(relx=0.01,rely =0.01)
entry_kilitlenme_durum = tk.Entry(label_frame_veri_kilitlenme)
entry_kilitlenme_durum.place(relx=0.2, rely=0.01)

label_kilitlenme_süre = tk.Label(label_frame_veri_kilitlenme,text="Kilitlenme Süre:")
label_kilitlenme_süre .place(relx=0.01,rely =0.18)
entry_kilitlenme_süre  = tk.Entry(label_frame_veri_kilitlenme)
entry_kilitlenme_süre .place(relx=0.2, rely=0.18)

label_kilitlenme_sayi = tk.Label(label_frame_veri_kilitlenme,text="Kilitlenme Sayı:")
label_kilitlenme_sayi .place(relx=0.01,rely =0.35)
entry_kilitlenme_sayi  = tk.Entry(label_frame_veri_kilitlenme)
entry_kilitlenme_sayi .place(relx=0.2, rely=0.35)

buton_arm= tk.Button(label_frame_veri_kilitlenme, text = "ARM")
buton_arm.place(relx=0.25, rely=0.55)

buton_ayril= tk.Button(label_frame_veri_kilitlenme, text = "DISARM")
buton_ayril.place(relx=0.5, rely=0.55)




# Arac Paneli Oluşturma Fonksiyonu
label_frame_arac = label_frame_olusturma(master, "SUNUCU", 0.6, 0.04, 0.34, 0.3)
label_arac = tk.Label(label_frame_arac, text="HANÇER İHA")
label_arac.pack(padx=15, pady=5, anchor=tk.CENTER)

frame_arac_sunucu_sag = label_frame_olusturma(label_frame_arac,text="",relx=0.01,rely=0.01, relwidth=0.3,relheight=0.6)
frame_arac_sunucu_sag.pack(side= tk.LEFT, anchor=tk.N)

frame_arac_sunucu_sol = label_frame_olusturma(label_frame_arac,relx=0.5,rely=0.01,  text="",relwidth=0.5,relheight=0.6)
frame_arac_sunucu_sol.pack(side = tk.TOP)

label_sunucu = tk.Label(frame_arac_sunucu_sag, text="Sunucu Giriş :")
label_sunucu.pack(padx=5)
label_kullanici = tk.Label(frame_arac_sunucu_sag, text="Kullanıcı Adı :")
label_kullanici.pack(padx=5)
label_sifre = tk.Label(frame_arac_sunucu_sag, text="Kullanıcı Şifre:")
label_sifre.pack(padx=5)

buton_baglan= tk.Button(label_frame_arac, text = "Bağlan")
buton_baglan.pack(pady=20,side = tk.LEFT,anchor=tk.N )

buton_ayril= tk.Button(label_frame_arac, text = "Ayril")
buton_ayril.pack(pady=20)

label_baglanti_durumu = tk.Label(label_frame_arac,text="Şimdilik Aktif Değil")
label_baglanti_durumu.pack(side = tk.LEFT,anchor=tk.N )

entry_sunucu = tk.Entry(frame_arac_sunucu_sol)
entry_sunucu.pack()
entry_kullanici = tk.Entry(frame_arac_sunucu_sol)
entry_kullanici.pack()
entry_sifre = tk.Entry(frame_arac_sunucu_sol)
entry_sifre.pack()





# Sonuç Paneli Oluşturma Fonksiyonu
label_frame_bilgi = label_frame_olusturma(master, "BİLGİ EKRANI", 0.04, top_margin / 28, 0.9, 0.2)

label_roll_aci = tk.Label(label_frame_bilgi,text="Roll Açısı:")
label_roll_aci .place(relx=0.01,rely =0.01)
entry_roll_aci  = tk.Entry(label_frame_bilgi)
entry_roll_aci .place(relx=0.1, rely=0.01)

label_pitch_aci = tk.Label(label_frame_bilgi,text="Pitch Açısı:")
label_pitch_aci .place(relx=0.01,rely =0.18)
entry_pitch_aci  = tk.Entry(label_frame_bilgi)
entry_pitch_aci .place(relx=0.1, rely=0.18)

label_yaw_aci = tk.Label(label_frame_bilgi,text="Yaw Açısı:")
label_yaw_aci .place(relx=0.01,rely =0.35)
entry_yaw_aci  = tk.Entry(label_frame_bilgi)
entry_yaw_aci .place(relx=0.1, rely=0.35)

#
label_arac_hiz = tk.Label(label_frame_bilgi,text="Araç Hızı:")
label_arac_hiz .place(relx=0.23,rely =0.01)
entry_arac_hiz  = tk.Entry(label_frame_bilgi)
entry_arac_hiz .place(relx=0.3, rely=0.01)

label_hava_hiz = tk.Label(label_frame_bilgi,text="Hava Hızı:")
label_hava_hiz .place(relx=0.23,rely =0.18)
entry_hava_hiz  = tk.Entry(label_frame_bilgi)
entry_hava_hiz .place(relx=0.3, rely=0.18)

label_yer_hiz = tk.Label(label_frame_bilgi,text="Yer Hızı:")
label_yer_hiz .place(relx=0.23,rely =0.35)
entry_yer_hiz  = tk.Entry(label_frame_bilgi)
entry_yer_hiz .place(relx=0.3, rely=0.35)

#

label_batarya = tk.Label(label_frame_bilgi,text="Batarya Durum:")
label_batarya .place(relx=0.43,rely =0.01)
entry_batarya  = tk.Entry(label_frame_bilgi)
entry_batarya .place(relx=0.5, rely =0.01)

label_yukseklik = tk.Label(label_frame_bilgi,text="Araç Yükseklik:")
label_yukseklik .place(relx=0.43,rely=0.18)
entry_yukseklik   = tk.Entry(label_frame_bilgi)
entry_yukseklik  .place(relx=0.5, rely=0.18)

label_mod = tk.Label(label_frame_bilgi,text="Mod Durum:")
label_mod.place(relx=0.43,rely=0.35)
entry_mod  = tk.Entry(label_frame_bilgi)
entry_mod .place(relx=0.5, rely=0.35)








# Fonksiyon Paneli Oluşturma Fonksiyonu
label_frame_fonksiyon = label_frame_olusturma(master, "ELLE KONTROL MOD", 0.6, 0.4, 0.35, 0.3)



frame_fonksiyon_sol= label_frame_olusturma(label_frame_fonksiyon,"",0.1,0.1,0.4,0.8)
frame_fonksiyon_sağ= label_frame_olusturma(label_frame_fonksiyon,"",0.5,0.1,0.4,0.8)

buton1=tk.Button(frame_fonksiyon_sol,text="Otonom Uçuş")
buton1.pack(pady=5)
buton2=tk.Button(frame_fonksiyon_sol,text="Otonom İniş")
buton2.pack(pady=5)
buton3=tk.Button(frame_fonksiyon_sol,text="Takip Başlat")
buton3.pack(pady=5)
buton4=tk.Button(frame_fonksiyon_sol,text="Rota İzle")
buton4.pack(pady=5)

buton5=tk.Button(frame_fonksiyon_sağ,text="Kamera", command=lambda :kamera_goruntusu_goster())
buton5.pack(pady=5)
buton6=tk.Button(frame_fonksiyon_sağ,text="Reset")
buton6.pack(pady=5)
buton7=tk.Button(frame_fonksiyon_sağ,text="Stabilize")
buton7.pack(pady=5)
buton8=tk.Button(frame_fonksiyon_sağ,text="Auto")
buton8.pack(pady=5)


# Butonları Dinamik Olarak Yerleştirme
buton_metinleri = ["Otonom Uçuş","Otonom İniş","Takip Başlat","Rota İzle", "Kamera", "Reset", "Stabilize",
                   "Auto"]
#buton_fonksiyonlari = [func1, func2, func3, func4, func5, func6, func7, func8, func9, func10, func11,func12]
for i, metin in enumerate(buton_metinleri):
    row = i // 2
    column = i % 2
    #buton = tk.Button(label_frame_fonksiyon, text=metin, width=10, height=1, background='White',command=buton_fonksiyonlari[i])
    #buton.grid(row=row, column=column, padx=40, pady=3)


def kamera_goruntusu_goster():
    def kamera_thread():
        # Kamera başlatma
        kamera = cv2.VideoCapture(0)

        while True:
            # Kameradan bir kare al
            ret, kare = kamera.read()

            # Eğer kare başarılı bir şekilde alındıysa
            if ret:
                # OpenCV kütüphanesinden görüntüyü Tkinter ile uyumlu hale getirme
                kare = cv2.cvtColor(kare, cv2.COLOR_BGR2RGB)
                kare = Image.fromarray(kare)
                kare = ImageTk.PhotoImage(kare)

                # Görüntüyü bir etikete yerleştirme
                label = tk.Label(label_frame_veri, image=kare)
                label.image = kare
                label.pack()

                # 10 ms bekleyerek kareyi güncelleme
                label.after(10, kamera_thread)
            else:
                messagebox.showerror("Hata", "Kamera görüntüsü alınamadı.")
                break

        # Kamerayı kapat
        kamera.release()

    # Kamera işlemlerini arka planda gerçekleştirme
    threading.Thread(target=kamera_thread, daemon=True).start()

"""
def start_video_capture():
    def video_thread():
        # Video kaydı için kamera yakalama
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            messagebox.showerror("Hata", "Kamera bulunamadı veya açılamadı!")
            return
        # Video kaydı için VideoWriter nesnesi oluşturma
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('video_kaydi.avi', fourcc, 20.0, (640, 480))

        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                # Her kareyi uygun formata dönüştürme
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = Image.fromarray(frame)
                frame = ImageTk.PhotoImage(frame)

                # Görüntüyü bir etikete yerleştirme
                label.config(image=frame)
                label.image = frame

                # 'q' tuşuna basılınca kayıttan çık
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

            # 30 ms bekleyerek kareyi güncelleme
            label.after(30)

        # Pencere ve kayıt nesnelerini serbest bırak
        cap.release()
        out.release()

    # İlk kareyi göstermek için bir etiket oluşturma
    label = tk.Label(label_frame_veri)
    label.pack()

    # Video işlemlerini arka planda gerçekleştirme
    threading.Thread(target=video_thread, daemon=True).start()
"""
def start_video_capture():
    def video_thread():
        # Video kaydı için kamera yakalama
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            messagebox.showerror("Hata", "Kamera bulunamadı veya açılamadı!")
            return

        # Video kaydı için VideoWriter nesnesi oluşturma
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('video_kaydi.avi', fourcc, 20.0, (640, 480))

        # FPS hesaplama için zaman değişkenleri
        start_time = cv2.getTickCount()
        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                # Her kareyi uygun formata dönüştürme
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = Image.fromarray(frame)
                frame = ImageTk.PhotoImage(frame)

                # Görüntüyü bir etikete yerleştirme
                label.config(image=frame)
                label.image = frame

                # FPS hesaplama
                frame_count += 1
                if cv2.getTickCount() - start_time > 1:
                    fps = frame_count / ((cv2.getTickCount() - start_time) / cv2.getTickFrequency())
                    fps_label.config(text=f"FPS: {round(fps, 2)}")

                    # FPS hesaplama için değişkenleri sıfırlama
                    start_time = cv2.getTickCount()
                    frame_count = 0

                # 'q' tuşuna basılınca kayıttan çık
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

            # 30 ms bekleyerek kareyi güncelleme
            label.after(30)

        # Pencere ve kayıt nesnelerini serbest bırak
        cap.release()
        out.release()

    # İlk kareyi göstermek için bir etiket oluşturma
    label = tk.Label(label_frame_veri)
    label.pack()

    # FPS bilgisini gösterecek bir etiket oluşturma
    fps_label = tk.Label(label_frame_veri, text="")
    fps_label.pack()

    # Video işlemlerini arka planda gerçekleştirme
    threading.Thread(target=video_thread, daemon=True).start()

master.mainloop()

