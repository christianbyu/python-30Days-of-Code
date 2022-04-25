print("+=====================================+")
print("|         Program Perhitungan         |")
print("|         Debit, Vol dan Waktu        |")
print("|              By Sibaay              |")
print("+=====================================+")
print("| 1. Volume            |     L/Dm3    |")
print("| 2. Jarak             |     L/Jam    |")
print("| 3. Waktu             |      Jam     |")
print("+=====================================+")

Menu = int(input("Masukan Pilihan (1-3) : "))

if Menu == 1:
    Debit = int(input("Masukan Debit : "))
    Waktu = int(input("Masukan Waktu : "))

    Vol = Debit * Waktu

    print("Jumlah Volume :", Vol, " L/Dm3")
elif Menu == 2:
    Waktu = int(input("Masukan Waktu : "))
    Vol = int(input("Masukan Volume  : "))

    Debit = Vol / Waktu
    
    print("Jumlah Debit :", Debit, "L/Jam")
elif Menu == 3:
    Vol = int(input("Masukan Volume  : "))
    Debit = int(input("Masukan Debit : "))

    Waktu = Vol / Debit
    
    print("Lama Waktu :", Waktu, " Jam")
else:
    print("Error!!!")