n1 = int(input("Введите первое двоичное число: "), 2)
n2 = int(input("Введите второе двоичное число: "), 2)

bit_or = n1 | n2
bit_and = n1 & n2
bit_xor = n1 ^ n2

print(f"Результат побитового OR: {bin(bit_or)}")
print(f"Результат побитового AND: {bin(bit_and)}")
print(f"Результат побитового XOR: {bin(bit_xor)}")