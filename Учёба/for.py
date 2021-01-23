c = int(input())
d = int(input())
a = int(input())
b = int(input())
print('\t', end='')
for i in range(a, b+1):
    g = len(str(i))
    g -= 1
    l = 4
    l -= g
    print(i, end=(l * ' '))
print('')
f = a
for i in range(c, d+1):
    m = a
    g = len(str(i * f))
    g -= 1
    l = 4
    l -= g
    o = 4 - len(str(i))
    print(i, end=(o * ' '))
    while m <= b:
        print(i * m, end=(l * ' '))
        m += 1
    print()
    f += 1