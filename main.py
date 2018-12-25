import pandas as pd
import os
from random import randint



data = pd.read_csv('sorular.csv', sep=';')
puan = 0
cevap = "_"
"""
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
"""
	

def liste_olustur(liste, sınır):
    sınır = list(sınır)
    liste = list()
    for i in range(0, len(sınır)):
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
kullanıcı1adı = "bengu"
kullanıcı2adı = "furkan"
kullanıcı1puan = 0
kullanıcı2puan = 0
for a in range(0,2):
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
                print("\n Soruyu pas geçmek için * tuşuna basınız.")
                tahmin = input("\n Bir harf tahmin ediniz :")

                if tahmin == "*":
                    cevap = kelime

                sonuc = bul(tahmin, kelime)


                if sonuc == True:
                    for k in range(0, len(kelime)):
                        if kelime[k] == tahmin:
                            cevap[k] = tahmin
                    print("tahmininiz kelimede var \n")
                    puan = puan + 100
                    print(puan)
                    print(cevap)
                    if cevap == kelime:

                        kontrol = kontrol + 1
                        listetemizle(cevap)

                else:
                    print("Yanlış girdiniz")
                    puan = puan - 100
                    print(puan)
                    print(cevap)
                    if cevap == kelime:

                        kontrol = kontrol + 1
                        listetemizle(cevap)



                    """
                    if len(kelime) == len(cevap): # bu olmazsa len lerinin eşitligi uzerinden hareket et zaten sadece dogruları atıyosun cevapların içine
                        kontrol = kontrol +1
                        print("Kelimenin tamamını buldunuz %d \n",puan)
                    """
               # print(soru)
                # print(str(kelime))

                #cls()
            # if tahmin == kelime:
            #  print("tebrikler")
            #  puan = puan + harf * 100
            #   print(puan)
			
            print(tahmin)
    if a == 0:
        print("1.OyuncuKullanıcıAdıGiriniz")
        kullanıcı1adı = input("ad")
        kullanıcı1puan = puan
        puan = 0
    if a == 1:
        print("2.OyuncuKullanıcıAdıGiriniz")
        kullanıcı2adı = input("ad")
        kullanıcı2puan = puan
        puan = 0
scores = []
scores.append(kullanıcı1puan)
scores.append(kullanıcı2puan)
if scores[0] > scores[1]:
	print(kullanıcı1adı)
	print("kazandı\n")
	print(scores[0])
else:
	print(kullanıcı2adı)
	print("kazandı\n")
	print(scores[1])
