import sqlite3

# liste = []
db = sqlite3.connect("KitapListesi.db")  # Kitaplİstesi adında bir veritabanı dosyası oluşturuyoruz

im = db.cursor()  # Veri tabanında işlem yapabilmek için imleç oluşturuyoruz
im.execute("CREATE TABLE IF NOT EXISTS Kitaplar (KitapAdi, KitapYazari)")  # imlecin execute metodunu kullanıyoruz

db.commit()

while True:

    print("YAPMAK İSTEDİĞİNİZ İŞLEMİ YAZINIZ.\nKitapEkle\nKitapSilme\nKitapBulma\nKitapListeleme")

    def kitapbulma():
        aranan_kitap = input("Aramak İstediğiniz Kitap= ")
        im.execute("SELECT *FROM Kitaplar")
        kitapismi = im.fetchall()
        j = 0
        for i in kitapismi:
            j += 1
            if i[0] == aranan_kitap:
                print(i)
                break
            if (i[0] != aranan_kitap) and (j == len(kitapismi)):
                print("Aradığınız Kitap Listede Bulunmamaktadır")

    def veriekleme():
        liste = []
        liste.append(input("KitapAdi:"))
        liste.append(input("KitapYazari:"))
        kitapekle(liste[0], liste[1])

    def kitapekle(kitapadi, kitapyazari):
        sql = "INSERT INTO Kitaplar VALUES ('{}','{}') ".format(kitapadi, kitapyazari)  # Tablomuza veri ekliyoruz
        im.execute(sql)  # Bu komut, oluşturduğumuz tabloya içerik eklememizi sağlıyor.
        db.commit()  # Bu girdiğimiz verileri veritabanına işleyebilmek için commit() adlı bir metottan yararlanıyoruz
        print("Kitap Eklendi..")

    def kitapsilme():
        silinecek_kitap = input("Silmek İstadiğiniz Kitap İsmi= ")
        im.execute("SELECT *FROM Kitaplar ")
        kliste = im.fetchall()
        j = 0
        for i in kliste:
            j += 1
            if i[0] == silinecek_kitap:
                im.execute("DELETE FROM Kitaplar WHERE KitapAdi= '{}'".format(silinecek_kitap))
                print(" '{}' Kitabı Silindi..".format(silinecek_kitap))
                break
            if (i[0] != silinecek_kitap) and (j == len(kliste)):
                print("Aradığınız Kitap Listede Bulunmamaktadır")
        db.commit()

    def kitaplarilistele():
        im.execute("SELECT *FROM Kitaplar ")
        kitaplistesi = im.fetchall()
        for i in kitaplistesi:
            print(i)

    istek = input("YAPMAK İSTEDİĞİNİZ İŞLEM:")

    if istek == "KitapEkle":
        veriekleme()
    if istek == "KitapSilme":
        kitapsilme()
    if istek == "KitapBulma":
        kitapbulma()
    if istek == "KitapListeleme":
        kitaplarilistele()

    istek = ""
