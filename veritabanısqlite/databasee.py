import sqlite3
global baglan
global im
global dosya_adi
sutunlar = " "
liste = []
print("YAPMAK İSTEDİĞİNİZ İŞLEMİ YAZINIZ.\nYENİ DOSYA OLUŞTURMA\nMETİN EKLEME\nDEĞER ALMA ")
istek = input("YAPMAK İSTEDİĞİNİZ İŞLEM:")


def yenidosya():
    print("Olusturmak istediginiz dosyanın ismini yazınız(LÜTFEN TÜRKÇE KARAKTER KULLANMAYINIZ)")
    dosya_adi = input("Dosya Adı: ")
    baglan  = sqlite3.connect("{}.svs".format(dosya_adi))
    im = baglan.cursor()  ### Veri tabanı üzerinde işlem yapabilmek için
    tabloolusturma()

def tabloolusturma():
    Tablo_adi = input("OLUŞTURMAK İSTEDİGİNİZ TABLONUN ADINI YAZINIZ.")
    sutunlar = input("TABLO SÜTUN BAŞLIKLARINI ARALARINDA BİRER BOŞLUK BIRAKARAK GİRİNİZ.")
    liste = sutunlar.split()
    im.execute("CREATE TABLE IF NOT EXISTS {} ({} TEXT,{} TEXT,{} TEXT,{} TEXT)".format(Tablo_adı,liste[0],liste[1],liste[2],liste[3]))
    ###CREATE TABLE kısmı bir SQL komutu olup, bu komut bir tablo oluşturulmasını sağlar.
    tablodegergirme()

def metinekleme(ad,soyad,numara,notu):
    sql  = "INSERT INTO Öğrenciler VALUES ('{}','{}','{}','{}') ".format(ad,soyad,numara,notu)
    im.execute(sql) ###Bu komut, oluşturduğumuz tabloya içerik eklememizi sağlıyor.
    baglan.commit()  ###Bu girdiğimiz verileri veritabanına işleyebilmek için commit() adlı bir metottan yararlanacağız:
    degeralma()

def tablodegergirme():
    liste[0]=input("Ad: ")
    liste[1]=input("Soyad: ")
    liste[2]=int(input("Numara: "))
    liste[3]=int(input("Notu: "))
    metinekleme(liste[0],liste[1],liste[2],liste[3])

def degeralma():
    im.execute("SELECT * FROM Öğrenciler  ")  ###Verileri süzme işini WHERE adlı bir SQL komutu yardımıyla gerçekleştireceğiz
    data = im.fetchall() ### Seçtiğimiz verileri veritabanından almak için.
    for i in data:
        print(i)

def metinsilme():
    im.execute("DELETE FROM Öğrenciler WHERE Notu = 50")
    im.execute("SELECT * FROM Öğrenciler  ")
    data = im.fetchall()  # Seçtiğimiz verileri veritabanından almak için.
    for i in data:
        print(i)
    baglan.commit()

if istek == "YENİ DOSYA OLUŞTURMA":
    yenidosya()
if istek == "METİN EKLEME":
    metinekleme()
if istek == "METİN SİLME":
    metinsilme()

#tabloolusturma()
#for i in range(5):
    #tablodegergirme()

#degeralma()
#tablodegergirme()
baglan.close()   ###bütün işlemleri bitirdikten sonra veritabanını kapatmak için