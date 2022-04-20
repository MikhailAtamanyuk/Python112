import math


class Pair:
    def __init__(self, a, b):
        self.__a_kat = a
        self.__b_kat = b

    @property
    def a_kat(self):
        return self.__a_kat

    @a_kat.setter
    def a_kat(self, a):
        self.__a_kat = a

    @property
    def b_kat(self):
        return self.__b_kat

    @b_kat.setter
    def b_kat(self, b):
        self.__b_kat = b

    def proiz(self):
        return self.__a_kat * self.__b_kat

    def sum(self):
        return self.__a_kat + self.__b_kat


class RightTriangle(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)

    def gip(self):
        return round(math.sqrt(self.a_kat ** 2 + self.b_kat ** 2), 2)

    def area(self):
        return 0.5 * self.a_kat * self.b_kat

    def res_gip(self):
        print(f'Гипотенуза ABC: {self.gip()}')

    def rect(self):
        print(f'Прямоугольный треугольник ABC: ({self.a_kat}, {self.b_kat}, {self.gip()})')

    def print_area(self):
        print(f'Площадь треугольника ABC: {self.area()}')

    def print_proiz(self):
        print(f'Произведение: {self.proiz()}')

    def print_sum(self):
        print(f'Сумма: {self.sum()}')


p1 = RightTriangle(5, 8)
p1.res_gip()
p1.rect()
p1.print_area()
print()
p1.print_sum()
p1.print_proiz()
print()
p1.a_kat = 10
p1.res_gip()
p1.b_kat = 20
p1.res_gip()
p1.print_sum()
p1.print_proiz()
p1.print_area()