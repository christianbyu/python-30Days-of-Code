print("+=================================+")
print("|    Program Menghitung Nilai     |")
print("+=================================+")
print("|           by Sibaay             |")
print("+=================================+")


NilaiPertama = int(input("Masukan Nilai 1 : "))
NilaiKedua = int(input("Masukan Nilai 2 : "))
RataRata = int(input("Masukan Rata - rata : "))

Final = (NilaiPertama + NilaiKedua)/2

if Final >= RataRata:
    print("Kamu Lulus!!")
elif Final <= RataRata:
    print("Kamu Remidi !!")
  
