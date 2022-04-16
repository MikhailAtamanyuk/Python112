import math


class Formula:
    count = 0

    @staticmethod
    def geron(a,b,c):
        Formula.count += 1
        p = (a+b+c)/2
        s = math.sqrt((p*(p-a))*(p-b)*(p-c))
        print(f"Площадь треугольника по формуле Герона равна ({a}, {b}, {c}): {s}")

    @staticmethod
    def geron2(a,b):
        Formula.count += 1
        s = a*b/2
        print(f"Площадь треугольника через основание и высоту ({a}, {b}): {s}")

    @staticmethod
    def sqr(a):
        Formula.count +=1
        s = a*a
        print(f"Площадь квадрата ({a}): {s}")

    @staticmethod
    def par(a,b):
        Formula.count += 1
        s = a*b
        print(f"Площадь прямоугольника ({a}, {b}): {s}")

    @staticmethod
    def num():
        print("Количество подсчетов площади:", Formula.count)


form = Formula()
form.geron(3,4,5)
form.geron2(6,7)
form.sqr(7)
form.par(2,6)
form.num()