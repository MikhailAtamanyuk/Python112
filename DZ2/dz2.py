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