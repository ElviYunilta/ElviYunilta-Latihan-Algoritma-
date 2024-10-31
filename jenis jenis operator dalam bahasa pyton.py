# Operator Aritmatika
a = 20
b = 10

# Penjumlahan
print(a + b)  # Output: 30

# Pengurangan
print(a - b)  # Output: 10

# Perkalian
print(a * b)  # Output: 200

# Pembagian
print(a / b)  # Output: 2

# Sisa bagi (modulus)
print(a % b)  # Output: 0

# Contoh Perbandingan 
a = 8
b = 5

# Menggunakan operator perbandingan
print("a == b:", a == b)  # Sama dengan (Output: False)
print("a != b:", a != b)  # Tidak sama dengan (Output: True)
print("a > b:", a > b)    # Lebih besar (Output: True)
print("a < b:", a < b)    # Lebih kecil (Output: False)
print("a >= b:", a >= b)  # Lebih besar atau sama dengan (Output: True)
print("a <= b:", a <= b)  # Lebih kecil atau sama dengan (Output: False)

# Operator Logika
a = True
b = False

print(a and b)  
print(a or b)   
print(not a)   

# Operator Bitwise
a = 5  
b = 3  

print(a & b)  
print(a | b)  

# Operator penugasab
x = 5
print(x)      # Output: 5

x += 5        # Sama dengan x = x + 5
print(x)      # Output: 10

x -= 3        # Sama dengan x = x - 3
print(x)      # Output: 7

x *= 2        # Sama dengan x = x * 2
print(x)      # Output: 14

x /= 4        # Sama dengan x = x / 4
print(x)      # Output: 3.5
# Contoh singkat Operator Identitas
x = [1, 2, 3]
y = x

print(x is y)  # Output: True (x dan y merujuk ke objek yang sama)
print(x is not y)  # Output: False

# Contoh singkat Operator Keanggotaan
fruits = ['apel', 'jeruk', 'pisang']

print('apel' in fruits)      # Output: True (apel ada dalam fruits)
print('mangga' not in fruits)  # Output: True (mangga tidak ada dalam fruits)