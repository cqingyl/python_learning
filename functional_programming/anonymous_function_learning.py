L = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6]))
print(L)


def f(x):
    return x * x


print(list(map(f, [1, 2, 3, 4, 5, 6])))


# 请用匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print(L)
L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)
