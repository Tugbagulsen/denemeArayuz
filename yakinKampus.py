from tkinter import *
from tkcalendar import DateEntry

master = Tk()

canvas = Canvas(master, width=750, height=450)
canvas.pack()  #anapencereye canvas koydu

frame_ust = Frame(master, bg="#add8e6")
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.75, relheight=0.1) #alanının onda 1lik kordiianatıyla x ve ylerden başla sonra x'in uzunluğu alanmın yüzde 75ini alsın

frame_alt_sol = Frame(master, bg="#add8e6")
frame_alt_sol.place(relx=0.1, rely=0.21, relheight=0.5, relwidth=0.24)

frame_alt_sag = Frame(master, bg="#add8e6")
frame_alt_sag.place(relx=0.35, rely=0.21, relheight=0.5, relwidth=0.5)


hatirlatma_tipi_etiket = Label(frame_ust,bg="#add8e6",text="Hatirlatma tipi", font="Verdana 12 bold")
hatirlatma_tipi_etiket.pack(side=LEFT, padx="10", pady="10")
#hatirlatma_tipi_etiket.grid(row=2, column=2)

hatirlatma_tipi_opsiyon = StringVar(frame_ust) #tanıtmak için önce onu açtık
hatirlatma_tipi_opsiyon.set("\t")  #default değer atadı

hatirlatma_tipi_acilir_menu= OptionMenu(frame_ust,hatirlatma_tipi_opsiyon,
                                        "Doğum Günü","Alisveris","Odeme")
hatirlatma_tipi_acilir_menu.pack(padx="10", pady="10", side=LEFT)


hatirlatma_tarih_secici = DateEntry(frame_ust, width=12, background="orange", foreground="black" , borderwidth=2, locale="de_DE")
hatirlatma_tarih_secici._top_cal.overrideredirect(True)
hatirlatma_tarih_secici.pack(side=RIGHT, padx="10", pady="10")

hatirlatma_tarihi_etiket = Label(frame_ust,bg="#add8e6",text="Hatirlatma Tarihi", font="Verdana 12 bold")
hatirlatma_tarihi_etiket.pack(side=RIGHT, padx="10", pady="10")


#part2

Label(frame_alt_sol, text="Hatirlatma Yöntemi",bg="#add8e6",font="Verdana 10 bold").pack(padx="10", pady="10", anchor=NW) #sol en üstte olsun

var = IntVar()
R1  = Radiobutton(frame_alt_sol,text="Sisteme Kaydet", variable=var, value=1, font="Verdana 10", bg="#add8e6", activebackground="white")  #bu seçilirse var değişkeni 1 seçeneğini alsın
R1.pack(anchor=NW, padx="15", pady="5")

R2  = Radiobutton(frame_alt_sol,text="E-posta gönder", variable=var, value=2, font="Verdana 10", bg="#add8e6", activebackground="white")
R2.pack(anchor=NW, padx="15", pady="5")

var1= IntVar()
C1 = Checkbutton(frame_alt_sol, text="Bir hafta önce",variable=var1, onvalue=1, offvalue=0, bg="#add8e6", font="Verdana 10")
C1.pack(anchor=NW, padx="22", pady="5")

var2= IntVar()
C2 = Checkbutton(frame_alt_sol, text="Bir gün önce",variable=var2, onvalue=1, offvalue=0, bg="#add8e6", font="Verdana 10")
C2.pack(anchor=NW, padx="22", pady="5")

var3= IntVar()
C3 = Checkbutton(frame_alt_sol, text="Aynı Gün",variable=var3, onvalue=1, offvalue=0, bg="#add8e6", font="Verdana 10")
C3.pack(anchor=NW, padx="22", pady="5")

#part3
from tkinter import messagebox
def gonder():
    son_mesaj= ""
    try:

        if var.get(): #var değeri varsa
            if var.get() == 1:
                son_mesaj+="Veriniz kaydedilmiştir."

                tip = hatirlatma_tipi_opsiyon.get() if hatirlatma_tipi_opsiyon.get()=="" else "Genel"  #true değilse genel yazdır yani
                tarih = hatirlatma_tarih_secici.get()
                mesaj = metin_alani.get("1.0","end") #get textte çalışmadığı için 1den sona kadar olanları al dendi

                with open("hatirlatmalar.txt", "w") as dosya:
                    dosya.write('{} kategorisinde , {} tarihine ve "{}" notuyla hatirlatma'.format(tip, tarih,mesaj))
                    dosya.close()

            elif var.get() == 2:
                son_mesaj += "E-posta yoluyla hatirlatma size ulaşacaktir"

            messagebox.showinfo("Başarili İşlem", son_mesaj)

        else:
            son_mesaj +="Gerekli alanları doldurun"
            messagebox.showwarning("Yetersiz Bilgi", son_mesaj)

    except:
        son_mesaj = "Başarisiz oldu "
        messagebox.showerror("BAşarısız işlem", son_mesaj)

    #finally:
     #   master.destroy() #sonra kapat yani başk ahherhangibir durumda

    return



Label(frame_alt_sag, text="Hatirlatma Mesajı",bg="#add8e6",font="Verdana 10 bold").pack(padx="10", pady="10", anchor=NW)

metin_alani = Text(frame_alt_sag, height=9, width=50)
metin_alani.tag_config('style',foreground="#bfbfbf",font=('Verdana',7,'bold'))
metin_alani.pack(padx="10", pady="5")

karsilama_metni = "Mesajı buraya girin"
metin_alani.insert(END,karsilama_metni, 'style')

gonder_butonu = Button(frame_alt_sag, text="Gönder", command=gonder)  #master.destroy
gonder_butonu.pack(anchor=N)


master.mainloop() #acık kalsin
