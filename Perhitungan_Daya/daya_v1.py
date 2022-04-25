print("+=====================================+")
print("|      Program Perhitungan Daya       |")
print("|              By Sibaay              |")
print("+=====================================+")
print("| 1. Daya (Power)      |      Watt    |")
print("| 2. Usaha (Weight)    |     Joule    |")
print("| 3. Waktu (Time)      |      Sec     |")
print("+=====================================+")

Menu = int(input("Masukan Pilihan (1-3) : "))

if Menu == 1:
    Weight = int(input("Masukan Weight  : "))
    Waktu = int(input("Masukan Waktu   : "))

    Pow = Weight / Waktu

    print("Jumlah Daya :", Pow, " Watt")
elif Menu == 2:
    Pow = int(input("Masukan Power   : "))
    Waktu = int(input("Masukan Waktu  : "))

    Weight = Pow * Waktu

    print("Total Usaha     :", Weight, " Joule")
elif Menu == 3:
    Weight = int(input("Masukan Weight : "))
    Pow = int(input("Masukan Power  : "))

    Waktu = Weight * Pow 

    print("Total Waktu    :", Waktu, " Sec")
else:
    print("Error!!!")