#Arbitrary Keyword Arguments (**kwargs)

def info_murid(**kwargs):
    for kunci, nilai in kwargs.items():
        print(f"{kunci}: {nilai}")

# Memanggil fungsi dengan beberapa argumen kunci
info_murid(nama="Budi", usia=17, kelas="12 IPA")