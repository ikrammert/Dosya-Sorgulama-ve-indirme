import os
import urllib.request

FileName =input("Dosyanin Tam Adini Giriniz:    ")

if not os.path.exists(FileName):
    print("Dosya mevcut değil.")
    download_link = input("İndirmek İstediğiniz Dosyanin linkini Giriniz:   ")
    urllib.request.urlretrieve(download_link)
    print("Dosya indiriliyor...")
    print("Dosya indirildi.")
else:
    print("Dosya mevcut.")

