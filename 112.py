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
# _________________________________________________________
shapes = int(input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))


def rectangle(height, width):
    return print("Площадь прямоугольника: ", height*width)


def triangle(height, width):
    return print("Площадь треугольника: ", (height*width)/2)


def circle(height):
    return print("Площадь круга: ", pi*height**2)


if shapes == 1:
    a = int(input("Введите длину прямоугольника: "))
    b = int(input("Введите ширину прямоугольника: "))
    rectangle(a, b)
elif shapes == 2:
    a = int(input("Введите первый катет: "))
    b = int(input("Введите второй катет: "))
    triangle(a, b)
elif shapes == 3:
    a = int(input("Введите радиус круга: "))
    circle(a)
else:
    print("Введите от 1 до 3")
print()
# _________________________________________________________
lt = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
print(lt)
lt2 = []
lt3 = []
for i in lt:
    if i == 3:
        if i not in lt2:
            lt2.append(i)
    if i % 2 != 0 and i % 3 != 0 and i != 1:
        if i not in lt2:
            lt2.append(i)
for i in lt:
    if i != 3:
        if i % 2 == 0 or i % 3 == 0:
            if i not in lt3:
                lt3.append(i)
print(lt2)
a = 100
b = 0
for i in lt2:
    if i < a:
        a = i
print("Min:", a)
print(lt3)
for i in lt3:
    if i > b:
        b = i
print("Max:", b)