import os
import time
import random

uang = 100000
admin = (random.getrandbits(8))
menu = {
    "Silverking":13000,
    "Chotato":9000,
    "Agua":4000,
    "Bubble gum":3500,
    "Yals":5000,
    "Magnum":5500
}
print("Uang Kamu Ada 100.000")
print("====== Daftar Menu Warteg Sukamaju ======")
for i in menu:
    print("Daftar Menu : ", i,"\t Harga : ",menu[i])
print("Pembelian di atas Rp75.000,- Mendapatkan Diskon 15%")
print("========================================")
beli = input("Pilih Menu : ")
jumlah = int(input("jumlah Pesanan : "))
bayar = jumlah * menu[beli] + admin

if bayar > 75000:
    diskon = bayar*15/75
    total = bayar - diskon + admin
else:
    total = bayar + admin
    uang = uang - total - admin
if total < uang:
    uang = uang - total - admin
print("=========== Struk Pembayaran ===========")
print("Menu yang di beli        : ",beli)
print("Jumlah yang di pesan     : ",jumlah)
print("Biaya Admin              :",admin)
print("Total biaya              : ",bayar)
print("Total yang harus dibayar : ",total)
print("========================================")
print("Uang kamu tersisa : ",uang)
print("====== TERIMASIH SUDAH BERBELANJA ======")
if total > uang:
    os.system('cls')
    time.sleep(2)
    print("Kamu gagal membeli karena uangmu kurang!!")