#SOAL 1
print("========== PILIH MENU ==========")
print("Operasi Matematika")
print("1. jumlah     [+]")
print("2. Kurang     [-]")
print("3. Kali       [*]")
print("4. Bagi       [/]")
print("================================")
#RUMUS
opsi = int(input("Pilihan Operasi (1/2/3/4) : "))
print ("===============================")
Bil1 = int(input("Masukkan Bilang Pertama : "))
Bil2 = int(input("Masukkan Bilang Kedua : "))
def jumlah(opsi,Bil1,Bil2):
    hasil = Bil1+Bil2
    return hasil
def kurang(opsi,Bil1,Bil2):
    hasil = Bil1-Bil2
    return hasil
def kali(opsi,Bil1,Bil2):
   hasil = Bil1*Bil2
   return hasil
def bagi(opsi,Bil1,Bil2):
   hasil = Bil1/Bil2
   return hasil

if opsi == 1:
   hasil = Bil1+Bil2
elif opsi == 2:
   hasil = Bil1-Bil2
elif opsi == 3:
   hasil = Bil1*Bil2
elif opsi == 4:
   hasil = Bil1/Bil2

print("Hasil : %d" %hasil)
