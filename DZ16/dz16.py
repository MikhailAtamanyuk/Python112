f = open("text1.txt", "w")
lines = ["\nЗамена строки в текстовом файле;", "\nизменить строку в списке;", "\nзаписать список в файл;"]
f.writelines(lines)
f.close()
print()

print("Тест:")
f = open("text1.txt", "r")
print(f.read())
f.close()
print()

pos1 = int(input("pos1 = "))
line_pos1 = lines[pos1]
ch1 = lines.index(lines[pos1])

pos2 = int(input("pos2 = "))
line_pos2 = lines[pos2]
ch2 = lines.index(lines[pos2])

a = -1
b = -1
for i in lines:
    a += 1
    if i == line_pos1:
        del lines[a]

for i in lines:
    b += 1
    if i == line_pos2:
        del lines[b]

lines.insert(ch1, line_pos2)
lines.insert(ch2, line_pos1)
print()

print("Тест:")
with open("text1.txt", "w") as text:
    text.writelines(lines)

with open("text1.txt", "r") as text:
    print(text.read())
print()
# _________________________________________________________
f = open("text2.txt", "w")
lines = ["\nЗамена строки в текстовом файле;", "\nизменить строку в списке;", "\nзаписать список в файл;"]
f.writelines(lines)
f.close()

print("Тест:")
f = open("text2.txt", "r")
print(f.read())
f.close()

lines.reverse()

with open("text2.txt", "w") as text:
    text.writelines(lines)

with open("text2.txt", "r") as text:
    print(text.read())
print()