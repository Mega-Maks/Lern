a = input()
b = input()
c = input()
d = input()
Dict1 = dict(zip(a, b))
Dict2 = dict(zip(b, a))
for i in c:
    print(Dict1[i], end='')
print()
for i in d:
    print(Dict2[i], end='')