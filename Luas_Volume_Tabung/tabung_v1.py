import math

print("+===================+")
print("|      Tabung       |")
print("+===================+")
print("| 1. Luas           |")
print("| 2. Keliling       |")
print("+===================+")

Menu = int(input("Pilih 1/2 : "))

if Menu == 1:
    r = float(input("Masukan Jari - jari  : "))
    t = int(input("Masukan Tinggi     : "))

    Luas = math.sqrt(2 * r) * (t * r)

    print("Luas Tabung :", Luas)
else:
    r = float(input("Masukan Jari - jari  : "))
    t = int(input("Masukan Tinggi     : "))

    Volume = math.sqrt(r * r * t)

    print("Volume Tabung :", Volume)