import ssl
import smtplib

kullanici = 'tugba.akrihatech@gmail.com'
sifre = 'Tg.280719'

alici = 'nesibe.akrihateh@gmail.com'
baslik = 'Python Gönderisi'
mesaj = 'Deneme Mesaj'

context = ssl.create_default_context()
port = 465
host = "smtp.gmail.com"

eposta_sunucusu = smtplib.SMTP_SSL(host = host, port= port, context= context)
eposta_sunucusu.login(kullanici, sifre)
eposta_sunucusu.sendmail(kullanici, alici, mesaj)

