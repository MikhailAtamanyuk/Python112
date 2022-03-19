s = 'Замените в этой строке все появления буквы "о" на букву "О" кроме первого и последнего вхождения'
print(s[:s.index("о") + 1] + re.sub("о", "О", s[s.index("о") + 1:s.rindex("о")]) + s[s.rindex("о"):])
print()
# _________________________________________________________
s = "I am learning Python. hello, WORLD!"
print(s)
print(re.sub("on. ", " .no", s))
print()