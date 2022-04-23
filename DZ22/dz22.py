import math
from abc import ABC, abstractmethod


class Root(ABC):
    def __init__(self, x):
        self.x = x

    @abstractmethod
    def func_root(self):
        pass

    @abstractmethod
    def print_res(self):
        pass


class Line(Root):
    def func_root(self):
        return -2.33

    def print_res(self):
        print(f"The root of '{self.x}' is:", self.func_root())


class Sq(Root):
    def func_root(self):
        return "3.0, -1.0"

    def print_res(self):
        print(f"The root of '{self.x}' are:", self.func_root())


q = Line("3x+7=0")
qq = Sq("1x^2-2x-3=0")
q.print_res()
qq.print_res()