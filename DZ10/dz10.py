def decor(*args):

    def wrapper(fn):
        def wrap(*f_args):
            fn(*f_args)
            a = sum(f_args) / len(f_args)
            return print("Среднее арифметическое чисел =", a)

        return wrap
    return wrapper


@decor(int, int, int, int)
def summa(*args):
    a = sum(args)
    print("Сумма чисел 2, 3, 3, 4 =", a)
    return a


summa(2, 3, 3, 4)
print()
# _________________________________________________________
str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."


def change_char_to_str(s, old, new):
    s2 = ""
    i = 0

    while i < len(s):
        if s[i] == old and i % 2 == 0:
            s2 = s2 + new
        else:
            s2 = s2 + s[i]
        i = i + 1

    return s2


str2 = change_char_to_str(str1, "N", "P")
print("str1 =", str1)
print("str2 =", str2)
print()
# _________________________________________________________
def change_char_to_str(str1, num):
    s1 = ""
    for i in range(0, len(str1)):
        if i == int(num):
            continue
        s1 = s1 + str1[i]
    return s1


s = "0123456789"
s2 = change_char_to_str(s, "4")
print("s =", s)
print("s2 =", s2)
# _________________________________________________________
def change_char_to_str(str1, num):
    s1 = ""
    for i in range(0, len(str1)):
        if s[i] == num:
            continue
        s1 = s1 + str1[i]
    return s1


s = "012345363738494"
s2 = change_char_to_str(s, "3")
print("s =", s)
print("s2 =", s2)