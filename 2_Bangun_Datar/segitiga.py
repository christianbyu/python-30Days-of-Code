import math

print("+===========================+")
print("| Program Luas dan Keliling |")
print("|         Segitiga          |")
print("|         By Sibaay         |")
print("+===========================+")

InputAlas = int(input("Masukan Alas Sisi (Cm) : "))
InputTinggi = int(input("Masukan Tinggi Sisi (Cm) : "))

SisiMiring = math.sqrt(InputAlas ** 2 + InputTinggi ** 2)

Luas = InputAlas * InputTinggi /2
Keliling = InputAlas + InputTinggi + SisiMiring

print("Sisi Miring : ", SisiMiring)
print("Luas Segitiga adalah : ", Luas)
print("Keliling Segitiga adalah :", Keliling)
