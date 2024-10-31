# Mendefinisikan variabel a dan b
a = 5  # dalam biner: 0101
b = 3  # dalam biner: 0011

# Menampilkan nilai a dan b dalam desimal dan biner
print('a berisi angka', a, 'desimal atau', bin(a), 'biner')
print('b berisi angka', b, 'desimal atau', bin(b), 'biner')

# Operasi bitwise
print('a & b  :', a & b, '->', bin(a & b))  # AND
print('a | b  :', a | b, '->', bin(a | b))  # OR
print('a ^ b  :', a ^ b, '->', bin(a ^ b))  # XOR
print('~a     :', ~a, '->', bin(~a))        # NOT
print('a << 1 :', a << 1, '->', bin(a << 1))  # Shift Left
print('a >> 1 :', a >> 1, '->', bin(a >> 1))  # Shift Right