print("+=====================================+")
print("|      Program Perhitungan Skala      |")
print("|                By Sibaay            |")
print("+=====================================+")
print("| 1. Jarak Peta        |       Jp     |")
print("| 2. Jarak Sebenarnya  |       Js     |")
print("| 3. Skala             |      1 : xx  |")
print("+=====================================+")

InputMenu = int(input("Apa yang mau kamu cari ? (1 -3) : "))

if InputMenu == 1:
    Skala = int(input("Masukan Skala : 1 : "))
    Jsb = int(input("Masukan Jarak Sebenarnya (Km) : "))

    Jp = (Skala * Jsb) / 100000

    print("Jarak pada Peta (Cm) : ", Jp, " Cm")
elif InputMenu == 2:
    Jsb = int(input("Masukan Jarak Sebenarnya (Km) : "))
    Jp = int(input("Masukan Jarak pada Peta (Cm) : "))

    Skala = (Jp / Jsb) * 100000

    print("Skala : ", "1 : ", Skala)
elif InputMenu == 3:
    Jp = int(input("Masukan Jarak pada Peta (Cm) : "))
    Skala = int(input("Masukan Skala : 1 : "))

    Jsb = Jp / Skala

    print("Jarak Sebenarnya : ", Jsb ," Km")
else:
    print("Error")

list_array = [
    ["Ayam", "Kebo", "Chicken"],
    ["Aku", "Kamu", "Dia"],
    ["Kopi", "Makan", "Minum"],
    ]
x = print("Kopi")
x = print(list_array[2][1])