'''
Македонський Богдан 125А
Лабораторна Робота №1
RSA
'''

import sympy

flag_p = 1
while flag_p:  # Перевірка числа р на простоту
    p = int(input("Введіть перше просте число(р) - "))
    a = sympy.isprime(p)
    if a:
        flag_p = 0
    else:
        print(f"Число р - {p} не є простим, введіть нове число")

flag_q = 1
while flag_q:  # Перевірка числа q на простоту
    q = int(input("Введіть друге просте число(q) - "))
    a = sympy.isprime(q)
    if a:
        flag_q = 0
    else:
        print(f"Число q - {q} не є простим, введіть нове число")

n = p * q  # Вирахування n
print(f'n - {n}')

fn = (p - 1) * (q - 1)  # Вирахування f(n)
print(f"f(n) - {fn}")

flag_e = 1
while flag_e:  # Перевірка числа e на простоту
    e = int(input(f"Введіть число е, повинно бути взаємопростим із f(n) - "))
    a = sympy.isprime(e)
    b = e < n
    if a:
        flag_e = 0
    else:
        print(f"Число e - {e} не є простим, введіть нове число")


for i in range(2, 1000000000):  # Пошук d яке б задовольняло ф-цію (e * d) * mod(f(n)) = 1
    if i * e % fn == 1:
        d = i
        break

print(f"d - {d}")

print(f"Відкритий ключ - ({e},{n})")
print(f"Закритий ключ - ({d},{n})")


name = input("Введіть своє ім\'я - ")
name = name.lower()
let_name = ' '.join(name)
let_name = let_name.split(" ")


letters = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

# Шифрування
coded_message = []
let_num_mass = []

for i in range(len(let_name)):  # Шифрування повідомлення
    let_id = letters.index(let_name[i])
    let_id += 1
    let_num_mass.append(let_id)
    code_num = let_id**e % n
    coded_message.append(code_num)

print("Введене ім'я у цифровому записі - ", let_num_mass)
print("Зашифроване повідомлення ", coded_message)

# Дешифрування

decoded_message = []

for i in coded_message:  # Розшифрування повідомлення
    decoded_num = i**d % n
    decoded_message.append(decoded_num)

print("Розшифроване повідомлення ", decoded_message)
