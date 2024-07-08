'''
1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı şeklinde bulmaya çalışın
** hak = 5
**100 üzerinden puanlayarak her soru 20 puan
**hak bilgisi kullanıcıdan alınsın her soru belirtilen can sayısı üzerinden hesaplansın
'''

import random
sayi = random.randint(1,100)
hak = 5
puan = 100

while hak > 0:
    hak -= 1
    tahmin = int(input('Tahmininiz: '))

    if tahmin == sayi:
        print('TEBRİKLER BİLDİNİZ :)')
        print(f'Puanınız: {puan}')
        break

    elif tahmin > sayi:
        print('Sayıyı azaltınız.')
        puan = puan - 20
        

    else:
        print('Sayıyı artırınız.')
        puan = puan - 20

    if hak == 0:
        print(f'Hakkınız bitti. Seçilen sayı : {sayi} Puanınız: 0')



