def slicer(a, b):
    lt = list(a)
    num2 = 0
    num4 = 0
    for i in a:
        num2 += 1
        if i == b:
            num4 += 1
            num1 = lt.index(i)
            if num4 == 2:
                num3 = num2
    if lt.count(b) >= 2:
        return print(tuple(lt[num1:num3]))
    elif lt.count(b) == 1:
        return print(tuple(lt[num1:]))
    elif lt.count(b) == 0:
        lt = ()
        return print(lt)


slicer((1, 2, 3), 8)
slicer((1, 8, 3, 4, 8, 8, 9, 2), 8)
slicer((1, 2, 8, 5, 1, 2, 9), 8)
# _________________________________________________________
import random

def tuple_random(a,b):
    tup=tuple([random.randint(a,b) for i in range(10)])
    return tup

tup1=tuple_random(0,5)
tup2=tuple_random(-5,0)
print(tup1)
print(tup2)
tup3=tup1+tup2
print(tup3)
print("0 =", tup3.count(0))