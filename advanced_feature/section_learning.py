# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trims(s):
    if s == '' or s == ' ':
        raise AttributeError('parameter error')
    return s[1:-1]


print(trims(' 1234 '))
print(trims(' 1234'))
print(trims('1234 '))
print(trims('  '))
print(trims('1234  '))


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def find_min_and_max(l):
    max = -1
    min = 100000
    for i in l:
        if i > max:
            max = i
        if i < min:
            min = i
    return max, min


num = range(1, 9)
print(*num)
print(find_min_and_max(num))
