class Clock:
    __DAY = 86400 # 24*60*60 - число секунд в дне

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть числом")

        self.__sec = sec % self.__DAY

    def get_format_time(self):
        s = self.__sec % 60 # секунды
        m = (self.__sec // 60) % 60 # минуты
        h = (self.__sec // 3600) % 24 # часы
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        else:
            return Clock(self.__sec + other.__sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        else:
            return Clock(self.__sec - other.__sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        else:
            return Clock(self.__sec * other.__sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        else:
            return Clock(self.__sec // other.__sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        else:
            return Clock(self.__sec % other.__sec)

    def __isub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        else:
            self.__sec -= other.__sec
            return self

    def __imul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        else:
            self.__sec *= other.__sec
            return self

    def __ifloordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        else:
            self.__sec //= other.__sec
            return self

    def __imod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        else:
            self.__sec %= other.__sec
            return self


c1 = Clock(600)
print("c1:", c1.get_format_time())
c2 = Clock(200)
res = c1 - c2
print("c1 - c2:", res.get_format_time())
res = c1 * c2
print("c1 * c2:", res.get_format_time())
res = c1 // c2
print("c1 // c2:", res.get_format_time())
res = c1 % c2
print("c1 % c2:", res.get_format_time())
c1 -= c2
print("c1 -= c2", c1.get_format_time())
c1 *= c2
print("c1 *= c2", c1.get_format_time())
c1 //= c2
print("c1 //= c2", c1.get_format_time())
c1 %= c2
print("c1 %= c2", c1.get_format_time())
