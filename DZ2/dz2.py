shapes = int(input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))


def rectangle(height, width):
    return print("Площадь прямоугольника равна: ", height*width)


def triangle(height, width):
    return print("Площадь треугольника равна: ", (height*width)/2)


def circle(height):
    return print("Площадь круга равна: ", pi*height**2)


if shapes == 1:
    a = int(input("Введите длину прямоугольника: "))
    b = int(input("Введите ширину прямоугольника: "))
    rectangle(a, b)
elif shapes == 2:
    a = int(input("Введите введите первый катет: "))
    b = int(input("Введите введите второй катет: "))
    triangle(a, b)
elif shapes == 3:
    a = int(input("Введите радиус круга: "))
    circle(a)
else:
    print("Введите от 1 до 3")
print()
# _________________________________________________________
def fun(lst):
    simple = []
    not_simple = []
    for i in lst:
        if i < 2:
            continue
        for j in range(2, i):
            if i % j == 0:
                not_simple.append(i)
        else:
            simple.append(i)
    print("Min: ", min(simple))
    print("Max: ", max(not_simple))

fun([6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1])