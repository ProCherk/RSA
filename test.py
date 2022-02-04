p = 31
q = 23
e = 53

n = p * q
print(f'n - {n}')

fn = (p - 1) * (q - 1)
print(f"fn - {fn}")

for i in range(2, 1000000000):
    if i * e % fn == 1:
        d = i
        break

d = int(d)

print(f"d - {d}")

print(f"Відкритий ключ - ({e},{n})")
print(f"Закритий ключ - ({d},{n})")


name = input("Введіть своє ім\'я - ")
name = name.lower()
let_name = ' '.join(name)
let_name = let_name.split(" ")


letters = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
# print(len(letters))

# Шифрування
coded_message = []

for i in range(len(let_name)):
    let_id = letters.index(let_name[i])
    let_id += 1
    print(let_id)
    code_num = let_id**e % n
    coded_message.append(code_num)

print("Coded message ", coded_message)

# Дешифрування

decoded_message = []

for i in coded_message:
    decoded_num = i**d % n
    decoded_message.append(decoded_num)

print(decoded_message)
