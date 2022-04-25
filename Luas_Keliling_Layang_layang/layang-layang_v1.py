print("+===================+")
print("|  Layang - layang  |")
print("+===================+")
print("| 1. Luas           |")
print("| 2. Keliling       |")
print("+===================+")

Menu = int(input("Pilih 1/2 : "))

if Menu == 1:
    d1 = int(input("Masukan Diagonal 1   : "))
    d2 = int(input("Masukan Diagonal 2   : "))

    Luas = (d1 * d2) / 2

    print("Luas Layang - layang :", Luas)
else:
    a = int(input("Masukan Sisi Pendek    : "))
    b = int(input("Masukan Sisi Panjang   : "))

    Keliling = (a * 2) + (b * 2)

    print("Keliling Layang - layang :", Keliling)