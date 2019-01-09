print('I`m "OK"', '''a
b
c''')

print()

a = 'ABC'
b = a
print('a =', a)
a = 'XYZ'
print('a =', a, 'b =', b)

print()

print('10 / 3=', 10 / 3, '10 // 3=', 10 // 3, '10 % 3=', 10 % 3, sep='\n')

print()

n = 123
f = 456.789
s0 = 'Hello, world'
s1 = 'Hello, "world"'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n, f, s0, s1, s2, s2, s3, s4, sep='\n')
