a = int(input())
h = []
c = []
if a < 0:
    a = -a
for i in range(a):
    h += [c]
    c = []
    for j in range(a):
        c += [0]
h += [c]
h.pop(0)
if a == 0:
    print(0)
elif len(h[0]) == 0:
    True
elif len(h) == 1 and len(h[0]) == 1:
    print(a * a)
elif a == 2:
    print(1, 2)
    print(4, 3)
else:
    m = 1
    UP = 1
    Down = -2
    Left = 1
    Right = -2
    for i in range(a):
        h[0][i] = m
        m += 1
    for i in range(1, a - 1):
        h[i][-1] = m
        m += 1
    for i in range(a - 1, 0, -1):
        h[-1][i] = m
        m += 1
    h[-1][0] = m
    m += 1
    for i in range(a - 2, 1, -1):
        h[i][0] = m
        m += 1
    h[1][0] = m
    m += 1
    p = a
    p -= 2
    x = 0
    y = 1
    while m <= a * a:
        while h[y][x + 1] == 0:
            h[y][x + 1] = m
            x += 1
            m +=1
        while h[y + 1][x] == 0:
            h[y + 1][x] = m
            y += 1
            m += 1
        while h[y][x - 1] == 0:
            h[y][x - 1] = m
            x -= 1
            m += 1
        while h[y - 1][x] == 0:
            h[y - 1][x] = m
            y -= 1
            m += 1
    l = len(h[0]) - 1
    for i in range(a):
        for j in range(a):
            if j == l:
                print(h[i][j])
            else:
                print(h[i][j], end=' ')
