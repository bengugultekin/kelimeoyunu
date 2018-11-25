import pandas as pd
from random import randint

data = pd.read_csv('sorular.csv', sep=';')
puan = 0


def sayi_uret(random):
    ayni = True
    while ayni:
        new_random = randint(0, 9)
        ayni = random == new_random
    return new_random


for i in range(1, 8):
    sorular = data.loc[data['level'] == i]
    random = -1
    for j in range(2):
        random = sayi_uret(random)
        soru = sorular.iloc[random]['soru']
        kelime = sorular.iloc[random]['kelime']
        harf = sorular.iloc[random]['harf']
        print(soru)
        print(kelime)

        for i in range(harf):
            print(' _ ', end='')

        print(kelime)
        tahmin = input()

        if tahmin == kelime:
            print("tebrikler")
            puan = puan + harf * 100
            print(puan)

        print(tahmin)
