#type data number
#ada tiga yaitu Integer,Float,complex number


x = 20
y =  10
z = 5

# Operasi aritmatika dengan integer
penjumlahan = x + y
print(penjumlahan)  

# Perkalian
perkalian = x * z
print(perkalian)  

# Pembagian bulat
pembagian_bulat = x // y
print(pembagian_bulat)  

# Menggunakan integer dalam loop
for i in range(5):
    print(i)  

# tipe data float
a = 20.5
b = 10.5
c = 1.2 

# Operasi aritmatika dengan float
hasil = a + b  
print(hasil)  
# Penggunaan float dalam fungsi matematika
import math
sqrt_value = math.sqrt(a)  # Akar kuadrat dari a
print(sqrt_value)  

#tipe data bilangan kompleks
a1 = 9 + 15j
b2 = 8 - 12j

# Menampilkan bagian real dan imajiner
print("Bagian real a1:", a1.real)  
print("Bagian imajiner a1:", a1.imag) 

# Operasi aritmatika pada bilangan kompleks
penjumlahan = a1 + b2 
print("Hasil penjumlahan:", penjumlahan)

perkalian = a1 * b2  
print("Hasil perkalian:", perkalian)

# Fungsi bilangan kompleks
konjugasi = a1.conjugate() 
print("Konjugat a1:", konjugasi)


