def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f())

'''
返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
'''


# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def create_counter():
    L = [0]

    def counter():
        L[0] += 1
        return L[0]

    return counter


def create_counter2():
    y = 0

    def counter():
        nonlocal
        y
        y += 1
        return y

    return counter


def create_counter3():
    global x
    x = 0

    def counter():
        global x
        x += 1
        return x

    return counter


# 测试:
counterA = create_counter3()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = create_counter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
