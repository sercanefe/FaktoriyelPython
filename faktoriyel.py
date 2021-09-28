# -*- coding: utf-8 -*-

sayi = int(input("Sayı Giriniz: "))

faktoriyel = 1

if sayi < 0:
    print("Faktöriyeli yok")
elif sayi == 0:
    print("Faktöriyel: 1")
else:
    for i in range(1,sayi+1):
        faktoriyel = faktoriyel * i
    print("Sonuç: ",faktoriyel)
            