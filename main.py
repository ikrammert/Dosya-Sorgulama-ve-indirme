import os
import urllib.request

FileName =input("Dosyanin Tam Adini Giriniz:    ")

if not os.path.exists(FileName):
    download_link = input("İndirmek İstediğiniz Dosyanin linkini Giriniz:   ")
    print("Dosya mevcut değil.")
    urllib.request.urlretrieve(download_link, FileName)
    print("Dosya indirildi.")
else:
    print("Dosya mevcut.")

