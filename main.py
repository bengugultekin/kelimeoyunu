import pandas as pd
from random import randint



data = pd.read_csv('sorular.csv', sep=';')
puan = 0
cevap = "_"


def liste_olustur(liste, sınır):
    sınır = list(sınır)
    liste = list(liste)
    for i in range(0, len(sınır) - 1):
        liste.append("_")
    return liste


def listetemizle(liste):
    for i in range(0, len(liste)):
        liste[i] = "_"


def bul(girdi, hedef):
    hedef = list(hedef)
    for i in range(0, len(hedef)):
        if (hedef[i] == girdi):
            return True


"""
def kontrolet(hedef):
    hedef = list(hedef)
    for i in range (0,hedef):
        if hedef[i]=="_":
           return False
    return True 
"""


def degistir(girdi, hedef):
    hedef = list(hedef)
    for i in range(0, len(hedef)):
        if hedef[i] == girdi:
            hedef[i] = girdi


def sayi_uret(random):
    ayni = True
    while ayni:
        new_random = randint(0, 9)
        ayni = random == new_random
    return new_random

    kontrol = 0


for i in range(1, 8):
    sorular = data.loc[data['level'] == i]
    random = -1
    for j in range(2):
        random = sayi_uret(random)
        soru = sorular.iloc[random]['soru']
        kelime = sorular.iloc[random]['kelime']
        harf = sorular.iloc[random]['harf']
        print(soru)
        # print(str(kelime))

        for i in range(harf):
            print(' _ ', end='')

        # print(kelime)

        kelime = list(kelime)
        # - işeretlerini bir listeye koyup bilinene kelimeleri eşelştigi şekilde - sembolunun uzerine override edicek
        # - işaretlerini override etmesi için ayrı bir fonksyon cıkar
        cevap = liste_olustur(cevap, kelime)
        kontrol = 0
        while kontrol < 1:
            tahmin = input()
            sonuc = bul(tahmin, kelime)
            if sonuc == True:
                for k in range(0, len(kelime)):
                    if kelime[k] == tahmin:
                        cevap[k] = tahmin
                print("tahmininiz kelimede var \n")
                puan = puan + 100
            else:
                print("Yanlış girdiniz")
                if cevap == kelime:
                    kontrol = kontrol + 1
                    listetemizle(cevap)

                """
                if len(kelime) == len(cevap): # bu olmazsa len lerinin eşitligi uzerinden hareket et zaten sadece dogruları atıyosun cevapların içine
                    kontrol = kontrol +1
                    print("Kelimenin tamamını buldunuz %d \n",puan)
                """
            print(soru)
            # print(str(kelime))
            print(cevap)
            continue

        # if tahmin == kelime:
        #  print("tebrikler")
        #  puan = puan + harf * 100
        #   print(puan)

        print(tahmin)
