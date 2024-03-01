from tkinter import *  # tkinter kütüphanesini içeri aktarır
from tkinter import messagebox

from tkcalendar import DateEntry  # tkcalendar modülünden DateEntry sınıfını içeri aktarır

master = Tk()  # tkinter'de ana pencereyi oluşturur

canvas = Canvas(master, width=750, height=450)  # çizim alanı oluşturur
canvas.pack()  # çizim alanını ana pencereye yerleştirir

# Üst çerçeve oluşturur
frame_ust = Frame(master, bg="#add8e6")  # arka plan rengini belirler
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.75, relheight=0.1)  # yerini belirler

# Sol alt çerçeve oluşturur
frame_alt_sol = Frame(master, bg="#add8e6")  # arka plan rengini belirler
frame_alt_sol.place(relx=0.1, rely=0.21, relheight=0.5, relwidth=0.24)  # yerini belirler

# Sağ alt çerçeve oluşturur
frame_alt_sag = Frame(master, bg="#add8e6")  # arka plan rengini belirler
frame_alt_sag.place(relx=0.35, rely=0.21, relheight=0.5, relwidth=0.5)  # yerini belirler

# Üst çerçeveye "Hatırlatma Tipi" etiketi ekler
hatirlatma_tipi_etiket = Label(frame_ust, bg="#add8e6", text="Hatırlatma tipi", font="Verdana 12 bold") #Görünüm
hatirlatma_tipi_etiket.pack(side=LEFT, padx="10", pady="10") #Konum

# Üst çerçeveye "Doğum Günü", "Alışveriş", "Ödeme" seçeneklerini içeren açılır menü ekler
hatirlatma_tipi_opsiyon = StringVar(frame_ust)  # bir String değişken tanımlar
hatirlatma_tipi_opsiyon.set("\t")  # varsayılan değeri ayarlar
hatirlatma_tipi_acilir_menu = OptionMenu(frame_ust, hatirlatma_tipi_opsiyon, "Doğum Günü", "Alışveriş", "Ödeme")
hatirlatma_tipi_acilir_menu.pack(padx="10", pady="10", side=LEFT)

# Üst çerçeveye tarih seçici ekler
hatirlatma_tarih_secici = DateEntry(frame_ust, width=12, background="orange", foreground="black", borderwidth=2, locale="de_DE")
hatirlatma_tarih_secici._top_cal.overrideredirect(True)  # tarih seçiciyi gizler
hatirlatma_tarih_secici.pack(side=RIGHT, padx="10", pady="10")

# Üst çerçeveye "Hatırlatma Tarihi" etiketi ekler
hatirlatma_tarihi_etiket = Label(frame_ust, bg="#add8e6", text="Hatırlatma Tarihi", font="Verdana 12 bold")
hatirlatma_tarihi_etiket.pack(side=RIGHT, padx="10", pady="10")


# Alt sol çerçeveye "Hatırlatma Yöntemi" etiketi ekler
Label(frame_alt_sol, text="Hatırlatma Yöntemi", bg="#add8e6", font="Verdana 10 bold").pack(padx="10", pady="10", anchor=NW)

# Alt sol çerçeveye "Sisteme Kaydet", "E-posta gönder" seçeneklerini içeren radyo düğmeleri ekler
var = IntVar()  # bir tamsayı değişkeni tanımlar
R1 = Radiobutton(frame_alt_sol, text="Sisteme Kaydet", variable=var, value=1, font="Verdana 10", bg="#add8e6", activebackground="white")
R1.pack(anchor=NW, padx="15", pady="5")
R2 = Radiobutton(frame_alt_sol, text="E-posta gönder", variable=var, value=2, font="Verdana 10", bg="#add8e6", activebackground="white")
R2.pack(anchor=NW, padx="15", pady="5")

# Alt sol çerçeveye "Bir hafta önce", "Bir gün önce", "Aynı Gün" seçeneklerini içeren onay kutuları ekler
var1 = IntVar()  # bir tamsayı değişkeni tanımlar
C1 = Checkbutton(frame_alt_sol, text="Bir hafta önce", variable=var1, onvalue=1, offvalue=0, bg="#add8e6", font="Verdana 10")
C1.pack(anchor=NW, padx="22", pady="5")
var2 = IntVar()  # bir tamsayı değişkeni tanımlar
C2 = Checkbutton(frame_alt_sol, text="Bir gün önce", variable=var2, onvalue=1, offvalue=0, bg="#add8e6", font="Verdana 10")
C2.pack(anchor=NW, padx="22", pady="5")
var3 = IntVar()  # bir tamsayı değişkeni tanımlar
C3 = Checkbutton(frame_alt_sol, text="Aynı Gün", variable=var3, onvalue=1, offvalue=0, bg="#add8e6", font="Verdana 10")
C3.pack(anchor=NW, padx="22", pady="5")


# Gonderme işlevi çağrıldığında gerçekleştirilecek işlevi tanımlar
def gonder():
    son_mesaj = ""  # bir ileti değişkeni tanımlar
    try:
        if var.get():  # var değişkeni varsa
            if var.get() == 1:  # var değişkeninin değeri 1 ise
                son_mesaj += "Veriniz kaydedilmiştir."  # iletiye mesaj ekler

                tip = hatirlatma_tipi_opsiyon.get() if hatirlatma_tipi_opsiyon.get() == "" else "Genel"  # kategori tipini belirler
                tarih = hatirlatma_tarih_secici.get()  # hatırlatma tarihini alır
                mesaj = metin_alani.get("1.0", "end")  # hatırlatma mesajını alır

                with open("hatirlatmalar.txt", "w") as dosya:  # hatırlatmaları dosyaya yazar
                    dosya.write('{} kategorisinde, {} tarihine ve "{}" notuyla hatırlatma'.format(tip, tarih, mesaj))
                    dosya.close()

            elif var.get() == 2:  # var değişkeninin değeri 2 ise
                son_mesaj += "E-posta yoluyla hatırlatma size ulaşacaktır."  # iletiye mesaj ekler

            messagebox.showinfo("Başarılı İşlem", son_mesaj)  # başarılı işlem iletilerini gösterir

        else:
            son_mesaj += "Gerekli alanları doldurun"  # iletiye mesaj ekler
            messagebox.showwarning("Yetersiz Bilgi", son_mesaj)  # yetersiz bilgi uyarısı iletilerini gösterir

    except:
        son_mesaj = "Başarısız oldu"  # iletiye mesaj ekler
        messagebox.showerror("Başarısız İşlem", son_mesaj)  # başarısız işlem iletilerini gösterir

    return


# Alt sağ çerçeveye "Hatırlatma Mesajı" etiketi ekler
Label(frame_alt_sag, text="Hatırlatma Mesajı", bg="#add8e6", font="Verdana 10 bold").pack(padx="10", pady="10", anchor=NW)

# Alt sağ çerçeveye metin alanı ekler
metin_alani = Text(frame_alt_sag, height=9, width=50)
metin_alani.tag_config('style', foreground="#bfbfbf", font=('Verdana', 7, 'bold'))
metin_alani.pack(padx="10", pady="5")

karsilama_metni = "Mesajı buraya girin"
metin_alani.insert(END, karsilama_metni, 'style')  # metin alanına karşılama metnini ekler

# Alt sağ çerçeveye "Gönder" düğmesi ekler
gonder_butonu = Button(frame_alt_sag, text="Gönder", command=gonder)  # gönder düğmesini oluşturur
gonder_butonu.pack(anchor=N)  # gönder düğmesini çerçeveye yerleştirir

master.mainloop()  # uygulamayı çalıştırır
