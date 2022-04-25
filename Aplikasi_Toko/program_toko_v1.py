print("+==============================+")
print("|    Program Toko Sederhana    |")
print("+==============================+")
print("|  Nama Barang   |     Harga    |")
print("+===============================+")
print("| 1. Kaos        | Rp. 100.000  |")
print("| 2. Celana      | Rp. 100.000  |")
print("| 3. Tas         | Rp. 150.000  |")
print("| 4. Kemeja      | Rp. 250.000  |")
print("| 5. Sepatu      | Rp. 200.000  |")
print("+===============================+")

NamaBarang = int(input("Pilih Barang yang akan dibeli (1-10) : "))

if NamaBarang == 1:
    Harga = 100000
elif NamaBarang == 2:
    Harga = 100000
elif NamaBarang == 3:
    Harga = 150000
elif NamaBarang == 4:
    Harga = 250000
elif NamaBarang == 5:
    Harga = 200000   
else :
    print("Mohon Maaf, Barang yang Anda cari tidak Ditemukan !!")

Jumlah = int(input("Masukan Jumlah Barang : "))
JumlahBarang = Harga*Jumlah

print("Total Belanja : Rp.", JumlahBarang)