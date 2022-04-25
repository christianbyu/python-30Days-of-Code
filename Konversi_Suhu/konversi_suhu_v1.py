print("+===================+")
print("|   Konversi Suhu   |")
print("+===================+")
print("|         _         |")
print("|        | |        |")
print("|       (   )       |")
print("|      (     )      |")
print("|     (       )     |")
print("|    (_ _ _ _ _)    |")
print("|                   |")
print("+===================+")

Menu = int(input("Pilih Konversi C/R/F/K (1 - 4) : "))

if Menu == 1:
    InputCelcius = int(input("Masukan nilai Celcius : "))
    NilaiReamour = (4 / 5) * InputCelcius
    NilaiFarenheit = (9 / 5) * InputCelcius + 32
    NilaiKelvin = InputCelcius + 273

    print("Nilai pada Reamour   : ", NilaiReamour, "R")
    print("Nilai pada Farenheit : ", NilaiFarenheit, "F")
    print("Nilai pada Kelvin    : ",NilaiKelvin, "K")
elif Menu == 2:
    InputReamour = int(input("Masukan nilai Reamour : "))
    NilaiCelcius = (5 / 4) * InputReamour
    NilaiFarenheit = (9 / 4) * InputReamour + 32
    NilaiKelvin = ( 5 / 4) * InputReamour + 273

    print("Nilai pada Celcius   : ", NilaiCelcius, "C")
    print("Nilai pada Farenheit : ", NilaiFarenheit, "F")
    print("Nilai pada Kelvin    : ",NilaiKelvin, "K")
elif Menu == 3:
    InputFarenheit = int(input("Masukan nilai Farenheit : "))
    NilaiCelcius = (5 / 9) * (InputFarenheit - 32)
    NilaiReamour= (4 / 9) * (InputFarenheit - 32)

    print("Nilai pada Celcius   : ", NilaiCelcius, "C")
    print("Nilai pada Farenheit : ", NilaiReamour, "R")
elif Menu == 4:
    InputKelvin = int(input("Masukan nilai Farenheit : "))
    NilaiCelcius = InputKelvin - 273
    NilaiReamour= (4 / 5) * (InputKelvin - 273)

    print("Nilai pada Celcius   : ", NilaiCelcius, "C")
    print("Nilai pada Farenheit : ", NilaiReamour, "R")
else:
    print("Masukan Salah!!")