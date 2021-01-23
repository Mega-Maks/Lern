a = [int(i) for i in input().split()]
b = int(input())
i = 0
d = 0
m = a[:]
if a.count(b) == 0:
    print('Отсутствует')
else:
    while m.count(b) > 1:
        m.pop(m.index(b))
        d += 1
    d = m.index(b) + d
    while a.index(b, i) < d:
        if i == len(a) -1:
            break
        else:
            c = a.index(b, i)
            print(c, end=' ')
        i = c + 1
    print(d, end=' ')
