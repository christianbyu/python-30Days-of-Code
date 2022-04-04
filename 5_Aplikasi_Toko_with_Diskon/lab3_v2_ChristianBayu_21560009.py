print("=================================")
print("|    Pricelist Ubay Computer    |")
print("=================================")
print("|  Nama Barang   |     Harga    |")
print("=================================")
print("| 1. Motherboard | Rp. 1.000.000|")
print("| 2. CPU         | Rp. 1.000.000|")
print("| 3. VGA         | Rp. 3.000.000|")
print("| 4. RAM         | Rp. 800.000  |")
print("| 5. Storage     | Rp. 500.000  |")
print("| 6. PSU         | Rp. 500.000  |")
print("| 7. Cooler      | Rp. 150.000  |")
print("| 8. Fan         | Rp. 100.000  |")
print("| 9. Case        | Rp. 500.000  |")
print("| 10. Monitor    | Rp. 1.000.000|")
print("=================================")

NamaBarang = int(input("Pilih Barang yang akan dibeli (1-10) : "))

if NamaBarang == 1:
    Harga = 1000000
elif NamaBarang == 2:
    Harga = 1000000
elif NamaBarang == 3:
    Harga = 3000000
elif NamaBarang == 4:
    Harga = 800000
elif NamaBarang == 5:
    Harga = 500000
elif NamaBarang == 6:
    Harga = 500000
elif NamaBarang == 7:
    Harga = 150000
elif NamaBarang == 8:
    Harga = 100000
elif NamaBarang == 9:
    Harga = 5000000
elif NamaBarang == 10:
    Harga = 1000000   
else :
    print("Mohon Maaf, Barang yang Anda cari tidak Ditemukan !!")

Jumlah = int(input("Masukan Jumlah Barang : "))
JumlahBarang = Harga*Jumlah

Diskon = int(input("Masukan Jumlah Diskon: "))
TotalDiskon = JumlahBarang * Diskon/100
TotalHarga = JumlahBarang - TotalDiskon

print("Total Belanja : Rp.", TotalHarga)