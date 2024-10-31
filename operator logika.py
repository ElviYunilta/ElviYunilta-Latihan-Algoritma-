# Mendefinisikan beberapa variabel
a = 10
b = 20
c = 15

# Menggunakan operator logika 'and'
print('Hasil dari (a < b) and (b > c)       :', (a < b) and (b > c))  # True, karena 10 < 20 dan 20 > 15
print('Hasil dari (a > b) and (c < a)       :', (a > b) and (c < a))  # False, karena 10 > 20 salah

print('\n')

# Menggunakan operator logika 'or'
print('Hasil dari (a < b) or (b < c)        :', (a < b) or (b < c))  # True, karena 10 < 20
print('Hasil dari (a > b) or (c > a)        :', (a > b) or (c > a))  # False, karena keduanya salah

print('\n')

# Menggunakan operator logika 'not'
print('Hasil dari not (a < b)                :', not (a < b))        # False, karena 10 < 20
print('Hasil dari not (c > a)                :', not (c > a))        # False, karena 15 > 10

# Contoh gabungan
print('\nContoh gabungan operator logika:')
print('Hasil dari (not (a < b)) or (c > a)   :', (not (a < b)) or (c > a))  # True, karena (False or True)
print('Hasil dari (a < b) and not (c > a)   :', (a < b) and not (c > a))  # True, karena (True and False)