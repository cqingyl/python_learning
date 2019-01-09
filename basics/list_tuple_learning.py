# 练习
# 请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L)
# tuple
t = ('a', 'b', L)
print(t)
L[2][0] = 'y'
L[2][1] = 'x'
t[2][0][2] = 'z'
print(t)
