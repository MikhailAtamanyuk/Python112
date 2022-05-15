class Valid:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.__name} должна быть целым числом")
        elif value < 0:
            raise ValueError(f"{self.__name} должно быть положительным")
        instance.__dict__[self.__name] = value


class Triangle:
    c1 = Valid()
    c2 = Valid()
    c3 = Valid()

    def __init__(self, c1, c2, c3):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def info(self):
        if self.c1 + self.c2 > self.c3 and self.c1 + self.c3 > self.c2 and self.c2 + self.c3 > self.c1:
            print(f"Треугольник со сторонами: {self.c1}, {self.c2}, {self.c3} существует")
        else:
            print(f"Треугольник со сторонами: {self.c1}, {self.c2}, {self.c3} не существует")


t1 = Triangle(2, 5, 6)
t2 = Triangle(5, 2, 8)
t3 = Triangle(7, 3, 6)

t1.info()
t2.info()
t3.info()