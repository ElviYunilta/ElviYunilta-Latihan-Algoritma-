#Arbitrary Arguments (*args) Python


def jumlahkan(*args):
    total = 0
    for angka in args:
        total += angka
    return total

# Memanggil fungsi dengan berbagai jumlah argumen
print(jumlahkan(1, 2, 3))       # Output: 6
print(jumlahkan(4, 5, 6, 7, 8)) # Output: 30