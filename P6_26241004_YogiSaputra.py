# Tugas Pertemuan 6 - Operator Logika NOT, AND, OR, dan XOR
# Nama: Yogi Saputra
# NIM: 26241004
# KELAS: 1/A
# MatKul: Pemrograman Dasar

a = int(input("Digit A: "))
b = int(input("Digit B: "))

kondisi1 = a >= 0
kondisi2 = b >= 4

print("Kondisi 1:", kondisi1)
print("Kondisi 2:", kondisi2)

print("NOT:", not kondisi1)
print("AND:", kondisi1 and kondisi2)
print("OR :", kondisi1 or kondisi2)
print("XOR:", kondisi1 ^ kondisi2)