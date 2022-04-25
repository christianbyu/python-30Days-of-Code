print("+===================+")
print("|       Prisma      |")
print("+===================+")
print("| 1. Luas           |")
print("| 2. Keliling       |")
print("+===================+")

Menu = int(input("Pilih 1/2 : "))

if Menu == 1:
    la = int(input("Masukan Luas Alas  : "))
    ka = int(input("Masukan Keliling Alas  : "))
    t = int(input("Masukan Tinggi     : "))

    Luas = (2 * la) + (ka * t)

    print("Luas Prisma :", Luas)
else:
    la = int(input("Masukan Luas Alas  : "))
    t = int(input("Masukan Tinggi   : "))

    Volume = la * t

    print("Volume Prisma :", Volume)