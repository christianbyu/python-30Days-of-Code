from subprocess import call

Menu = int(input("Masukan Pilihan 1/2/3/4 : "))

if Menu == 1:
    call("./upd.sh", shell=True)
elif Menu == 2:
    call("./upg.sh", shell=True)
elif Menu == 3:
    call("./update.sh", shell=True)
elif Menu == 4:
    call("./remove.sh", shell=True)
else:
    print("Error")

