import database as db


def log_in():
    loop = True
    while loop:
        card_no = input("Kart Numarası: ")
        passw = input("Şifre: ")
        for i in db.data:
            if card_no == i[4] and passw == i[5]:
                global customerInfo
                customerInfo = list(i)
                print("Hoşgeldiniz ", customerInfo[1], customerInfo[2])
                loop = False
                break

        while loop:
            print("Eksik veya Hatalı Giriş Yaptınız, Lütfen Tekrar Deneyiniz")
            break


def bakiye_sorgula():
    print("Bakiyeniz: ", customerInfo[6])


def para_yatir():
    amount = int(input("Tutar Giriniz: "))
    customerInfo[6]+= amount
    db.update_customer("balance", customerInfo[6], customerInfo[4])
    print("Yeni Bakiyeniz: ", customerInfo[6])


def para_cek():
    amount = int(input("Tutar Giriniz: "))
    customerInfo[6] -= amount
    db.update_customer("balance", customerInfo[6], customerInfo[4])
    print("Yeni Bakiyeniz: ", customerInfo[6])


def sifre_guncelle():
    loop = True
    while loop:
        password = input("Şifre Giriniz: ")

        if password == customerInfo[5]:
            loop2 = True
            while loop2:
                newPassword = input("Yeni Şifre Giriniz: ")
                newPasswordAgain = input("Yeni Şifreyi Tekrar Giriniz: ")

                if newPassword == newPasswordAgain:
                    db.update_customer("password", newPassword, customerInfo[4])
                    print("Şifreniz Başarıyla Güncellendi")
                    loop = False
                    loop2 = False
                    break

                while loop2:
                    print("Eksik veya Hatalı Giriş Yaptınız, Lütfen Tekrar Deneyiniz")
                    break

        while loop:
            print("Eksik veya Hatalı Giriş Yaptınız, Lütfen Tekrar Deneyiniz")
            break
