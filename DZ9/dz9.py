ls = [3, 6, 8, 9, 1, 2]
print(ls)
print(list(map(lambda x: ls.index(x) ** 2 * ls.index(x) * x, ls)))
print()
# _________________________________________________________
l = [3, -4, -6, 7, -8, 3, -12, 4, 7]
res = (list(filter(lambda s: s < 0, l)))
print(res)
print(abs(sum(res))
# _________________________________________________________
nums = [3, 5, 7, 3, 9, 5, 7, 2]
print(list(map(lambda x: x ** 2, nums)))
print(list(map(lambda x: x ** 2 * x, nums)))
print()
# _________________________________________________________
def func_compute(n):
    def inner(x):
        return n * x
    return inner

res = func_compute(2)
print(res(15))
print(res(20))

res = func_compute(3)
print(res(15))
print(res(20))
print()