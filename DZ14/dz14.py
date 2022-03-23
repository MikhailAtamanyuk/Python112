import re

s = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, +7 (499) 456-45-78"
reg = r"[\(\)+\d\s-]+"
print(re.findall(reg, s))
# _________________________________________________________
names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']


def count_items(lst):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += count_items(item)
        else:
            count += 1
    return count


print(count_items(names))