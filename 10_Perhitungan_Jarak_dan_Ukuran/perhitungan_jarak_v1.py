print("+============================+")
print("| Program Perhitungan Jarak  |")
print("|           By Sibaay        |")
print("+============================+")
print("| 1. Milimeter   |     Mm    |")
print("| 2. Centimeter  |     Cm    |")
print("| 3. Decimeter   |     Dm    |")
print("| 4. Meter       |     m     |")
print("| 5. Dekameter   |     Dam   |")
print("| 6. Hektometer  |     hm    |")
print("| 7. Kilometer   |     Km    |")
print("+==============================+")

Menu = int(input("Masukan Pilihan (1-7) : "))

if Menu == 1:
    IntMm = int(input("Masukan nilai Mm (Milimeter) : "))
    NilaiCm = IntMm * 10
    NilaiDm = IntMm * 100
    NilaiM = IntMm * 1000
    NilaiDam = IntMm * 10000
    Nilaihm = IntMm * 100000
    NilaiKm = IntMm * 1000000

    print("Nilai dalam Cm  : ", NilaiCm, "Cm")
    print("Nilai dalam Dm  : ", NilaiDm, "Dm")
    print("Nilai dalam M   : ", NilaiM, "M")
    print("Nilai dalam Dam : ", NilaiDam, "Dam")
    print("Nilai dalam Hm  : ", Nilaihm, "Hm")
    print("Nilai dalam Km  : ", NilaiKm, "Km")

elif Menu == 2:
    IntCm = int(input("Masukan nilai Cm (Centimeter) : "))
    NilaiMm = IntCm / 10
    NilaiDm = IntCm * 10
    NilaiM = IntCm * 100
    NilaiDam = IntCm * 1000
    NilaiHm = IntCm * 10000
    NilaiKm = IntCm * 100000

    print("Nilai dalam Mm  : ", NilaiMm, "Mm")
    print("Nilai dalam Dm  : ", NilaiDm, "Dm")
    print("Nilai dalam M   : ", NilaiM, "M")
    print("Nilai dalam Dam : ", NilaiDam, "Dam")
    print("Nilai dalam hm  : ", NilaiHm, "Hm")
    print("Nilai dalam Km  : ", NilaiKm, "Km")
elif Menu == 3:
    IntDm = int(input("Masukan nilai Dm (Desimeter) : "))
    NilaiMm = IntDm / 100
    NilaiCm = IntDm / 10
    NilaiM = IntDm * 10
    NilaiDam = IntDm * 100
    Nilaihm = IntDm * 1000
    NilaiKm = IntDm * 10000

    print("Nilai dalam Mm  : ", NilaiMm, "Mm")
    print("Nilai dalam Cm  : ", NilaiCm, "Cm")
    print("Nilai dalam M   : ", NilaiM, "M")
    print("Nilai dalam Dam : ", NilaiDam, "Dam")
    print("Nilai dalam Hm  : ", Nilaihm, "Hm")
    print("Nilai dalam Km  : ", NilaiKm, "Km")
elif Menu == 4:
    IntM = int(input("Masukan nilai M (Meter) : "))
    NilaiMm = IntM / 1000
    NilaiCm = IntM / 100
    NilaiDm = IntM / 10
    NilaiDam = IntM * 10
    Nilaihm = IntM * 100
    NilaiKm = IntM * 1000

    print("Nilai dalam Mm  : ", NilaiMm, "Mm")
    print("Nilai dalam Cm  : ", NilaiCm, "Cm")
    print("Nilai dalam Dm   : ", NilaiDm, "M")
    print("Nilai dalam Dam : ", NilaiDam, "Dam")
    print("Nilai dalam Hm  : ", Nilaihm, "Hm")
    print("Nilai dalam Km  : ", NilaiKm, "Km")
elif Menu == 5:
    IntDam = int(input("Masukan nilai Dam (Dekameter) : "))
    NilaiMm = IntDam / 10000
    NilaiCm = IntDam / 1000
    NilaiDm = IntDam / 100
    NilaiM = IntDam / 10
    NilaiHm = IntDam * 10
    NilaiKm = IntDam * 100

    print("Nilai dalam Mm  : ", NilaiMm, "Mm")
    print("Nilai dalam Cm  : ", NilaiCm, "Cm")
    print("Nilai dalam Dm  : ", NilaiDm, "Dm")
    print("Nilai dalam M   : ", NilaiM, "M")
    print("Nilai dalam Hm  : ", NilaiHm, "Hm")
    print("Nilai dalam Kms  : ", NilaiKm, "Km")
elif Menu == 6:
    IntHm = int(input("Masukan nilai Hm (Hektometer) : "))
    NilaiMm = IntHm / 1000000
    NilaiCm = IntHm / 10000
    NilaiDm = IntHm / 1000
    NilaiM = IntHm / 100
    NilaiDam = IntHm / 10
    NilaiKm = IntHm * 10

    print("Nilai dalam Mm  : ", NilaiMm, "Mm")
    print("Nilai dalam Cm  : ", NilaiCm, "Cm")
    print("Nilai dalam Dm  : ", NilaiDm, "Dm")
    print("Nilai dalam M   : ", NilaiM, "M")
    print("Nilai dalam Dam : ", NilaiDam, "Dam")
    print("Nilai dalam Km  : ", NilaiKm, "Km")
elif Menu == 7:
    IntKm = int(input("Masukan nilai Km (Kilometer) : "))
    NilaiMm = IntKm / 1000000
    NilaiCm = IntKm / 100000
    NilaiDm = IntKm / 10000
    NilaiM = IntKm / 1000
    NilaiDam = IntKm / 100
    NilaiHm = IntKm / 10

    print("Nilai dalam Mm  : ", NilaiMm, "Mm")
    print("Nilai dalam Cm  : ", NilaiCm, "Cm")
    print("Nilai dalam Dm  : ", NilaiDm, "Dm")
    print("Nilai dalam M   : ", NilaiM, "M")
    print("Nilai dalam Dam : ", NilaiDam, "Hm")
    print("Nilai dalam Hm  : ", NilaiHm, "Hm")
else:
    print("Error")
    
