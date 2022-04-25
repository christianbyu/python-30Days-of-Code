print("+===================+")
print("|     Trapesium     |")
print("+===================+")
print("| 1. Luas           |")
print("| 2. Keliling       |")
print("+===================+")

Menu = int(input("Pilih 1/2 : "))

if Menu == 1:
    a = int(input("Masukan Sisi Bawah : "))
    b = int(input("Masukan Sisi Atas  : "))
    t = int(input("Masukan Tinggi     : "))

    Luas = ((a + b) / 2) * t

    print("Luas Trapesium :", Luas)
else:
    a = int(input("Masukan Sisi Bawah  : "))
    b = int(input("Masukan Sisi Atas   : "))
    c = int(input("Masukan Sisi Miring : "))

    Keliling = a + b + (c * 2)

    print("Keliling Trapesium :", Keliling)