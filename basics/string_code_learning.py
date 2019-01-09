print(ord('A'), chr(65), b'abc')

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print('%.2f%%' % r)

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
print('Hello, %s, 成绩提升了 %.1f%%' % ('小明', 17.125))
