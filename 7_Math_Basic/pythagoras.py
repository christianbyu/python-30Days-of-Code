import math

print("+==========================+")
print("| Program Rumus Pythagoras |")
print("|         By Sibaay        |")
print("+==========================+")
print("|        +                 |")
print("|        | +               |")
print("|      A |   +  C          |")
print("|        |     +           |")
print("|        |_______+         |")
print("|           B              |")
print("+==========================+")

print("Apa yang akan kamu cari?")
print("1. Nilai A")
print("2. Nilai B")
print("3. Nilai C")
pilih = int(input("Masukan Pilihan (1/2/3) : "))

if pilih == 1:
    b = int(input("Masukan nilai B : "))
    c = int(input("Masukan nilai C : "))

    a = math.sqrt(c ** 2 - b ** 2)

    print("Nilai A : ", a)
elif pilih == 2:
    a = int(input("Masukan nilai A : "))
    c = int(input("Masukan nilai C : "))

    b = math.sqrt(c ** 2 - a ** 2)

    print("Nilai B : ", b)
elif pilih == 3:
    a = int(input("Masukan nilai A : "))
    b = int(input("Masukan nilai B : "))

    c = math.sqrt(a ** 2 + b ** 2)

    print("Nilai C : ", c)
else :
    print("Masukan Error!!")
