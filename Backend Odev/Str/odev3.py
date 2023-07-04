ad = input("isim")
soyad = input("soyisim")
yas = input("yas")
if yas.isnumeric():
    print("Isim : {} \nSoyisim: {} \nYas: {}".format(ad,soyad,yas))
else:
    print("Lutfen yasa bir sayi giriniz")    