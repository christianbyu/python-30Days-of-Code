print("+=====================================+")
print("|    Program Perhitungan Kecepatan    |")
print("|              By Sibaay              |")
print("+=====================================+")
print("| 1. Kecepatan         |     m/sec    |")
print("| 2. Jarak             |       m      |")
print("| 3. Waktu             |      sec     |")
print("| 4. Rata - rata Kec   |     m/sec    |")
print("+=====================================+")

Menu = int(input("Apa yang mau kamu hitung ? Pilih (1-4) : "))

if Menu == 1 :
    print("Menghitung Kecepatan/Kelajuan . . .")

    Jarak = int(input("Masukan Jarak (M)   : "))
    Waktu = int(input("Masukan Waktu (Min) : "))

    Kecepatan = Jarak / (Waktu/60)

    print("Kecepatan : ", Kecepatan, "m/sec")
elif Menu == 2 :
    print("Menghitung Jarak . . .")

    Kecepatan = int(input("Masukan Kelajuan (m/sec)  : "))
    Waktu = int(input("Masukan Waktu (Min) : "))

    Jarak = Kecepatan * (Waktu/60)

    print("Kecepatan : ", Jarak, "m")
elif Menu == 3 :
    print("Menghitung Waktu . . .")

    Kecepatan = int(input("Masukan Kelajuan (m/sec)  : "))
    Jarak = int(input("Masukan Jarak (M)   : "))

    Waktu = Jarak / (Kecepatan/60)

    print("Kecepatan : ", Waktu, "Sec")
elif Menu == 4 :
    print("Menghitung Rata - rata Kecepatan . . .")

    Jarak1 = int(input("Masukan Jarak 1 (M)   : "))
    Jarak2 = int(input("Masukan Jarak 2 (M)   : "))

    Waktu1 = int(input("Masukan Waktu 1 (Min) : "))
    Waktu2 = int(input("Masukan Waktu 2 (Min) : "))
    
    RrJarak = (Jarak1 + Jarak2) / 2
    RrWaktu = (Waktu1 + Waktu2) / 2

    RrKec = RrJarak / (RrWaktu/60)

    print("Rata - Rata Kecepatan : ", RrKec, "m/sec")  
else:
    print("Error")
