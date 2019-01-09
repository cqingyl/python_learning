# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(*num):
    count = 1
    for n in num:
        count = count * n
    return count


print(product(1, 3, 4, 5))


def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)


print(fact(998))


def fact_iter(n, iter):
    if n == 1:
        return iter
    return fact_iter(n - 1, n * iter)


def fact2(n):
    return fact_iter(n, 1)


print(fact2(100))
