s = "Дана ст(рока символов, среди которых есть одна открыв)ающаяся"
print(s)
print(s[s.find("(") + 1:s.find(")")])
# _________________________________________________________
# s = input("Строка: ")
s = "11 23 44 55 23 22"
# n = input("Ее заменяемая подстрока: ")
n = "23"
# b = input("Новая подстрока: ")
b = "!!!"
new_s = ''
for i in s.split():
    if i != n:
        new_s = new_s + f" {i}"
    else:
        new_s = new_s + f" {b}"
print(new_s)
# _________________________________________________________
s1 = '''Ежевику для ежат
Принесли два ежа.
Ежевику еле-eле
Ежата возле ели съели.'''
print(text)
count = 0
for i in range(len(s1.split())):
    if s1.split()[i].find("е") == 0 or s1.split()[i].find("Е") == 0:
        count += 1
print("Количество слов начинающихся на 'е': ", count)