#Named Parameter / Keyword Arguments

def info(nama, usia=20):
    return f"Nama: {nama}, Usia: {usia} tahun"

# Memanggil fungsi dengan parameter bernama
print(info(nama="Andi"))  # Output: Nama: Andi, Usia: 20 tahun
print(info(nama="Budi", usia=25))  # Output: Nama: Budi, Usia: 25 tahun