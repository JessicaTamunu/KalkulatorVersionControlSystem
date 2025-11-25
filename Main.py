def tambah(a, b):
    return a + b

print("=== KALKULATOR KELOMPOK ===")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

pilihan = input("Pilih operasi (1/2/3/4): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == "1":
    print("Hasil:", tambah(angka1, angka2))
