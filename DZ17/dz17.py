text = ["Первый файл", "Второй файл"]
with open("1text.txt", "w") as ff, open("2text.txt", "w") as fs:
    ff.write(text[0])
    fs.write(text[1])

ls = ["1text.txt", "2text.txt"]
with open('3text.txt', 'w') as f:
    f.write("Третий файл = ")
    for i in ls:
        s = open(i).read()
        f.write(s)
        f.write('.')

with open('3text.txt', 'r') as f:
    print(f.read())
# _________________________________________________________
with open('4text.txt', 'w') as f:
    f.write("первая строка\nстрока номер два\nтретья строка\n4 строка")
with open('4text.txt', 'r') as f:
    count = 0
    for i in f:
        print(i, f"{len(i)} симв. {len(i.split())} сл.")
        count += 1
    print(f"{count} стр.")
# _________________________________________________________
direct = r"/Users/Админ/Python112/DZ17"
lst = os.listdir(direct)
for i in lst:
    chek = os.path.isfile(direct+r"/"+i)
    if chek:
        size = os.path.getsize(direct + "/" + i)
        print(os.path.basename(direct + "/" + i), "- file -", size, "bytes")
    else:
        print(os.path.basename(direct+"/"+i), "- dir")