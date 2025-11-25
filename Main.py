def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol!"
    return a / b

# integrasi ke menu
if pilihan == "3":
    print("Hasil:", kali(angka1, angka2))

elif pilihan == "4":
    print("Hasil:", bagi(angka1, angka2))
