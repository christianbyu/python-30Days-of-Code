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

varNamaBarang = int(input("Pilih Barang yang akan dibeli (1-10) : "))

if varNamaBarang == 1:
    varHargaSatuan = 1000000
elif varNamaBarang == 2:
    varHargaSatuan = 1000000
elif varNamaBarang == 3:
    varHargaSatuan = 3000000
elif varNamaBarang == 4:
    varHargaSatuan = 800000
elif varNamaBarang == 5:
    varHargaSatuan = 500000
elif varNamaBarang == 6:
    varHargaSatuan = 500000
elif varNamaBarang == 7:
    varHargaSatuan = 150000
elif varNamaBarang == 8:
    varHargaSatuan = 100000
elif varNamaBarang == 9:
    varHargaSatuan = 5000000
elif varNamaBarang == 10:
    varHargaSatuan = 1000000   
else :
    print("Mohon Maaf, Barang yang Anda cari tidak Ditemukan !!")

varJumlah = int(input("Masukan Jumlah Barang : "))
varJumlahBarang = varHargaSatuan*varJumlah

Diskon = int(input("Masukan Jumlah Diskon: "))
varTotalDiskon = varJumlahBarang * Diskon/100
varTotalHarga = varJumlahBarang - varTotalDiskon

print("Total Belanja : Rp.", varTotalHarga)