import math

print("=======================")
print("| Program Luas Kerucut|")
print("|       By Sibaay     |")
print("========================")

# Input data panjang dan lebar
r = float(input("Masukan jari-Jari: "))
t = float(input("Masukan Tinggi: "))

# Fungsi perhitungan luas dan keliling
pelukis = math.sqrt((r*r)+(t*t)) #Pencarian nilai pelukis (garis pelukis)

luas = math.pi*r*(pelukis+r) # Perhitungan luas kerucut

# Mencetak nilai luas dan keliling
print("Garis Pelukis :", pelukis)
print("Luas :", luas)
