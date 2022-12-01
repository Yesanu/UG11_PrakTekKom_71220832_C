#Soal 2
print ("Pemeriksa Kelipatan 9")
Kelipatan = int(input("Masukkan kelipatan 9 yang ingin diperiksa : "))
#Rumus
def kelipatan_9():
    if Kelipatan % 9==0 :
        print ("Benar")
    else :
        print ("Salah")

kelipatan_9()
