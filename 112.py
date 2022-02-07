import random
import time

w = int(input("Размерность массива: "))
m = [[random.randint(0, 100) for x in range(w)] for y in range(w)]
print("Массив из случайных чисел от 0 до 100: ")
for row in m:
    for col in row:
        print(col, end="\t")
    print()
m1 = []
i = 0
for row in m:
    for col in row:
        m1.append(row[i])
        break
    i += 1
print("Минимальный элемент массива: ", min(m1))
print("Максимальный элемент массива: ", max(m1))
# _________________________________________________________
w = 6
m = [[random.randint(0, 10) for x in range(w)] for y in range(w)]
m1 = [random.randint(0, 10) for i in range(w)]
for row in m:
    for col in row:
        print(col, end="\t")
    print()
print(m1)
print()
i = 0
while i < len(m):
    m.pop(i)
    m.insert(i, m1)
    i += 2
for row in m:
    for col in row:
        print(col, end="\t")
    print()
# _________________________________________________________
import locale

# locale.setlocale(locale.LC_ALL, "ru")
#
# print(time.strftime("Сегодня: %B %d, %Y", time.localtime()))

print("Hello, World!")