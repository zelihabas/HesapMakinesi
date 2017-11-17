sayi1 = float(input ("1. Sayıyı Giriniz :"))
sayi2 = float(input ("2. Sayıyı Giriniz :"))

islem = input("Yapmak istediğiniz işlemi seçiniz : (+,-,*,/):")

if  islem == "+" :
    sonuc = sayi1 + sayi2
    print (sonuc)

elif islem  == "-":
    sonuc = sayi1 - sayi2
    print (sonuc)

elif islem == "*" :
    sonuc = sayi * sayi2
    print (sonuc)

elif islem == "/" and sayi2 != 0 :
    sonuc = sayi1 / sayi2
    print (sonuc)

else :
    print ("Hatalı Giriş Yaptınız !")
