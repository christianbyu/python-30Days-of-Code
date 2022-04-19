from unicodedata import decimal


biner = int(input("Masukan Biner : "))
dec = decimal(biner)
oct = oct(dec)
print("Konversi ke Octal : ", oct)