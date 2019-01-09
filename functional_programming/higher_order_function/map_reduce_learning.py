from functools import reduce


# functional
def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def f(x):
    return x[0].upper() + x[1:].lower()


l = ['adam', 'LISA', 'barT']
r = map(f, l)
print(list(r))


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def h(x, y):
    return x * y


def prod(l):
    return reduce(h, l)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    L = [int(i) for i in s.split('.')[0]]
    integer = 0
    for i in L:
        integer = i + integer * 10
    decimal = 0
    L = [int(j) for j in s.split('.')[1]]
    L = L[::-1]
    for i in L:
        decimal = i + decimal / 10
    return integer + decimal / 10


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
