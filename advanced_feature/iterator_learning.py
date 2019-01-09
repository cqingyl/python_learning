l = []
for x in range(1, 11):
    l.append(x)
print(l)

s = [x * y for x in range(1, 11) for y in range(1, 11)]
print(s)

k = [x * x for x in range(1, 11) if x % 2 == 0]
print(k)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [i.lower() for i in L1 if isinstance(i, str)]
print(L2)
