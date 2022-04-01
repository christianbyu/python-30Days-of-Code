import math

print("======================================")
print("| Program Luas dan Keliling Lingkaran|")
print("|             By Sibaay              |")
print("======================================")

# Input data panjang dan lebar
r = float(input("Masukan jari-jari: "))

# Fungsi perhitungan luas dan keliling
luas = math.pi*(r*r)
keliling = 2*math.pi*r

# Mencetak nilai luas dan keliling
print("Luas :", luas)
print("Keliling:", keliling)