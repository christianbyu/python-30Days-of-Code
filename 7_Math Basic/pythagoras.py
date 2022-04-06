from calendar import c
import math

from pyrsistent import b

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
    print(a) 
elif pilih == 2:
    print(b)
elif pilih == 3:
    print(c)
else :
    print("Masukan Error!!")

def fungsi_a(b, c, a):
    b = int(input("Masukan nilai B : "))
    c = int(input("Masukan nilai C : "))

    a = math.sqrt(c ** 2 - b ** 2)

    print("Nilai A : ", a)

def fungsi_b(a, c, b):
    a = int(input("Masukan nilai A : "))
    c = int(input("Masukan nilai B : "))

    b = math.sqrt(c ** 2 - a ** 2)

    print("Nilai B : ", b)

def fungsi_c(a, b, c):
    a = int(input("Masukan nilai A : "))
    b = int(input("Masukan nilai B : "))

    c = math.sqrt(a ** 2 + b ** 2)

    print(" Nilai C : ", c)