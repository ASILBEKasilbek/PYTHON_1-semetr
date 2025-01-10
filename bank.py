while 1:
    print("         KIRISH")
    print("      1-Uzbekcha")
    print("      2-Ruscha")
    print("      3-Inglizcha")
    k1=input("Tilni tanlang:")
    print("         PASSWORD")
    n=input("Plastik kartangiz parolini kiriting:")
    d=12183
    while d!=8:
        print("         BOSH MENU")
        print("""        1-Balansni tekshirish
            2-Naqd pul olish
            3-SMS xabar ulash
            4-Parolni o'zgartirish
            5-Mobil aloqa uchun to'lov
            6-Kredit to'lovlari
            7-Komunal to'lovlar
            8-Dasturdan chiqish""")
        d=int(input("Tanlang:"))
        q=1
        while int(q)!=0:
            if int(d)==1:
                print("         BALANSNI TEKSHIRISH")
                print("      Balansingizda ... so'm mablag' bor")
                print("      0-Orqaga")
                q=input("Tanlang:")
            elif int(d)==2:
                print("""Naqd pul olish
    1-200 ming
    2-150 ming
    3-200 ming
    4-300 ming
    5-Boshqa summa
    0-Orqaga""")
                y=int(input("Tanlang:"))
                if y==0:
                    q=0
            elif d==3:
                print("         SMS XABAR ULASH")
                print("""1-SMS xabarni o'chirish
2-SMS xabarni 
0-ortagan""")
                y=int(input("Tanlang:"))
                if y==0:
                    q=0
            elif d==4:
                print("         PAROLNI O'ZGARTIRISH")
                print("""1-Yangi parolni kiritish
0-Orqaga
""")
                y=int(input("Tanlang:"))
                if y==0:
                    q=0
            elif d==5:
                print("         MOBIL ALOQA UCHUN TO'LOV")
                print("""1-Uzmobile
2-Beeline
3-Usell
4-UMS
5-Perfectum
0-Orqaga""")
                y=int(input("Tanlang:"))
                if y==0:
                    q=0     
            elif d==6:
                print("         KREDIT TO'LOVLARI")
                print("""1-Kredit raqami
0-Orqaga
""")
                y=int(input("Tanlang:"))
                if y==0:
                    q=0
            elif d==7:
                print("         KOMUNAL TO'LOVLAR")
                print("""1-Eleckt energiyasi
2-Jarimalar
3-Gaz
4-Suv
0-Orqaga""")
                y=int(input("Tanlang:"))
                if y==0:
                    q=0
            else:
                print("Xato kod Boshqa kod kiriting:")
                q=0
                
                
                