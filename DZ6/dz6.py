lst1 = ['red', 'green', 'blue']
lst2 = ['#FF0000','#008000', '#0000FF']
f = {key: value for key, value in zip(lst1, lst2)}
print(f)
# _________________________________________________________
f = {k: v**3 for k, v in zip(list(range(1, 11)), list(range(1, 11)))}
print(f)
# _________________________________________________________
colors_1 = ["color", "fruit", "pet"]
num_1 = ["blue", "apple", "dog"]

f = {k: v for k, v in zip(colors_1, num_1)}
print(f)
# _________________________________________________________
def min_elem(*num):
    lst = list(num)
    min_el = min(lst)
    return min_el

print(min_elem(10, 9))
print(min_elem(2, 3, 4))
print(min_elem(3, 5, 10, 6))
# _________________________________________________________
def sum_elem(*num):
    s = 0
    for i in num:
        s += i
        print(s, end=" ")
    print()

sum_elem(3, 9, 1)
sum_elem(2, 5, 4, 2)
sum_elem(3, 5, 10, 6, 3)