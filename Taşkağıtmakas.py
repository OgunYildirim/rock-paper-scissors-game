from random import randint
puan = 0
while True :
    seçenekler=["taş","kağıt","makas"]
    bilgisayar_seçimi=seçenekler[randint(0,2)]
    kullanıcı=input("taş,kağıt,makas seçeneklerinden birini seçiniz : (çıkmak için 'q' basın)")
    if kullanıcı == "q" :
        print("oyundan çıkılıyor...")
        print("Puanınız",puan)
        break
    elif kullanıcı == bilgisayar_seçimi : 
        print("Berabere bitti puan kazanamadınız .")
    elif kullanıcı == "taş" :
        if bilgisayar_seçimi == "kağıt" :
            print("Bilgisayar kağıt seçti")
            print("Kaybettiniz",bilgisayar_seçimi,kullanıcı,"ı sarar")
            puan= puan - 1
            print("Yeni puanınız",puan)
        elif bilgisayar_seçimi == "makas":
            print("Bilgisayar makas seçti")
            print("Kazandınız",kullanıcı,bilgisayar_seçimi,"ı kırar")
            puan = puan + 1 
            print("Yeni puanınız",puan)
    elif kullanıcı == "kağıt" :
        if bilgisayar_seçimi == "makas" :
            
            print("Bilgisayar makas seçti")
            print("Kaybettiniz",bilgisayar_seçimi,kullanıcı,"ı keser")
            puan = puan - 1
            print("Yeni puanınız",puan)
        elif bilgisayar_seçimi == "taş" :
            print("Bilgisayar taş seçti")
            print("Kazandınız",kullanıcı,bilgisayar_seçimi,"ı sarar")
            puan = puan + 1
            print("Yeni puanınız",puan)
    elif kullanıcı == "makas" :
        if bilgisayar_seçimi == "kağıt":
            print("Bilgisayar kağıt seçti")
            print("Kazandınız",kullanıcı,bilgisayar_seçimi,"ı keser")
            puan = puan + 1
            print("Yeni puanınız",puan)
        elif bilgisayar_seçimi == "taş" :
            print("Bilgisayar taş seçti")
            print("Kaybettiniz",bilgisayar_seçimi,kullanıcı,"ı kırar")
            puan = puan - 1
            print("yeni puanınız",puan)
    












