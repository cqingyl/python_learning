# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#
# ax2 + bx + c = 0
#
# 的两个解。
#
# 提示：计算平方根可以调用math.sqrt()函数：
# x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
# x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
import math


def quadratic(a, b, c):
    for i in (a, b, c):
        if not (isinstance(i, (int, float))):
            raise TypeError('parameter type error!')

    delta = b * b - 4 * a * c
    if a == 0:
        return -c / b
    if delta > 0:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    elif delta == 0:
        x1 = x2 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    else:
        raise ArithmeticError('')
    return x1, x2


print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


num = [1, 2, 3, 4, 5, 6]
print(calc(*num))


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('zhangsan', 18, city='beijing', gender='female')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('zhangsan', 18, **extra)


def person2(name, age, *, city, job):
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)


person2('zhang', 23, city='chengdu', job='engineer')


def person3(name, age, *args, city, job):
    print(name, age, args, city, job)


person3('zhangsan', 28, 'cc', 'ee', city='chengdu', job='engineer')


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


args = (1, 2, 3)
kw = {'d': 'op', 'x': '#', 'y': 's', 'v': 'f', 'z': 'z', 'l': 'l'}
f2(*args, **kw)
