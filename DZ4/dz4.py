s1 = set(input("Введите первую строку: "))
s2 = set(input("Введите вторую строку: "))
s1 = set("Python")
s2 = set("Programming language")
s3 = s1 - s2
print("Искомыми буквами являются: ")
for i in s3:
    print(i, end=" ")
# _________________________________________________________
s=input("Введите строку: ")
s = "Привет, мир!"
vowels = "аяоёуюыиэе"
def count_vowels(st):
    return sum([1 for x in s.lower() if x in vowels])

print("Количество гласных равно:", count_vowels(s))
# _________________________________________________________
s1 = set(input("Введите первую строку: "))
s2 = set(input("Введите вторую строку: "))
s1 = set("test")
s2 = set("string")
s3 = s1 | s2
print("Искомыми буквами являются: ")
for i in s3:
    print(i, end=" ")
# _________________________________________________________
s1 = set(input("Введите первую строку: "))
s2 = set(input("Введите вторую строку: "))
s1 = set("hello")
s2 = set("world")
s3 = s1 ^ s2
print("Искомыми буквами являются: ")
for i in s3:
    print(i, end=" ")