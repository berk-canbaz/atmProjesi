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
    db.update_customer(customerInfo[6], customerInfo[4])
    print("Yeni Bakiyeniz: ", customerInfo[6])


def para_cek():
    amount = int(input("Tutar Giriniz: "))
    customerInfo[6] -= amount
    db.update_customer(customerInfo[6], customerInfo[4])
    print("Yeni Bakiyeniz: ", customerInfo[6])