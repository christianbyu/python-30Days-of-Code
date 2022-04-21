Menu = int(input("Masukan Pilihan (1-4) : "))

if Menu == 1:
    Volt = int(input("Masukan Tegangan   : "))
    Amp = float(input("Masukan Kuat Arus  : "))
    Time = int(input("Masukan Waktu      : "))

    Joule = Volt * Amp * Time

    print("Energi Listrik     :", Joule,  (" Joule"))
else:
    print("Error")